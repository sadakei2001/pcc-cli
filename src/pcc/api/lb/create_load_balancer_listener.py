# -*- coding: utf-8 -*-

def command():
    return "create-load-balancer-listener"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--load-balancer-no", required=True)
    parser.add_argument("--load-balancer-port", required=True)
    parser.add_argument("--service-port", required=True)
    parser.add_argument("--protocol", required=True)
    parser.add_argument("--ssl-key-no", required=False)

def execute(requester, args):
    farm_no = args.farm_no
    load_balancer_no = args.load_balancer_no
    load_balancer_port = args.load_balancer_port
    service_port = args.service_port
    protocol = args.protocol
    ssl_key_no = args.ssl_key_no

    parameters = {}
    parameters["FarmNo"] = farm_no
    parameters["LoadBalancerNo"] = load_balancer_no
    parameters["LoadBalancerPort"] = load_balancer_port
    parameters["ServicePort"] = service_port
    parameters["Protocol"] = protocol

    if (ssl_key_no != None):
        parameters["SslKeyNo"] = ssl_key_no

    return requester.execute("/CreateLoadBalancerListener", parameters)
