from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    # Get port from environment variable (default to 5000 if not found)
    port = int(os.environ.get("PORT", 5000))

    # Run the app
    app.run(debug=True, host='0.0.0.0', port=port)
