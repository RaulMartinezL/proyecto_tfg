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
                
                sh 'docker-compose -v /var/run/docker.sock:/var/run/docker.sock down' 
                sh 'docker -v /var/run/docker.sock:/var/run/docker.sock stop $(docker ps -a -q) '
                sh 'docker-compose -v /var/run/docker.sock:/var/run/docker.sock build ' 
                sh 'docker-compose -v /var/run/docker.sock:/var/run/docker.sock up '
            }
        }
    }
}
