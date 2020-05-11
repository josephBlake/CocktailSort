import unittest
import random
from sorting import CocktailShaker

class CocktailShakerTests(unittest.TestCase):
    def test_sorted_case(self):
        array = [random.random() for x in range(100)]
        array.sort()
        sorted = array[:]
        CocktailShaker.cocktail_shaker_sort(array)
        self.assertEqual(len(sorted), len(array))

    def test_reverse_sorted_case(self):
        array = [random.random() for x in range(100)]
        array.sort(reverse=True)
        sorted = array[:]
        sorted.sort()
        CocktailShaker.cocktail_shaker_sort(array)
        self.assertEqual(len(sorted), len(array))

    def test_random_case(self):
        array = [random.random() for x in range(100)]
        random.shuffle(array)
        sorted = array[:]
        sorted.sort()
        CocktailShaker.cocktail_shaker_sort(array)
        self.assertEqual(len(sorted), len(array))

if __name__ == "__main__":
    unittest.main()
