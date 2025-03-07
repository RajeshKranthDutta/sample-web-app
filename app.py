from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Sample Web App!"

@app.route('/about')
def about():
    # Simple logic to simulate some additional feature
    return "This is a sample web app built to demonstrate Flask functionality."

@app.route('/new-feature')
def new_feature():
    # Simulating a new feature that doesn't break the app
    return "This is a new feature added to the app."

if __name__ == "__main__":
    # Ensure the app is reachable and listening on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
