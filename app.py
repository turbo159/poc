from flask import Flask
#import certifi
import urllib3
import os
import socket

# Connect to Redis

app = Flask(__name__)

@app.route("/")
def hello():
	http = urllib3.PoolManager()
		#cert_reqs='CERT_REQUIRED',
		#ca_certs=certifi.where())
	r = http.request('GET', 'https://servicesqa.na.cargill.com:8443/core/request/info?hello=there')

	return r.data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)