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
        sh 'docker run ghcr.io/aquasecurity/trivy:latest image vishaljain088/dockerwebapp > trivyreport.json'		
      }
    }
	stage("Email Notification"){
      steps {
        emailext (attachmentsPattern: 'trivyreport.json', subject: "Trivy Scanning", body: '''${SCRIPT, template="groovy-html.template"}''', mimeType: 'text/html', to: 'jenkinsbyjain@gmail.com')
      }
    }
    stage('Scan Severity') {
      steps {
        sh 'docker run ghcr.io/aquasecurity/trivy:latest image --exit-code 1 --severity CRITICAL vishaljain088/dockerwebapp'
      }
    }
  }
}
