import json
import boto3


def get_mirror_secrets(secret_id):
    client = boto3.client('secretsmanager')
    get_secret_value_response = client.get_secret_value(
            SecretId=secret_id
    )
    return json.loads(get_secret_value_response['SecretString'])


