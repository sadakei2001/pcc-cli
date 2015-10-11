# -*- coding: utf-8 -*-

def command():
    return "edit-farm"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--comment", required=False)

def execute(requester, args):
    farm_no = args.farm_no
    comment = args.comment

    parameters = {}
    parameters["FarmNo"] = farm_no

    if (comment != None):
        parameters["Comment"] = comment

    return requester.execute("/EditFarm", parameters)
