import requests


def status_cloud_portal():
    # print self.url
    # res = requests.get(self.url)
    res = requests.get('https://cloudportal.silver-peak.com/portal/static/')
    # print res.status_code
    # print res.text
    #print res.status_code
    # print res.text
    return res.status_code


def status_cloud_portal_fe():
    res = requests.get('https://cloudportal-fe.silverpeak.cloud/portal/static/')
    #print res.status_code
    # print res.text
    return res.status_code


def status_cloud_portal_ws():
    res = requests.get('https://cloudportal-ws.silverpeak.cloud/portal/static/')
    #print res.status_code
    # print res.text
    return res.status_code


status_cloud_portal
status_cloud_portal_fe
status_cloud_portal_ws
