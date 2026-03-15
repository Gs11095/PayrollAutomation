
import re

# Funzioni di supporto per formattare i numeri

#   1. format_italian    --> formatta il valore in output con i separatori usati in italia
#   2. parse_ral         --> formatta la ral in input per poter essere elaborata piu facilmente dal calcolatore e la restituisce come float

def format_italian(number: float) -> str:
    if number == 0:
        return "0"
    # Separatore migliaia in inglese
    num_formattato = "{:,.2f}".format(number)
    num_formattato = num_formattato.replace(',', 'X').replace('.', ',').replace('X', '.')

    if num_formattato.endswith(',00'):
        num_formattato = num_formattato[:-3]
    return num_formattato

# -------------------------------------------------------------------------------------------------------------------------------------------

def parse_ral(ral_input: str) -> float:
    if re.search(r"[.,]{2,}", ral_input) or re.search(r"[^0-9.,]", ral_input):
        raise ValueError("Formato numero non valido")

    ral_input = ral_input.strip().replace(" ", "")

    if not ral_input or ral_input == "0":
        return 0.0

    # Se format italiano
    if "," in ral_input and "." in ral_input:
        if ral_input.rfind(",") > ral_input.rfind("."):
            ral_input = ral_input.replace(".", "").replace(",", ".")
        else:
            # Se format europeo
            ral_input = ral_input.replace(",", "")
    elif "," in ral_input:
        # Se soltanto virgola
        ral_input = ral_input.replace(",", "")
    elif "." in ral_input:
        # Se soltanto punto (capisco se e' separatore migliaia o decimali con max 2 cifre)
        parts = ral_input.split(".")
        if len(parts[-1]) == 3:
            ral_input = "".join(parts)

    return float(ral_input)