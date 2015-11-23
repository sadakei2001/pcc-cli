# -*- coding: utf-8 -*-

def command():
    return "list-load-balancer-listener"

def init_argument(parser):
    parser.add_argument("--load-balancer-no", required=True)

def execute(requester, args):
    load_balancer_no = args.load_balancer_no

    parameters = {}
    parameters["LoadBalancerNo"] = load_balancer_no

    return requester.execute("/ListLoadBalancerListener", parameters)
