pipeline {
    agent any

    stages {
        stage('code build') {
            steps {
                git branch: 'main', url: 'https://github.com/Raja4123/j-d-swarm-py.git'
            }
        }
        stage('Docker build & tag') {
            steps {
                sh 'docker build -t pyapp .'
                sh 'docker tag pyapp:latest raja4123/py-laptops'
            }
        }
        stage('Docker push') {
            steps {
                withDockerRegistry(credentialsId: 'docker-cred') {
                    sh 'docker push raja4123/py-laptops'
                }
            } 
        }
        stage('Stack deploy') {
            steps {
                sh 'docker stack deploy -c compose.yml python-app'
            }
        }
    }
}
