import groovy.transform.Field

@Field def optionalCits = [
    "cit1" : "description1",
    "cit2" : "description2",
    "cit3" : "description3",
]

properties([ parameters(optionalCits.collect { cit, description -> 
    booleanParam(name: cit, defaultValue: false, description: description)
})
])

pipeline { 
    agent any
    parameters {
        string(
            name: "Additional",
            defaultValue: "",
            description: "Additional parameters for the build"
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
    }
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