def bulidConnectionString(params):
	return ';'.join(["%s=%s" %(k, v) for k, v in params.items()])

if __name__ == "__main__":
	myParams = {
		"server": "mpilgrim",\
		"database": "master",\
		"uid": "sa",\
		"pwd": "secret",\
	}
	print (bulidConnectionString(myParams))

import queue
s = queue.Queue(-1)
print(s)