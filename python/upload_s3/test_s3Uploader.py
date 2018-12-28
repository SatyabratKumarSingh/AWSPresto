from unittest import TestCase

from upload_s3 import S3Uploader

class TestS3Uploader(TestCase):

    def test_upload(self):
        bucket_name = "sat-001-insurance-csv"
        aws_access_key_id = "XXXX"
        aws_secret_access_key = "XXXX"
        file_path = '/Users/satya/PycharmProjects/python_presto/resources/insurance_sample.csv'
        uploader_s3 = S3Uploader(aws_access_key_id, aws_secret_access_key)
        uploader_s3.upload(file_path,bucket_name)
