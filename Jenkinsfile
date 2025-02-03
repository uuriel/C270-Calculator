pipeline {
    agent any

    environment {
        // Define environment variables here if necessary
        DOCKER_IMAGE = 'nodejs_app'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull the code from GitHub
                git 'https://github.com/uuriel/C270-Calculator.git'  
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove any existing container
                    sh 'docker ps -q --filter "name=$DOCKER_IMAGE" | xargs -r docker stop | xargs -r docker rm'

                    // Run the app container
                    sh 'docker run -d -p 3000:3000 --name $DOCKER_IMAGE $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    // Clean up by removing unused Docker images and containers
                    sh 'docker system prune -f'
                }
            }
        }
    }

    post {
        success {
            echo 'Build and deployment completed successfully.'
        }

        failure {
            echo 'There was a problem with the build or deployment.'
        }
    }
}