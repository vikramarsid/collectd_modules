import requests


class Test:

    def __init__(self,url):
        self.url = url
        #return self

    def status_cloud_portal(self):
        res = requests.get('https://'+self.url+'.silver-peak.com/portal/static/')
        print

