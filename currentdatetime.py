import datetime
from time import sleep
from dateutil.parser import parse as dp


while True:
	t = datetime.datetime.now()
	t_iso = t.isoformat()
	t_parsed = dp(t_iso)
	t_secs = t_parsed.strftime('%s')
	print ("Current date & time = %s" % t_secs)
	sleep(5)