import json

import pytest
from moto import mock_aws
from boto3 import client
import downloadJson


@pytest.fixture(scope="module")
def s3_client():
    with mock_aws():
        s3_client = client("s3")
        yield s3_client


def test_create_bucket(s3_client):
    bucket_name = "meu-bucket"
    s3_client.create_bucket(Bucket=bucket_name)

    bucket = s3_client.list_buckets()["Buckets"][0]
    assert bucket["Name"] == bucket_name


def test_upload_object(s3_client):
    bucket_name = "meu-bucket"
    object_key = "meu-objeto.json"
    j = [{"nome":"endereco","campos":[{"Field":"id","Type":"int","Null":"NO","Key":"PRI","Default":"None","Extra":"auto_increment"},{"Field":"rua","Type":"varchar(200)","Null":"YES","Key":"","Default":"None","Extra":""},{"Field":"numero","Type":"varchar(200)","Null":"YES","Key":"","Default":"None","Extra":""}]}]
    object_body = json.dumps(j)

    s3_client.create_bucket(Bucket=bucket_name)
    s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=object_body)

    response = downloadJson.getJsonBucket(nameBucket=bucket_name, nameFile=object_key)
    assert response == object_body
