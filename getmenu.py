from urlrepo import UrlRepo
import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from menudatabase import MenuDatabase
from google.appengine.ext import db

from storemenu import MenuStorage
from mytime import MyTime
from mymenuparser import MyMenuParser

from datetime import date, timedelta, datetime

class GetMenu(webapp.RequestHandler):

    def getMenu(self):
        dh = self.request.get("dh")
        self.response.headers["Content-Type"] = "application/json"

        if self.request.get('time') == "true":
            self.response.out.write(datetime.now())
            self.response.out.write("\n")
            self.response.out.write(MyTime.getTheTimeNow())
            self.response.out.write("\n")

        #"Hack" to allow first-time storage of menus, 
        #where necessary url-command is: slugmenu.appspot.com/getmenu.py?exe=storeAllMenus[&num_to_store=#]
        if self.request.get('exe') == "storeAllMenus":
            num_dh = 8;
            if self.request.get('num_to_store') != "":
                num_dh = self.request.get('num_to_store')
            self.response.out.write( MenuStorage.storeAllMenus(num_dh) )
            return

        if dh == "":
            self.response.out.write( 
                json.dumps(
                    {"request":{"success":0}, 
                    "response":{"message":"Error! Null Dining Hall!"}
                    }
                )
            )
            return

        if dh not in UrlRepo.dhs:
            self.response.out.write( 
                json.dumps(
                    {"request":{"success":0}, 
                    "response":{"message":"Invalid Dining Hall: "+dh}
                    }
                )
            )
            return

        #For testing!
        
        if self.request.get('debug') == "url":
            self.response.out.write("#URL")
            self.response.out.write("\n")
            self.response.out.write(UrlRepo.getUrl(dh, MyTime.getTheTimeNow()))
            self.response.out.write("\n")

        if self.request.get('debug') == "simple":
            self.response.out.write("#MENU")
            self.response.out.write("\n")
            self.response.out.write(UrlRepo.getUrl(dh, MyTime.getTheTimeNow()))
            self.response.out.write("\n")
            self.response.out.write(
                json.dumps(
                    MyMenuParser.getMenuFor(dh, MyTime.getTheTimeNow())
                    , indent = 4, sort_keys = True
                ))
            self.response.out.write("\n")

        if self.request.get('debug') == "verbose":
            self.response.out.write("#HTML")
            self.response.out.write("\n")
            html = MyMenuParser.getHtmlFrom( UrlRepo.getUrl(dh, MyTime.getTheTimeNow()) )
            self.response.out.write(html)
            self.response.out.write("\n")

        dtdate = 0
        if self.request.get('dtdate') != '':
                dtdate = int(self.request.get('dtdate'))
                if dtdate > 7:
                    self.response.out.write(
                        json.dumps(
                            {"request":{"success":0}, 
                            "response":{"message":"Cannot get more than 1 week ahead!"}
                            }
                        )
                    )
                    return
        
        q = db.GqlQuery(
            "SELECT * FROM MenuDatabase " +
            "WHERE dh=:1 AND time=:2",
                dh, MyTime.getTheTimeNowPlus(dtdate))

        json_str = ''
        for i in q:
            json_str += i.menu

        try:
            self.response.out.write( 
                json.dumps(
                    json.loads(json_str), indent=4, sort_keys=True
                )
            )
        except ValueError as ve:
            self.response.out.write( 
                json.dumps(
                    {"request":{"success":0}, 
                    "response":{"message":ve.args[0]}
                    }
                )
            )

    def get(self):
        self.getMenu()

    def post(self):
        self.getMenu()

def main():
    application = webapp.WSGIApplication([("/getmenu.py", GetMenu)], debug=True)
    util.run_wsgi_app(application)

if __name__ == "__main__":
    main()
