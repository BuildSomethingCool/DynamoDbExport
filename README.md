# DynamoDB Export Script

This repo contains the source code for a containerized python script that will export a DynamoDB table to csv format in s3. It takes in the source table name and destination bucket name as environment variables

## Env variables
### SRC_TABLE - name of the DynamoDB table
### DEST_BUCKET_NAME - Name of the destination s3 bucket

#### Image location - public.ecr.aws/t9y1m9m9/dynamodb_export

#### Continuous Integration - This script is deployed to ECR on pushed to main via github actions