pipeline {
  agent any
  stages {
    stage('Web test') {
      steps {
        sh 'pip install -r requirements.txt -f /var/lib/jenkins/workspace/devops-web_web/'
        sh '''
python test_temp.py -v'''
      }
    }

  }
}