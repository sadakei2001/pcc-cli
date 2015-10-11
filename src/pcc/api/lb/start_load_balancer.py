# -*- coding: utf-8 -*-

def command():
    return "start-load-balancer"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--load-balancer-no", required=True)

def execute(requester, args):
    farm_no = args.farm_no
    load_balancer_no = args.load_balancer_no

    parameters = {}
    parameters["FarmNo"] = farm_no
    parameters["LoadBalancerNo"] = load_balancer_no

    return requester.execute("/StartLoadBalancer", parameters)
