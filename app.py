from flask import Flask

from flask import redirect, url_for, request, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


# Flask web app
@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()