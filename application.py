import os
from flask import Flask, render_template, request
 
application = Flask('application')

@application.route("/")
def root():
    return render_template("index.html")


@application.route("/help")
def helppage():
    return render_template("help.html")


@application.route("/hello")
def index():
    return "Hello World from Flask Hello Page.<b> v1.0"


@application.route("/run", methods=["POST"])
def run_command():
    command = request.form.get("cmd")  # Getting user input
    output = os.popen(command).read()  # Insecure: allows command injection
    return f"Command output: <pre>{output}</pre>"


# --------Main------------------
if __name__ == "__main__":
    application.run(debug=True)
# ------------------------------


