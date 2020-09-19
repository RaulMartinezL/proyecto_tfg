pipeline {
    
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'ls'
            }
        }
        stage('Tests') {
            steps {
                echo 'Testing...'
                sh 'python3 backend/manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
