def format_italian(number: float) -> str:
    if number == 0:
        return "0"
    # separatore migliaia in inglese
    num_formattato = "{:,.2f}".format(number)
    # sostituzione per stile italiano
    num_formattato = num_formattato.replace(',', 'X').replace('.', ',').replace('X', '.')
    # rimuovo ",00" se i decimali sono zero
    if num_formattato.endswith(',00'):
        num_formattato = num_formattato[:-3]
    return num_formattato