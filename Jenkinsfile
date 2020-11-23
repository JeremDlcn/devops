pipeline {
  agent any
  stages {
    stage('Web test') {
      steps {
        sh 'pip install -r /var/lib/jenkins/workspace/devops-web_web/requirements.txt'
        sh '''
python test_temp.py'''
      }
    }

  }
}