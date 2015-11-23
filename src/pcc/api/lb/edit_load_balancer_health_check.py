# -*- coding: utf-8 -*-

def command():
    return "edit-load-balancer-health-check"

def init_argument(parser):
    parser.add_argument("--load-balancer-no", required=True)
    parser.add_argument("--check-protocol", required=True)
    parser.add_argument("--check-port", required=True)
    parser.add_argument("--check-path", required=False)
    parser.add_argument("--check-timeout", required=True)
    parser.add_argument("--check-interval", required=True)
    parser.add_argument("--healthy-threshold", required=True)
    parser.add_argument("--unhealthy-threshold", required=True)

def execute(requester, args):
    load_balancer_no = args.load_balancer_no
    check_protocol = args.check_protocol
    check_port = args.check_port
    check_path = args.check_path
    check_timeout = args.check_timeout
    check_interval = args.check_interval
    healthy_threshold = args.healthy_threshold
    unhealthy_threshold = args.unhealthy_threshold

    parameters = {}
    parameters["LoadBalancerNo"] = load_balancer_no
    parameters["CheckProtocol"] = check_protocol
    parameters["CheckPort"] = check_port
    parameters["CheckTimeout"] = check_timeout
    parameters["CheckInterval"] = check_interval
    parameters["HealthyThreshold"] = healthy_threshold
    parameters["UnhealthyThreshold"] = unhealthy_threshold

    if (check_path != None):
        parameters["CheckPath"] = check_path

    return requester.execute("/EditLoadBalancerHealthCheck", parameters)
