pipeline {
    
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'ls'
                sh  'pip3 install -r /config/backend/requirements.txt'
            }
        }
        stage('Tests') {
            steps {
                echo 'Testing...'
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'pytest'
            }
        }
    }
}
