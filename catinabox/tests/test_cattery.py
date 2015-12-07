import unittest
from catinabox import cattery

class test_add_remove(unittest.TestCase):
    ## set up cats
    def setUp(self):
        self.test = cattery.Cattery()

    ## add cats

    def test__add_cats__succeeds(self):
        self.test.add_cats(["Fluffy", "Snookums"])

        self.assertEqual(self.test.cats, ["Fluffy", "Snookums"])
        self.assertEqual(self.test.num_cats, 2)

    ## remove cats

    def test__remove_cat__succeeds(self):
        self.test.add_cats(["Fluffy", "Junior"])
        self.test.remove_cat("Fluffy")

        self.assertEqual(self.test.cats, ["Junior"])
        self.assertEqual(self.test.num_cats, 1)

    def test__remove_cat__no_cats__fails(self):
        c = cattery.Cattery()

        with self.assertRaises(cattery.CatNotFound):
            c.remove_cat("Fluffles")

    def test__remove_cat__cat_not_in_cattery__fails(self):
        self.test.add_cats(["Fluffy"])

        with self.assertRaises(cattery.CatNotFound):
            self.test.remove_cat("Snookums")


if __name__ == "__main__":
    unittest.main()
