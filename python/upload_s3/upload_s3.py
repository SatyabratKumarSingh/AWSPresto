import boto3, os
import progressbar

bucket_name = "sat-001-insurance-csv"
file_path = '/Users/satya/PycharmProjects/python_presto/resources/insurance_sample.csv'

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

statinfo = os.stat(file_path)

up_progress = progressbar.progressbar.ProgressBar(maxval=statinfo.st_size)

up_progress.start()

def upload_progress(chunk):
    up_progress.update(up_progress.currval + chunk)

s3.upload_file(file_path, bucket_name, os.path.basename(file_path)
, Callback=upload_progress)

up_progress.finish()
