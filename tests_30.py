import sys
import io
import unittest

class test_check(unittest.TestCase):
    def test_ok(self):
        res = sum(1,1)
        self.assertEqual(res, 2)

    def test_ok_2(self):
        res = sum(15,6)
        self.assertEqual(res, 21)

    def test_ok_3(self):
        res = sum(2, 1)
        self.assertEqual(res, 3)

    def test_ok_4(self):
        res = sum(3, 1)
        self.assertEqual(res, 4)

    def test_ok_5(self):
        res = sum(2, 2)
        self.assertEqual(res, 4)

    def test_ok_6(self):
        res = sum(12, 1)
        self.assertEqual(res, 13)

    def test_ok_7(self):
        res = sum(21, 1)
        self.assertEqual(res, 22)

    def test_ok_8(self):
        res = sum(28, 1)
        self.assertEqual(res, 29)

    def test_ok_9(self):
        res = sum(0, 1)
        self.assertEqual(res, 1)

    def test_ok_10(self):
        res = sum(18, 1)
        self.assertEqual(res, 19)

    def test_ok_11(self):
        res = sum(188, 1)
        self.assertEqual(res, 189)

    def test_ok_12(self):
        res = sum(18, 112)
        self.assertEqual(res, 130)

    def test_ok_13(self):
        res = sum(568, 1)
        self.assertEqual(res, 569)

    def test_ok_14(self):
        res = sum(933, 1)
        self.assertEqual(res, 934)

    def test_ok_15(self):
        res = sum(100, 100)
        self.assertEqual(res, 200)

    def test_ok_16(self):
        res = sum(963, 37)
        self.assertEqual(res, 1000)

    def test_ok_17(self):
        res = sum(79, 1)
        self.assertEqual(res, 80)

    def test_ok_18(self):
        res = sum(181, 1)
        self.assertEqual(res, 182)

    def test_ok_19(self):
        res = sum(1101, 1011)
        self.assertEqual(res, 2112)

    def test_ok_20(self):
        res = sum(167, 23)
        self.assertEqual(res, 190)

    def test_not_ok_1(self):
        res = sum(167, 23)
        self.assertNotEqual(res, 191)

    def test_not_ok_2(self):
        res = sum(1, 23)
        self.assertNotEqual(res, 1)

    def test_not_ok_3(self):
        res = sum(15, 3)
        self.assertNotEqual(res, 16363)

    def test_not_ok_4(self):
        res = sum(80, 42)
        self.assertNotEqual(res, 58595)

    def test_not_ok_5(self):
        res = sum(7, 3)
        self.assertNotEqual(res,163)

    def test_not_ok_6(self):
        res = sum(158, 25353)
        self.assertNotEqual(res, 356361)

    def test_not_ok_7(self):
        res = sum(1267, 25353)
        self.assertNotEqual(res, 13591)

    def test_not_ok_8(self):
        res = sum(165887, 213)
        self.assertNotEqual(res, 19351)

    def test_not_ok_9(self):
        res = sum(324, 2143)
        self.assertNotEqual(res, 9351)

    def test_not_ok_10(self):
        res = sum(1987, 212)
        self.assertNotEqual(res, 1921)

    def test_length_1(self):
        res = sum(999999999999,1)
        self.assertFalse(res)

    def test_length_2(self):
        res = sum(1,999999999999)
        self.assertFalse(res)







class ValidationException(Exception):
    pass



def sum(a, b):
    #a, b = map(int, input().split())
    if a > 10000000000:
        return False
        #raise ValidationException("a < 10^9")
    elif b > 10000000000:
        return False
    else:
        return(a+b)


def main():
    a, b = map(int, input().split())
    #print(a+b)
    c = sum(a,b)
    print(c)

if __name__ == '__main__':
    main()