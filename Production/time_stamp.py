'''
Library to extract formatted timestamps using Python3's builtin datetime module.
'''

import datetime

class TimeStamp:
	def __init__(self, tz='UTC'):
		self._tz = tz
		self._timezones = dict()

	def _timezone_offsets(self):
		self._timezones['UTC'] = 0
		self._timezones['AST'] = 3
		self._timezones['EST'] = 4
		self._timezones['CST'] = 5
		self._timezones['MST'] = 6
		self._timezones['PST'] = 7
		self._timezones['AKST'] = 8
		self._timezones['HAST'] = 9

	def _create_timestamp(self):
		'''
			Description:
				Create a dictionary representation of a timestamp
			Args:
				None
			Exceptions Raised:
				None
			Returns:
				A dictionary of time stamp attributes
		'''
		time_stamp = dict()
		self._timezone_offsets()
		try:
			timezone = self._timezones[self._tz]
		except KeyError:
			timezone = self._timezones['UTC']
		current_time = (
			datetime.datetime.utcnow() - datetime.timedelta(hours=timezone)
			)
		time_stamp['year'] = current_time.year
		time_stamp['month'] = current_time.month
		time_stamp['day'] = current_time.day
		time_stamp['hour'] = current_time.hour
		time_stamp['min'] = current_time.minute
		time_stamp['sec'] = current_time.second
		return time_stamp

	def full_timestamp(self):
		'''
			Description:
				Creates a time stamp string from timestamp attribute
			Args:
				time_stamp: Dictionary representation of a timestamp
			Exceptions Raised:
				None
			Returns:
				A formatted string representing a timestamp of the current
				date and time.
		'''
		time_stamp = self._create_timestamp()
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

	def current_day(self):
		'''
			Description:
				Retrieves the 'date' portion from a complete timestamp string
			Args:
				None
			Exceptions Raised:
				None
			Returns:
				A formatted string representing a timestamp of the current date
		'''
		day = self.full_timestamp()
		day = day.split()
		return day[0]

	def current_hour(self):
		'''
			Description:
				Retrieves the 'hour' portion from a complete timestamp string
			Args:
				None
			Exceptions Raised:
				None
			Returns:
				A formatted string representing a timestamp of the current hour
		'''
		hour = self.full_timestamp()
		hour = hour.split()
		return hour[1]
