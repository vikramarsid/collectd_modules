import requests, json

headers = {"Content-Type": "application/json"}
payload = {"user": "admin", "password": "admin"}


def gms_login(url):
    p = requests.post('https://' + url + '/gms/rest/authentication/login', data=json.dumps(payload), headers=headers,
                      verify=False)
    id = p.headers['Set-Cookie'].split(";")
    gms_session_id = id[0]
    # print p.status_code
    print p.text
    # print gmsSessionID

    return gms_session_id

    # gmsLogin()
