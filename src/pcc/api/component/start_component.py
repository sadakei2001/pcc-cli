# -*- coding: utf-8 -*-

def command():
    return "start-component"

def init_argument(parser):
    parser.add_argument("--component-no", required=True)
    parser.add_argument("--instance-nos", required=True)

def execute(requester, args):
    component_no = args.component_no
    instance_nos = args.instance_nos

    parameters = {}
    parameters["ComponentNo"] = component_no
    parameters["InstanceNos"] = instance_nos

    return requester.execute("/StartComponent", parameters)
