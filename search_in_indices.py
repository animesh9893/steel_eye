import requests
from requests.auth import HTTPBasicAuth
from config import url,name,pasw,indices_name
import json

from getHeader import getHeader


def Search(name,data):
  url_ = url+name+"/_search"
  payload = json.dumps(data)

  headers = getHeader()
  headers['Content-Type'] = 'application/json'

  response = requests.request("POST", url_, headers=headers, data=payload)

  return response.text

