import datetime
from time import sleep
import dateutil.parser as dp


try:
	while True:
		t = datetime.datetime.now()
		parsed_t = dp.parse(t)
		t_secs = parsed_t.timestamp()
		print ("Current date & time = %s" % t_secs)
		sleep(5)
except:
	
