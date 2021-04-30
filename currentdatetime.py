import datetime
from time import sleep

while True:
	i = datetime.datetime.now()
	print ("Current date & time = %s" % i)
	sleep(5)

