import boto3 as bo
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

s3 = bo.client("s3")
CONFIG = {
    "S3_URI": os.environ.get("S3_URI")
}

        
def get_most_recent_brain_data(all_brain_data) -> str:
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    return [brain_data["Key"] for brain_data in sorted(all_brain_data, key=get_last_modified)][-1]


def pull_brain_data():
    print(s3)
    all_brain_data = s3.list_objects_v2(Bucket=CONFIG["S3_URI"])["Contents"]
    most_recent_brain_data = get_most_recent_brain_data(all_brain_data)
    brain_data_dataframe = get_brain_data_having_key(most_recent_brain_data)
    return brain_data_dataframe

def get_brain_data_having_key(csv_key):
    response = s3.get_object(Bucket=CONFIG["S3_URI"], Key=csv_key)
    df = pd.read_csv(response["Body"])
    return df
    