import boto3


aws_mag_con=boto3.session.Session(profile_name= 'developer')
s3_obj= aws_mag_con.resource('s3')

for bucket in s3_obj.buckets.all():
    print(bucket.name)


print("LIST OF IAM ")

iam_obj= aws_mag_con.resource('iam')

for each_user in iam_obj.users.all():
    print(each_user.name)




