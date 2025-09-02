from flask import Flask, request, Response, send_file
import requests
import json
import os

app = Flask(__name__)

# Carregar config fixa
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
API_KEY = config["API_KEY"]
BASE_URL = config["BASE_URL"].rstrip('/')

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent', '').lower()
    print(f"=== Novo acesso: {user_agent} ===")

    # Identificar PSP (exemplo de User Agent: "Mozilla/4.0 (PSP (PlayStation Portable); 2.00)")
    if "playstation portable" in user_agent:
        response = send_file('psp_index.html')
        # PSP's browser doesn't handle application/xhtml+xml well — use text/html
        response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        # Some old browsers (like the PSP) treat Content-Disposition with a filename
        # as a download. Remove it so the page renders inline.
        if 'Content-Disposition' in response.headers:
            del response.headers['Content-Disposition']
        return response
    else:
        response = send_file('index.html')
        response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        return response

@app.after_request
def add_cors_headers(resp):
    # CORS/fallback for older clients (safe for same-origin too)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return resp

@app.route('/resposta', methods=['GET', 'POST', 'OPTIONS'])
def gerar_resposta():
    if request.method == 'OPTIONS':
        # Preflight
        return Response("", status=204)

    # request.values merges args (GET) and form (POST)
    pergunta = (request.values.get("pergunta") or "").strip()
    modelo = (request.values.get("modelo") or "TheDrummer-Valkyrie-49B-v1").strip()

    if not pergunta:
        return Response("Pergunta vazia", status=400, mimetype="text/plain; charset=utf-8")

    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {
        "model": modelo,
        "messages": [{"role": "user", "content": pergunta}],
        "temperature": 0.7,
        "max_tokens": 256,
        "top_p": 0.95
    }

    try:
        r = requests.post(f"{BASE_URL}/chat/completions", json=payload, headers=headers, timeout=60)
        r.raise_for_status()
        data = r.json()
        if "choices" in data and data["choices"]:
            content = data["choices"][0]["message"]["content"]
            return Response(content, mimetype="text/plain; charset=utf-8")
        else:
            return Response("Erro ao gerar resposta", status=502, mimetype="text/plain; charset=utf-8")
    except Exception as e:
        # Don't leak stack traces to old clients; return plain text
        return Response(f"Erro: {str(e)}", status=500, mimetype="text/plain; charset=utf-8")

@app.route('/modelos')
def listar_modelos():
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        r = requests.get(f"{BASE_URL}/v1/models", headers=headers, timeout=30)
        r.raise_for_status()
        data = r.json()

        if isinstance(data, list):
            modelos = [model.get('id', '') for model in data if isinstance(model, dict)]
        elif isinstance(data, dict) and 'data' in data:
            modelos = [model.get('id', '') for model in data['data'] if isinstance(model, dict)]
        else:
            modelos = []

        return Response(json.dumps(modelos), mimetype="application/json")

    except Exception as e:
        return Response(f"Erro ao carregar modelos: {str(e)}", status=500, mimetype="text/plain")

if __name__ == '__main__':
    # Bind to LAN for the DSI; disable debug for stability
    app.run(host='0.0.0.0', port=5000, debug=False)