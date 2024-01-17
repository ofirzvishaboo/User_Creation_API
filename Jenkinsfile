pipeline {
  agent any
  stages {
    stage('checkout code- github') {
      steps {
        git(url: 'https://github.com/ofirzvishaboo/flask_devop_project.git', branch: 'master')
      }
    }

    stage('run rest_app') {
      steps {
        sh 'nohup python rest_app.py &'
      }
    }

    stage('run web_app') {
      steps {
        sh 'nohup python web_app.py &'
      }
    }

    stage('run backend_testing') {
      steps {
        sh 'pwd'
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