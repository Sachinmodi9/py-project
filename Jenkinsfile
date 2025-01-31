pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Sachinmodi9/py-project.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'npm install'  // Or 'pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'npm test'  // Or 'pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
