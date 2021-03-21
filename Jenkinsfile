pipeline {
    agent { 
        label {
            label 'master'
        }
    }
    stages {
        stage('Run containers') {
            steps {
                sh 'docker-compose up --scale chrome=1'
            }
        }
    }
}
