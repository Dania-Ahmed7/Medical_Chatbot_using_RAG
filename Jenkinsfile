pipeline {
  environment {
    dockerimagename = "saadriaz999/devops-myapp"
    dockerImage = ""
  }
  agent any
  stages {
    stage('Checkout Source') {
      steps {
        git 'https://github.com/saadriaz999/DevOps.git'
      }
    }
//     stage('Build image') {
//       steps{
//         script {
//           dockerImage = docker.build dockerimagename
//         }
//       }
//     }
//     stage('Pushing Image') {
//       environment {
//           registryCredential = 'dockerhub-credentials'
//            }
//       steps{
//         script {
//           sh 'unset DOCKER_HOST'
//
//
//           docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
//             dockerImage.push("latest")
//           }
//         }
//       }
//     }
    stage('Deploying React.js container to Kubernetes') {
      steps {
        script {
          kubernetesDeploy(configs: "qdrant-deployment.yml")
          kubernetesDeploy(configs: "flask-deployment.yml")
          kubernetesDeploy(configs: "qdrant-service.yml")
          kubernetesDeploy(configs: "flask-service.yml")
        }
      }
    }
  }
}