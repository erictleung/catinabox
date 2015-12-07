import unittest
from catinabox import catmath

class test_math(unittest.TestCase):

    def test__cat_years_to_hooman_years__middle_age__succeeds(self):
        self.assertEqual(catmath.cat_years_to_hooman_years(8), 40)


    def test__cat_years_to_hooman_years__less_than_one_year__succeeds(self):
        self.assertEqual(catmath.cat_years_to_hooman_years(.5), 2.5)


    def test__cat_years_to_hooman_years__0__returns_0(self):
        self.assertEqual(catmath.cat_years_to_hooman_years(0), 0)

if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(test_math)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
