from salary_calculator.constants_tax_rules import IRPEF_BRACKETS, CITY_TAX_BRACKETS, REGION_TAX_BRACKETS
from salary_calculator.net_salary_calculator import calculate_inps, calculate_taxable_income, calculate_progressive_tax, calculate_regional_tax, calculate_city_tax
from support_functions.parsing import format_italian, parse_ral

#result = calculate_city_tax(12000, "Milano")
#print(result)


#num_formattato = parse_ral("35,000.77")
#print(num_formattato)

#format = format_italian(num_formattato)
#print(format)



result = calculate_regional_tax(35000, "Lombardia")
print(result)