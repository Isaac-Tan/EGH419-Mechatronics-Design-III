import datetime
from time import sleep
from dateutil.parser import parse as dp

def timestamp():
	t = datetime.datetime.now()
	t_iso = t.isoformat()
	t_parsed = dp(t_iso)
	t_secs = t_parsed.strftime('%s')
	print (t_secs)
	return t_secs

while True:
	filename = timestamp()
	print(f"This is the filename: {filename}")