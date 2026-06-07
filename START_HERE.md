# 🚀 START HERE - Ollama Web App

## What You Have

A **complete, self-explanatory web application** that teaches you about:
- Web servers (Python + Flask)
- APIs and HTTP requests
- Ports and networking
- Frontend-Backend communication
- JSON data format
- Integration with external services (Ollama)

**All code is heavily commented for learning!**

---

## Quick Start (3 Commands)

**Terminal 1:**
```bash
ollama serve
```

**Terminal 2:**
```bash
cd ~/Desktop/Development/sandbox/ollama_web_app
pip install -r requirements.txt
python backend.py
```

**Browser:**
```
http://localhost:5000
```

---

## Files Overview

| File | Purpose | Lines |
|------|---------|-------|
| **backend.py** | Python server (port 5000) | 240 |
| **static/index.html** | Frontend interface | 456 |
| **requirements.txt** | Python dependencies | 2 |
| **README.md** | Complete guide | 389 |
| **ARCHITECTURE.md** | Visual diagrams | 307 |
| **QUICK_REFERENCE.md** | Concept lookup | 10K+ |
| **GETTING_STARTED.txt** | Setup guide | 10K+ |

---

## The 4-Step Message Flow

```
1. You type in browser
   ↓
2. Browser sends HTTP POST to backend (port 5000)
   ↓
3. Backend sends HTTP POST to Ollama (port 11434)
   ↓
4. Response flows back: Ollama → Backend → Browser → You see answer
```

---

## Key Concepts

🚪 **PORT** - Virtual "door" (5000 for us, 11434 for Ollama)
📋 **API** - Rules for how programs communicate
🛣️ **ENDPOINT** - Specific URL path (/api/chat)
➡️ **REQUEST** - Message TO the backend
⬅️ **RESPONSE** - Message FROM the backend
📦 **JSON** - Data format {"message": "hello"}

---

## Reading Order

1. **This file** (5 min)
2. **GETTING_STARTED.txt** (10 min)
3. **ARCHITECTURE.md** (15 min - visual diagrams)
4. **backend.py** (30 min - read all comments)
5. **static/index.html** (30 min - read all comments)
6. **Run the app!**

---

## What You'll Learn

✅ How web servers work  
✅ How HTTP requests/responses work  
✅ What APIs are  
✅ How ports separate services  
✅ How JSON transfers data  
✅ How frontend & backend communicate  
✅ JavaScript fetch() API  
✅ Python Flask framework  
✅ Error handling  
✅ Client-server architecture  

---

## Troubleshooting

**"Cannot connect to Ollama"**
- Make sure `ollama serve` is running in Terminal 1
- Run `ollama pull qwen` first time

**"Port 5000 already in use"**
- Edit `backend.py` line 24: `FLASK_PORT = 8000`

**"Frontend won't load"**
- Wait 5 seconds for backend to fully start
- Visit exactly: `http://localhost:5000`

**"Responses are slow"**
- Normal! First response takes 30-60 seconds (model loads)
- Subsequent responses are fast

---

## Next: Read ARCHITECTURE.md

�� **[ARCHITECTURE.md](ARCHITECTURE.md)** has visual diagrams showing how everything connects!

Then read **backend.py** and **static/index.html** - every line is explained.

---

**Questions? The answers are in the comments!**
