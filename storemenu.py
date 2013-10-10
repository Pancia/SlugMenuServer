from google.appengine.ext import db
from menudatabase import MenuDatabase

from mymenuparser import MyMenuParser

from urlrepo import UrlRepo
import json

from mytime import MyTime

class MenuStorage():

    @staticmethod
    def storeAllMenus(tot_days):
        db.delete(db.GqlQuery("SELECT * FROM MenuDatabase"))
        successCode = "Updated: \n"
        for dh in UrlRepo.dhs:
            #Today and tmrw
            for i in range(tot_days):
                d = MyTime.getTheTimeNowPlus(i)
                menu = MyMenuParser.getMenuFor(dh, d)
                successCode += MenuStorage.store(dh, menu, d)
                successCode += UrlRepo.getUrl(dh, d) + "\n"

        return successCode[:-2] #[:-2] removes the last ", "

    @staticmethod
    def store(dh, menu, d):
        menustr = json.dumps(menu)

        mydb = MenuDatabase(dh=dh, menu=menustr, time=d)
        mydb.put()

        return dh + ", "

@staticmethod
def main():
    MenuStorage.storeAllMenus(2)

if __name__ == "__main__":
    main()