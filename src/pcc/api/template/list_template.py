# -*- coding: utf-8 -*-

def command():
    return "list-template"

def init_argument(parser):
    pass

def execute(requester, args):
    return requester.execute("/ListTemplate")
