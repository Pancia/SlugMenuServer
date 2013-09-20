from google.appengine.ext import db

class MenuDatabase(db.Model):
    dh = db.StringProperty()
    menu = db.TextProperty()
    time = db.DateProperty()