import urllib2
from myhtmlparser import MyHTMLParser
import menuutils

from urlrepo import UrlRepo

class MyMenuParser():

	@staticmethod
	def	getHtmlFrom(url):
		return urllib2.urlopen( url ).read()

	@staticmethod
	def getMenuFor(dh, date):
		parser = MyHTMLParser()
		html = parser.strip_tags(  MyMenuParser.getHtmlFrom( UrlRepo.getUrl(dh, date) )  )
		menu = parser.cleanHtmlMenu(html)
		menu = menuutils.split_by_meal(menu)
		menu = menuutils.tagMenu(menu, dh)
		return menu