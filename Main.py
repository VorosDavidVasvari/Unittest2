import unittest
import math

def armstrong_szam(num: int) -> bool:
    sum: int = 0

    for i in range(len(str(num))):
        sum += math.pow(int(str(num)[i]), len(str(num)))

    return num == sum

def jelszo_erosseg(passwd: str) -> int:
    if (len(passwd) == 0) or ("jelszo" in passwd) or ("123" in passwd): return 0

    strength: int = 1

    strengthChars = ".-_"

    if len(passwd) > 5: strength += 1
    if len(passwd) > 8: strength += 2

    for c in strengthChars:
        for ch in passwd:
            if ch == c: strength += 2

    return strength

def maganhangzot_torol(txt: str) -> str:
    newTxt: str = ""
    maganhangzok = "aeiouáéíóöőúüű"

    for c in txt:
        if c.lower() not in maganhangzok: newTxt += c

    return newTxt

class Maganhangzok(unittest.TestCase):
    def test_1(self):
        self.assertEqual(maganhangzot_torol("Iden Java szigeten voltunk nyaralni. Nem is tudtam, hogy elneveztek egy helyet egy programozasi nyelvrol."), "dn Jv szgtn vltnk nyrln. Nm s tdtm, hgy lnvztk gy hlyt gy prgrmzs nylvrl.")

class Jelszoerosseg(unittest.TestCase):
    def test_hazi_macska_4_life(self):
        self.assertEqual(jelszo_erosseg("hazi_macska_4_life"), 10)
    def test_ez1feltorhetetlenjelszo(self):
        self.assertEqual(jelszo_erosseg("ez1feltorhetetlenjelszo"), 0)

class ArmstrongTest(unittest.TestCase):
    def test_153_true(self):
        self.assertTrue(armstrong_szam(153))
    def test_8208_true(self):
        self.assertTrue(armstrong_szam(8208))
    def test_1999_false(self):
        self.assertFalse(armstrong_szam(1999))

if __name__ == "__main__":
    unittest.main()
