import datetime
from time import sleep
from dateutil.parser import parse


while True:
	t = datetime.datetime.now()
	t_iso = t.isoformat()
	#t_secs = parse(t_iso).timestamp()
	print ("Current date & time = %s" % t_iso)
	sleep(5)