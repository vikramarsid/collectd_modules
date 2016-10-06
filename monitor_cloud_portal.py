from portal_status import check_portal_status
from ws_status.ws_monitor import WsMonitor


def monitor_cloud_portal():
    # Add Ip_address associated with gms
    gms_ip = WsMonitor("gms_ip")
    print 'Status of Cloud Portal:', check_portal_status.status_cloud_portal()
    print 'Status of Cloud Portal-fe:', check_portal_status.status_cloud_portal_fe()
    print 'Status of Silver-Peak Cloud Portal-ws', check_portal_status.status_cloud_portal_ws()
    return 'Appliance WS Status', WsMonitor.status(gms_ip)

monitor_cloud_portal()
