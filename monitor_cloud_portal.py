from portal_status import check_portal_status
from ws_status.ws_monitor import WsMonitor


def monitor_cloud_portal():
    gms_ip = WsMonitor("10.0.194.100")
    print 'Status of Cloud Portal:', check_portal_status.status_cloud_portal()
    print 'Status of Cloud Portal-fe:', check_portal_status.status_cloud_portal_fe()
    print 'Status of Silver-Peak Cloud Portal-ws', check_portal_status.status_cloud_portal_ws()
    return 'Appliance WS Status', WsMonitor.status(gms_ip)

monitor_cloud_portal()
