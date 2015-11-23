# -*- coding: utf-8 -*-

def command():
    return "attach-component"

def init_argument(parser):
    parser.add_argument("--component-no", required=True)
    parser.add_argument("--instance-no", required=True)

def execute(requester, args):
    component_no = args.component_no
    instance_no = args.instance_no

    parameters = {}
    parameters["ComponentNo"] = component_no
    parameters["InstanceNo"] = instance_no

    return requester.execute("/AttachComponent", parameters)
