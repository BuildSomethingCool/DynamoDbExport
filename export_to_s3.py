from dynamo import scan_table
import util
import os

table_name = os.getenv("SRC_TABLE")
dest_bucket = os.getenv('DEST_BUCKET_NAME')


if __name__ == '__main__':
    csv_name = f'raw-{table_name}.csv'
    data = scan_table(table_name)
    columns = data[0].keys()
    out_filename = util.export_to_csv(csv_name, columns, data)
    r = util.put_to_s3(out_filename, csv_name, 'raw-tweets-3082')
    print(r)


