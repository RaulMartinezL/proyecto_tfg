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
                sh 'pytest /backend/post/tests.py'
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
