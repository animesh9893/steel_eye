import requests
from requests.auth import HTTPBasicAuth
from config import url,name,pasw

def CheckTesting():
  response = requests.get(url,auth = HTTPBasicAuth(name,pasw))
  return response.text

if __name__ == '__main__':
  print(CheckTesting())