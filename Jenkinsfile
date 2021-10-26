pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
        cron('0 0 * * *')
    }
   
    //agent { docker {image 'python:3.7.2'}}
    stages {
        stage("Compile") {
            steps {
                echo "no need to build the python code"
            }
        }
        stage("Unit test") {
            steps {
                sh "python Test.py"
            }
        }
    }
}