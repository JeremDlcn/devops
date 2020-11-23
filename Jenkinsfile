pipeline {
  agent any
  stages {
    stage('Web test') {
      parallel {
        stage('Web test') {
          steps {
            sh 'python main.py'
          }
        }

        stage('Test client') {
          steps {
            sh 'python Test_unitaire_SEB.py'
          }
        }

      }
    }

  }
}