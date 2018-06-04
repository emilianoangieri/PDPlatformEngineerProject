def lambda_handler(event, context):
    # TODO implement
    import boto3
    client = boto3.client('sns')
    
    email=str(event['data']['email'])
    print("This is the email to unsubscribe "+email)
    
    #find all email in subscription
    response = client.list_subscriptions_by_topic(
    TopicArn='arn:aws:sns:eu-west-1:489290800165:email',
    )
    
    
    for email_addr in response['Subscriptions']:
        if email_addr['Endpoint'] == email:
            print('Email present in subscription. I can unsubscribe')
            print('SubscriptionArn is '+email_addr['SubscriptionArn'])
            response = client.unsubscribe(
            SubscriptionArn=email_addr['SubscriptionArn']
            )
            return 'Email '+email_addr['Endpoint']+' sucessfully unsubscribe'
             
        print(email_addr['Endpoint'])
    
    #response = client.unsubscribe(
    #SubscriptionArn='string'
    #)
    
    
    return 'Email not found'
