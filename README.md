# 🎮 AI for Your Dusty Consoles: PSP/DSI Edition

**Step 1:** Stop crying about your retro tech. This app lets your PSP and DSI *finally* join the AI revolution.

---

### **What It Does**
- **PSP (PlayStation Portable):** Squeezes ChatGPT into that 2005 browser. *Note:* You *must* include `http://` in the URL (e.g., `http://192.168.1.100:5000`). No exceptions.
- **DSi (Nintendo DSi):** Uses both screens for improved vertical scrolling, think like a book, scroll down and texts pops at the top, oh and its more modern, like just your pc IP:Port already works, aka: `192.168.1.100:5000`

---

### **Setup for Noobs**
1. **Install Python 3.8+** (You Probably already have it).
2. Clone this repo.
3. Rename and edit `config.json.example` with your API key from **[Infermatic.ai](https://ui.infermatic.ai/)** (or whatever overpriced service you’re using).
4. **(Optional)** Make sure to edit `server.py` with a valid AI model name if you are not using Infermatic.
5. Run `start.bat` to just let the app install/start itself. Magic!

---

### **Running the Server**
- **PSP:** Enter `http://[Your-IP]:5000` in the XMB browser.
- **DSi:** Type `[Your-IP]:5000` in the DSi Browser. No `http://` needed here.

---

### **Why This Rules**
- **Zero JavaScript for PSP:** Their browser can’t handle modern shit.
- **DSi’s Dual Screens:** We *finally* use that top screen for something other than knowing where we are.
- **Cross-Platform:** Same server serves both PSP and DSI. Lazy devs rejoice.

---

### **Troubleshooting**
- **PSP Can't Show Content** Have you included `http://` in the URL?
- **DSi Freezes?** Close and reopen. It’s 2008 again.
- **No Responses?** Your API key is wrong. Duh.

---

### **Customization**
- **Change Models:** Edit `server.py` and replace `TheDrummer-Valkyrie-49B-v1` with whatever your API uses.
- **Bigger Responses:** For DSI users, increase the `max_tokens` in `server.py` to get more text, for example: `max_tokens = 1024`, for PSP users I recommend buying a DSI instead.

---

### **Contributing**
If you’re some retro gaming nerd who wants to optimize this to work on even more retro consoles (Wii, Wii U, etc.), fork away. Just send the pull request once you tested on real hardware, make sure all changes are based on user agent detection and each consome must have their own HTML file.

---

### **License**
MIT License. Do what you want with it, I may update this, or may not.

---

### **Legal BS**
This project is for educational purposes only. No consoles were harmed to make this possible. Also, don't be evil, but if you do, I won't stop you.

---

### **Credits**
- [Infermatic.ai](https://ui.infermatic.ai/) for providing the API
- The internet for being awesome
- Myself for making this happen
- You for reading this far