# 🔧 Setup Fix for Port and Flask Issues

## Problems Fixed

### 1. ✅ Ollama Port Already in Use (11434)
**Problem:** `listen tcp 127.0.0.1:11434: bind: address already in use`

**Solution:** On this machine, Ollama is already running as a background system service. **You do not need to run `ollama serve` manually.**

**Check service status:**
```bash
systemctl is-active ollama
```

If you ever actually need to restart it:
```bash
sudo systemctl restart ollama
```

### 2. ✅ Flask AttributeError with Python 3.14
**Problem:** `AttributeError: module 'pkgutil' has no attribute 'get_loader'`

**Solution:** Flask 2.3.0 doesn't support Python 3.14. Updated to Flask 3.1.3

**What I Fixed:**
- Updated `requirements.txt` to use `flask>=3.1,<4`
- Updated virtual environment with Flask 3.1.3

---

## 🚀 Correct Startup Sequence

### Terminal 1: Check Ollama
Ollama is usually already running as a service. Verify it:
```bash
systemctl is-active ollama
```
If it says `active`, move to the next step.

### Terminal 2: Set up and run backend
```bash
cd ~/Desktop/Development/sandbox/ollama_web_app

# Activate virtual environment
source .venv/bin/activate

# Install/upgrade dependencies
python -m pip install -q -r requirements.txt

# Run backend
python backend.py
```

Wait for: `Backend running on http://localhost:5000/`

### Terminal 3 (or Browser): Open the app
```bash
# Open in browser
http://localhost:5000
```

Or use curl:
```bash
curl http://localhost:5000/api/health
```

---

## ✅ Verify Everything Works

### Check Ollama is accessible:
```bash
curl http://localhost:11434/api/tags
```

Expected: JSON with available models

### Check Backend is running:
```bash
curl http://localhost:5000/api/health
```

Expected: JSON with status info and available models

### Test the chat endpoint:
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello Qwen!"}'
```

Expected: Response from Qwen model in JSON

---

## 🐛 Troubleshooting

### "Port 11434 still busy"
```bash
# Find what's using it
lsof -i :11434

# Kill the process (replace PID with actual number)
kill -9 <PID>

# Or forcefully kill all Python processes using it
pkill -9 -f ollama
```

### "Flask still giving errors"
```bash
# Make sure you're using the virtual environment
source .venv/bin/activate

# Verify Flask version
python -c "import flask; print(flask.__version__)"

# Should show: 3.1.3 or higher (not 2.3.0)
```

### "Backend can't find Ollama"
```bash
# Make sure Ollama is actually running
ps aux | grep ollama

# Check if it's listening on the port
netstat -tlnp | grep 11434

# Or use curl
curl -v http://localhost:11434/api/tags
```

### "Still getting Flask errors"
1. Delete the virtual environment:
   ```bash
   rm -rf .venv
   ```

2. Create a fresh one:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

3. Try again

---

## 📝 Summary of Changes

| Issue | Fix |
|-------|-----|
| Ollama port busy | Kill old process or use different port |
| Flask AttributeError | Update to Flask 3.1.3 |
| Python 3.14 incompatibility | Flask 3.1.3 supports Python 3.14 |

---

## ✨ Expected Output When Running

### Terminal 1 (Ollama):
```
>>> pulling manifest
>>> pulling 93ab76a93e25
>>> pulling 18e8f2b3b844
>>> pulling 75e83d95e6ad
>>> pulling 2d60b8de896a
>>> pulling 5ac6f3d2d59c
>>> verifying sha256 digest
>>> writing manifest
>>> success
listening on 127.0.0.1:11434
```

### Terminal 2 (Backend):
```
============================================================================
🚀 OLLAMA WEB APP BACKEND STARTING
============================================================================

✓ Backend running on: http://localhost:5000/
✓ Ollama will communicate on: http://localhost:11434/
✓ Using model: qwen

IMPORTANT ENDPOINTS:
  - GET  http://localhost:5000/               (View the app)
  - GET  http://localhost:5000/api/health    (Check status)
  - POST http://localhost:5000/api/chat      (Send messages)

BEFORE RUNNING:
  1. Install dependencies: pip install flask requests
  2. Start Ollama: ollama serve (in another terminal)
  3. Install model: ollama pull qwen

============================================================================

 * Serving Flask app 'backend'
 * Debug mode: on
 * Running on http://localhost:5000
```

### Browser:
- Beautiful chat interface loads
- Ready to chat with Qwen!

---

## 🎯 Now You're Ready!

Try this exact sequence:

```bash
# Terminal 1
lsof -ti:11434 | xargs kill -9 2>/dev/null || true
ollama serve

# Terminal 2 (wait for Ollama to say "listening on...")
cd ~/Desktop/Development/sandbox/ollama_web_app
source .venv/bin/activate
python backend.py

# Terminal 3 or Browser
http://localhost:5000
```

Good luck! 🚀
