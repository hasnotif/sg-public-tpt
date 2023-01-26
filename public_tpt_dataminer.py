import json
import urllib
from urllib.parse import urlparse

import httplib2 as http

def main():
    #Authentication parameters
    headers = {'AccountKey': 'T/uOGZ60RV+ySexzg5g1Tg==', 'accept': 'application/json'}

    #API parameters
    url = 'http://datamall2.mytransport.sg/'
    path = 'ltaodataservice/PV/Bus'

    #Build query string & specify type of API call
    target = urlparse(url + path)
    print(target.geturl())
    method = 'GET'
    body = ''

    #Get handle to http
    h = http.Http()
 
    #Obtain results
    response, content = h.request(target.geturl(), method, body, headers)

    #Parse JSON to print
    jsonObj = json.loads(content)
    print(json.dumps(jsonObj, sort_keys=True, indent=4))

if __name__ == "__main__":
    main()