import boto3
import time
import logging
import json
import sys


def scan_table(table_name):
    def remove_types(tweet):
        reformatted_tweet = {}
        for k, v in tweet.items():
            reformatted_tweet[k] = list(v.values())[0]
        return reformatted_tweet

    client = boto3.client('dynamodb')
    paginator = client.get_paginator('scan')
    scanned_data = []

    for page in paginator.paginate(TableName=table_name):
        items = page['Items']
        for item in items:
            r = remove_types(item)
            scanned_data.append(r)

    return scanned_data
