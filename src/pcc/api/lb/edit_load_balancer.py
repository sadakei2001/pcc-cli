# -*- coding: utf-8 -*-

def command():
    return "edit-load-balancer"

def init_argument(parser):
    parser.add_argument("--load-balancer-no", required=True)
    parser.add_argument("--component-no", required=True)
    parser.add_argument("--security-groups", required=True)
    parser.add_argument("--subnet", required=False)
    parser.add_argument("--comment", required=False)
    parser.add_argument("--is-internal", required=False)

def execute(requester, args):
    load_balancer_no = args.load_balancer_no
    component_no = args.component_no
    security_groups = args.security_groups
    subnet = args.subnet
    comment = args.comment
    is_internal = args.is_internal

    parameters = {}
    parameters["LoadBalancerNo"] = load_balancer_no
    parameters["ComponentNo"] = component_no
    parameters["SecurityGroups"] = security_groups

    if (subnet != None):
        parameters["Subnet"] = subnet

    if (comment != None):
        parameters["Comment"] = comment

    if (is_internal != None):
        parameters["IsInternal"] = is_internal

    return requester.execute("/EditLoadBalancer", parameters)
