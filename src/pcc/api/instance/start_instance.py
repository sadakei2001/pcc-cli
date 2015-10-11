# -*- coding: utf-8 -*-

def command():
    return "start-instance"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--instance-no", required=True)
    parser.add_argument("--is-start-service", required=False)

def execute(requester, args):
    farm_no = args.farm_no
    instance_no = args.instance_no
    is_start_service = args.is_start_service

    parameters = {}
    parameters["FarmNo"] = farm_no
    parameters["InstanceNo"] = instance_no

    if (is_start_service != None):
        parameters["IsStartService"] = is_start_service

    return requester.execute("/StartInstance", parameters)
