import boto3

client = boto3.client('medialive')

response = client.create_input(
    Destinations=[
        {
            'StreamName': 'test111'
        },
    ],
    InputSecurityGroups=[
        'xxxxxxx',
    ],
    Name='test111',
    RoleArn='arn:aws:iam::xxxxxxxxxxxx:user/xxxxx',

    Type='RTP_PUSH',
)

print (response)
