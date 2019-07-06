from urllib2 import Request, urlopen, URLError
import os
import socket

# Connect to Redis

@app.route("/")
def hello():
    request = Request('https://servicesqa.na.cargill.com:8443/core/request/info?hello=there')

    response = urlopen(request)
    result = response.read()
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)