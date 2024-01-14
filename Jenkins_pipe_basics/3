pipeline{
    agent any 
    environment{
        Newversion = "1.2.4"
    }
    stages{
        stage("Build"){
            steps{
                echo "Hello calling environment ${Newversion}"
            }
        }
    }
}