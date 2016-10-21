# -*- coding: utf-8 -*-

def command():
    return "edit-instance-vmware"

def init_argument(parser):
    parser.add_argument("--instance-no", required=True)
    parser.add_argument("--instance-type", required=True)
    parser.add_argument("--key-name", required=True)
    parser.add_argument("--compute-resource", required=True)
    parser.add_argument("--is-static-ip", required=True)
    parser.add_argument("--ip-address", required=False)
    parser.add_argument("--subnet-mask", required=False)
    parser.add_argument("--default-gateway", required=False)
    parser.add_argument("--comment", required=False)

def execute(requester, args):
    instance_no = args.instance_no
    instance_type = args.instance_type
    key_name = args.key_name
    compute_resource = args.compute_resource
    is_static_ip = args.is_static_ip
    ip_address = args.ip_address
    subnet_mask = args.subnet_mask
    default_gateway = args.default_gateway
    comment = args.comment

    parameters = {}
    parameters["InstanceNo"] = instance_no
    parameters["InstanceType"] = instance_type
    parameters["KeyName"] = key_name
    parameters["ComputeResource"] = compute_resource
    parameters["IsStaticIp"] = is_static_ip

    if (ip_address != None):
        parameters["IpAddress"] = ip_address

    if (subnet_mask != None):
        parameters["SubnetMask"] = subnet_mask

    if (default_gateway != None):
        parameters["DefaultGateway"] = default_gateway

    if (comment != None):
        parameters["Comment"] = comment

    return requester.execute("/EditInstanceVmware", parameters)
