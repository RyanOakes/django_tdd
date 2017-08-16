#!/usr/bin/env groovy

pipeline {

    agent {
        docker {
            image 'ubuntu'
            args '-u root'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                echo "Success"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                echo "Goodbye"
            }
        }
    }
}
