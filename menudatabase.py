from google.appengine.ext import db

class MenuDatabase(db.Model):
    mykey = db.StringProperty()
    myval = db.StringProperty()