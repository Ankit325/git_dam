import streamlit as st
import boto3
import os


input_bucket='custom-labels-console-ap-northeast-1-c8d279ec4d'

#Upload to streamlit
uploader= st.file_uploader("Choose a file")
#Upload to s3
if uploader is not None:
    s3 = boto3.client('s3')
    client=boto3.client('rekognition')
    s3.upload_fileobj(uploader, input_bucket, uploader.name)
    st.write("File uploaded")
    response=client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': input_bucket,
                'Name': uploader.name,
            }
        },
        Features=["IMAGE_PROPERTIES"],

    )
    st.write(response)

#Download from s3
# my_bucket = s3.Bucket(input_bucket)
# for s3_file in my_bucket.objects.all():
#     s3_file.download_file(os.path.basename(s3_file.key))
#     st.write("File downloaded")

    
   