from HTMLParser import HTMLParser
import menuutils
 
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def strip_tags(self, html):
        self.feed(html)
        return [word.strip() for word in self.fed]

    def cleanHtmlMenu(self, html):
        menu = []
        for i in range( len(html) ):
            if html[i] == 'M&M':
                continue
            if html[i] == '&':
                html[i] = html[i-1] + " " + html[i] + " " + html[i+1]
                html[i-1] = ''
                html[i+1] = ''
            if html[i] == "Nutritive Analysis":
                    html[i] = ''
        for i in html:
                if i != '':
                        menu.append(i)
        index = menuutils.find(menu, "Menus for")
        return menu[index:-2]
