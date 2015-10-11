# -*- coding: utf-8 -*-

def command():
    return "create-farm"

def init_argument(parser):
    parser.add_argument("--farm-name", required=True)
    parser.add_argument("--template-no", required=True)
    parser.add_argument("--comment")

def execute(requester, args):
    farm_name = args.farm_name
    template_no = args.template_no
    comment = args.comment

    parameters = {}
    parameters["CloudName"] = farm_name
    parameters["TemplateNo"] = template_no

    if (comment != None):
        parameters["Comment"] = comment

    return requester.execute("/CreateFarm", parameters)
