"""
=============================================================================
PYTHON BACKEND - Web App with Ollama Integration
=============================================================================

This is a simple web server that:
1. Runs on a specific PORT (localhost:5000)
2. Exposes API endpoints (URLs your frontend can request)
3. Handles HTTP requests from the frontend
4. Communicates with Ollama running on its own port (localhost:11435 by default for this project)
5. Returns JSON responses that the frontend displays

KEY CONCEPTS EXPLAINED:
- PORT: A virtual "door" on your computer (5000 for our app, 11435 for Ollama in this project)
- API: Application Programming Interface - rules for how apps communicate
- ENDPOINT: A specific URL path on the API (e.g., /chat, /health)
- REQUEST: Message sent FROM frontend TO backend (with data)
- RESPONSE: Message sent FROM backend TO frontend (with results)
- JSON: Standard format for sending structured data over the web
=============================================================================
"""

from flask import Flask, request, jsonify
import requests
import os
from pathlib import Path
from urllib.parse import urlparse

# ============================================================================
# STEP 1: Create a Flask app instance
# ============================================================================
# Flask is a web framework that makes it easy to create web servers
app = Flask(__name__)

# ============================================================================
# CONSTANTS - Important configuration values
# ============================================================================

# PORT where this Flask server will listen.
# Your browser will access this at: http://localhost:5000 by default.
# You can override it when starting the app:
#   FLASK_PORT=5001 python backend.py
FLASK_PORT = int(os.environ.get("FLASK_PORT", "5000"))

# Ollama runs SEPARATELY and exposes an API. Its built-in default is 11434.
# On many systems, this port is already busy because Ollama runs as a background
# service. If you get a "port already in use" error when running 'ollama serve',
# it means Ollama is already running and you can just start this backend.
#
# To move Ollama to another port, start Ollama and this backend with the same 
# OLLAMA_HOST value:
#   OLLAMA_HOST=127.0.0.1:11435 ollama serve
#
# You can also point the backend at a full URL:
#   OLLAMA_BASE_URL=http://127.0.0.1:11435 python backend.py
DEFAULT_OLLAMA_HOST = "127.0.0.1:11434"
OLLAMA_HOST_SETTING = os.environ.get("OLLAMA_HOST", DEFAULT_OLLAMA_HOST)
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", OLLAMA_HOST_SETTING)

if not OLLAMA_BASE_URL.startswith(("http://", "https://")):
    OLLAMA_BASE_URL = f"http://{OLLAMA_BASE_URL}"

OLLAMA_BASE_URL = OLLAMA_BASE_URL.rstrip("/")
OLLAMA_URL_PARTS = urlparse(OLLAMA_BASE_URL)
OLLAMA_PORT = OLLAMA_URL_PARTS.port or (443 if OLLAMA_URL_PARTS.scheme == "https" else 80)

# The model name to use (must be installed in Ollama).
# You can override it with: MODEL_NAME=llama3.2:1b python backend.py
MODEL_NAME = os.environ.get("MODEL_NAME", "qwen2.5:1.5b")

# ============================================================================
# STEP 2: Define API ENDPOINTS
# ============================================================================
# An endpoint is a specific URL on your server that does something
# When you visit these URLs, specific functions run

@app.route("/", methods=["GET"])
def home():
    """
    ENDPOINT: / (root or home)
    HTTP METHOD: GET
    PURPOSE: Serve the HTML frontend when user visits http://localhost:5000/
    
    Returns: The HTML page (static/index.html)
    """
    return Path("static/index.html").read_text(encoding="utf-8")


@app.route("/api/health", methods=["GET"])
def health_check():
    """
    ENDPOINT: /api/health
    HTTP METHOD: GET
    PURPOSE: Check if backend is running and Ollama is available
    
    This is useful for debugging - you can test this in your browser:
    http://localhost:5000/api/health
    
    Returns: JSON status information
    """
    response_data = {
        "status": "Backend is running!",
        "flask_port": FLASK_PORT,
        "ollama_url": OLLAMA_BASE_URL,
        "ollama_port": OLLAMA_PORT,
        "model": MODEL_NAME
    }
    
    # Try to check if Ollama is running
    try:
        ollama_response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=10)
        if ollama_response.status_code == 200:
            response_data["ollama_status"] = "Ollama is running"
            response_data["available_models"] = [m["name"] for m in ollama_response.json()["models"]]
        else:
            response_data["ollama_status"] = "Ollama is not responding"
    except requests.exceptions.ConnectionError:
        response_data["ollama_status"] = f"ERROR: Cannot connect to Ollama at {OLLAMA_BASE_URL}"
        response_data["help"] = f"Start Ollama with: OLLAMA_HOST={OLLAMA_URL_PARTS.netloc} ollama serve"
    except requests.exceptions.Timeout:
        response_data["ollama_status"] = f"ERROR: Ollama did not respond at {OLLAMA_BASE_URL}"
        response_data["help"] = "Check whether Ollama is running and responsive"
    
    return jsonify(response_data)


