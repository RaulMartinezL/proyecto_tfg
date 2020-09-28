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
                sleep time: 2500, unit: 'MILLISECONDS'
                
                // sh 'python3 backend/manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // sleep time: 9999, unit: 'MILLISECONDS'
                
                
                sh 'chmod -R 755 .'
                // sh 'docker-compose down' 
                // sh 'docker stop $(docker ps -a -q) '
                // sh 'docker stop nginx_web'
                // sh 'docker stop backend_web'
                // sh 'docker stop frontend_web'
                sh 'docker-compose build ' 
                sh 'docker-compose up '
            }
        }
    }
}
