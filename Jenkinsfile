pipeline {
    
    agent {
        docker { image 'python:3' }
    }
    
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
