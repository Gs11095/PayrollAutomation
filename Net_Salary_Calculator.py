#  Import costanti fiscali

from Config.Constants_Tax_Rules import SCAGLIONI_IRPEF, INPS_RATE, REGIONAL_TAX_RATE, CITY_TAX_RATE


# Definizione singole funzioni per calcolare breakdown fiscale
# 1) INPS --> Calcola l'imponibile fiscale dopo la detrazione del contributo INPS del lavoratore
# 2) REGIONAL_TAX --> Calcola l'addizionale regionale
# 3) CITY_TAX --> Calcola l'addizionale comunale
# 4) IRPEF --> Calcola l'IRPEF 
# --------------------------------------------------------------------------------------------------------------

#1 INPS 
def calculate_inps(RAL:float)->float:
    inps_contributions = RAL*INPS_RATE
    return inps_contributions

#2 TAXABLE INCOME
def calculate_taxable_income(RAL:float, inps_contributions:float)->float:
    taxable_income = RAL-inps_contributions
    return taxable_income

#3 REGIONAL TAX 
def calculate_regional_tax(imponibile:float)->float:
    addizionale_regionale = imponibile*REGIONAL_TAX_RATE
    return addizionale_regionale

#4 CITY TAX 
def calculate_city_tax(imponibile:float)->float:
    addizionale_comunale = imponibile*CITY_TAX_RATE
    return addizionale_comunale

#5 IRPEF
def calculate_irpef(taxable_income:float) -> float:
    
    irpef = 0.0
    previous_limite = 0.0

    for limite, aliquota in SCAGLIONI_IRPEF:
        taxable_amount = min(limite, taxable_income) - previous_limite
        
        if taxable_amount <= 0:
            break 
        
        irpef += taxable_amount * aliquota
        previous_limite = limite
        
      
    return irpef                      


# ---------------------------------------------------------------------------------------------------------------

# Funzione main orchestratrice del flusso, esegue le funzioni sopra per calcolare l'intero breakdown fiscale

def calculate_net_salary(RAL:float):
    
    inps_contributions = calculate_inps(RAL)
    taxable_income = calculate_taxable_income(RAL, inps_contributions)

    regional_tax = calculate_regional_tax(taxable_income)
    city_tax = calculate_city_tax(taxable_income)
    irpef = calculate_irpef(taxable_income)
    
    net_annual_salary = RAL - (inps_contributions + regional_tax + city_tax + irpef)
    net_monthly_salary = net_annual_salary/12

    return {
                'ral': RAL,
                'inps': inps_contributions,
                'taxable_income': taxable_income,
                'irpef': irpef,
                'regional_tax': regional_tax,
                'city_tax': city_tax,
                'net_annual': net_annual_salary,
                'net_monthly': net_monthly_salary
            }

result = calculate_net_salary(40000)
print(result)