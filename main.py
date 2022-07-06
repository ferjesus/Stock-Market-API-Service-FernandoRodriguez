#! /usr/bin/env python
from flask import Flask, request,jsonify
from flask_httpauth import HTTPBasicAuth
import json
import sys
from datetime import datetime
import logging

from CMarketInfo import *
app = Flask(__name__)
auth = HTTPBasicAuth()
log = logging.getLogger("simple_example")


@app.route('/marketinfo', methods=['POST'])
#Return marketinfo
def f_cquerymarketinfo():
   lcData = request.get_data()
   headers = request.headers
   bearer = headers.get('Authorization')
   token = bearer.split()[1]
   app.logger.debug(lcData)
   app.logger.debug(headers)
   lo=CMarketInfo()
   lo.pcParam = json.loads(lcData)
   lo.pcToken = token
   llOk = lo.omMarketinfo()
   if llOk:
      app.logger.debug( lo.pcHttpCode)
      return lo.pcData, lo.pcHttpCode 
   else:
      app.logger.debug(lo.pcError, lo.pcHttpCode)
      return lo.pcError, lo.pcHttpCode 

@app.route('/auth')
@auth.login_required
def get_response():
	return "{'token':'X86NOH6II01P7R24'}"
	

@auth.verify_password
def f_authenticate(username, password):
	if username and password:
		if username == 'fer' and password == 'pwd':
			return True
		else:
			return False
	return False
		

if __name__ == '__main__':
   #app.run(host='localhost', debug=True, port=8080)
   app.run(host='0.0.0.0', debug=True, port=8080, threaded=True)
   #app.run(host='192.168.0.3', debug=True, port=8080)
