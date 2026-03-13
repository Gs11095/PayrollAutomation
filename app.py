import os
from flask import Flask, render_template, request
from net_salary_calculator import calculate_net_salary

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        ral_input = request.form.get("ral", "0")
        # qui puoi fare il parsing come hai già implementato
        ral_input = ral_input.replace(".", "").replace(",", ".")
        try:
            ral = float(ral_input)
            result = calculate_net_salary(ral, "lombardia", "milano")
        except:
            result = {"error": "Inserisci un numero valido"}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # usa la porta fornita da Render
    app.run(host="0.0.0.0", port=port)