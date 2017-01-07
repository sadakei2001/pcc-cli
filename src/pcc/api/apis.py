# -*- coding: utf-8 -*-

__commands = []
__apis = {}

def commands():
    return __commands

def get(command):
    return __apis.get(command)

def add(api):
    command = api.command()
    __commands.append(command)
    __apis[command] = api


# Farm
from .farm import list_farm
from .farm import create_farm
from .farm import edit_farm
from .farm import delete_farm
add(list_farm)
add(create_farm)
add(edit_farm)
add(delete_farm)

# Instance
from .instance import list_instance
from .instance import describe_instance
from .instance import create_instance
from .instance import edit_instance_aws
from .instance import edit_instance_vmware
from .instance import delete_instance
from .instance import start_instance
from .instance import stop_instance
from .instance import start_all_instance
from .instance import stop_all_instance
from .instance import enable_zabbix_monitoring_instance
from .instance import disable_zabbix_monitoring_instance
add(list_instance)
add(describe_instance)
add(create_instance)
add(edit_instance_aws)
add(edit_instance_vmware)
add(delete_instance)
add(start_instance)
add(stop_instance)
add(start_all_instance)
add(stop_all_instance)
add(enable_zabbix_monitoring_instance)
add(disable_zabbix_monitoring_instance)

# Component
from .component import list_component_type
from .component import list_component
from .component import describe_component
from .component import create_component
from .component import edit_component
from .component import delete_component
from .component import get_attachable_component
from .component import attach_component
from .component import detach_component
from .component import start_component
from .component import stop_component
from .component import start_all_component
from .component import stop_all_component
add(list_component_type)
add(list_component)
add(describe_component)
add(create_component)
add(edit_component)
add(delete_component)
add(get_attachable_component)
add(attach_component)
add(detach_component)
add(start_component)
add(stop_component)
add(start_all_component)
add(stop_all_component)

# LoadBalancer
from .lb import list_load_balancer
from .lb import describe_load_balancer
from .lb import create_load_balancer
from .lb import edit_load_balancer
from .lb import delete_load_balancer
from .lb import attach_load_balancer
from .lb import detach_load_balancer
from .lb import start_load_balancer
from .lb import stop_load_balancer
from .lb import describe_load_balancer_health_check
from .lb import edit_load_balancer_health_check
from .lb import list_load_balancer_listener
from .lb import create_load_balancer_listener
from .lb import delete_load_balancer_listener
from .lb import enable_load_balancer_listener
from .lb import disable_load_balancer_listener
add(list_load_balancer)
add(describe_load_balancer)
add(create_load_balancer)
add(edit_load_balancer)
add(delete_load_balancer)
add(attach_load_balancer)
add(detach_load_balancer)
add(start_load_balancer)
add(stop_load_balancer)
add(describe_load_balancer_health_check)
add(edit_load_balancer_health_check)
add(list_load_balancer_listener)
add(create_load_balancer_listener)
add(delete_load_balancer_listener)
add(enable_load_balancer_listener)
add(disable_load_balancer_listener)

# Platform
from .platform import list_platform
from .platform import describe_platform
add(list_platform)
add(describe_platform)

# Image
from .image import list_image
add(list_image)

# Address
from .address import list_aws_address
from .address import add_aws_address
from .address import edit_aws_address
from .address import delete_aws_address
add(list_aws_address)
add(add_aws_address)
add(edit_aws_address)
add(delete_aws_address)

# Template
from .template import list_template
add(list_template)
