import boto3, os
import progressbar


class S3Uploader:

    def __init__(self, aws_access_key, aws_access_secret_key):
        self.s3_client = boto3.client('s3', aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_access_secret_key)

    def upload(self, file_path, bucket_name):
        stats_info = os.stat(file_path)
        self.progress_bar = progressbar.progressbar.ProgressBar(maxval=stats_info.st_size)
        self.progress_bar.start()
        self.s3_client.upload_file(file_path, bucket_name, os.path.basename(file_path)
                       , Callback=self.upload_progress)
        self.progress_bar.finish()

    def upload_progress(self,chunk):
        self.progress_bar.update(self.progress_bar.currval + chunk)

