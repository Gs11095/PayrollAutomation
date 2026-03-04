from dataclasses import dataclass

@dataclass
class EmployeeInput:
    name: str
    gross_salary: float
    region: str
    contract_type: str

@dataclass
class PayRollResult:
    net_salary: float
    irpef: float
    contributions: float
    regional_tax: float