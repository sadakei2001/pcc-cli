# -*- coding: utf-8 -*-

def command():
    return "detach-load-balancer"

def init_argument(parser):
    parser.add_argument("--load-balancer-no", required=True)
    parser.add_argument("--instance-no", required=True)

def execute(requester, args):
    load_balancer_no = args.load_balancer_no
    instance_no = args.instance_no

    parameters = {}
    parameters["LoadBalancerNo"] = load_balancer_no
    parameters["InstanceNo"] = instance_no

    return requester.execute("/DetachLoadBalancer", parameters)
