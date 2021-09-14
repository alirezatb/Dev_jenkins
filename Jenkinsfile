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
	        sh 'docker build -t mynlpmodel1:v1 .'
	        }
	   }
	   stage('Run Image') {
	        steps {
	        sh 'docker run -d -p 5000:4000 --name nlpmodel1 mynlpmodel1:v1'
	        }
	   }
	   stage('Testing'){
	        steps {
	            echo 'Testing..'
	            }
	   }
    }
}
