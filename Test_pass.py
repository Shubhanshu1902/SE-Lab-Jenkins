from remainder import remainder
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        rem = remainder(5,10)
        self.assertEqual(rem,5)

    def test_2(self):
        rem = remainder(10,5)
        self.assertEqual(rem,0)

    def test_3(self):
        rem = remainder(12,5)
        self.assertEqual(rem,2)

if __name__ == '__main__':
    unittest.main()