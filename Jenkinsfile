pipeline {
	agent any
	    stages {
	        stage('Clone Repository') {
	        /* Cloning the repository to our workspace */
	        steps {
	        checkout scm
	        }
	   }
	   stage('Build Image') {
	        steps {
	        sh 'docker build -t mynlpmodel:v2 .'
	        }
	   }
	   stage('Run Image') {
	        steps {
	        sh 'docker run -d -p 5000:5000 --name nlpmodel mynlpmodel:v2'
	        }
	   }
	   stage('Testing'){
	        steps {
	            sh 'py.test --junitxml results.xml tests/*.py'
	            }
	   }
    }
}
