pipeline {
    agent any

    environment {
        IMAGE_NAME = "dipoelegbede/greeter-app:${env.GIT_COMMIT}"
        KUBE_CONFIG = credentials('k8s-config')
        SLACK_WEBHOOK = credentials('slack-webhook')
    }

    stages {
        stage('Pull Docker Image') {
            steps {
                script {
                    sh "docker pull ${IMAGE_NAME}"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig([credentialsId: 'k8s-config']) {
                        sh "kubectl apply -f k8s/deployment.yaml"
                    }
                }
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
