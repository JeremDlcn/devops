pipeline {
  agent any
  stages {
    stage('Web test') {
      steps {
        sh 'pip install peewee'
        sh '''
python test_temp.py'''
      }
    }

  }
}