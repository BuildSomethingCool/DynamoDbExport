from dynamo import scan_table
from sqs import read_input_variables
import util
import os


param_input_src = os.getenv('INPUT_STORE')
table_name = ''
dest_bucket = ''
if param_input_src.lower() == 'env':
    table_name = os.getenv("SRC_TABLE") 
    dest_bucket = os.getenv('DEST_BUCKET_NAME')
else:
    params = read_input_variables()
    table_name = params[0]
    dest_bucket = params[1]


if __name__ == '__main__':
    csv_name = f'raw-{table_name}.csv'
    data = scan_table(table_name)
    columns = data[0].keys()
    out_filename = util.export_to_csv(csv_name, columns, data)
    r = util.put_to_s3(out_filename, csv_name, dest_bucket)
    print(r)


