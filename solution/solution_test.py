import unittest
from solution import calculate_stamp_duty

class TestStampDuty(unittest.TestCase):

    def test_125000(self):
        self.assertEqual(0, calculate_stamp_duty(125000))

    def test_250000(self):
        self.assertEqual(2500, calculate_stamp_duty(250000))

    def test_925000(self):
        self.assertEqual(36250, calculate_stamp_duty(925000))

    def test_1500000(self):
        self.assertEqual(93750, calculate_stamp_duty(1500000))

    def test_2000000(self):
        self.assertEqual(153750, calculate_stamp_duty(2000000))

if __name__ == '__main__':
    unittest.main()
