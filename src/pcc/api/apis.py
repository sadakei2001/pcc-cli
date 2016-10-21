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
import farm.list_farm
import farm.create_farm
import farm.edit_farm
import farm.delete_farm
add(farm.list_farm)
add(farm.create_farm)
add(farm.edit_farm)
add(farm.delete_farm)

# Instance
import instance.list_instance
import instance.describe_instance
import instance.create_instance
import instance.edit_instance_aws
import instance.edit_instance_vmware
import instance.delete_instance
import instance.start_instance
import instance.stop_instance
import instance.start_all_instance
import instance.stop_all_instance
import instance.enable_zabbix_monitoring_instance
import instance.disable_zabbix_monitoring_instance
add(instance.list_instance)
add(instance.describe_instance)
add(instance.create_instance)
add(instance.edit_instance_aws)
add(instance.edit_instance_vmware)
add(instance.delete_instance)
add(instance.start_instance)
add(instance.stop_instance)
add(instance.start_all_instance)
add(instance.stop_all_instance)
add(instance.enable_zabbix_monitoring_instance)
add(instance.disable_zabbix_monitoring_instance)

# Component
import component.list_component_type
import component.list_component
import component.describe_component
import component.create_component
import component.edit_component
import component.delete_component
import component.get_attachable_component
import component.attach_component
import component.detach_component
import component.start_component
import component.stop_component
import component.start_all_component
import component.stop_all_component
add(component.list_component_type)
add(component.list_component)
add(component.describe_component)
add(component.create_component)
add(component.edit_component)
add(component.delete_component)
add(component.get_attachable_component)
add(component.attach_component)
add(component.detach_component)
add(component.start_component)
add(component.stop_component)
add(component.start_all_component)
add(component.stop_all_component)

# LoadBalancer
import lb.list_load_balancer
import lb.describe_load_balancer
import lb.create_load_balancer
import lb.edit_load_balancer
import lb.delete_load_balancer
import lb.attach_load_balancer
import lb.detach_load_balancer
import lb.start_load_balancer
import lb.stop_load_balancer
import lb.describe_load_balancer_health_check
import lb.edit_load_balancer_health_check
import lb.list_load_balancer_listener
import lb.create_load_balancer_listener
import lb.delete_load_balancer_listener
import lb.enable_load_balancer_listener
import lb.disable_load_balancer_listener
add(lb.list_load_balancer)
add(lb.describe_load_balancer)
add(lb.create_load_balancer)
add(lb.edit_load_balancer)
add(lb.delete_load_balancer)
add(lb.attach_load_balancer)
add(lb.detach_load_balancer)
add(lb.start_load_balancer)
add(lb.stop_load_balancer)
add(lb.describe_load_balancer_health_check)
add(lb.edit_load_balancer_health_check)
add(lb.list_load_balancer_listener)
add(lb.create_load_balancer_listener)
add(lb.delete_load_balancer_listener)
add(lb.enable_load_balancer_listener)
add(lb.disable_load_balancer_listener)

# Platform
import platform.list_platform
import platform.describe_platform
add(platform.list_platform)
add(platform.describe_platform)

# Image
import image.list_image
add(image.list_image)

# Address
import address.list_aws_address
import address.add_aws_address
import address.edit_aws_address
import address.delete_aws_address
add(address.list_aws_address)
add(address.add_aws_address)
add(address.edit_aws_address)
add(address.delete_aws_address)

# Template
import template.list_template
add(template.list_template)
