def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    email=str(event['data']['email'])
    print("This is the email to subscribe "+email)
    
    import boto3

    client = boto3.client('sns')
    
    #find all email in subscription
    response = client.list_subscriptions_by_topic(
    TopicArn='arn:aws:sns:eu-west-1:489290800165:email',
    )
    
    
    for email_addr in response['Subscriptions']:
        if email_addr['Endpoint'] == email:
            print('Email already present in subscription')
            raise MyValidationError("Email already present in subscription") 
        print(email_addr['Endpoint'])

    #subscribe email
    response = client.subscribe(
    TopicArn='arn:aws:sns:eu-west-1:489290800165:email',
    Protocol='email',
    Endpoint=email
    )
    
    return 'email '+email+' successfull subscribed'

class MyValidationError(Exception):
    pass