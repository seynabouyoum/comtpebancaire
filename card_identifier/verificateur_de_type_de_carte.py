# Constantes de nom de carte
AMERICAN_Express= 'AMERICAN_Express'
MASTERCARD = 'MasterCard'
VISA = 'Visa'
UNKNOWN = 'Unknown'
# Constantes de numéro de carte
AMERICAN_Express_2 = ('39', '30')
MASTERCARD_2 = ('41', '10')
VISA_1 = ('14','15')


def identify_card_type(card_num):
    """Identifie le type de carte en fonction du numéro de carte.
    Cette information est fournie par les  6 premiers chiffres du numéro de carte.
    Entrée: numéro de carte, int ou
    chaîne Sortie: Type de carte, chaîne
    >> > identifiant_card_type('370000000000002')
    'AMERICAN_Express'
    >> > identifiant_card_type('5424000000000015')
    'MasterCard'
    >> > identifiant_card_type('4007000000027')
    'Visa'
    >> > identifiant_card_type('400700000002')
    'Inconnu'
    "" """

    card_type = UNKNOWN
    card_num = str(card_num)

    # AMERICAN_Express
    if len(card_num) == 15 and card_num[:2] in AMERICAN_Express_2:
        card_type = AMERICAN_Express

    # MasterCard, Visa
    elif len(card_num) == 16:
        # MasterCard
        if card_num[:2] in MASTERCARD_2:
            card_type = MASTERCARD

        # Visa
        elif card_num[:1] in VISA_1:
            card_type = VISA

    # VISA
    elif (len(card_num) == 13) and (card_num[:1] in VISA_1):
        card_type = VISA

    return card_type
print("Numero de carte ou nom de carte",identify_card_type(58965214785696634))
