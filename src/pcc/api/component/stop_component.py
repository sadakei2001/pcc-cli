# -*- coding: utf-8 -*-

def command():
    return "stop-component"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--component-no", required=True)
    parser.add_argument("--instance-nos", required=True)
    parser.add_argument("--is-stop-instance", required=False)

def execute(requester, args):
    farm_no = args.farm_no
    component_no = args.component_no
    instance_nos = args.instance_nos
    is_stop_instance = args.is_stop_instance

    parameters = {}
    parameters["FarmNo"] = farm_no
    parameters["ComponentNo"] = component_no
    parameters["InstanceNos"] = instance_nos

    if (is_stop_instance != None):
        parameters["IsStopInstance"] = is_stop_instance

    return requester.execute("/StopComponent", parameters)
