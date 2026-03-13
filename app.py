from flask import Flask, render_template, request
from net_salary_calculator import calculate_net_salary

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":
        ral = float(request.form["ral"])

        result = calculate_net_salary(
            RAL=ral,
            region="lombardia",
            city="milano"
        )

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)