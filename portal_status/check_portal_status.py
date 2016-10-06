import requests


def status_cloud_portal():
    # print self.url
    # res = requests.get(self.url)
    res = requests.get('portal')
    return res.status_code


def status_cloud_portal_fe():
    res = requests.get('portal-fe')
    #print res.status_code
    # print res.text
    return res.status_code


def status_cloud_portal_ws():
    res = requests.get('portal-ws')
    #print res.status_code
    # print res.text
    return res.status_code

# status_cloud_portal
# status_cloud_portal_fe
# status_cloud_portal_ws
