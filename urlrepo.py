class UrlRepo():

	base_url = "http://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&locationNum="
	dt_date = "&dtdate=" #9%2F10%2F2013

	#valid dhs
	dhs = ["nine", "eight", "cowell", "porter", "crown"]

	#codes for each dining hall's ?locationNum=
	dh_loc_nums = {"nine":"40", "eight":"30", "cowell":"05", "porter":"25", "crown":"20"}

	@staticmethod
	def getFormattedDateUrl(date):
		return UrlRepo.dt_date + str(date.month) + "%2F" + str(date.day) + "%2F" + str(date.year) 

	@staticmethod
	def getUrl(dh, date):
		return UrlRepo.base_url + UrlRepo.dh_loc_nums[dh] + UrlRepo.getFormattedDateUrl(date)
