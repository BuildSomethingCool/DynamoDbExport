import csv
import traceback


def export_to_csv(csv_name, headers, data):
    try:
        with open(f'/tmp/{csv_name}', "w") as out_file:
            writer = csv.writer(out_file, delimiter=',')
            writer.writerow(headers)
            for i in data:
                stage_row = []
                for row in headers:
                    stage_row.append(i[row])
                writer.writerow(stage_row)
    except:
        return

    return f'/tmp/{csv_name}'


def put_to_s3(filename, shortname, bucket_name):
    try:
        with open(filename, "r") as in_file:
            import boto3
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(bucket_name)
            response = bucket.put_object(
                ACL='private',
                Body=open(filename, 'rb').read(),
                Key=f"raw/{shortname}"
            )
            return response
    except Exception as e:
        print("Upload to s3 failed", e)
        traceback.print_exc()
        return
