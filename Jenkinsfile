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
                
                
                // sh 'python3 backend/manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // sleep time: 9999, unit: 'MILLISECONDS'
                
                
                // sh 'chmod -R 755 .'
                // sh 'docker-compose down' 
                // sh 'docker stop $(docker ps -a -q) '
                // sh 'docker rm $(docker ps -a -q) '
                // sh 'COMPOSE_HTTP_TIMEOUT=500 docker-compose build ' 
                sh 'docker-compose up -d'
            }
        }
    }
}
