import math
import unittest


def taxcalc(price):
    """Compute the total tax for a given price."""
    try:
        p = float(price)
    except:
        raise ValueError("{} is not a valid price input".format(price))

    if p < 0:
        return 0
    else:
        tax = p * 0.13
        # Round up to two decimal places
        return math.ceil(tax * 100) / 100.0


class TestTaxcalc(unittest.TestCase):

    def test_positive_integer(self):
        actual = taxcalc(100)
        expected = 13
        self.assertEqual(actual, expected)

    def test_zero(self):
        actual = taxcalc(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_negative_integer(self):
        actual = taxcalc(-10)
        expected = 0
        self.assertEqual(actual, expected)

    def test_positive_float(self):
        actual = taxcalc(10.00)
        expected = 1.30
        self.assertEqual(actual, expected)

    def test_negative_float(self):
        actual = taxcalc(-10.00)
        expected = 0
        self.assertEqual(actual, expected)

    def test_positive_string_integer(self):
        actual = taxcalc("100")
        expected = 13
        self.assertEqual(actual, expected)

    def test_negative_string_integer(self):
        actual = taxcalc("-100")
        expected = 0
        self.assertEqual(actual, expected)

    def test_positive_string_float(self):
        actual = taxcalc("10.00")
        expected = 1.30
        self.assertEqual(actual, expected)

    def test_negative_string_float(self):
        actual = taxcalc("-10.00")
        expected = 0
        self.assertEqual(actual, expected)

    def test_round_to_two_decimals(self):
        actual = taxcalc(0.05)
        expected = 0.01  # Rounded from 0.0065
        self.assertEqual(actual, expected)

    def test_round_up_instead_of_down(self):
        actual = taxcalc(0.01)
        expected = 0.01  # Rounded from 0.0013
        self.assertEqual(actual, expected)

    def test_invalid_string_input(self):
        with self.assertRaises(ValueError):
            taxcalc("$1,000")

    def test_invalid_list_input(self):
        with self.assertRaises(ValueError):
            taxcalc([1000])


if __name__ == "__main__":
    unittest.main()
