import requests, json


def appliance_info(gms_session_id, url):
    headers = {
        "Content-Type": "application/json",
        "Cookie": gms_session_id
    }
    r = requests.get('https://'+url+'/gms/rest/appliance', headers=headers, verify=False)
    # print r.status_code
    l = r.text
    decode = json.loads(l)
    lis = []
    for i in range(len(decode)):
        lis.append(decode[i]['id'])
        # print lis
    return lis
