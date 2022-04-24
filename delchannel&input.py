import boto3
import time

client = boto3.client('medialive')

response = client.list_channels()

for channel in response["Channels"]:
    channel_arn = channel["Arn"]
    channel_uid = channel_arn.split(":")[-1]
    input_uid=channel["InputAttachments"][0]["InputId"]
    response = client.delete_channel(ChannelId=channel_uid)
    print('deleted channel:'+channel_uid)
    time.sleep(5)
    response = client.delete_input(InputId=input_uid)
    print('deleted input:'+input_uid)
