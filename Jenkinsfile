pipeline{
    agent any
    environment {
        //once you sign up for Docker hub, use that user_id here
        registry = "prakasarul222/mlops"
        //- update your credentials ID after creating credentials for connecting to Docker Hub
        registryCredential = 'dockerhub'
        dockerImage = ''
    }

     stages {

        stage ('checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/prakasarul/dsml_mlops_flask_app.git']])
            }
        }
        stage ('Build docker image') {
            steps {
                script {
                dockerImage = docker.build registry + ":$BUILD_NUMBER"
                //dockerImage = docker.build registry + ":$BUILD_NUMBER"

                }
            }
        }
        stage('Upload Image') {
            steps{   
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                    }
                        }
            }
        }
     }
}