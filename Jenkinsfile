pipeline {
  agent any
  stages {
    stage('Test connexion BDD') {
      steps {
        sh 'python test_unitaire_collecteur.py -v'
      }
    }

    stage('Delivery') {
      steps {
        sh '/home/admin-local/delivery.sh'
      }
    }

  }
}