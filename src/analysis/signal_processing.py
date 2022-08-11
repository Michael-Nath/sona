import boto3
import pandas as pd
import math
import io

client = boto3.client('s3')

response = client.get_object(Bucket="sona-brain-data", Key="shubhJul-17-2022.csv")

df = pd.read_csv(response["Body"])
df_list = list(df.columns.values)
print(len(df_list))



#https://realpython.com/python-scipy-fft/ - explains how to use scipy with example