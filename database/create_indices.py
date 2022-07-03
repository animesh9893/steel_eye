import requests
from config import url,name,pasw,indices_name
from getHeader import getHeader

def CreateIndices(name):
  url_ =url+name

  payload={}
  headers = getHeader()

  response = requests.request("PUT", url_, headers=headers, data=payload)

  return response.text

if __name__ == '__main__':
  print(CreateIndices(indices_name))
