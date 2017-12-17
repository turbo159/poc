from urllib2 import Request, urlopen, URLError

request = Request('https://itunes.apple.com/search?term=simple minds')

try:
	response = urlopen(request)
	result = response.read()
	output = result.split(",")
	
	for st in output:
		print(st)
except URLError, e:
    print 'Some kind of error:', e