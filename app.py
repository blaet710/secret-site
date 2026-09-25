from flask import Flask, render_template, request
import os

app = Flask(__name__)

PASSWORD = os.environ.get("PASSWORD")


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    secret = False

    if request.method == "POST":
        password = request.form["password"]

        if password == PASSWORD:
            secret = True
        else:
            message = "비밀번호가 틀렸습니다."

    return render_template(
        "index.html",
        message=message,
        secret=secret
    )


if __name__ == "__main__":
    app.run()