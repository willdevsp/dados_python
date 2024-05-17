import boto3
s3Client = boto3.client("s3")

def getJsonBucket(nameBucket,nameFile):
    data = s3Client.get_object(Bucket=nameBucket, Key=nameFile)
    jsonData = data["Body"].read().decode('utf-8')
    return jsonData
