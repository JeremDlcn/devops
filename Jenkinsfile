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
        sh 'docker-compose -f /home/admin-local/devops/ stop'
        sh '/home/admin-local/delivery.sh'
        sh 'docker-compose -f /home/admin-local/devops/ start'
      }
    }

  }
}