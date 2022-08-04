
import boto3
# s3_client = boto3.client('s3')
def upload_to_s3(file_path, file_name):
    s3_resource = boto3.resource('s3')

    # with open('/Users/rohitsingh/Documents/Projects/IUC/FormSubmission/gcp/init_gcp.py', 'rb') as FID:
    #     file_path = FID
    file_path.seek(0)
    import io
    respo=s3_resource.meta.client.upload_fileobj(
        io.BytesIO(file_path.read()),
        'iuc-website-abstracts-fall-pts-2022',
        file_name,
        ExtraArgs={'ACL': 'public-read', 'ContentType': "application/pdf"})
    return "https://iuc-website-abstracts-fall-pts-2022.s3.us-east-2.amazonaws.com/" + file_name


# s3_client.meta.client.upload_file(
#     Filename=first_file_name, Bucket=first_bucket_name,
#     Key=first_file_name, ExtraArgs={
#                           'ACL': 'public-read'})