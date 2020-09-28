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
                
                
                sh 'chmod -R 755 .'
                sh 'docker-compose down' 
                sh 'docker-compose build' 
                sh 'docker-compose up -d'
            }
        }
    }
}
