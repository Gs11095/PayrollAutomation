#  Import costanti fiscali

from constants_tax_rules import IRPEF_BRACKETS, INPS_RATE, REGION_TAX_BRACKETS, CITY_TAX_BRACKETS
# Definizione singole funzioni per calcolare breakdown fiscale
#--------------------------------------------------------------------------------------------------------------------------------------------------
# 1) INPS                   --> Calcola il contributo INPS del lavoratore
# 2) TAXABLE INCOME         --> Calcola l'imponibile fiscale dopo contributi INPS
# 3) IRPEF e REGIONAL TAX   --> Calcola le imposte progressive partendo dagli scaglioni. Utilizzata per IRPEF, REGIONAL TAX e CITY TAX.
# 4) REGIONAL_TAX           --> Calcola l'addizionale regionale
# 5) CITY_TAX               --> Calcola l'addizionale comunale
# -------------------------------------------------------------------------------------------------------------------------------------------------

#1 INPS 
def calculate_inps(RAL:float)->float:
    inps_contributions = RAL*INPS_RATE
    return inps_contributions

#2 TAXABLE INCOME
def calculate_taxable_income(RAL:float, inps_contributions:float)->float:
    taxable_income = RAL-inps_contributions
    return taxable_income

#3 IRPEF, REGIONAL TAX
def calculate_progressive_tax(taxable_income:float, brackets) -> float:
    
    tax = 0.0
    previous_limit = 0.0

    for limit, tax_rate in brackets:
        taxable_amount = min(limit, taxable_income) - previous_limit
        
        if taxable_amount <= 0:
            break 
        
        tax += taxable_amount * tax_rate
        previous_limit = limit
    return tax                  

#4 REGIONAL TAX
def calculate_regional_tax(taxable_income:float, region):
    brackets = REGION_TAX_BRACKETS[region]
    return calculate_progressive_tax(taxable_income, brackets)

#5 CITY TAX
def calculate_city_tax(taxable_income:float, city):
    brackets = CITY_TAX_BRACKETS[city]
    return calculate_progressive_tax(taxable_income, brackets)



# ---------------------------------------------------------------------------------------------------------------

# Funzione main orchestratrice del flusso, esegue le funzioni sopra per calcolare l'intero breakdown fiscale

def calculate_net_salary(RAL:float, region:str, city:str):
    
    inps_contributions = calculate_inps(RAL)
    taxable_income = calculate_taxable_income(RAL, inps_contributions)

    regional_tax = calculate_regional_tax(taxable_income, region)
    city_tax = calculate_city_tax(taxable_income, city)
    irpef = calculate_progressive_tax(taxable_income, IRPEF_BRACKETS)
    
    total_tax = (inps_contributions + regional_tax + city_tax + irpef)
    net_annual_salary = RAL - total_tax
    net_monthly_salary = net_annual_salary/12

    return {
                'ral': round(RAL,2),
                'region': region,
                'city': city,
                'inps': round(inps_contributions,2),
                'taxable_income': round(taxable_income,2),
                'irpef': round(irpef,2),
                'regional_tax': round(regional_tax,2),
                'city_tax': round(city_tax,2),
                'net_annual': round(net_annual_salary,2),
                'net_monthly': round(net_monthly_salary,2)
            }