pipeline {
    
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'ls'
                sh 'add-apt-repository ppa:deadsnakes/ppa'
                sh 'apt-get update'
                sh 'apt-get install python3.6'
                sh 'apt install python3-pip'
                sh 'update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1'
                sh 'chmod -R 755 .'
                sh  'pip3 install -r config/backend/requirements.txt'
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
