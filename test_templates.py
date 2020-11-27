import unittest
import os.path

# Création de la class contenant les tests
class TempTest(unittest.TestCase):

    def test_main_file(self):
        """ Test si le fichier main.py existe
        
        main.py est coeur du projet flask
        """
        self.assertTrue(os.path.isfile('./main.py'))

    def test_models_file(self):
        """ Test de l'existance du fichier models.py

        models.py contient le modèle des tables de la base de données
        """
        self.assertTrue(os.path.isfile('./models.py'))

    def test_template(self):
        """Test de l'existance des templates HTML
        Les templates HTML sont les vues gérer par du Javascript
        """
        self.assertTrue(os.path.isfile('./templates/index.html'))


# Lancement des tests uniquement si le fichier 
# est directement appelé par ligne de commande
if __name__ == "__main__":
    unittest.main()
