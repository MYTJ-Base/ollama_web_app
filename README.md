# 🤖 Ollama Web App - Learn Web Development Concepts

A **fully self-explanatory** web application that demonstrates important web development concepts through a working chatbot powered by Qwen (via Ollama).

## 📚 What You'll Learn

This project teaches you:

- **PORTS**: How different services communicate on different ports
  - Port 5000: Your Python backend
  - Port 11434: Ollama AI backend
  
- **APIs**: Application Programming Interfaces (rules for communication)
  - `/api/health` - Check system status
  - `/api/chat` - Send/receive messages
  
- **HTTP METHODS**: Different types of requests
  - `GET`: Request data (no body needed)
  - `POST`: Send data to the server
  
- **REQUEST/RESPONSE CYCLE**: How data flows through the web
  - Frontend sends HTTP request
  - Backend processes it
  - Backend sends HTTP response
  - Frontend displays the response
  
- **JSON**: Standard format for exchanging data over the web
  
- **CLIENT-SERVER ARCHITECTURE**: Frontend and backend working together

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** - [Download](https://www.python.org/downloads/)
   - *Note: If using Python 3.14+, you must use Flask 3.1.0 or newer.*
2. **Ollama** - [Download](https://ollama.ai)
3. **Qwen Model** - Will download automatically

### Step 1: Install Dependencies

```bash
cd ollama_web_app
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Step 2: Start Ollama (in a separate terminal)

If `11434` is already in use by Ollama, you can skip this step because Ollama is already running.

```bash
ollama serve
```

You should see:
```
listening on 127.0.0.1:11434
```

### Step 3: Download the Qwen Model (first time only)

In another terminal:
```bash
ollama pull qwen2.5:1.5b
```

This downloads the Qwen model. You only need to do this once.

### Step 4: Start the Python Backend

```bash
source .venv/bin/activate
python backend.py
```

You should see:
```
🚀 OLLAMA WEB APP BACKEND STARTING
========================================
✓ Backend running on: http://localhost:5000/
✓ Ollama will communicate at: http://127.0.0.1:11434/
✓ Using model: qwen2.5:1.5b

IMPORTANT ENDPOINTS:
  - GET  http://localhost:5000/               (View the app)
  - GET  http://localhost:5000/api/health    (Check status)
  - POST http://localhost:5000/api/chat      (Send messages)
```

### Step 5: Open Your Browser

Go to: **http://localhost:5000**

Start chatting with Qwen!

## 📁 Project Structure

```
ollama_web_app/
├── backend.py              # Python backend (Flask server)
├── static/
│   └── index.html         # Frontend (HTML, CSS, JavaScript)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔍 Understanding the Architecture

### How It Works

```
Browser (Frontend)
    ↓
    ├─ User types message
    ├─ JavaScript creates fetch() request
    ├─ HTTP POST to http://localhost:5000/api/chat
    ↓
Python Backend (Port 5000)
    ├─ Flask receives request
    ├─ Parses JSON data
    ├─ Creates new HTTP request
    ├─ HTTP POST to http://localhost:11434/api/generate
    ↓
Ollama (Port 11434)
    ├─ Receives message
    ├─ Processes with Qwen model
    ├─ Generates response
    ├─ Returns JSON
    ↓
Python Backend
    ├─ Receives response from Ollama
    ├─ Creates JSON response
    ├─ Sends HTTP response back to browser
    ↓
Browser (Frontend)
    ├─ JavaScript receives response
    ├─ Parses JSON
    ├─ Displays message in chat
    └─ Done! ✓
```

## 📖 Code Walkthrough

### Backend (backend.py)

**Key Components:**

1. **Imports**
   ```python
   from flask import Flask, request, jsonify
   import requests
   ```
   - Flask: Web server framework
   - requests: Make HTTP requests to Ollama

2. **Port Configuration**
   ```python
   FLASK_PORT = int(os.environ.get("FLASK_PORT", "5000"))
   OLLAMA_BASE_URL = "http://127.0.0.1:11434"
   ```

3. **Endpoints (API Routes)**
   ```python
   @app.route("/", methods=["GET"])
   # Serves the HTML frontend
   
   @app.route("/api/health", methods=["GET"])
   # Check if everything is running
   
   @app.route("/api/chat", methods=["POST"])
   # Process messages and send to Ollama
   ```

4. **Request/Response Flow**
   ```python
   # 1. Receive request from frontend
   data = request.get_json()
   
   # 2. Send request to Ollama
   ollama_response = requests.post(ollama_endpoint, json=data)
   
   # 3. Send response back to frontend
   return jsonify(response_data)
   ```

### Frontend (index.html)

**Key Components:**

1. **HTML Structure**
   - Chat display area
   - Message input box
   - Send button

2. **CSS Styling**
   - Modern gradient design
   - User vs Bot message styling
   - Loading animations

3. **JavaScript**
   ```javascript
   // Send message function
   async function sendMessage() {
       // 1. Get user input
       const message = messageInput.value;
       
       // 2. Create request
       const requestBody = { message: message };
       
       // 3. Send to backend
       const response = await fetch('/api/chat', {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify(requestBody)
       });
       
       // 4. Display response
       const data = await response.json();
       addMessage(data.message, 'bot');
   }
   ```

## 🧪 Testing the API

### Test the Health Endpoint

Open in browser or use curl:
```bash
curl http://localhost:5000/api/health
```

Response:
```json
{
  "status": "Backend is running!",
  "flask_port": 5000,
  "ollama_url": "http://127.0.0.1:11434",
  "ollama_port": 11434,
  "model": "qwen2.5:1.5b",
  "ollama_status": "Ollama is running",
  "available_models": ["qwen2.5:1.5b"]
}
```

### Test the Chat Endpoint

Using curl:
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Python?"}'
```

## 🐛 Troubleshooting

### "Cannot connect to Ollama on port 11434"

**Solution:**
```bash
# Terminal 1: Start Ollama
OLLAMA_HOST=127.0.0.1:11434 ollama serve

# Terminal 2: Pull Qwen model
ollama pull qwen2.5:1.5b

# Terminal 3: Run the app
source .venv/bin/activate
python backend.py
```

### "Port 11434 is already in use"

Ollama's built-in default is `127.0.0.1:11434`. On many Linux systems, Ollama runs as a background system service automatically. If you see this error, it means **Ollama is already running and ready to use**. You do not need to run `ollama serve` manually.

You can check if the service is active with:
```bash
systemctl is-active ollama
```

If you still want to use a different Ollama port:
```bash
OLLAMA_HOST=127.0.0.1:11435 ollama serve
```

The backend defaults to `127.0.0.1:11434`. To use another port, start both processes with the same value:
```bash
OLLAMA_HOST=127.0.0.1:11500 ollama serve
OLLAMA_HOST=127.0.0.1:11500 python backend.py
```

If you start a new Ollama server on a new port, that server may have an empty model directory. Pull the model on that same port:
```bash
OLLAMA_HOST=127.0.0.1:11435 ollama pull qwen2.5:1.5b
```

### "AttributeError: module 'pkgutil' has no attribute 'get_loader'"

**Solution:**
This happens on Python 3.14+ when using an old version of Flask. Upgrade Flask to version 3.1 or newer:
```bash
pip install --upgrade flask werkzeug
```

### Browser shows "Cannot reach backend"

**Solution:**
- Make sure backend is running: `python backend.py`
- Check that it says "running on http://localhost:5000"
- No firewall blocking port 5000

### Model is slow to respond

**Solution:**
- Qwen is running on your CPU (unless you have GPU)
- First response takes longer as model loads into memory
- Subsequent responses are faster
- Be patient - AI takes time! ⏳

### Port already in use

**Solution:**
```bash
# Kill the process using port 5000
lsof -ti:5000 | xargs kill -9

# Or change the port in backend.py
FLASK_PORT = 5001  # Use different port
```

## 📚 Learning Resources

### Web Concepts

1. **HTTP Methods**: [MDN - HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
2. **REST APIs**: [REST API Guide](https://restfulapi.net/)
3. **JSON**: [JSON Tutorial](https://www.w3schools.com/js/js_json.asp)
4. **Ports**: [Network Ports Explained](https://www.lifewire.com/network-ports-3291066)

### Technologies Used

- **Flask**: [Flask Documentation](https://flask.palletsprojects.com/)
- **Fetch API**: [MDN - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- **Ollama**: [Ollama Documentation](https://github.com/ollama/ollama)

## 🎨 Customize It!

### Change the Model

Edit `backend.py`:
```python
MODEL_NAME = "mistral"  # or "llama2", "neural-chat", etc.
```

Then pull it:
```bash
ollama pull mistral
```

### Change the Port

Edit `backend.py`:
```python
FLASK_PORT = 8000  # Use 8000 instead of 5000
```

### Add More Features

- Conversation history (save to file/database)
- Multiple models selection
- Response streaming
- User authentication
- Persistent chat storage

## 📝 HTTP Status Codes Reference

| Code | Meaning | When Used |
|------|---------|-----------|
| 200 | OK | Request successful ✓ |
| 400 | Bad Request | Missing/invalid data |
| 500 | Server Error | Backend crashed |
| 503 | Service Unavailable | Ollama not running |
| 504 | Gateway Timeout | Ollama too slow |

## 🔐 Security Note

This is a **learning project** and runs on `localhost` only (your computer). 

For production:
- Never expose on the internet without authentication
- Validate all user input
- Use HTTPS instead of HTTP
- Add rate limiting
- Use environment variables for secrets

## 💡 Key Takeaways

After working with this project, you understand:

✅ How ports separate different services  
✅ How APIs define communication rules  
✅ How HTTP requests/responses work  
✅ How JSON transfers data  
✅ How frontend and backend communicate  
✅ How to call external APIs from your backend  
✅ How to handle errors gracefully  

## 📞 Need Help?

Check the comments in the code - every concept is explained!

- `backend.py`: Backend explanation
- `static/index.html`: Frontend explanation

## 🚀 Next Steps

1. **Modify** the frontend UI
2. **Add** new API endpoints
3. **Experiment** with different models
4. **Deploy** to a real server (Heroku, AWS, etc.)
5. **Add** a database to save conversations

## 📄 License

Free to use for learning purposes!

---

**Happy Learning! 🎓**
