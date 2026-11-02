from flask import Flask, render_template, request
from password_utils import generate_password, rate_password

app = Flask(__name__)

MIN_LEN = 8
MAX_LEN = 15


def default_options():
    return {
        "length": 12,
        "upper": True,
        "lower": True,
        "digits": True,
        "symbols": True,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    opts = default_options()
    result = {}

    if request.method == "POST":
        try:
            length = int(request.form.get("length", 12))
        except (TypeError, ValueError):
            length = 12

        opts = {
            "length": length,
            "upper": request.form.get("upper") == "on",
            "lower": request.form.get("lower") == "on",
            "digits": request.form.get("digits") == "on",
            "symbols": request.form.get("symbols") == "on",
        }

        if not MIN_LEN <= length <= MAX_LEN:
            result = {"error": f"Choose a password length between {MIN_LEN} and {MAX_LEN}."}
        elif not any(opts[key] for key in ("upper", "lower", "digits", "symbols")):
            result = {"error": "Select at least one character type."}
        else:
            password = generate_password(
                length=length,
                uppercase=opts["upper"],
                lowercase=opts["lower"],
                digits=opts["digits"],
                symbols=opts["symbols"],
            )
            result = {"password": password, "complexity": rate_password(password)["level"]}

    return render_template(
        "index.html",
        result=result,
        opts=opts,
        min_len=MIN_LEN,
        max_len=MAX_LEN,
    )


if __name__ == "__main__":
    app.run(debug=True)
