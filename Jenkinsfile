pipeline {
    agent any
        docker {
            image 'python:alphine'
            // Specify additional options if needed, e.g., reuseNode, args, etc.
        }
        environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials-id')
        DOCKER_IMAGE_NAME = 'your-docker-hub-username/your-docker-image-name'
        IMAGE_TAG = "${BUILD_NUMBER}"
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

        stage('Run web_app') {
            steps {
                script {
                    sh 'nohup python web_app.py &'
                }
            }
        }

        stage('Run backend_testing') {
            steps {
                script {
                    sh 'python backend_testing.py'
                }
            }
        }

        stage('Run frontend_testing') {
            steps {
                script {
                    sh 'python frontend_testing.py'
                }
            }
        }

        stage('Run combined_testing') {
            steps {
                script {
                    sh 'python combined_testing.py'
                }
            }
        }

        stage('Run clean_environment') {
            steps {
                script {
                    sh 'python clean_environment.py'
                }
            }
        }
    }
}
