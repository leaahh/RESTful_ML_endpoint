pipeline {
  agent any
  
  stages{ 
    stage('Create Staging branch'){ 
      steps{ 
        echo 'Create Staging branch'
        
        bat 'git branch -d staging'
        bat 'git push origin --delete staging'
        
        bat 'git checkout dev'
        // bat 'git pull'
        
        //bat 'git checkout -b staging dev'
        bat 'git branch staging'
        bat 'git checkout staging'
        bat 'git push --set-upstream origin staging'
      } 
    }
    
    stage('Build'){
      steps{ 
        echo 'Build'
        bat 'pip install -r requirements.txt'
      }
    }
    
    stage('Test'){
      steps{
        echo 'Test' 
        bat 'python test_main.py' 
      }
    } 
    
    stage('Deploy'){
      steps{
        echo 'Deploy'
        
        bat 'docker build -t flask .'
        
        withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerhub_pwd', usernameVariable: 'dockerhub_login')]) {
          bat 'docker login -u %dockerhub_login% -p %dockerhub_pwd%'
          bat 'docker tag flask %dockerhub_login%/restful_ml_endpoint:latest'
          bat 'docker push %dockerhub_login%/restful_ml_endpoint:latest'
        }
      }
    }
    
    /*
    stage('Merging'){
      steps{
        echo 'Clean Up : Merge and Delete staging branch'

        bat 'git checkout main'
        bat 'git merge staging'
        bat 'git push'
        
        bat 'git branch -d staging'
        bat 'git push origin --delete staging'
      } 
    }*/
  } 
}