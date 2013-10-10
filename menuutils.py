def split_by_meal(list):
        t = {}
        t["response.title"] = list[0]
        t["server.warning"] = 0
        t["server.error"] = 0

        try:
                b = list.index("Breakfast")
        except ValueError, ve:
                t["server.warning"] += 1
                b = 0
        try:
                l = list.index("Lunch")
        except ValueError, ve:
                t["server.warning"] += 2
                l = 0
        try:
                d = list.index("Dinner")
        except ValueError, ve:
                t["server.warning"] += 4
                d = 0

        if b == 0:
                if l==0 and d==0:
                        t["server.error"] = 1
                elif l == 0:
                        t["menu.dinner"] = list[2:]
                elif d == 0:
                        t["menu.lunch"] = list[2:]
                else:
                        t["menu.lunch"] = list[l+1:d]
                        t["menu.dinner"] = list[d+1:]
                return t
        elif l == 0:
                if d == 0:
                        t["menu.breakfast"] = list[2:]
                else:
                        t["menu.breakfast"] = list[2:d]
                        t["menu.dinner"] = list[d+1:]
                return t
        elif d == 0:
                t["menu.breakfast"] = list[2:l]
                t["menu.lunch"] = list[l+1:]
                return t

        elif b!=0 and l!=0 and d!=0:
                t["menu.breakfast"] = list[2:l]
                t["menu.lunch"] = list[l+1:d]
                t["menu.dinner"] = list[d+1:]
                return t

        return t

def tagMenu(menu, dh):
        if len(menu) != 0 and menu["server.error"] != 1:
               menu["request.success"] = 1
               menu["response.message"] = "Got the menu!"
        else:
               menu["request.success"] = 0
               menu["response.message"] = "Couldn't get the menu,\nthe dining hall might be closed for the day."
        if dh != None:
            menu["menu.dh"] = dh
        return menu

def find(list, substr):
        for i, s in enumerate(list):
                if substr in s:
                        return i
        return -1
