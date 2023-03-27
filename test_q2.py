from q2_atm import ATM
import q2


class Testq2:
    def test_extract_Pin(self):
        atm = ATM()
        lValues = [0, 500, 434, 9999, 25, 6, 1, 8431]
        for i in lValues:
            encrypted_pin = atm.encrypt_PIN(i)
            assert i == q2.extract_PIN(encrypted_pin)

    def test_extract_card(self):
        atm = ATM()
        lValues = [12345678, 123456789, 99999999, 999999999, 10000000, 100000000, 54295869, 918273456]
        for i in lValues:
            encrypted_card = atm.encrypt_credit_card(i)
            assert i == q2.extract_credit_card(encrypted_card)

    def test_verify_server_approval(self):
        atm = ATM()
        assert atm.verify_server_approval(q2.forge_signature())
