from flask import Flask, render_template, request
from salary_calculator.net_salary_calculator import calculate_net_salary
from support_functions.parsing import parse_ral
import os
from salary_calculator.employee import Employee

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calcola_ral():
    result = None
    error = None

    if request.method == "POST":
        
        ral_input = request.form.get("ral", "").strip()
        #months = request.form.get("months", "").strip()
        #months_int = int(months)
        print(ral_input)
        
        try:
           # Formatto ral
           ral_parsed = parse_ral(ral_input)
           print(ral_parsed)
        
           # Creo l'oggetto con soltanto la ral perche gli altri valori sono costanti della classe
           employee = Employee(ral=ral_parsed) #months=months_int)

           # Lancio funzione calcolatore
           result = calculate_net_salary(employee)
        
        except:
            result = {"error": "Inserisci un numero valido"}

    return render_template("index.html", result=result, error=error)

# Faccio partire l'app soltanto se eseguita direttamente
# Mi collego alla porta inserita in variabile ambiente oppure alla 5000
# Avvio server flask accesibile da qualsiasi IP
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)