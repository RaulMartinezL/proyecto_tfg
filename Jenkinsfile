pipeline {
    
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'pip3 install pytest'
            }
        }
        stage('Tests') {
            steps {
                echo 'Testing...'
                sh '/backend/manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
