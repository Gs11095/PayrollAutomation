#  Import costanti fiscali e funzioni di supporto
from support_functions.parsing import format_italian
from salary_calculator.constants_tax_rules import IRPEF_BRACKETS, INPS_RATE, REGION_TAX_BRACKETS, CITY_TAX_BRACKETS
from salary_calculator.employee import Employee

# Definizione singole funzioni per calcolare breakdown fiscale
#--------------------------------------------------------------------------------------------------------------------------------------------------
# 1) INPS                   --> Calcola il contributo INPS del lavoratore
# 2) TAXABLE INCOME         --> Calcola l'imponibile fiscale dopo contributi INPS
# 3) IMPOSTE PROGRESSIVE    --> Calcola le imposte progressive partendo dagli scaglioni. Utilizzata per IRPEF, REGIONAL TAX e CITY TAX.
# 4) REGIONAL_TAX           --> Calcola l'addizionale regionale
# 5) CITY_TAX               --> Calcola l'addizionale comunale
# -------------------------------------------------------------------------------------------------------------------------------------------------

#1 INPS 
def calculate_inps(ral:float)->float:
    inps_contributions = ral*INPS_RATE
    return inps_contributions

#2 TAXABLE INCOME
def calculate_taxable_income(ral:float, inps_contributions:float)->float:
    taxable_income = ral-inps_contributions
    return taxable_income

#3 IMPOSTE PROGRESSIVE
def calculate_progressive_tax(taxable_income:float, brackets) -> float:
    
    tax = 0.0
    previous_limit = 0.0

    for limit, tax_rate in brackets:
        
        # Se ho un solo bracket l'aliquota non e' progressiva su quanto eccede dal limite
        if len(brackets) == 1:
            # Non contando l'eccedenza l'aliquota sara' nulla per valori minori/uguali all limite e valorizzata per valori maggiori
            if taxable_income <= limit:
                return 0.0
        else:
            return taxable_income * tax_rate
        
        # Procedo col calcolo progressivo
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

def calculate_net_salary(employee):
    # Recupero i dati passati dalla classe employee
    ral = employee.ral
    region = employee.region
    city = employee.city
    months = employee.months
    contract_type = employee.contract_type
    
    inps_contributions = calculate_inps(ral)
    taxable_income = calculate_taxable_income(ral, inps_contributions)

    regional_tax = calculate_regional_tax(taxable_income, region)
    city_tax = calculate_city_tax(taxable_income, city)
    irpef = calculate_progressive_tax(taxable_income, IRPEF_BRACKETS)
    
    total_tax = (inps_contributions + regional_tax + city_tax + irpef)
    net_annual_salary = ral - total_tax
    net_monthly_salary = net_annual_salary/months

    result = {
            'ral': format_italian(ral),
            'region': region,
            'city': city,
            'inps': format_italian(inps_contributions),
            'taxable_income': format_italian(taxable_income),
            'irpef': format_italian(irpef),
            'regional_tax': format_italian(regional_tax),
            'city_tax': format_italian(city_tax),
            'net_annual': format_italian(net_annual_salary),
            'net_monthly': format_italian(net_monthly_salary)
        }
    return result