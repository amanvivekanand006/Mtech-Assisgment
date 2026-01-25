pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pip install pytest'
                bat 'pytest'
            }
        }

        stage('Package') {
            steps {
                bat 'python setup.py bdist_wheel'
            }
        }
    }
}