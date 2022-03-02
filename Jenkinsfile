pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  stages {
    stage('Clone Repository') {
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        sh 'docker build -t vishaljain088/dockerwebapp .'
      }
    }
    stage('Scan') {
      steps {
        sh 'docker run ghcr.io/aquasecurity/trivy:latest image vishaljain088/dockerwebapp > scanning.txt'		
      }
    }
	stage("Email Notification"){
      steps {
        emailext (attachmentsPattern: 'scanning.txt', subject: "Trivy Scanning", body: '''${SCRIPT, template="groovy-html.template"}''', mimeType: 'text/html', to: 'vishal.j@westagilelabs.com')
      }
    }
  }
}