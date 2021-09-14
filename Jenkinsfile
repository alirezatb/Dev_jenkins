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
<<<<<<< HEAD
	        sh 'docker build -t mynlpmodel1:v1 .'
=======
	        sh 'docker build -t mynlpmodel:v1 .'
>>>>>>> 33ed398b95e8fdc637de438a93aa1d1c60782ac4
	        }
	   }
	   stage('Run Image') {
	        steps {
<<<<<<< HEAD
	        sh 'docker run -d -p 5000:4000 --name nlpmodel1 mynlpmodel1:v1'
=======
	        sh 'docker run -d -p 5000:4000 --name nlpmodel mynlpmodel:v1'
>>>>>>> 33ed398b95e8fdc637de438a93aa1d1c60782ac4
	        }
	   }
	   stage('Testing'){
	        steps {
	            echo 'Testing..'
	            }
	   }
    }
}
