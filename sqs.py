import boto3
import json

twitter_message_group_id = "twitterLandingTable"
queue_name = "twitter_queue.fifo"

def read_input_variables():
    client = boto3.client('sqs')
    queues = client.list_queues()['QueueUrls']
    queue_url = ''
    for _ in queues:
        if queue_name in _:
            queue_url = _
            break
    response = client.receive_message(
        QueueUrl = queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10
    )
    json_resp = json.loads(response['Messages'][0]['Body'])
    table_name = json['table_name']
    s3_bucket_name = json['s3_bucket_name']

    return table_name, s3_bucket_name