from flask import Flask, render_template, request
from net_salary_calculator import calculate_net_salary

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        raw_ral = request.form.get("ral", "").strip()

        # Pulizia della stringa per gestire input italiani o inglesi
        # es: 40.000 → 40000, 40,500 → 40.500
        cleaned_ral = raw_ral.replace('.', '').replace(',', '.')
        
        try:
            ral_float = float(cleaned_ral)
            # calcolo netto
            result = calculate_net_salary(ral_float, region="Lombardia", city="Milano")
        except ValueError:
            error = "Inserisci una RAL valida!"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)