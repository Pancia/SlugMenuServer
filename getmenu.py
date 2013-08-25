from urlrepo import UrlRepo
import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from menudatabase import MenuDatabase
from google.appengine.ext import db

from storemenu import MenuStorage

class GetMenu(webapp.RequestHandler):
    def getMenu(self):
        dh = self.request.get("dh")
        self.response.headers["Content-Type"] = "application/json"

        #"Hack" to allow first-time storage of menus, 
        #where necessary url-command is: slugmenu.appspot.com/getmenu.py?exe=storemenus
        if self.request.get('exe') == "storemenus":
            ms = MenuStorage()
            self.response.out.write( ms.storeMenus() )
            return

        if dh == "":
            self.response.out.write( json.dumps({"success":0, "message":"Please enter a valid dining hall"}) )
            return

        if dh not in UrlRepo.repo:
            self.response.out.write( json.dumps({"success":0, "message":dh+" must be closed today."})+"\n" )
            return
        
        q = db.GqlQuery("SELECT * FROM MenuDatabase WHERE mykey >=:1 AND mykey <=:2", dh, dh+"2")

        json_str = ''
        for i in q:
            json_str += i.myval

        self.response.out.write( json.dumps(json.loads(json_str), indent=4, sort_keys=True) )

    def get(self):
        self.getMenu()

    def post(self):
        self.getMenu()

def main():
    application = webapp.WSGIApplication([("/getmenu.py", GetMenu)],debug=True)
    util.run_wsgi_app(application)

if __name__ == "__main__":
    main()
