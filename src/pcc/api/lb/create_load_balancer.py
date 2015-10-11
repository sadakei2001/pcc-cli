# -*- coding: utf-8 -*-

def command():
    return "create-load-balancer"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--load-balancer-name", required=True)
    parser.add_argument("--load-balancer-type", required=True)
    parser.add_argument("--component-no", required=True)
    parser.add_argument("--platform-no", required=True)
    parser.add_argument("--comment", required=False)
    parser.add_argument("--is-internal", required=False)

def execute(requester, args):
    farm_no = args.farm_no
    load_balancer_name = args.load_balancer_name
    load_balancer_type = args.load_balancer_type
    component_no = args.component_no
    platform_no = args.platform_no
    comment = args.comment
    is_internal = args.is_internal

    parameters = {}
    parameters["FarmNo"] = farm_no
    parameters["LoadBalancerName"] = load_balancer_name
    parameters["LoadBalancerType"] = load_balancer_type
    parameters["ComponentNo"] = component_no
    parameters["PlatformNo"] = platform_no

    if (comment != None):
        parameters["Comment"] = comment

    if (is_internal != None):
        parameters["IsInternal"] = is_internal

    return requester.execute("/CreateLoadBalancer", parameters)
