import streamlit as st
import boto3
import os
import json
import time

output_bucket='final-output-0123456'
input_bucket='image-test-0123456'

# Upload to streamlit
uploader= st.file_uploader("Choose a file")
#Upload to s3
if uploader is not None:
    s3 = boto3.client('s3')
    s3.upload_fileobj(uploader, input_bucket, uploader.name)
    name=uploader.name
    st.write("File uploaded")
    #Change file name
    # st.write(name)
    base=os.path.splitext(name)[1]
    # st.write(base)
    file_name=name.replace(base, '.json')
    #st.write(file_name)

    #Refreshing cache
    # clients=boto3.client("storagegateway")
    # response = clients.refresh_cache(
    #         FileShareARN='arn:aws:s3:ap-northeast-1:990490295689:accesspoint/accessoutput-0123456')

    # Download from s3
    time.sleep(10)
    s3_r=boto3.resource("s3")
    # file_name="78666984.json"
    my_bucket=s3_r.Bucket(output_bucket)
    for object in my_bucket.objects.all():
        #print(object)
        # st.write(object.key)
        if(object.key==file_name):
            st.write("File found")
            s3.download_file(output_bucket, object.key, object.key)
            st.write("File downloaded")
            # Read json file
            with open(object.key) as f:
                data = json.load(f)
                st.write(data)