pipeline {
  agent any
  stages {
    stage('Web test') {
      steps {
        sh 'pip install -r requirements.txt'
        sh '''
python test_temp.py'''
      }
    }

  }
}