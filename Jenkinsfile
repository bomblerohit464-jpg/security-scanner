
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Install Tools') {
            steps {
                bat '"C:\\Users\\mithu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
                bat '"C:\\Users\\mithu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install bandit pip-audit'
            }
        }

        stage('Bandit Security Scan') {
            steps {
                script {
                    int result = bat(
                        returnStatus: true,
                        script: '"C:\\Users\\mithu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m bandit -r app.py -f json -o bandit-report.json'
                    )

                    if (result != 0) {
                        echo 'Bandit found potential issues or encountered an error.'
                        currentBuild.result = 'UNSTABLE'
                    } else {
                        echo 'Bandit scan completed successfully.'
                    }
                }
            }
        }

        stage('Dependency Audit') {
            steps {
                script {
                    int result = bat(
                        returnStatus: true,
                        script: '"C:\\Users\\mithu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip_audit -r requirements.txt -f json -o dependency-report.json'
                    )

                    if (result != 0) {
                        echo 'Dependency vulnerabilities found or audit encountered an error.'
                        currentBuild.result = 'UNSTABLE'
                    } else {
                        echo 'Dependency audit completed successfully.'
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: '*-report.json',
                allowEmptyArchive: true
            )
        }
    }
}
