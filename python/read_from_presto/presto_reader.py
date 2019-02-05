import boto3

aws_access_key_id = "XXXX"
aws_secret_access_key = "XXXX"
client = boto3.client('emr', region_name='us-east-1',aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)
response = client.run_job_flow(
            Name="Satya's Spark Presto Cluster",
            LogUri='s3://sat-emr-presto-logs/logs',
            ReleaseLabel='emr-5.20.0',
            Applications=[
                {
                    'Name': 'Spark'
                },
                {
                    'Name': 'Presto'
                },
            ],
            Instances={
                'InstanceGroups': [
                    {
                        'Name': "Master nodes",
                        'Market': 'ON_DEMAND',
                        'InstanceRole': 'MASTER',
                        'InstanceType': 'm1.medium',
                        'InstanceCount': 1,
                    },
                    {
                        'Name': "Slave nodes",
                        'Market': 'ON_DEMAND',
                        'InstanceRole': 'CORE',
                        'InstanceType': 'm1.medium',
                        'InstanceCount': 1,
                    }
                ],
                'Ec2KeyName': 'aws_emr',
                'KeepJobFlowAliveWhenNoSteps': True,
                'TerminationProtected': False,
            },

            VisibleToAllUsers=True,
            JobFlowRole='EMR_EC2_DefaultRole',
            ServiceRole='EMR_DefaultRole',

        )
print ('cluster created with the step...', response['JobFlowId'])


