from flask import Flask, render_template, request
from net_salary_calculator import calculate_net_salary
from support_functions import parse_ral
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        
        ral_input = request.form.get("ral", "").strip()
        print(ral_input)
        
        try:
           # Formatto ral
           ral_parsed = parse_ral(ral_input)
           print(ral_parsed)
           # Lancio funzione calcolatore
           result = calculate_net_salary(ral_parsed, "Lombardia", "Milano", 12)
        
        except:
            result = {"error": "Inserisci un numero valido"}

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)