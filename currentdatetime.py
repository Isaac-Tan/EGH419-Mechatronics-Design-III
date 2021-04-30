import datetime
from time import sleep
from dateutil.parser import parser


while True:
	t = datetime.datetime.now()
	t_iso = t.isoformat()
	t_secs = parse(t_iso).timestamp()
	print ("Current date & time = %s" % t_secs)
	sleep(5)