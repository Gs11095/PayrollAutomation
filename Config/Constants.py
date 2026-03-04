#Costanti

SCAGLIONI_IRPEF = [
    (15000, 0.23),
    (28000, 0.25),
    (55000, 0.35),
    (75000, 0.43),
    (float('inf'), 0.43)
]

CONTRIBUTIONS_PERCENT = {"employee": 0.09, "employer": 0.24}

REGIONAL_TAX = {"Lazio": 0.01, "Lombardia": 0.012, "Toscana": 0.009}