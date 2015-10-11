# -*- coding: utf-8 -*-

def command():
    return "create-component"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--component-name", required=True)
    parser.add_argument("--component-type-no", required=True)
    parser.add_argument("--disk-size", required=True)
    parser.add_argument("--comment", required=False)

def execute(requester, args):
    farm_no = args.farm_no
    component_name = args.component_name
    component_type_no = args.component_type_no
    disk_size = args.disk_size
    comment = args.comment

    parameters = {}
    parameters["FarmNo"] = farm_no
    parameters["ComponentName"] = component_name
    parameters["ComponentTypeNo"] = component_type_no
    parameters["DiskSize"] = disk_size

    if (comment != None):
        parameters["Comment"] = comment

    return requester.execute("/CreateComponent", parameters)
