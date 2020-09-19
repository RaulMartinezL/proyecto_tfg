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
                
                sh 'docker-compose down -v /var/run/docker.sock:/var/run/docker.sock'
                sh 'docker stop $(docker ps -a -q) -v /var/run/docker.sock:/var/run/docker.sock'
                sh 'docker-compose build -v /var/run/docker.sock:/var/run/docker.sock' 
                sh 'docker-compose up -v /var/run/docker.sock:/var/run/docker.sock'
            }
        }
    }
}
