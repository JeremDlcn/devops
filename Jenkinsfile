pipeline {
  agent any
  stages {
    stage('Test client') {
      parallel {
        stage('Test client') {
          steps {
            sh 'python Test_unitaire_SEB.py -v'
          }
        }

        stage('error') {
          steps {
            sh 'python test_unitaire_collecteur.py -v'
          }
        }

      }
    }

    stage('Delivery') {
      steps {
        sh 'docker-compose -f /home/admin-local/devops/ stop'
        sh '/home/admin-local/delivery.sh'
        sh 'docker-compose -f /home/admin-local/devops/ start'
      }
    }

  }
}