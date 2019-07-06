import certifi
import urllib3



def test():

	http = urllib3.PoolManager()
		#cert_reqs='CERT_REQUIRED',
		#ca_certs=certifi.where())

	try:
		r = http.request('GET', 'https://servicesqa.na.cargill.com:8443/core/request/info?hello=there')
		status = r.status
		print 'Status: ', status

	except urllib3.exceptions.ConnectionError, e:
		print 'Some kind of error:', e

	return r.data
	
print test()
