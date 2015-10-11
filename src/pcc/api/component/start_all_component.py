# -*- coding: utf-8 -*-

def command():
    return "start-all-component"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)

def execute(requester, args):
    farm_no = args.farm_no

    parameters = {}
    parameters["FarmNo"] = farm_no

    return requester.execute("/StartAllComponent", parameters)
