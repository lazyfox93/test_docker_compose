pipeline {
    agent { 
        label {
            label 'master'
        }
    }
    stages {
        stage('Run tests') {
            steps {
                sh 'docker-compose up --scale chrome=1 --abort-on-container-exit --build'
            }
        }
        stage('Cleanuo') {
            steps {
                sh 'docker container prune -f'
            }
        }
    }
}
