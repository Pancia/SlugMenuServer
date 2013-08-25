from google.appengine.ext import db
from menudatabase import MenuDatabase

import urllib2
from myhtmlparser import MyHTMLParser
import menuutils

from urlrepo import UrlRepo
import json

class MenuStorage():
    def storeMenus(self):
        db.delete(db.GqlQuery("SELECT * FROM MenuDatabase"))
        successCode = "Updated: "
        for dh, url in UrlRepo.repo.items():
            parser = MyHTMLParser()
            html = parser.strip_tags( urllib2.urlopen(url).read() )
            menu = parser.cleanHtmlMenu(html)
            menu = menuutils.split_by_meal(menu)
            menu = menuutils.tagMenu(menu, dh)
            successCode += self.store(dh, menu)
        return successCode[:-2]
        
    def store(self, dh, menu):
        successCode = ""
        menustr = json.dumps(menu)
        if len(menustr) > 500:
            menu1 = menustr[:500]
            menu2 = menustr[500:]
        else:
            menu1 = menustr
            menu2 = ""

        if dh=="nine":
            mydb1 = MenuDatabase(mykey="nine1", myval=menu1)
            mydb2 = MenuDatabase(mykey="nine2", myval=menu2)
            mydb1.put()
            mydb2.put()
            successCode += "nine, "
        elif dh=="eight":
            mydb1 = MenuDatabase(mykey="eight1", myval=menu1)
            mydb2 = MenuDatabase(mykey="eight2", myval=menu2)
            mydb1.put()
            mydb2.put()
            successCode += "eight, "
        elif dh=="crown":
            mydb1 = MenuDatabase(mykey="crown1", myval=menu1)
            mydb2 = MenuDatabase(mykey="crown2", myval=menu2)
            mydb1.put()
            mydb2.put()
            successCode += "crown, "
        elif dh=="porter":
            mydb1 = MenuDatabase(mykey="porter1", myval=menu1)
            mydb2 = MenuDatabase(mykey="porter2", myval=menu2)
            mydb1.put()
            mydb2.put()
            successCode += "porter, "
        elif dh=="cowell":
            mydb1 = MenuDatabase(mykey="cowell1", myval=menu1)
            mydb2 = MenuDatabase(mykey="cowell2", myval=menu2)
            mydb1.put()
            mydb2.put()
            successCode += "cowell, "

        return successCode

def main():
    ms = MenuStorage()
    ms.storeMenus()

if __name__ == "__main__":
    main()