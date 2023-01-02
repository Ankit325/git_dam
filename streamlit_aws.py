import streamlit as st
import boto3
import os
import json


input_bucket='custom-labels-console-ap-northeast-1-c8d279ec4d'

#Upload to streamlit
uploader= st.file_uploader("Choose a file")
#Upload to s3
if uploader is not None:
    s3 = boto3.client('s3')
    s3.upload_fileobj(uploader, input_bucket, uploader.name)
    st.write("File uploaded")
    
    # Download from s3
    s3_r=boto3.resource("s3")
    my_bucket=s3_r.Bucket(input_bucket)
    for object in my_bucket.objects.all():
        #print(object)
        if(object.key.endswith(".json")):
            s3.download_file(input_bucket, object.key, object.key)
            st.write("File downloaded")
            # Read json file
            with open(object.key) as f:
                data = json.load(f)
                st.write(data)