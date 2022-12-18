from main import gcd
import unittest


class TestHi(unittest.TestCase):
    def test_1(self):
        a = 10
        b = 15
        self.assertEqual(gcd(a, b), 5)

    def test_2(self):
        a = 35
        b = 10
        self.assertEqual(gcd(a, b), 5)

    def test_3(self):
        a = 31
        b = 2
        self.assertEqual(gcd(a, b), 1)


if __name__ == "__main__":
    unittest.main()
