from gms_login import gms_login
from appliance_ws_status import appliance_ws_status
from gms_logout import gms_logout
from appliance_info import appliance_info


class WsMonitor:
    def __init__(self, url):
        self.url = url

    def status(self):
        gms_session_id = gms_login(self.url)
        # print gms_session_id
        lis = appliance_info(gms_session_id, self.url)
        if lis:
            portal_status = appliance_ws_status(gms_session_id, lis[0], self.url)
            # for i in range(len(lis)):
            #   portal_status = appliance_ws_status(gms_session_id, lis[i])
            print portal_status
        else:
            print "Appliance not available"
        gms_logout(gms_session_id, self.url)


        # status()
