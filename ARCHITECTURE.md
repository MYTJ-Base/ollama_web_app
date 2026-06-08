"""
================================================================================
ARCHITECTURE OVERVIEW - How Everything Connects
================================================================================

SYSTEM COMPONENTS:

┌─────────────────────────────────────────────────────────────────────────────┐
│                              YOUR COMPUTER                                  │
│                                                                              │
│  ┌─────────────────────────────┐         ┌──────────────────────────────┐  │
│  │   BROWSER (Port: varies)    │         │   OLLAMA (Port: 11434)       │  │
│  │                             │         │                              │  │
│  │  Frontend: HTML + CSS + JS  │         │  AI Model Backend            │  │
│  │  - Chat Interface           │         │  - Qwen Model               │  │
│  │  - Input Box                │         │  - LLM Processing           │  │
│  │  - Message Display          │         │  - Response Generation      │  │
│  │                             │         │                              │  │
│  └────────────┬────────────────┘         └──────────────┬───────────────┘  │
│               │                                         │                   │
│               │ HTTP/JSON                               │ HTTP/JSON         │
│               │ POST /api/chat                          │ POST /api/generate
│               │                                         │                   │
│               ▼                                         ▲                   │
│  ┌─────────────────────────────────────────────────────┴────────────────┐  │
│  │                                                                      │  │
│  │        PYTHON BACKEND (Flask) - Port: 5000                          │  │
│  │                                                                      │  │
│  │  1. Receives HTTP POST from browser                                 │  │
│  │  2. Parses JSON data (user message)                                 │  │
│  │  3. Creates HTTP POST to Ollama API                                 │  │
│  │  4. Waits for Ollama response                                       │  │
│  │  5. Returns response as JSON to browser                             │  │
│  │                                                                      │  │
│  │  Endpoints:                                                         │  │
│  │  - GET  /               → Serve HTML                                │  │
│  │  - GET  /api/health     → Check status                              │  │
│  │  - POST /api/chat       → Process message                           │  │
│  │                                                                      │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘


================================================================================
MESSAGE FLOW - Step by Step
================================================================================

Step 1: USER TYPES MESSAGE
┌──────────────────────┐
│ Browser sees "hello" │
│ User clicks "Send"   │
└──────────────────────┘
           ▼

Step 2: JAVASCRIPT CREATES REQUEST
┌────────────────────────────────────────┐
│ fetch('/api/chat', {                   │
│   method: 'POST',                      │
│   body: JSON.stringify({               │
│     message: "hello"                   │
│   })                                   │
│ })                                     │
└────────────────────────────────────────┘
           ▼

Step 3: HTTP REQUEST TO BACKEND
┌──────────────────────────────────────────────┐
│ POST http://localhost:5000/api/chat HTTP/1.1 │
│ Content-Type: application/json               │
│ Content-Length: 24                           │
│                                              │
│ {"message":"hello"}                          │
└──────────────────────────────────────────────┘
           ▼

Step 4: PYTHON BACKEND RECEIVES REQUEST
┌─────────────────────────────────────────┐
│ @app.route('/api/chat', methods=['POST'])
│ def chat():                              │
│     data = request.get_json()            │
│     user_message = data['message']       │
│     # Extract: "hello"                   │
└─────────────────────────────────────────┘
           ▼

Step 5: BACKEND SENDS TO OLLAMA
┌────────────────────────────────────────────────┐
│ POST http://localhost:11434/api/generate       │
│ Content-Type: application/json                 │
│                                                │
│ {                                              │
│   "model": "qwen2.5:1.5b",                             │
│   "prompt": "hello",                           │
│   "stream": false                              │
│ }                                              │
└────────────────────────────────────────────────┘
           ▼

Step 6: OLLAMA PROCESSES WITH QWEN MODEL
┌─────────────────────────────────────────────┐
│ Qwen Model (Running in Ollama)               │
│ - Receives: "hello"                          │
│ - Processes tokens                           │
│ - Generates response                         │
│ - Output: "Hello! How can I help you today?" │
└─────────────────────────────────────────────┘
           ▼

Step 7: OLLAMA SENDS RESPONSE TO BACKEND
┌────────────────────────────────────────────────────────┐
│ HTTP/1.1 200 OK                                        │
│ Content-Type: application/json                         │
│                                                        │
│ {                                                      │
│   "response": "Hello! How can I help you today?",      │
│   "model": "qwen2.5:1.5b",                                     │
│   "created_at": "2024-06-07T18:00:00Z",              │
│   "done": true                                         │
│ }                                                      │
└────────────────────────────────────────────────────────┘
           ▼

Step 8: BACKEND PROCESSES OLLAMA RESPONSE
┌──────────────────────────────────────────────────┐
│ response_json = ollama_response.json()            │
│ model_response = response_json['response']        │
│ # Extract: "Hello! How can I help you today?"    │
└──────────────────────────────────────────────────┘
           ▼

Step 9: BACKEND SENDS RESPONSE TO FRONTEND
┌──────────────────────────────────────────────────────────┐
│ HTTP/1.1 200 OK                                          │
│ Content-Type: application/json                           │
│                                                          │
│ {                                                        │
│   "message": "Hello! How can I help you today?",         │
│   "model": "qwen2.5:1.5b",                                       │
│   "status": "success",                                   │
│   "user_query": "hello"                                  │
│ }                                                        │
└──────────────────────────────────────────────────────────┘
           ▼

Step 10: FRONTEND RECEIVES RESPONSE
┌─────────────────────────────────────────────────┐
│ .then(response => response.json())               │
│ .then(data => {                                  │
│   addMessage(data.message, 'bot')                │
│   // Display: "Hello! How can I help you today?" │
│ })                                               │
└─────────────────────────────────────────────────┘
           ▼

Step 11: USER SEES RESPONSE
┌────────────────────────────────────────────┐
│ Chat Box:                                  │
│ ┌────────────────────────────────────────┐ │
│ │ 👤 You: hello                          │ │
│ │                                        │ │
│ │ 🤖 Qwen: Hello! How can I help you    │ │
│ │         today?                         │ │
│ └────────────────────────────────────────┘ │
└────────────────────────────────────────────┘


================================================================================
PORT ASSIGNMENTS
================================================================================

YOUR BROWSER
    │
    │ (You type in address bar)
    │ http://localhost:5000
    ▼
┌─────────────────────────────────┐
│ PYTHON BACKEND (Port 5000)      │
│ Flask Server                    │
│ - Listens for HTTP requests     │
│ - Routes requests to functions  │
│ - Sends HTTP responses back     │
└──────────────┬──────────────────┘
               │
               │ (Backend communicates with)
               │ http://localhost:11434
               ▼
            ┌──────────────────────────┐
            │ OLLAMA (Port 11434)      │
            │ AI Service              │
            │ - Receives prompts       │
            │ - Runs Qwen model       │
            │ - Returns responses      │
            └──────────────────────────┘


================================================================================
KEY CONCEPTS SUMMARY
================================================================================

PORT (🚪):
  - Virtual "door" on your computer
  - Each service listens on its own port
  - Port 5000: Our Flask backend
  - Port 11434: Ollama service

API (📋):
  - Rules for how programs communicate
  - Defines what requests look like
  - Defines what responses look like
  - Our API has 3 endpoints: /, /api/health, /api/chat

ENDPOINT (🛣️):
  - Specific path on a server
  - Like a room number in a building
  - /api/chat is the "chat room"
  - Each endpoint does something different

REQUEST (📤):
  - Message sent FROM one program TO another
  - Contains: method (GET/POST), URL, headers, body
  - Browser sends → Backend receives
  - Backend sends → Ollama receives

RESPONSE (📥):
  - Message sent FROM one program TO another
  - Contains: status code, headers, body
  - Ollama sends → Backend receives
  - Backend sends → Browser receives

JSON (📦):
  - Text format for structured data
  - Easy for all languages to read
  - Example: {"message": "hello", "status": "ok"}
  - Used for all request/response bodies

HTTP METHODS (🎯):
  - GET: Retrieve data (no body)
  - POST: Send data (with body)
  - PUT: Update data
  - DELETE: Remove data

STATUS CODES (✓/✗):
  - 200: OK - Success!
  - 400: Bad Request - Bad data
  - 500: Server Error - Backend crashed
  - 503: Service Unavailable - Ollama not running
  - 504: Gateway Timeout - Ollama too slow


================================================================================
FILE STRUCTURE
================================================================================

ollama_web_app/
│
├── backend.py                 ← Python Flask server (Port 5000)
│                             All the endpoint logic
│
├── static/
│   └── index.html            ← Frontend HTML/CSS/JavaScript
│                             Chat interface that users interact with
│
├── requirements.txt          ← Python dependencies
│                             python -m pip install -r requirements.txt
│
├── start.sh                  ← Quick start script
│                             bash start.sh
│
├── README.md                 ← Complete guide
│                             Read this for full understanding
│
└── ARCHITECTURE.md           ← This file!
                             Visual overview of everything


================================================================================
TYPICAL DEVELOPMENT WORKFLOW
================================================================================

Terminal 1: Start Ollama
  $ ollama serve
  → Ollama starts on port 11434

Terminal 2: Start Backend
  $ python backend.py
  → Flask starts on port 5000

Terminal 3 (Browser): Open Frontend
  → Visit http://localhost:5000
  → Chat loads
  → Type message
  → Flow: Browser → Backend (5000) → Ollama (11434) → Response flows back

Real-world example:
  You: "What is Python?"
  Browser sends to Port 5000
  Port 5000 sends to Port 11434
  Port 11434 returns: "Python is a programming language..."
  Port 5000 returns to Browser
  You see: "Python is a programming language..."


================================================================================
"""

print(__doc__)
