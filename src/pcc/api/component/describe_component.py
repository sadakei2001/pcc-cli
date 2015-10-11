# -*- coding: utf-8 -*-

def command():
    return "describe-component"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--component-no", required=True)

def execute(requester, args):
    farm_no = args.farm_no
    component_no = args.component_no

    parameters = {}
    parameters["FarmNo"] = farm_no
    parameters["ComponentNo"] = component_no

    return requester.execute("/DescribeComponent", parameters)
