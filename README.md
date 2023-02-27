# Deploying Titanic Survivor Model 
Deploying ML Model
1. Command to deploy the api to heroku
 - heroku login
 - heroku create  (to create an app with heroku cli)
 - git subtree push --prefix ci-and-publishing/titanic-survivor-api heroku master
 2. Deploy to Docker and AWS ECS


 [![CircleCI](https://dl.circleci.com/status-badge/img/gh/mcamara-aneo/ml-model-deployment/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/mcamara-aneo/ml-model-deployment/tree/main)