# -*- coding: utf-8 -*-

def command():
    return "edit-component"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--component-no", required=True)
    parser.add_argument("--disk-size", required=True)
    parser.add_argument("--comment", required=False)
    parser.add_argument("--custom-param1", required=False)
    parser.add_argument("--custom-param2", required=False)
    parser.add_argument("--custom-param3", required=False)

def execute(requester, args):
    farm_no = args.farm_no
    component_no = args.component_no
    disk_size = args.disk_size
    comment = args.comment
    custom_param1 = args.custom_param1
    custom_param2 = args.custom_param2
    custom_param3 = args.custom_param3

    parameters = {}
    parameters["FarmNo"] = farm_no
    parameters["ComponentNo"] = component_no
    parameters["DiskSize"] = disk_size

    if (comment != None):
        parameters["Comment"] = comment

    if (custom_param1 != None):
        parameters["CustomParam1"] = custom_param1

    if (custom_param2 != None):
        parameters["CustomParam2"] = custom_param2

    if (custom_param3 != None):
        parameters["CustomParam3"] = custom_param3

    return requester.execute("/EditComponent", parameters)
