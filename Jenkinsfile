pipeline {
  agent any
  stages {
    stage('Web test') {
      steps {
        sh 'virtual venv'
        sh '. venv/bin/activate'
        sh 'pip install -r requirements.txt '
        sh '''
python test_temp.py -v'''
      }
    }

  }
}