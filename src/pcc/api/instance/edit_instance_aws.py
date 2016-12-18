# -*- coding: utf-8 -*-

def command():
    return "edit-instance-aws"

def init_argument(parser):
    parser.add_argument("--instance-no", required=True)
    parser.add_argument("--instance-type", required=True)
    parser.add_argument("--key-name", required=True)
    parser.add_argument("--security-groups", required=True)
    parser.add_argument("--subnet", required=True)
    parser.add_argument("--availability-zone", required=False)
    parser.add_argument("--ip-address", required=False)
    parser.add_argument("--private-ip-address", required=False)
    parser.add_argument("--comment", required=False)

def execute(requester, args):
    instance_no = args.instance_no
    instance_type = args.instance_type
    key_name = args.key_name
    security_groups = args.security_groups
    subnet = args.subnet
    availability_zone = args.availability_zone
    ip_address = args.ip_address
    private_ip_address = args.private_ip_address
    comment = args.comment

    parameters = {}
    parameters["InstanceNo"] = instance_no
    parameters["InstanceType"] = instance_type
    parameters["KeyName"] = key_name
    parameters["SecurityGroups"] = security_groups
    parameters["Subnet"] = subnet

    if (availability_zone != None):
        parameters["AvailabilityZone"] = availability_zone

    if (ip_address != None):
        parameters["IpAddress"] = ip_address

    if (private_ip_address != None):
        parameters["PrivateIpAddress"] = private_ip_address

    if (comment != None):
        parameters["Comment"] = comment

    return requester.execute("/EditInstanceAws", parameters)
