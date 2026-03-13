#Costanti

# Contributi INPS a carico del lavoratore
INPS_RATE = 0.0919

# Scaglioni IRPEF
IRPEF_BRACKETS = [
    (15000, 0.23),
    (28000, 0.25),
    (55000, 0.35),
    (75000, 0.43),
    (float('inf'), 0.43)
]

# Scaglioni addizionale comunale Lombardia, scalabile ad altre regioni
REGIONAL_TAX_BRACKETS = {
    "lombardia" : [
        (15000, 0.0123),
        (28000, 0.0158,)
        (50000, 0.0172)
        (float('inf'), 0.0173)
    ]
}

# Scaglioni per addizionale comunale Milano, scalabile ad altre citta'
CITY_TAX_BRACKET= {
    "milano": [
        (23000, 0.0),       
        (float("inf"), 0.008)
    ]
}