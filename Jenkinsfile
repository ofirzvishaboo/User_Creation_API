pipeline {
  agent any
  stages {
    stage('checkout code- github') {
      steps {
        git(url: 'https://github.com/ofirzvishaboo/User_Creation_API.git', branch: 'master')
      }
    }

    stage('run rest_app') {
      steps {
        sh 'pip3 install -r requirements.txt'
        sh 'nohup python3 rest_app.py &'
      }
    }

    stage('run web_app') {
      steps {
        sh 'nohup python3 web_app.py &'
      }
    }

    stage('run backend_testing') {
      steps {
        sh 'python3 backend_testing.py'
      }
    }

    stage('run frontend_testing') {
      steps {
        sh 'docker run -d --name selenium -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:latest'
        sh 'python3 frontend_testing.py'
      }
    }

    stage('run combined_testing') {
      steps {
        sh 'python3 combined_testing.py'
      }
    }

    // stage('run clean_environment') {
    //   steps {
        
    //   }
    // }

  }
  post {
        always {
            sh 'docker stop selenium'
            sh 'docker rm selenium'
            sh 'python3 clean_environment.py'
        }
    }
}
