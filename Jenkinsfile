pipeline {
  agent any
  stages {
    stage('Web test') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        sh '''
python test_temp.py'''
      }
    }

  }
}