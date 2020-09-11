pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                sh  '''#!bin/bash
                    pip install -r /config/backend/requirements.txt
                    
                    pip install pytest-django
                    '''
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
