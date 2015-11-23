# -*- coding: utf-8 -*-

def command():
    return "delete-load-balancer-listener"

def init_argument(parser):
    parser.add_argument("--load-balancer-no", required=True)
    parser.add_argument("--load-balancer-port", required=True)

def execute(requester, args):
    load_balancer_no = args.load_balancer_no
    load_balancer_port = args.load_balancer_port

    parameters = {}
    parameters["LoadBalancerNo"] = load_balancer_no
    parameters["LoadBalancerPort"] = load_balancer_port

    return requester.execute("/DeleteLoadBalancerListener", parameters)
