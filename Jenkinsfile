pipeline {
  agent {
        docker {
            image 'python:3.11.4'
        }
    }
    stages {
        stage('Run rest_app') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    sh 'nohup python rest_app.py &'
                }
            }
        }

    stage('run web_app') {
      steps {
        sh 'nohup python web_app.py &'
      }
    }

    stage('run backend_testing') {
      steps {
        sh 'python backend_testing.py'
      }
    }

    stage('run frontend_testing') {
      steps {
        sh 'python frontend_testing.py'
      }
    }

    stage('run combined_testing') {
      steps {
        sh 'python combined_testing.py'
      }
    }

    stage('run clean_environment') {
      steps {
        sh 'python clean_environment.py'
      }
    }

  }
}