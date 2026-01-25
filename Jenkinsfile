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
                sh '''
                    python --version
                    python -m pip install pytest
                    python -m pytest
                '''
            }
        }

        stage('Package') {
            steps {
                sh '''
                    python -m pip install wheel
                    python setup.py bdist_wheel
                '''
            }
        }
    }
}
