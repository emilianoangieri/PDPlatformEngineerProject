## Product Development Platform Engineer Project

Below it is reported the architecture diagram of Platform Engineer Project.

![alt text](https://github.com/emilianoangieri/PDPlatformEngineerProject/blob/master/architecture.PNG)

### Project Description

The architecture is composed of frontend and backend.
The frontend is a static website hosting reachable here http://test-pdp-platform-engineer-project.s3-website-eu-west-1.amazonaws.com.

![alt text](https://github.com/emilianoangieri/PDPlatformEngineerProject/blob/master/s3-website.PNG)

Basically there are two main options available on frontend, subscribe and unsubscribe.

Clicking on "subscribe" or "unsubsribe" a form will be shown and is possible to add the email that the user would like to subscribe/unsubscribe to the email joke.

![alt text](https://github.com/emilianoangieri/PDPlatformEngineerProject/blob/master/subscribe.PNG)


The submit form of subscribe call a method defined on the api-gaetway, called subscribe2.
This method trigger a lambda function named "subscribe" that add the email address into an SNS topic named "email". 


The submit form of unsubscribe call a method defined on the api-gaetway, called unsubscribe.
This method trigger a lambda function named "unsubscribe" that remove the email address from an SNS topic named "email".


A lambda function named "send_joke" retrieve the joke from https://icanhazdadjoke.com/api#fetch-a-random-dad-joke and publish it to the SNS topic named "email".
A CloudWatch rules named "send-joke-trigger" trigger the lambda function named "send_joke" every midnight.


### Some technical details

The "subscribe" and "unsubsribe" lambda function checks before complete any action, if an email exist or not on SNS topic named "email".
The api gateway methods (both subscribe2 and unsubscribe) before passing the parameter received from frontend to lambda, processed it into the "Integration Request" - "Body mapping template" steps, transoforming the source data into a json readble from lambda (the code is available in api-gateway/Integration Request) folder.


![alt text](https://github.com/emilianoangieri/PDPlatformEngineerProject/blob/master/api-gateway.PNG)
