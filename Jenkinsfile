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
                sh '''#!bin/bash
                    pytests --continue-on-collection-errors backend/manage.py backend/post/tests.py
                    '''
            }
        }
    }
}
