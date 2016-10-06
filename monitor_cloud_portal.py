from portal_status import check_portal_status
from ws_status.ws_monitor import WsMonitor
import socket
#from ws_status import ws_monitor
#from portal_status.test import Test


def monitor_cloud_portal():
    address = "10.0.194.100"
    try:
        socket.inet_aton(address)
        return "valid"
    except socket.error:
        return "Invalid Format"
    
    gms_ip = WsMonitor(address)
    #Test.status_cloud_portal(a)
    #a = Test(url,url2,url3)
    print 'Status of Cloud Portal:', check_portal_status.status_cloud_portal()
    print 'Status of Cloud Portal-fe:', check_portal_status.status_cloud_portal_fe()
    print 'Status of Silver-Peak Cloud Portal-ws', check_portal_status.status_cloud_portal_ws()
    return 'Appliance WS Status', WsMonitor.status(gms_ip)

monitor_cloud_portal()
