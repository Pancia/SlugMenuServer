from datetime import date, timedelta, datetime

class MyTime():

	@staticmethod
	def getTheTimeNow():
		return (datetime.today() + timedelta(hours=-7)).date()

	@staticmethod
	def getTheTimeNowPlus(dz):
		return MyTime.getTheTimeNow()+timedelta(days=dz)

