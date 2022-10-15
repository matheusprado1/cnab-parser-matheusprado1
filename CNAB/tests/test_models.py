from ..models import CNAB
from django.test import TestCase


class TestModel(TestCase):
    @classmethod
    def setUp(cls):

        cls.cnab_data = {
            'type': 2,
            'date': '20220101',
            'value': '0000022000',
            'cpf': '12345678901',
            'card': '123456789012',
            'hour': '122900',
            'owner': 'JOÃO PEDRO',
            'name': 'JOÃO PEDRO   PADARIA DO JOÃO       '
        }

        cls.cnab = CNAB.objects.create(**cls.cnab_data)

    def test_max_lengths(self):
        date_max_length = self.cnab._meta.get_field("date").max_length
        value_max_length = self.cnab._meta.get_field("value").max_length
        cpf_max_length = self.cnab._meta.get_field("cpf").max_length
        card_max_length = self.cnab._meta.get_field("card").max_length
        hour_max_length = self.cnab._meta.get_field("hour").max_length
        owner_max_length = self.cnab._meta.get_field("owner").max_length
        name_max_length = self.cnab._meta.get_field("name").max_length

        self.assertEqual(date_max_length, 8)
        self.assertEqual(value_max_length, 10)
        self.assertEqual(cpf_max_length, 11)
        self.assertEqual(card_max_length, 12)
        self.assertEqual(hour_max_length, 6)
        self.assertEqual(owner_max_length, 14)
        self.assertEqual(name_max_length, 19)

    def test_type_validators(self):
        self.cnab._meta.get_field("type")._validators[0].limit_value = 9
        self.cnab._meta.get_field("type")._validators[1].limit_value = 1

    def test_date_validators(self):
        self.cnab._meta.get_field("date")._validators[0].max_length = 8
        self.cnab._meta.get_field("date")._validators[1].min_length = 8

    def test_cpf_validator(self):
        self.cnab._meta.get_field("cpf")._validators[0].max_length = 11
        self.cnab._meta.get_field("cpf")._validators[1].min_length = 11

    def test_hour_validator(self):
        self.cnab._meta.get_field("hour")._validators[0].max_length = 6
        self.cnab._meta.get_field("hour")._validators[1].min_length = 6

    def test_card_validator(self):
        self.cnab._meta.get_field("card")._validators[0].max_length = 12
        self.cnab._meta.get_field("card")._validators[1].min_length = 12

    def test_cnab_fields(self):
        self.assertEqual(
            self.cnab.type, self.cnab_data["type"]
        )
        self.assertEqual(self.cnab.date, self.cnab_data["date"])
        self.assertEqual(self.cnab.value, self.cnab_data["value"])
        self.assertEqual(self.cnab.cpf, self.cnab_data["cpf"])
        self.assertEqual(self.cnab.card, self.cnab_data["card"])
        self.assertEqual(self.cnab.hour, self.cnab_data["hour"])
        self.assertEqual(self.cnab.owner, self.cnab_data["owner"])
        self.assertEqual(self.cnab.name, self.cnab_data["name"])
