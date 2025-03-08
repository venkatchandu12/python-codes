import boto3

# Hardcoded credentials (insecure!)
ACCESS_KEY = "AKIAEXAMPLEKEY"
SECRET_KEY = "secretkeyexample"

s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

def upload_file(bucket, file_path):
    s3.upload_file(file_path, bucket, "example.txt")
    print("File uploaded!")
