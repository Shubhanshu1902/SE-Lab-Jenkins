import groovy.transform.Field

@Field def optionalCits = [
    "cit1" : "description1",
    "cit2" : "description2",
    "cit3" : "description3",
]

properties([
    parameters(
        [booleanParam(name: 'RUN_ALL', defaultValue: false, description: 'Set all cits to true')] +
        optionalCits.collect { cit, description ->
            booleanParam(name: cit, defaultValue: false, description: description)
        } + [
            string(name: 'Additional', defaultValue: '', description: 'Additional parameters for the build')
        ]
    )
])


pipeline { 
    agent any
    parameters {
        booleanParam(
            name: "RUN_ALL",
            defaultValue: false,
            description: "Set all cits to true"
        )
        booleanParam(
            name: "tp1",
            defaultValue: false,
            description: "des1"
        )

        booleanParam(
            name: "tp2",
            defaultValue: false,
            description: "des2"
        )
        booleanParam(
            name: "cit1",
            defaultValue: false,
            description: "description1"
        )
        booleanParam(
            name: "cit2",
            defaultValue: false,
            description: "description2"
        )
        booleanParam(
            name: "cit3",
            defaultValue: false,
            description: "description3"
        )
    }
    stages {
        stage('Set CITs if RUN_ALL') {
            steps {
                script {
                    if (params.RUN_ALL) {
                        params.cit1 = true
                        params.cit2 = true
                        params.cit3 = true
                    }
                }
            }
        }
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