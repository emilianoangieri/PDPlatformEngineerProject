def lambda_handler(event, context):
    # TODO implement
    
    url = "https://icanhazdadjoke.com"
    #import urllib.request
    #contents = urllib.request.urlopen(url)
    
    import subprocess
    proc = subprocess.Popen(["curl", "-H Accept: application/json", "https://icanhazdadjoke.com/"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    
    print(out)
    
    import boto3
    client = boto3.client('sns')
    
    response = client.publish(
    TopicArn='arn:aws:sns:eu-west-1:489290800165:email',
    Message=out,
    Subject='your joke',
    )
    
    return "ok"