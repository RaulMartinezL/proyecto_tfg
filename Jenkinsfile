pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                sh  'pip install -r /config/backend/requirements.txt'
                }
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
