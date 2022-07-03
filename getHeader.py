from http.client import HTTPSConnection
from base64 import b64encode

from config import url,name,pasw

# this header is use to setup basic auth of API
def getHeader():
	c = HTTPSConnection("steeleye.es.ap-south-1.aws.elastic-cloud.com/")
	st = name+":"+pasw
	userAndPass = b64encode(st.encode()).decode("ascii")

	headers = { 'Authorization' : 'Basic %s' %  userAndPass }
	return headers

if __name__ == '__main__':
	print(getHeader())