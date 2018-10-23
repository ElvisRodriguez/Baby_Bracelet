'''
Library to extract formatted timestamps using Python3's builtin datetime module.
'''

import datetime

def create_timestamp():
	'''
		Description:
			Creates a Dictionary object for time stamp string formatting.
		Args:
			None
		Exceptions Raised:
			None
		Returns:
			Dictionary object with keys representing all time components from
			datetime module's datetime.utcnow
	'''
	time_stamp = {}
	# Shift current time to 4 hours ago to set UTC to EST
	current_time = datetime.datetime.utcnow() - datetime.timedelta(hours=4)
	time_stamp['year'] = current_time.year
	time_stamp['month'] = current_time.month
	time_stamp['day'] = current_time.day
	time_stamp['hour'] = current_time.hour
	time_stamp['min'] = current_time.minute
	time_stamp['sec'] = current_time.second
	return time_stamp

def format_timestamp(time_stamp=create_timestamp()):
	'''
		Description:
			Creates a time stamp string from a Dictionary object.
		Args:
			time_stamp: A Dictionary object representing the current date/time.
		Exceptions Raised:
			TypeError: Raised if time_stamp is not a Dictionary object.
			KeyError: Raised if time_stamp does not have any of the following
					  key values:['year','month','day','hour','minute','second']
		Returns:
			A formatted string representing a time_stamp of the current
			date and time in EST.
	'''
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
	'''
		Description:
			Creates a time stamp string from a Dictionary object.
		Args:
			time_stamp: A Dictionary object representing the current date.
		Exceptions Raised:
			TypeError: Raised if time_stamp is not a Dictionary object.
			KeyError: Raised if time_stamp does not have any of the following
					  key values: ['year','month','day']
		Returns:
			A formatted string representing a time_stamp of the current
			date in EST.
	'''
	month = time_stamp['month'] if time_stamp['month'] > 9 else '0{MM}'.format(
		MM=time_stamp['month']
	)
	day = time_stamp['day'] if time_stamp['day'] > 9 else '0{DD}'.format(
		DD=time_stamp['day']
	)
	return '{YY}/{MM}/{DD}'.format(YY=time_stamp['year'], MM=month, DD=day)

def current_hour(time_stamp=create_timestamp()):
	'''
		Description:
			Creates a time stamp string from a Dictionary object.
		Args:
			time_stamp: A Dictionary object representing the current time.
		Exceptions Raised:
			TypeError: Raised if time_stamp is not a Dictionary object.
			KeyError: Raised if time_stamp does not have any of the following
					  key values: ['hour','minute','second']
		Returns:
			A formatted string representing a time_stamp of the current
			time in EST.
	'''
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
