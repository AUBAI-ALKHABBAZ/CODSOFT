"""
Company : CodeSoft
_______________________________________
Student : AUBAI ALKHABBAZ
_______________________________________
Program :  testing.py for Calculator app using python
_______________________________________
py version : 3.8
_______________________________________
Libraries :  unittest
_______________________________________
"""

from simple_Calc import cal_fun,rad_fun
import unittest
# init class for TestCase
class CalculatorTests(unittest.TestCase):

    # TestCase N_1
    def test_add(self):
        calc = cal_fun(7,3,'+')
        self.assertEqual(10, calc._cal_fun__sum())

    # TestCase N_2
    def test_subtract(self):
        calc = cal_fun(7,3,'-')
        self.assertEqual(4, calc._cal_fun__sub())

    # TestCase N_3
    def test_prod(self):
        calc = cal_fun(7,3,'*')
        self.assertEqual(21, calc._cal_fun__prod())

    # TestCase N_4
    def test_div(self):
        calc = cal_fun(10,2,'/')
        self.assertEqual(5, calc._cal_fun__div())

    # TestCase N_5
    def test_Sqrt_1(self):
        calc = cal_fun(16,0,'S')
        self.assertEqual(4, calc._cal_fun__Sqrt_cal())

    # TestCase N_6
    def test_Sqrt_2(self):
        calc = cal_fun(-16,0,'S')
        self.assertEqual("nan", calc._cal_fun__Sqrt_cal())

    # TestCase N_7
    def test_Exp(self):
        calc = cal_fun(1,0,'E')
        self.assertEqual(2.72, calc._cal_fun__Exp_cal())

    # TestCase N_8
    def test_factorial_1(self):
        calc = cal_fun(10,0,'F')
        self.assertEqual(3628800, calc._cal_fun__factorial_cal())

    # TestCase N_9
    def test_factorial_2(self):
        calc = cal_fun(3,0,'F')
        self.assertEqual(6, calc._cal_fun__factorial_cal())

    # TestCase N_10
    def test_prime_1(self):
        calc = cal_fun(1, 0, 'P')
        self.assertTrue(calc._cal_fun__prim_cal())

    # TestCase N_11
    def test_prime_2(self):
        calc = cal_fun(10, 0, 'P')
        self.assertFalse(calc._cal_fun__prim_cal())

    # TestCase N_12
    def test_cos(self):
        calc =rad_fun(1, 0, 'cos')
        self.assertEqual(0.5403023058681398,calc._rad_fun__cos())

    # TestCase N_13
    def test_sin(self):
        calc =rad_fun(1, 0, 'sin')
        self.assertEqual(0.8414709848078965,calc._rad_fun__sin())

    # TestCase N_14
    def test_fab(self):
        calc = cal_fun(10,0,'fab')
        self.assertEqual(88, calc._cal_fun__fabo_fun())


if __name__ == '__main__':
    unittest.main()