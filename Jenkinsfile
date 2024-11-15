pipeline {
    agent any

    environment {
        IMAGE_NAME = "dipoelegbede/greeter-app:latest"
        KUBECONFIG = "/var/lib/jenkins/.kube/config"
        MINIKUBE_HOME = "/var/lib/jenkins/.minikube"
        HOME = "/var/lib/jenkins"
        SLACK_WEBHOOK = credentials('slack-webhook')
    }

    stages {

        stage('Debug') {
            steps {
                echo "Starting Kubernetes deployment stage..."
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                    sh """
                        minikube status
                        kubectl get node
                        kubectl apply -f k8s/deployment.yml
                    """
            }
        }
    }

    // post {
    //     success {
    //         script {
    //             sendSlackNotification("Deployment succeeded for ${env.BRANCH_NAME}")
    //             // updateJiraTicket("Deployment succeeded")
    //         }
    //     }
    //     failure {
    //         script {
    //             sendSlackNotification("Deployment failed for ${env.BRANCH_NAME}")
    //             // updateJiraTicket("Deployment failed")
    //         }
    //     }
    // }
}

// def sendSlackNotification(message) {
//     withEnv(["SLACK_WEBHOOK=${SLACK_WEBHOOK}"]) {
//         sh '''
//             curl -X POST -H "Content-type: application/json" \
//             --data "{\"text\": \"'${message}'\"}" "$SLACK_WEBHOOK"
//         '''
//     }
// }

// def updateJiraTicket(comment) {
//     sh """
//         curl -X POST -H "Content-Type: application/json" \
//         -u "${JIRA_USER}:${JIRA_API_TOKEN}" \
//         --data '{"body": "${comment}"}' \
//         ${JIRA_URL}/rest/api/2/issue/<issue-id>/comment
//     """
// }
