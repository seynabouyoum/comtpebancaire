from nose.tools import assert_equals
from card_identifier.emetteur_de_carte import identify_card_issuer


american_Express_cards = [
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
    '4012888888881881',
    '4266841343738991'
]

unknown_cards = [
    '6684424830380130',
]


issuers = {
    "american_Express": "VISA",
    "mc": "MASTERCARD",
    "visa": "VISA",
    "unknown": "Not found"
}


class TestIdentifyCreditCardIssuer(object):
    def check_card(self, card_num, card_issuer):
        assert_equals(identify_card_issuer(card_num)["scheme"],
                      issuers[card_issuer])

    def test_american_Express(self):
        for american_Express in american_Express_cards:
            yield self.check_card, american_Express_cards, "american_Expresss"


    def test_mc(self):
        for mc_card in mc_cards:
            yield self.check_card, mc_card, "mc"

    def test_visa(self):
        for visa_card in visa_cards:
            yield self.check_card, visa_card, "visa"


    def test_unknown(self):
        for unknown_card in unknown_cards:
            yield self.check_card, unknown_card, "unknown"
