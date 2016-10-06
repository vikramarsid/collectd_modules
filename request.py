import requests, json


payload = {"user": "admin", "password": "admin"}
headers = {
    "Content-Type": "application/json",
}

# "Cache-Control": "no-cache",
# "Origin": "https://10.0.194.100",
# "Host": "10.0.194.100",
# "X-Requested-With": "XMLHttpRequest",
# "Accept": "*/*",
# "Content-Length": "35",
with requests.Session() as s:
     p = s.post('https://10.0.194.100/gms/rest/authentication/login', data=json.dumps(payload), headers=headers, verify=False)
     #p = s.post('https://10.0.194.100/gms/rest/authentication/login', headers=headers, data=payload, verify=False)
#    # print p.text
     print p.status_code
     print p.headers
     id= p.headers['Set-Cookie'].split(";")
     gmsSessionID = id[0]
     print gmsSessionID
    #gmsSessionID=id['']
     print p.cookies
     print p.text
     #print p.headers
     #print p.request.headers

     headers2={"Cookie": gmsSessionID
     }
     headers3={"Cookie": gmsSessionID,
               "Content-Type": "application/json"
     }
     #print headers2
     r1 = s.get('https://10.0.194.100/gms/rest/spPortal/applianceWSStatus/1.NE', headers=headers3, verify=False)
     print r1.status_code
     print r1.text
     print r1.headers

     r=s.get('https://10.0.194.100/gms/rest/authentication/logout', headers=headers2, verify=False)
     print r.status_code
     print r.text
     #print r.cookies
     #print r.request.headers
     #print r.headers
     #r = s.get('https://10.0.194.100:443/gms/rest/spPortal/applianceWSStatus/0.NE',verify=False)
     #print r.status_code
