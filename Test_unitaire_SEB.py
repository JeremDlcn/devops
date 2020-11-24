# --coding:Latin-1 -

import random
import unittest


class RandomTest(unittest.TestCase):

    """Test case utilise pour tester les fonctions du module 'random'."""

    def test_choice(self):
        """Test le fonctionnement"""
        liste = list(range(10))
        elt = random.choice(liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, liste)


unittest.main()
