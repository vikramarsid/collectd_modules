import requests, json, operator


def appliance_info(gms_session_id, url):
    headers = {
        "Content-Type": "application/json",
        "Cookie": gms_session_id
    }
    r = requests.get('https://'+url+'/gms/rest/appliance', headers=headers, verify=False)
    # print r.status_code
    l = r.text
    decode = json.loads(l)
    # len(decode)
    # print decode
    # print json.dumps(decode,sort_keys=True, indent = 4)
    ret = ''
    # for key,value in decode.items():
    #   print ((key,value))s
    lis = []
    for i in range(len(decode)):
        lis.append(decode[i]['id'])
        # print lis
        # [[d['id'] for d in decode]
    # print list(map(operator.itemgetter('id'), l))
    return lis
    # appliance_id = [d["id"] for d in l]
    # print appliance_id
    # applianceInfo(appliance_id)
