import requests


def appliance_ws_status(gms_session_id, appliance_id, url):
    headers = {"Cookie": gms_session_id,
               "Content-Type": "application/json"
               }
    # url = https://gms_ip/gms/rest/spPortal/applianceWSStatus/+applianceID
    r = requests.get('https://'+url+'/gms/rest/spPortal/applianceWSStatus/' + appliance_id, headers=headers,
                     verify=False)
    # print applianceID + r.text
    # return r.status_code
    #return appliance_id + r.text
    return r.text
