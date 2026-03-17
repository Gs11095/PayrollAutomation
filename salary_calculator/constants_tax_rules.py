# Costanti

# Contributi INPS a carico del lavoratore
INPS_RATE = 0.0919

# Scaglioni IRPEF - FONTE: Ministero ec. e finanze, Agenzia delle entrate 2025 
IRPEF_BRACKETS = [
    (28000, 0.23),
    (50000, 0.35),
    (float('inf'), 0.43)
]

# Scaglioni addizionale comunale Lombardia, scalabile ad altre regioni - FONTE: Ministero ec. e finanze 2025
REGION_TAX_BRACKETS = {
    "Lombardia" : [
        (15000, 0.0123),
        (28000, 0.0158),
        (50000, 0.0172),
        (float('inf'), 0.0173)
    ]
}

# Scaglioni per addizionale comunale Milano, scalabile ad altre citta' - FONTE: Ministero ec. e finanze 2025
CITY_TAX_BRACKETS= {
    "Milano": [
        (23000, 0.008)       
    ]
}