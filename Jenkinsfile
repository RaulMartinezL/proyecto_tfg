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
