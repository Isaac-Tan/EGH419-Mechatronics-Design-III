import datetime
from time import sleep
from datetime import datetime
#from iso8601 import parse_date
from dateutil.parser import parser


try:
	while True:
		t = datetime.datetime.now()
		t_secs = parse(t).timestamp()
		print ("Current date & time = %s" % t_secs)
		sleep(5)
except:
	print ("Finish")