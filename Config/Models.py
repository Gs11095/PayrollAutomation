from dataclasses import dataclass

@dataclass
class RAL_Input:
    gross_salary: float
    region: str
    contract_type: str

@dataclass
class Net_Output:
    net_salary: float
    irpef: float
    contributions: float
    regional_tax: float