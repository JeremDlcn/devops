import os
import unittest


class SizeTest(unittest.TestCase):

    def test_choice(self):
        list_json_files = os.listdir('JSON_Files')
        length = str(len(list_json_files))
        # Vérifie qu'il y a 50 fichiers dans le dossier JSON_Files
        # Check that there are 50 files in the JSON_Files folder
        self.assertIn("50", length)


unittest.main()
