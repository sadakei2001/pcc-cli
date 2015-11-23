# -*- coding: utf-8 -*-

def command():
    return "list-platform"

def init_argument(parser):
    pass

def execute(requester, args):
    return requester.execute("/ListPlatform")
