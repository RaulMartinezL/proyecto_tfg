pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                echo 'funcionas' 
            }
        }
        stage('prueba') {
            steps {
                sh 'pytest --continue-on-collection-errors backend/post/tests.py'
            }
        }
    }
}
