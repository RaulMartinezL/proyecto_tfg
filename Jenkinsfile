pipeline {
    
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh  'pip3 install -r /config/backend/requirements.txt'
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
