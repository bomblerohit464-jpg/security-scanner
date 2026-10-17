
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is checked out from GitHub'
            }
        }

        stage('Install Tools') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pip install bandit pip-audit'
            }
        }

        stage('Bandit Security Scan') {
            steps {
                script {
                    def result = bat(
                        returnStatus: true,
                        script: 'python -m bandit -r app.py -f json -o bandit-report.json'
                    )

                    if (result != 0) {
                        echo 'Bandit reported findings or encountered an error.'
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('Dependency Audit') {
            steps {
                script {
                    def result = bat(
                        returnStatus: true,
                        script: 'python -m pip_audit -r requirements.txt -f json -o dependency-report.json'
                    )

                    if (result != 0) {
                        echo 'Dependency audit reported vulnerabilities or encountered an error.'
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*-report.json',
                             allowEmptyArchive: true
        }
    }
}
