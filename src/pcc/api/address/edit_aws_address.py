# -*- coding: utf-8 -*-

def command():
    return "edit-aws-address"

def init_argument(parser):
    parser.add_argument("--address-no", required=True)
    parser.add_argument("--comment", required=True)

def execute(requester, args):
    address_no = args.address_no
    comment = args.comment

    parameters = {}
    parameters["AddressNo"] = address_no
    parameters["Comment"] = comment

    return requester.execute("/EditAwsAddress", parameters)
