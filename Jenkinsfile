pipeline {
    agent any
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
