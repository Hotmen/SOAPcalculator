import unittest
from polishrecord import ExpToPolish, Polish

class TestExpToPolishCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(ExpToPolish('(8+5*2)/(((2*3)+1)-4)'), '8 5 2 * + 2 3 * 1 + 4 - /')
    def test_second(self):
        self.assertEqual(ExpToPolish('3*(1+5*(1+1))'), '3 1 5 1 1 + * + *')
    def test_no_brackets(self):
        self.assertEqual(ExpToPolish('23+15*3/5-18'), '23 15 3 * 5 / + 18 -')
    def test_with_brackets(self):
        self.assertEqual(ExpToPolish('2*(15-5)/(8-3*(2-1))'), '2 15 5 - * 8 3 2 1 - * - /')
    def test_with_lide_minus(self):
        self.assertEqual(ExpToPolish('-5+15-5*2'), '-5 15 + 5 2 * -')
    def test_with_witespaces(self):
        self.assertEqual(ExpToPolish('2 *( 15 -5)/(8 -3*( 2-1))'), '2 15 5 - * 8 3 2 1 - * - /')
    def test_operators_order(self):
        self.assertEqual(ExpToPolish('10/2*5-6'), '10 2 / 5 * 6 -')
    def test_endwith_operator(self):
        self.assertEqual(ExpToPolish('10/2*5-6+'), 'Error! Check input expression')
    def test_startwith_operator(self):
        self.assertEqual(ExpToPolish('*10/2*5-6'), 'Error! Check input expression')
    def test_missed_operator(self):
        self.assertEqual(ExpToPolish('10/2*5-6 2'), 'Error! Missed operator between numbers')

class TestPolishCase(unittest.TestCase):
    def test_wrong_operands_number(self):
        self.assertEqual(Polish('8 5 2 * + 2 3 * 1 + 4 - / *'), 'Error! Wrong numbers of operands')
    def test_zero_divizion(self):
        self.assertEqual(Polish('8 5 + 5 5 - /'), 'Error! Zero division!')
    def test_complex1(self):
        self.assertEqual(Polish('8 5 2 * + 2 3 * 1 + 4 - /'), (8+5*2)/(((2*3)+1)-4))
    def test_complex2(self):
        self.assertEqual(Polish('2 15 5 - * 8 3 2 1 - * - /'), 2 *( 15 -5)/(8 -3*( 2-1)))
    def test_complex3(self):
        self.assertEqual(Polish('-5 15 + 5 2 * -'), -5+15-5*2)


if __name__ == '__main__':
    unittest.main()