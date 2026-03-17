# Definizione classe employee

class Employee:

    def __init__(self, 
                 ral: float,
                 #months: int, 
                 region: str = "Lombardia", 
                 city: str = "Milano", 
                 contract_type: str = "Tempo indeterminato", 
                 months = 12
                 ):
        self.ral = ral
        #self.months = months
        self.region = region
        self.city = city
        self.contract_type = contract_type
        self.months = months