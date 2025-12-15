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

def elmozdulas(path: str) -> str:
    x = 0
    y = 0

    for seps in path:
        if seps == 'J':
            x += 1
        elif seps == 'B':
            x -= 1
        elif seps == 'F':
            y += 1
        elif seps == 'L':
            y -= 1

    if x == 0 and y == 0:
        return "Nem mentunk sehova"

    eredmeny = []

    if x > 0:
        eredmeny.append(f"{x} lepes jobbra")
    elif x < 0:
        eredmeny.append(f"{-x} lepes balra")

    if y > 0:
        eredmeny.append(f"{y} lepes fel")
    elif y < 0:
        eredmeny.append(f"{-y} lepes le")

    return ", ".join(eredmeny)

def Karifa(magassag):
    for i in range(magassag):
        szokoz = magassag - i - 1
        csillag = 2 * i + 1
        print(' ' * szokoz + '*' * csillag)

    for _ in range(2):
        print(' ' * (magassag - 2) + "|||")


class Elmozdulas(unittest.TestCase):
    def test_JJFBFFFFFFBBBL(self):
        self.assertEqual(elmozdulas("JJFBFFFFFFBBBL"), "2 lepes balra, 6 lepes fel")
    def test_FBLLLJLLJ(self):
        self.assertEqual(elmozdulas("FBLLLJLLJ"), "1 lepes jobbra, 4 lepes le")
    def test_FFF(self):
        self.assertEqual(elmozdulas("FFF"), "3 lepes fel")
    def test_FFLLBBJJ(self):
        self.assertEqual(elmozdulas("FFLLBBJJ"), "Nem mentunk sehova")

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
    print("Kérem adja meg milyen magas legyen a karácsonyfa: ", end='')
    Karifa(int(input()))
    unittest.main()
