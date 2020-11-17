import unittest

class TempTest(unittest.TestCase):

    def test_temp(self):
        # f = Data.select()
        # for cf in f:     
        #     print(cf.numero_unite, cf.nom_unite)
        # self.assertTrue(tempTest(cf.tankTemp))
        self.assertTrue(tempTest(3))

def tempTest(temp):
    if temp >= 2.5 and temp <= 4:
        return True
    else:
        return False


if __name__ == "__main__":
    unittest.main()