from Config.Constants import SCAGLIONI_IRPEF

def calculate_irpef(gross_salary:float) -> float:
    irpef = 0
    for limite, aliquota in SCAGLIONI_IRPEF:
        if imponibile == gross_salary
            break 
        imponibile = min((limite[1] - limite[0]), gross_salary)
        irpef = irpef + (imponibile * aliquota)
        gross_salary = gross_salary - imponibile
    return irpef