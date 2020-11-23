pipeline {
  agent any
  stages {
    stage('Web test') {
      steps {
        sh 'sudo apt install python3-setuptools'
        sh 'pip install peewee'
        sh '''
python test_temp.py'''
      }
    }

  }
}