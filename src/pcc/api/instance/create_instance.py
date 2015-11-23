# -*- coding: utf-8 -*-

def command():
    return "create-instance"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--instance-name", required=True)
    parser.add_argument("--image-no", required=True)
    parser.add_argument("--instance-type", required=False)
    parser.add_argument("--comment", required=False)

def execute(requester, args):
    farm_no = args.farm_no
    image_no = args.image_no
    instance_name = args.instance_name
    instance_type = args.instance_type
    comment = args.comment

    parameters = {}
    parameters["FarmNo"] = farm_no
    parameters["ImageNo"] = image_no
    parameters["InstanceName"] = instance_name

    if (instance_type != None):
        parameters["InstanceType"] = instance_type

    if (comment != None):
        parameters["Comment"] = comment

    return requester.execute("/CreateInstance", parameters)