@app.route("/api/chat", methods=["POST"])
def chat():
    """
    ENDPOINT: /api/chat
    HTTP METHOD: POST
    PURPOSE: Send a message to Ollama's configured model and get a response
    
    How it works:
    1. Frontend sends a REQUEST (POST) with a message in the body
    2. This function receives the message
    3. We send it to Ollama's API
    4. Ollama processes it with the configured model
    5. We return the response as JSON
    
    REQUEST FORMAT (what frontend sends):
    {
        "message": "What is Python?"
    }
    
    RESPONSE FORMAT (what we send back):
    {
        "message": "Python is a programming language...",
        "model": "qwen2.5:1.5b",
        "status": "success"
    }
    """
    
    # STEP 1: Get the message from the REQUEST
    # request.get_json() reads the body of the POST request as JSON
    data = request.get_json()
    
    if not data or "message" not in data:
        # Return an error if the message is missing
        return jsonify({
            "error": "Message is required",
            "status": "failed"
        }), 400  # 400 = Bad Request error code
    
    user_message = data["message"]
    
    # STEP 2: Create the request to send to Ollama
    # Ollama has its own API running on the configured Ollama port
    # We're making an HTTP request TO Ollama FROM our backend
    ollama_endpoint = f"{OLLAMA_BASE_URL}/api/generate"
    
    ollama_request_data = {
        "model": MODEL_NAME,
        "prompt": user_message,
        "stream": False  # Don't stream - wait for full response
    }
    
    try:
        # STEP 3: Send the request to Ollama
        # This is an HTTP POST request (just like the frontend sent to us)
        ollama_response = requests.post(
            ollama_endpoint,
            json=ollama_request_data,
            timeout=120  # Wait up to 120 seconds for response
        )
        
        # STEP 4: Check if the request was successful
        if ollama_response.status_code == 200:
            response_json = ollama_response.json()
            model_response = response_json.get("response", "No response from model")
            
            # STEP 5: Send response back to frontend
            return jsonify({
                "message": model_response,
                "model": MODEL_NAME,
                "status": "success",
                "user_query": user_message
            })
        else:
            return jsonify({
                "error": f"Ollama returned status {ollama_response.status_code}",
                "status": "failed"
            }), 500  # 500 = Server Error
    
    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": f"Cannot connect to Ollama at {OLLAMA_BASE_URL}",
            "help": f"Start Ollama with: OLLAMA_HOST={OLLAMA_URL_PARTS.netloc} ollama serve",
            "status": "failed"
        }), 503  # 503 = Service Unavailable
    
    except requests.exceptions.Timeout:
        return jsonify({
            "error": "Ollama took too long to respond (120s timeout)",
            "status": "failed"
        }), 504  # 504 = Gateway Timeout
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "failed"
        }), 500


# ============================================================================
# STEP 3: Error Handlers - Handle common errors gracefully
# ============================================================================

@app.route("/api/chat", methods=["OPTIONS"])
def handle_options():
    """
    Handle CORS preflight requests (browser security feature)
    """
    return jsonify({}), 200


# ============================================================================
# STEP 4: Run the server
# ============================================================================

if __name__ == "__main__":
    # Print helpful information
    print("\n" + "="*70)
    print("🚀 OLLAMA WEB APP BACKEND STARTING")
    print("="*70)
    print(f"\n✓ Backend running on: http://localhost:{FLASK_PORT}/")
    print(f"✓ Ollama will communicate at: {OLLAMA_BASE_URL}/")
    print(f"✓ Using model: {MODEL_NAME}\n")
    print("IMPORTANT ENDPOINTS:")
    print(f"  - GET  http://localhost:{FLASK_PORT}/               (View the app)")
    print(f"  - GET  http://localhost:{FLASK_PORT}/api/health    (Check status)")
    print(f"  - POST http://localhost:{FLASK_PORT}/api/chat      (Send messages)")
    print("\nBEFORE RUNNING:")
    print("  1. Install dependencies: python -m pip install -r requirements.txt")
    print(f"  2. Start Ollama: OLLAMA_HOST={OLLAMA_URL_PARTS.netloc} ollama serve (in another terminal)")
    print(f"  3. Install model: ollama pull {MODEL_NAME}")
    print("\n" + "="*70 + "\n")
    
    # Start the Flask server
    # debug=True means the server reloads when you change the code
    app.run(
        host="localhost",  # Only accessible from this computer
        port=FLASK_PORT,
        debug=True  # Auto-reload on code changes
    )
