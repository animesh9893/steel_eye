import requests
from requests.auth import HTTPBasicAuth
import json

from config import url,name,pasw,indices_name

from getHeader import getHeader


def InsertIntoIndices(name,data):

  url_ = url+name+"/_doc"
  payload = json.dumps(data)
  headers = getHeader()
  headers['Content-Type'] = 'application/json'

  response = requests.request("POST", url_, headers=headers, data=payload)
  return response.text


if __name__ == '__main__':
  print(InsertIntoIndices(indices_name,{"name":"Animesh Shrivatri","age":19}))





