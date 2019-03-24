from nose.tools import assert_equals
from card_identifier.verificateur_de_type_de_carte import identify_card_type


american_Express_cards = [
    '370000000000002', 
    '372322409401021',
    '372322409401005',
    '375987654321001'

]


mc_cards = [
    '5424000000000015',
    '5589871003986236',
    '5401683100112371'
]
visa_cards = [
    '4007000000027',
    '4012888888881881',
    '4266841343738991'
]
unknown_cards = [
    '400700000002',
    '6090883271926957',
    '6006496142903742460'  
]


class TestIdentifyCreditCardType(object):
    def check_card(self, card, type):
        assert_equals(identify_card_type(card), type)

    def test_american_Express(self):
        for american_Express_card in american_Express_cards:
            yield self.check_card, american_Express_cards, "AMERICAN_Express"


    def test_mc(self):
        for mc_card in mc_cards:
            yield self.check_card, mc_card, "MasterCard"

    def test_visa(self):
        for visa_card in visa_cards:
            yield self.check_card, visa_card, "Visa"

    def test_unknown(self):
        for unknown_card in unknown_cards:
            yield self.check_card, unknown_card, "Unknown"
