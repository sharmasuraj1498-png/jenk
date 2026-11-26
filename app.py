from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My To-Do App surai  is op webhook done again </h1>
    <p>Deployed using Jenkins CI/CD</p>
    <p>Version 1.0</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
