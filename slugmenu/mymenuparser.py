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
		menu = menuutils.tagMenu(
			menuutils.split_by_meal(
				parser.cleanHtmlMenu(
					parser.strip_tags(
						MyMenuParser.getHtmlFrom( UrlRepo.getUrl(dh, date) )
					)
				)
			), dh
		)
		return menu