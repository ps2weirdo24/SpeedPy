#Import Libraries
import time     #For Delay calculations
import sys    #for system related information
from subprocess import Popen, PIPE
import subprocess
import re
import json as m_json
import socket
import urllib
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
try:
    import urllib.request       #Python 3.x
except ImportError:
    import urllib2      #Python 2.x
###### End of Import ######


class Tracer:
    def __init__(self, url):
        to_return = []
        while True:
            if 'http' not in url:
                url = "http://" + url
            elif "www" not in url:
                url = "www."[:7] + url[7:]
            else:
                url = url
                break
        url = urlparse(url)
        url = url.netloc
        #print(url)
        p = Popen(['tracert', url], stdout=PIPE)
        while True:
            line = p.stdout.readline()
            line2 = str(line).replace('\\r','').replace('\\n','')
            #print(line2)
            to_append = []
            start_parse = line.split(" ")
            for item in start_parse:
                if item:
                    to_append.append(item)
                to_return.append(to_append)
            if not line:
                break
        self.response = to_return[4:(len(to_return)-3)]

    def get_response(self):
        return self.response


"""
###### Traceroute to a website ######
def my_traceroute(url,*arg):
    to_return = []
    while True:
        if 'http' not in url:
            url = "http://" + url
        elif "www" not in url:
            url = "www."[:7] + url[7:]
        else:
            url = url
            break
    url = urlparse(url)
    url = url.netloc
    print(url)
    p = Popen(['tracert', url], stdout=PIPE)
    while True:
        line = p.stdout.readline()
        line2 = str(line).replace('\\r','').replace('\\n','')
        if len(arg)>0:
            file = open(arg[0], "a")
            file.write(line2)
            file.close()
        #print(line2)
        to_append = []

        start_parse = line2.split(" ")

        for item in start_parse:
        	if item:
        		to_append.append(item)

        to_return.append(to_append)

        if not line:
            break
    return to_return[4:(len(to_return)-3)]
####################
"""

if __name__=="__main__":
    thisone = Tracer("google.com")
    for item in thisone.get_response():
        print(item)