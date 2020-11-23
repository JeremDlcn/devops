import unittest
from main import data
import json
data = json.loads(data())


class TempTest(unittest.TestCase):

    def test_temp(self):

        res = data[0]['info']['unit']
        self.assertTrue(res, 1)



if __name__ == "__main__":
    unittest.main()
