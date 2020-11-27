//Pipeline Jenkins permettant de lancé le fichier de test
pipeline {
  agent any
  stages {
    stage('Web test') {
      parallel {
        stage('Web test') {
          steps {
            sh '''
python test_templates.py -v'''
          }
        }

        stage('Test connexion BDD') {
          steps {
            sh 'python test_unitaire_collecteur.py -v'
          }
        }

      }
    }

  }
}