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
        sh 'docker-compose -f /home/admin-local/devops/docker-compose.yml stop'
        sh '/home/admin-local/delivery.sh'
        sh 'docker-compose -f /home/admin-local/devops/docker-compose.yml build'
        sh 'docker-compose -f /home/admin-local/devops/docker-compose.yml start'
      }
    }

  }
}