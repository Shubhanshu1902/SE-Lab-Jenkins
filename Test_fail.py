from remainder import remainder
import unittest

class Test_fail(unittest.TestCase):
    def test_1(self):
        rem = remainder(100,10)
        self.assertEqual(rem,5)

    def test_2(self):
        rem = remainder(12,10)
        self.assertEqual(rem,5)

if __name__ == '__main__':
    unittest.main()