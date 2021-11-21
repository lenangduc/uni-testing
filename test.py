import unittest
dict_price = {
        1: 18000,
        2: 20000
    }
def count_money(type, number):
    price = dict_price[type]
    if number < 2:
        return price
    elif number >= 4:
        return price * number * 0.5
    else:
        return price * number * 0.75

class TestMethods(unittest.TestCase):
    def test_flow_data_1(self):
        self.assertEqual(count_money(1, 1), 15000)

    def test_flow_data_2(self):
        self.assertEqual(count_money(1, 2), 22500)

    def test_flow_data_3(self):
        self.assertEqual(count_money(1, 4), 30000)

if __name__ == '__main__':
    unittest.main(verbosity=2)