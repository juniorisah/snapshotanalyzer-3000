import boto3

if --name-- == '--main--':
    session = boto3.Session(profile_name='shotty')
    ec2 = session.resource( 'ec2' )

    for i in ec2.instance.all():
        print(i)
