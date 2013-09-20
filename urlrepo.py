from datetime import date, timedelta

class UrlRepo():

	base_url = "http://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&locationNum="
	dt_date = "&dtdate=" #9%2F10%2F2013

	#valid dhs
	dhs = ["nine", "eight", "cowell", "porter", "crown"]

	#codes for each dining hall's ?locationNum=
	dh_loc_nums = {"nine":"40", "eight":"30", "cowell":"05", "porter":"25", "crown":"20"}

	def getFormattedDateUrl(self, date):
		return str(date.month) + "%2F" + str(date.day) + "%2F" + str(date.year) 

	def getUrl(self, dh, date):
		return self.base_url + self.dh_loc_nums[dh] + self.dt_date+self.getFormattedDateUrl(date)
