'''
Library to extract formatted timestamps using Python3's builtin datetime module.
'''
import datetime

class TimeStamp:
	# TODO (Elvis): Add class docstring for TimeStamp class
	def __init__(self, tz='UTC'):
		self._tz = tz
		self._timezones = dict()

	def _timezone_offsets(self):
		# TODO (Elvis): Add method docstring for TimeStamp._timezone_offsets() method
		self._timezones['UTC'] = 0
		self._timezones['AST'] = 4
		self._timezones['EST'] = 5
		self._timezones['CST'] = 6
		self._timezones['MST'] = 7
		self._timezones['PST'] = 8
		self._timezones['AKST'] = 9
		self._timezones['HAST'] = 10

	def _create_timestamp(self):
		'''
			Description:
				Create a dictionary representing datetime attributes
			Args:
				None
			Exceptions Raised:
				None
			Returns:
				A dictionary of datetime attributes
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

	def timestamp(self):
		'''
			Description:
				Creates a time stamp string from timestamp attribute
			Args:
				None
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

	def date(self):
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
		time_stamp = self.timestamp()
		time_stamp = time_stamp.split()
		return time_stamp[0]

	def time(self):
		'''
			Description:
				Retrieves the 'time' portion from a complete timestamp string
			Args:
				None
			Exceptions Raised:
				None
			Returns:
				A formatted string representing a timestamp of the current time
		'''
		time_stamp = self.timestamp()
		time_stamp = time_stamp.split()
		return time_stamp[1]
