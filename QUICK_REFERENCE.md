"""
╔════════════════════════════════════════════════════════════════════════════╗
║                     OLLAMA WEB APP - QUICK REFERENCE                       ║
╚════════════════════════════════════════════════════════════════════════════╝

📋 PROJECT OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A self-explanatory web application that demonstrates:
  ✓ Web development architecture
  ✓ HTTP requests and responses
  ✓ APIs and endpoints
  ✓ Ports and services
  ✓ Frontend-Backend communication
  ✓ Integration with external services

Everything is heavily commented for learning!


🚀 QUICK START (3 Steps)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Terminal A - Start Ollama
  $ ollama serve

Step 2: Terminal B - Start Backend
  $ cd ollama_web_app
  $ pip install -r requirements.txt
  $ python backend.py

Step 3: Browser - Open App
  → http://localhost:5000
  → Start chatting!


📁 FILE GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─ BACKEND (Python)
│
├─ backend.py (240 lines)
│  • Flask server on port 5000
│  • 3 endpoints: /, /api/health, /api/chat
│  • Communicates with Ollama on port 11434
│  • Every line is explained
│  • Key concepts:
│    - Flask framework
│    - HTTP requests/responses
│    - JSON parsing
│    - Error handling
│
└─ requirements.txt
   • Flask: Web server
   • Requests: HTTP client


┌─ FRONTEND (JavaScript, HTML, CSS)
│
└─ static/index.html (456 lines)
   • Beautiful chat interface
   • HTML structure
   • CSS styling & animations
   • JavaScript fetch() API
   • Every function explained
   • Key concepts:
     - async/await
     - fetch() for HTTP requests
     - DOM manipulation
     - Event listeners


┌─ DOCUMENTATION
│
├─ README.md (389 lines)
│  • Complete setup guide
│  • Architecture explanation
│  • Troubleshooting section
│  • Learning resources
│
├─ ARCHITECTURE.md (307 lines)
│  • Visual message flow
│  • ASCII diagrams
│  • Port assignments
│  • Step-by-step breakdown
│
├─ start.sh (60 lines)
│  • Quick start script
│  • Checks dependencies
│  • Verifies Ollama is running
│  • Starts backend with logging
│
└─ QUICK_REFERENCE.md (This file!)
   • Overview of everything
   • Common commands
   • Concepts explained


🔌 PORTS & SERVICES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Port 5000:  Python Backend (Flask)
            - What: Your web server
            - Access: http://localhost:5000
            - Running: python backend.py

Port 11434: Ollama Service
            - What: AI model backend
            - Access: http://localhost:11434
            - Running: ollama serve

Browser:    HTTP Client
            - What: Firefox, Chrome, Safari, etc.
            - Purpose: Views your app


🔌 API ENDPOINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GET http://localhost:5000/
  Purpose: Serve the chat interface
  Returns: HTML page
  Use: Open in browser

GET http://localhost:5000/api/health
  Purpose: Check if everything is running
  Returns: JSON status info
  Use: Verify system is ready

POST http://localhost:5000/api/chat
  Purpose: Send message, get response
  Sends: {"message": "Your question"}
  Returns: {"message": "Response", "status": "success"}
  Use: Frontend sends messages here


📊 MESSAGE FLOW (4 Steps)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. User Types in Browser
   "What is Python?"
        ↓

2. Frontend Sends HTTP POST to Backend
   fetch('/api/chat', { body: {"message": "What is Python?"} })
        ↓

3. Backend Forwards to Ollama
   requests.post('http://localhost:11434/api/generate', data)
        ↓

4. Response Flows Back
   Ollama → Backend → Browser → Display to User


🎯 KEY CONCEPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PORT
  Definition: Virtual "door" for services on your computer
  Example: 5000, 11434, 3000, 8080
  Why: Multiple services can't use same port
  Used in: http://localhost:5000

API
  Definition: Contract between client & server
  Contains: Endpoints, methods, formats
  Example: Our /api/chat endpoint
  Purpose: Define how programs communicate

ENDPOINT
  Definition: Specific URL path on a server
  Examples: /, /api/health, /api/chat
  Method: GET (retrieve) or POST (send data)
  Returns: Usually JSON

HTTP METHOD
  GET:    Request data (no body)
  POST:   Send data (with body)
  PUT:    Update existing data
  DELETE: Remove data

REQUEST
  Definition: Message FROM client TO server
  Parts: Method, URL, headers, body
  Format: Usually JSON for body
  Example: POST /api/chat with {"message": "..."}

RESPONSE
  Definition: Message FROM server TO client
  Parts: Status code, headers, body
  Status: 200 (OK), 400 (error), 500 (server error)
  Format: Usually JSON

JSON
  Definition: Text format for data
  Readable by: All programming languages
  Example: {"name": "Qwen", "type": "AI"}
  Used: All requests and responses

fetch() API
  Definition: JavaScript way to make HTTP requests
  Returns: Promise (wait for response)
  Syntax: fetch(url, options).then().catch()
  Modern: async/await syntax


💻 COMMON COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Setup:
  pip install -r requirements.txt     Install Python packages
  ollama pull qwen                    Download Qwen model

Running:
  ollama serve                        Start Ollama (Terminal 1)
  python backend.py                   Start Flask (Terminal 2)
  bash start.sh                       Use quick start script

Testing (Terminal 3):
  curl http://localhost:5000/api/health
                                      Test health endpoint
  curl -X POST http://localhost:5000/api/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "hello"}'         Test chat endpoint

Troubleshooting:
  lsof -ti:5000 | xargs kill -9      Kill port 5000
  ps aux | grep ollama                Check if Ollama running
  curl http://localhost:11434/api/tags
                                      Check Ollama API


🔍 UNDERSTANDING CODE LOCATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Want to learn about...         Look in file...
─────────────────────────────────────────────────────
Ports & Configuration          backend.py (lines 20-35)
Flask Setup                     backend.py (lines 37-41)
API Endpoints                   backend.py (lines 45-240)
Request/Response Flow           backend.py (lines 120-150)
Ollama Integration              backend.py (lines 122-125)
Error Handling                  backend.py (lines 155-180)

Frontend UI                     static/index.html (lines 1-200)
CSS Styling                     static/index.html (lines 10-150)
HTML Structure                  static/index.html (lines 210-280)
JavaScript Functions            static/index.html (lines 285-456)
fetch() Implementation          static/index.html (lines 330-380)
Message Handling                static/index.html (lines 385-420)
Event Listeners                 static/index.html (lines 440-456)


⚠️ TROUBLESHOOTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Problem: "Cannot connect to Ollama"
Solution:
  1. Open new terminal
  2. Run: ollama serve
  3. Run: ollama pull qwen
  4. Retry

Problem: "Port 5000 already in use"
Solution:
  lsof -ti:5000 | xargs kill -9
  Or change FLASK_PORT = 5001 in backend.py

Problem: "Empty responses from Qwen"
Solution:
  1. Verify Ollama running: curl localhost:11434/api/tags
  2. Check model installed: ollama list
  3. Restart: Kill Ollama, restart with "ollama serve"

Problem: "Slow first response"
Solution:
  Normal! Model loads into memory first time.
  Subsequent responses are faster.

Problem: "Frontend won't load"
Solution:
  1. Check backend running: python backend.py
  2. Wait 10 seconds for server to start
  3. Visit http://localhost:5000 (not 5001 or other port)


📚 LEARNING PATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Read this file (overview)
   ↓
2. Read ARCHITECTURE.md (visual diagrams)
   ↓
3. Read README.md (complete guide)
   ↓
4. Open backend.py, read all comments
   ↓
5. Open static/index.html, read all comments
   ↓
6. Run the app and use it
   ↓
7. Try modifying the code:
   - Change model: backend.py line 34
   - Change port: backend.py line 24
   - Change UI: static/index.html


🎓 WHAT YOU'LL LEARN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Web Development Fundamentals:
  ✓ How web servers work
  ✓ How HTTP requests work
  ✓ How APIs are structured
  ✓ How ports separate services
  ✓ How JSON transfers data
  ✓ How frontend/backend communicate

Python Backend:
  ✓ Flask framework
  ✓ Routing and endpoints
  ✓ Request/response handling
  ✓ Making HTTP requests to other APIs
  ✓ Error handling
  ✓ JSON parsing

Frontend:
  ✓ HTML structure
  ✓ CSS styling and animations
  ✓ JavaScript fetch() API
  ✓ Async/await syntax
  ✓ DOM manipulation
  ✓ Event handling

Real-world Skills:
  ✓ Integration with external APIs
  ✓ Debugging HTTP issues
  ✓ Understanding request/response cycles
  ✓ Basic error handling


✨ NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Easy:
  • Change the model (backend.py line 34)
  • Change colors (static/index.html line 30-40)
  • Add more endpoints
  • Save chat history

Medium:
  • Add a database (SQLite)
  • Add user authentication
  • Add model selection dropdown
  • Stream responses

Hard:
  • Deploy to cloud (Heroku, AWS)
  • Add WebSocket for real-time updates
  • Build mobile app
  • Add conversation history with persistence


🔗 USEFUL RESOURCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Flask:       https://flask.palletsprojects.com/
JavaScript:  https://developer.mozilla.org/en-US/docs/Web/JavaScript
HTTP:        https://developer.mozilla.org/en-US/docs/Web/HTTP
JSON:        https://www.json.org/
Ollama:      https://github.com/ollama/ollama
REST API:    https://restfulapi.net/


📞 GETTING HELP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Every part of the code is commented!
  • Read the comments in backend.py
  • Read the comments in static/index.html
  • Check README.md troubleshooting section
  • Review ARCHITECTURE.md for flow diagrams


════════════════════════════════════════════════════════════════════════════════
                          Happy Learning! 🚀
════════════════════════════════════════════════════════════════════════════════
"""

print(__doc__)
