# -*- coding: utf-8 -*-

def command():
    return "stop-all-component"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--is-stop-instance", required=False)

def execute(requester, args):
    farm_no = args.farm_no
    is_stop_instance = args.is_stop_instance

    parameters = {}
    parameters["FarmNo"] = farm_no

    if (is_stop_instance != None):
        parameters["IsStopInstance"] = is_stop_instance

    return requester.execute("/StopAllComponent", parameters)
