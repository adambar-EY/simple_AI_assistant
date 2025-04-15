# Save this file as app.py

# Import necessary libraries
from flask import Flask, request, jsonify
import os # Used for getting port in some hosting environments

# Initialize the Flask application
app = Flask(__name__)

# --- Simple Rule-Based "AI" Logic ---
def get_bot_response(user_message):
    """
    Generates a response based on simple predefined rules.
    Converts the input message to lowercase for case-insensitive matching.
    """
    message = user_message.lower().strip() # Convert to lowercase and remove leading/trailing whitespace

    # Define rules and corresponding responses
    if "hello" in message or "hi" in message or "hey" in message:
        return "Hello there! How can I assist you today?"
    elif "how are you" in message:
        return "I'm a program, so I don't have feelings, but I'm running correctly! Thanks for asking."
    elif "your name" in message:
        return "I am a simple rule-based assistant built with Python and Flask."
    elif "what can you do" in message or "help" in message:
        return "I can respond to simple greetings and questions like 'hello', 'how are you', 'what is your name?', or 'bye'."
    elif "bye" in message or "goodbye" in message or "see you" in message:
        return "Goodbye! Have a nice day."
    else:
        # Default response if no specific rule matches
        return "I'm sorry, I don't understand that yet. Can you try asking something else?"

# --- API Endpoints ---

# Define the main route for handling chat requests via POST method
@app.route("/chat", methods=["POST"])
def chat():
    """
    Handles incoming chat messages sent as JSON.
    Expects JSON payload like: {"message": "user's message here"}
    Returns JSON payload like: {"response": "bot's response here"}
    """
    try:
        # Get the user's message from the JSON data in the request
        user_message = request.json["message"]

        # Check if the message is empty or None
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        # Get the bot's response using the rule-based logic
        bot_response = get_bot_response(user_message)

        # Return the bot's response as JSON
        return jsonify({"response": bot_response})

    except KeyError:
        # Handle cases where the 'message' key is missing in the request JSON
        return jsonify({"error": "Missing 'message' field in JSON payload"}), 400
    except Exception as e:
        # Log the error for debugging (in a real app, use proper logging)
        print(f"An error occurred: {e}")
        # Return a generic error response
        return jsonify({"error": "An internal server error occurred"}), 500

# Define a simple home route (GET request) to check if the server is alive
@app.route("/")
def home():
    """Provides a simple confirmation that the web service is running."""
    return "Simple AI Assistant is up and running!"

# --- Running the Application ---

if __name__ == "__main__":
    app.run(port=5000)

