"""
Module: WSMonitor
Author: CS Madugundi
Date:
"""
class WsMonitor:

    def __init__(self):
        pass

    def gms_login(url):
        headers = {"Content-Type": "application/json"}
        payload = {"user": "admin", "password": "admin"}
        _url = 'https://' + url + '/gms/rest/authentication/login'
        try:
            request_data = json.dumps(payload)      # Not needed to JSONified
            respose = requests.post(_url, request_data, headers, False)
            id = respose.headers['Set-Cookie'].split(";")
            gms_session_id = id[0]
            response_body = respose.text
        except Exception:
            print "GMS_LOGIN_STATUS : %s" % Exception.message
        print "GMS_LOGIN_SUCCESSFULL : \n %s" % response_body
        return gms_session_id

    def gms_logout(gms_session_id,url):
        try:
            headers = {"Cookie": gms_session_id}
            _url = 'https://' + url + '/gms/rest/authentication/logout'
            response = requests.get(_url,headers,False)
            response_body = response.text
        except Exception:
            print "GMS_LOGOUT_STATUS : %s" % Exception.message
        print "GMS_LOGOUT_SUCCESSFULL : \n %s" % response_body
        return response_body

    def appliance_ws_status(gms_session_id, appliance_id, url):
        headers = {"Cookie": gms_session_id,"Content-Type": "application/json"}
        _url = 'https://' + url + '/gms/rest/spPortal/applianceWSStatus/' + appliance_id
        try:
            response = requests.get(_url, headers, False)
            response_body = response.text
        except Exception:
            print "APPLIANCE_WS_STATUS : %s" % Exception.message
        print "APPLIANCE_WS_SUCCESS : \n %s" % response_body
        return response_body

    def appliance_info(gms_session_id, url):
        headers = {"Content-Type": "application/json","Cookie": gms_session_id}
        _url = 'https://' + url + '/gms/rest/appliance'
        appl_info = []
        try:
            response = requests.get(_url, headers, False)
            response_body = response.text
            obj = json.loads(response_body)
            for i in range(len(obj)):
                appl_info.append(obj[i]['id'])
        except Exception:
            print "APPLIANCE_INFO_STATUS : %s" % Exception.message
        print "APPLIANCE_INFO_SUCCESS : \n %s" % appl_info
        return appl_info

    def status(self, url):
        gms_session_id = self.gms_login(url)

        lis = self.appliance_info(gms_session_id, url)

        if lis:
            portal_status = self.appliance_ws_status(gms_session_id, lis[0], url)
            print portal_status
        else:
            print "Appliance not available"

        gms_logout(gms_session_id, url)
