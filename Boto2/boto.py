import boto3

client = boto3.client('s3')

# response = client.create_bucket(
#     Bucket='bucket-satyam-123'
# )


response = client.get_bucket_acl(
    Bucket='bucket-satyam-123',

)
print(response)
owner = response['Owner']['DisplayName']
print(owner)






