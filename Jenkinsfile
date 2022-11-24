pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Shubhanshu1902/SE-Lab-Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x remainder.py"
                sh "python remainder.py"
            }
        }
        stage('To pass tests') {
            steps {
                sh "chmod u+x Tests.py"
                sh "python Tests.py"
            }
        }

        stage('To fail tests') {
            steps {
                sh "chmod u+x Test_fail.py"
                sh "python Test_fail.py"
            }
        }
        
    } 
}