#!/bin/env python2.7
"""
Module: Portal Status
Author: CS Madugundi
Date:
"""
from ws_status import WsMonitor
import requests

class MonitorCloudPortal(object):

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

    def get_status(self, path):
        _url = 'https://' + path + '.silver-peak.com/portal/static/'
        res = requests.get(_url)
        res_status_code = res.status_code
        return res_status_code

    def monitor_cloud_portal(self):
        # Add Ip_address associated with gms
        gms_ip = "0.0.0.0"

        print '-> Status of Cloud Portal: ' + self.get_status("portal")
        print '-> Status of Cloud Portal-fe: ' + self.get_status("portal-fe")
        print '-> Status of Silver-Peak Cloud Portal-ws ' + self.get_status("portal-ws")
        print '-> Appliance WS Status:\n'
        WsMonitor.status(gms_ip)

if __name__ == '__main__':
    monitor_cloud_portal()
