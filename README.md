## Product Development Platform Engineer Project

Below it is reported the architecture diagram of Platform Engineer Project.

![alt text](https://github.com/emilianoangieri/PDPlatformEngineerProject/blob/master/architecture.PNG)

### Project Description

The architecture is composed of frontend and backend.
The frontend is a static website hosting reachable here http://test-pdp-platform-engineer-project.s3-website-eu-west-1.amazonaws.com.

![alt text](https://github.com/emilianoangieri/PDPlatformEngineerProject/blob/master/s3-website.PNG)

Basically there are two main options available on frontend, subscribe and unsubscribe.
Clicking on "subscribe" or "unsubsribe" a form will be shown and is possible to add the email that the user would like to subscribe/unsubscribe to the email joke.
The submit form of subscribe call a method defined on the api-gaetway, called subscribe2.
This method trigger a lambda function named "subscribe" that add the email address into an SNS topic named "email". 

The submit form of unsubscribe call a method defined on the api-gaetway, called unsubscribe.
This method trigger a lambda function named "unsubscribe" that remove the email address from an SNS topic named "email".

A lambda function named "subscribe" trigger 


The backed is composed of an api gateway that expose two methods, subscribe2 and unsubscribe.

#### Frontend details

Put all of your relevant code and documentation in a git repository. We prefer GitHub, but as long as it is web accessible, you can put it up wherever you have an account.

How you organize your project and generate CloudFormation is up to you. All we ask is that you include the final CloudFormation template in a `cloudformation.yaml` file at the root of your project.

#### Notes
  * You should be able to stay in the AWS "Free Tier" for this project.
  * We expect a minimal project to take 2-5 hours of your time, depending on your familiarity with AWS.
  * While AWS SES would provide prettier email formatting, it is not free. You may use AWS SNS topics with an email endpoint.
  * Feel free to use a public API for your random content.
    * [Inspirational Quotes](http://forismatic.com/en/api/)
    * [Ron Swanson Quotes](https://ron-swanson-quotes.herokuapp.com/v2/quotes)
    * [Chuck Norris Jokes](https://api.chucknorris.io/)
    * [Dad Jokes](https://icanhazdadjoke.com/api#fetch-a-random-dad-joke)

#### Bonus Points
If you have extra time and really want to impress us, here are a few suggestions.

  * Add tests and CI via CodeBuild
  * Add CodePipeline to auto-deploy your CloudFormation template
  * Add a simple UI that uses your API
  * Fully utilize APIGateway's capabilities in the swagger specification (validation, models, etc)
  * Extend functionality
    * Allow subscriptions to schedule their emails
    * Allow subscriptions to choose topics for their random content
  * Add a CloudWatch dashboard that shows important metrics for monitoring your service
