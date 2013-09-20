from google.appengine.ext import db
from menudatabase import MenuDatabase

import urllib2
from myhtmlparser import MyHTMLParser
import menuutils

from urlrepo import UrlRepo
import json

from datetime import date, timedelta

class MenuStorage():
    def storeAllMenus(self):
        db.delete(db.GqlQuery("SELECT * FROM MenuDatabase"))
        successCode = "Updated: \n"
        urlrepo = UrlRepo()
        for dh in UrlRepo.dhs:
            for i in range(8):
                parser = MyHTMLParser()
                d = date.today()+timedelta(days=i)
                html = parser.strip_tags(  urllib2.urlopen( urlrepo.getUrl(dh, d) ).read()  )
                menu = parser.cleanHtmlMenu(html)
                menu = menuutils.split_by_meal(menu)
                menu = menuutils.tagMenu(menu, dh)
                successCode += self.store(dh, menu, d)
                successCode += urlrepo.getUrl(dh, d) + "; \n"

        return successCode[:-2] #[:-2] removes the last ", "

    def store(self, dh, menu, d):
        successCode = ""
        menustr = json.dumps(menu)

        mydb = MenuDatabase(dh=dh, menu=menustr, time=d)
        mydb.put()

        return successCode + dh + ", "

def main():
    ms = MenuStorage()
    ms.storeAllMenus()

if __name__ == "__main__":
    main()