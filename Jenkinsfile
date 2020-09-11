pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('Build') {
            steps {
                sh  'pip install -r /config/backend/requirements.txt'
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
