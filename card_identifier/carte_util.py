def format_card(card_num):

    import re
    card_num = str(card_num)
    # Regex to remove any nondigit characters
    return re.sub(r"\D", "", card_num)


def validate_card(card_num):
    """"" Vérifiez si la carte de crédit est valide en utilisant l 'algorithme de Luhn
    Entrée: numéro de carte,
    entier ou chaîne
    Sortie: valide?, Booléen
    """


    double = 0
    total = 0

    digits = str(card_num)

    for i in range(len(digits) - 1, -1, -1):
        for c in str((double + 1) * int(digits[i])):
            total += int(c)
        double = (double + 1) % 2

    return (total % 10) == 0
