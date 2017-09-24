from troposphere import (
    Base64,
    ec2,
    GetAtt,
    Join,
    Output,
    Parameter,
    Ref,
    Template,
)

ApplicationPort = "3000"

t = Template()
t.add_description("Talk Me Up: We empower your words!")
t.add_parameter(Parameter(
    "KeyPair",
    Description="EC2 KeyPair to SSH",
    Type="AWS::EC2::KeyPair::KeyName",
    ConstraintDescription="must be the name of an existing EC2 KeyPair.",
))
t.add_resource(ec2.SecurityGroup(
    "SecurityGroup",
    GroupDescription="Allow SSH and TCP/{} access".format(ApplicationPort),
    SecurityGroupIngress=[
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp="0.0.0.0/0",
        ),
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort=ApplicationPort,
            ToPort=ApplicationPort,
            CidrIp="0.0.0.0/0",
        ),
    ],
))

ud = Base64(Join('\n', [
    "#!/bin/bash",
    "sudo yum -y install git",
    "git clone https://github.com/du6/talkmeup.git",
    "sudo yum -y install python35",
    "sudo yum -y install python35-setuptools",
    "sudo easy_install-3.5 pip",
    "pip3 install --upgrade pip",
    "sudo python3 -m pip install virtualenv",
    "virtualenv -p python3 talkmeup-env",
    "source talkmeup-env/bin/activate",
    "cd talkmeup",
    "pip install -r requirements.txt",
    "python manage.py migrate",
    "python manage.py runserver 0.0.0.0:" + ApplicationPort,
]))

t.add_resource(ec2.Instance(
    "instance",
    ImageId="ami-9e90a5fe",
    InstanceType="t2.micro",
    SecurityGroups=[Ref("SecurityGroup")],
    KeyName=Ref("KeyPair"),
    UserData=ud,
))
t.add_output(Output(
    "InstancePublicIp",
    Description="Public IP of our instance",
    Value=GetAtt("instance", "PublicIp"),
))
t.add_output(Output(
    "WebUrl",
    Description="Application endpoint",
    Value=Join("", [
        "http://", GetAtt("instance", "PublicDnsName"),
        ":",
        ApplicationPort,
    ]),
))

print (t.to_json())
