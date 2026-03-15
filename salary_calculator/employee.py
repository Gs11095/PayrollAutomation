# Definizione classe employee

class Employee:

    def __init__(self, 
                 ral: float, 
                 region: str = "Lombardia", 
                 city: str = "Milano", 
                 contract_type: str = "Tempo indeterminato", 
                 months: int = 12):
        self.ral = ral
        self.region = region
        self.city = city
        self.contract_type = contract_type
        self.months = months