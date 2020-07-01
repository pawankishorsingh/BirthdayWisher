LOG_FILE = 'birthday_persons.log'
pipeline {
    agent any
    options { timestamps () }
    stages {
        stage('SCM Checkout') {
            steps {
                git credentialsId: '49c91405-0df0-4069-ac6b-8fac74e73d26', url: 'git@git.corp.adobe.com:coretech/BirthdayWisher.git'
            }
        }
        stage('Check Python Version') {
            steps {
                sh 'python --version'
            }            
        }
         stage('Run Python') {
            steps {
                sh 'python main.py'
            }
        }
        stage('Set Build Description') {
            steps {
                script {
                    if (fileExists (file: LOG_FILE)) {
                        def data = readFile(file: LOG_FILE)
                        currentBuild.description = data
                        echo 'Build description updated successfully'
                    }
                    else {
                        echo 'No need to update build description since there are no birthdays today.'
                    }
                }    
            }
        }        
    }
}
