import boto3
import time
aws_con=boto3.session.Session(profile_name="developer")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="ap-south-1")


my_inst_ob=ec2_con_re.Instance("i-0bf26c4deff3b3b85")
print("Starting given instance....")
my_inst_ob.stop()
