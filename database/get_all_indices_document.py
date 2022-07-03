import requests
from requests.auth import HTTPBasicAuth
from config import url,name,pasw,indices_name
import json

from getHeader import getHeader

def GetAllIndicesDocument(name):
  url_ = url+name+"/_search?pretty=true&q=*:*"

  payload={}
  headers = getHeader()

  response = requests.request("GET", url_, headers=headers, data=payload)

  return response.text

if __name__ == '__main__':
  ans = GetAllIndicesDocument(indices_name)
  print(ans)