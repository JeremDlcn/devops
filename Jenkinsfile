pipeline {
  agent any
  stages {
    stage('Test client') {
      steps {
        sh 'python Test_unitaire_SEB.py -v'
      }
    }

    stage('Delivery') {
      steps {
        sh '/home/admin-local/delivery.sh'
      }
    }

  }
}