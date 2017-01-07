# -*- coding: utf-8 -*-

import sys
import datetime
import hmac
import hashlib
import base64
import json

class Requester:

    api_path = "/rest"

    def __init__(self, url, access_id, access_key, options = None):
        if (url.endswith("/")):
            self.url = url[0:-1]
        else:
            self.url = url

        self.access_id = access_id
        self.access_key = access_key
        self.options = options


    def execute(self, endpoint, parameters = None):
        param = "AccessId=" + self.access_id
        param += "&Timestamp=" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        if (parameters != None):
            for parameter in parameters:
                param += "&" + parameter + "=" + str(parameters[parameter])

        if sys.version_info[0] == 2:
            import urllib2

            signature = hmac.new(self.access_key, self.api_path + endpoint + "?" + param, hashlib.sha256).hexdigest()

            param += "&Signature=" + signature
            querystring = base64.b64encode(param)

            request = urllib2.Request(self.url + self.api_path + endpoint + "?" + querystring)
            response_json = urllib2.urlopen(request).read()

            response = json.loads(response_json, "utf-8")

        else:
            import urllib.request

            signature = hmac.new(self.access_key.encode("utf-8"), (self.api_path + endpoint + "?" + param).encode("utf-8"), hashlib.sha256).hexdigest()

            param += "&Signature=" + signature
            querystring = base64.b64encode(param.encode("utf-8"))

            request = urllib.request.Request(self.url + self.api_path + endpoint + "?" + querystring.decode("utf-8"))
            response_json = urllib.request.urlopen(request).read()

            response = json.loads(response_json.decode("utf-8"), "utf-8")

        return response
