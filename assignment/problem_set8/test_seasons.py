import unittest
from datetime import date
from seasons import get_minutes, number_to_words


class TestGetMinutes(unittest.TestCase):
    def test_same_day(self):
        """Age 0 days = 0 minutes."""
        self.assertEqual(get_minutes(date.today()), 0)

    def test_one_day(self):
        """1 day = 1440 minutes."""
        self.assertEqual(get_minutes(date(2026, 10, 5)), 1440)

    def test_exact_years(self):
        """1 year = 365 * 24 * 60 minutes (ignoring leap years in this simple calc)."""
        self.assertEqual(get_minutes(date(2025, 10, 6)), 365 * 24 * 60)


class TestNumberToWords(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(number_to_words(0), "zero")

    def test_single_digit(self):
        self.assertEqual(number_to_words(5), "five")

    def test_teens(self):
        self.assertEqual(number_to_words(13), "thirteen")

    def test_tens(self):
        self.assertEqual(number_to_words(40), "forty")

    def test_hundred(self):
        self.assertEqual(number_to_words(100), "one hundred")

    def test_thousand(self):
        self.assertEqual(number_to_words(1000), "one thousand")

    def test_complex(self):
        self.assertEqual(number_to_words(1234), "one thousand two hundred thirty-four")

    def test_large(self):
        self.assertEqual(number_to_words(525600), "five hundred twenty-five thousand six hundred")


if __name__ == "__main__":
    unittest.main()