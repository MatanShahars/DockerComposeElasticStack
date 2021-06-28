import requests
import os
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl = os.environ.get('SSL')
num_requests = os.environ.get('NUM_REQUESTS')
if ssl=="true":
    for x in range(int(num_requests)):
      response = requests.get("https://nginx:443",verify=False)

if  ssl=="false":
    for x in range(int(num_requests)):
      response = requests.get("http://nginx:80", allow_redirects=False)