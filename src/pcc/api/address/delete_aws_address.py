# -*- coding: utf-8 -*-

def command():
    return "delete-aws-address"

def init_argument(parser):
    parser.add_argument("--address-no", required=True)

def execute(requester, args):
    address_no = args.address_no

    parameters = {}
    parameters["AddressNo"] = address_no

    return requester.execute("/DeleteAwsAddress", parameters)
