import requests


def gms_logout(gms_session_id,url):
    headers = {
        "Cookie": gms_session_id
    }
    r = requests.get('https://'+url+'/gms/rest/authentication/logout', headers=headers, verify=False)
    #print r.status_code
    print r.text
