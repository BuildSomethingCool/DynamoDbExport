from dynamo import scan_table
import util


if __name__ == '__main__':
    data = scan_table('RawTweets-phoenix_suns')
    columns = data[0].keys()
    out_filename = util.export_to_csv('raw-RawTweets-phoenix_suns.csv', columns, data)
    r = util.put_to_s3(out_filename, 'raw-RawTweets-phoenix_suns.csv', 'raw-tweets-3082')
    print(r)


