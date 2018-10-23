import datetime

def create_timestamp():
	time_stamp = {}
	current_time = datetime.datetime.utcnow() - datetime.timedelta(hours=4)
	time_stamp['year'] = current_time.year
	time_stamp['month'] = current_time.month
	time_stamp['day'] = current_time.day
	time_stamp['hour'] = current_time.hour
	time_stamp['min'] = current_time.minute
	time_stamp['sec'] = current_time.second
	return time_stamp

def format_timestamp(time_stamp=create_timestamp()):
	month = time_stamp['month'] if time_stamp['month'] > 9 else '0{MM}'.format(
		MM=time_stamp['month']
	)
	day = time_stamp['day'] if time_stamp['day'] > 9 else '0{DD}'.format(
		DD=time_stamp['day']
	)
	hour = time_stamp['hour'] if time_stamp['hour'] > 9 else '0{HH}'.format(
		HH=time_stamp['hour']
	)
	minute = time_stamp['min'] if time_stamp['min'] > 9 else '0{mm}'.format(
		mm=time_stamp['min']
	)
	second = time_stamp['sec'] if time_stamp['sec'] > 9 else '0{ss}'.format(
		ss=time_stamp['sec']
	)
	return '{YY}/{MM}/{DD} {HH}:{mm}:{ss}'.format(YY=time_stamp['year'],
												  MM=month, DD=day, HH=hour,
												  mm=minute, ss=second)

def current_date(time_stamp=create_timestamp()):
	month = time_stamp['month'] if time_stamp['month'] > 9 else '0{MM}'.format(
		MM=time_stamp['month']
	)
	day = time_stamp['day'] if time_stamp['day'] > 9 else '0{DD}'.format(
		DD=time_stamp['day']
	)
	return '{YY}/{MM}/{DD}'.format(YY=time_stamp['year'], MM=month, DD=day)

def current_hour(time_stamp=create_timestamp()):
	hour = time_stamp['hour'] if time_stamp['hour'] > 9 else '0{HH}'.format(
		HH=time_stamp['hour']
	)
	minute = time_stamp['min'] if time_stamp['min'] > 9 else '0{mm}'.format(
		mm=time_stamp['min']
	)
	second = time_stamp['sec'] if time_stamp['sec'] > 9 else '0{ss}'.format(
		ss=time_stamp['sec']
	)
	return '{HH}:{mm}:{ss}'.format(HH=hour, mm=minute, ss=second)
