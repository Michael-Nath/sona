from webbrowser import get
import boto3 as bo
import json

def get_most_recent_brain_data(all_brain_data):
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    return [brain_data["Key"] for brain_data in sorted(all_brain_data, key=get_last_modified)][-1]


def pull_brain_data():
    CONFIG = json.load("config.json")
    s3 = bo.client("s3")
    all_brain_data = s3.list_objects_v2(Bucket=CONFIG["bucket"])["Contents"]
    most_recent_brain_data = get_most_recent_brain_data(all_brain_data)
    return most_recent_brain_data
