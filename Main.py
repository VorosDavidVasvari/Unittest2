import unittest
import math

def armstrong_szam(num: int) -> bool:
    sum: int = 0

    for i in range(len(str(num))):
        sum += math.pow(int(str(num)[i]), len(str(num)))

    return num == sum

class ArmstrongTest(unittest.TestCase):
    def test_153_true(self):
        self.assertTrue(armstrong_szam(153))
    def test_8208_true(self):
        self.assertTrue(armstrong_szam(8208))
    def test_1999_false(self):
        self.assertFalse(armstrong_szam(1999))

if __name__ == "__main__":
    unittest.main()
