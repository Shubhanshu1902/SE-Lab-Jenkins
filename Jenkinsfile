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
                sh "./remainder.py"
            }
        }
        stage('To pass tests') {
            steps {
                sh "chmod u+x test.py"
                sh "./Test_pass.py"
            }
        }

        stage('To fail test') {
            steps {
                sh "chmod u+x test.py"
                sh "./Test_fail.py"
            }
        }
    } 
}