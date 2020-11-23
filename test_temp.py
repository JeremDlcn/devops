import unittest
import os.path


class TempTest(unittest.TestCase):

    def test_main_file(self):
        self.assertTrue(os.path.isfile('./main.py'))

    def test_models_file(self):
        self.assertTrue(os.path.isfile('./main.py'))

    def test_template(self):
        self.assertTrue(os.path.isfile('./templates/index.html'))



if __name__ == "__main__":
    unittest.main()