def split_by_meal(list):
        t = {}
        t["title"] = list[0]
        t["warning"] = 0
        t["_error"] = 0

        try:
                b = list.index("Breakfast")
        except ValueError, ve:
                t["warning"] += 1
                b = 0
        try:
                l = list.index("Lunch")
        except ValueError, ve:
                t["warning"] += 2
                l = 0
        try:
                d = list.index("Dinner")
        except ValueError, ve:
                t["warning"] += 4
                d = 0

        if b == 0:
                if l==0 and d==0:
                        t["_error"] = 1
                elif l == 0:
                        t["dinner"] = list[2:]
                elif d == 0:
                        t["lunch"] = list[2:]
                else:
                        t["lunch"] = list[l+1:d]
                        t["dinner"] = list[d+1:]
                return t
        elif l == 0:
                if d == 0:
                        t["breakfast"] = list[2:]
                else:
                        t["breakfast"] = list[2:d]
                        t["dinner"] = list[d+1:]
                return t
        elif d == 0:
                t["breakfast"] = list[2:l]
                t["lunch"] = list[l+1:]
                return t

        elif b!=0 and l!=0 and d!=0:
                t["breakfast"] = list[2:l]
                t["lunch"] = list[l+1:d]
                t["dinner"] = list[d+1:]
                return t

        return t

def tagMenu(menu, dh):
        if len(menu) != 0 and menu["_error"] != 1:
               menu["success"] = 1
               menu["message"] = "It Works!"
        else:
               menu["success"] = 0
               menu["message"] = "Couldn't get the menu,\n try again but the dining hall might be closed for the day."
        if dh != None:
            menu["dh"] = dh
        return menu

def split_by_submeal(sublist):
        dict = {}
        list = []
        dictstr = ""
        for i in range(len(sublist)):
                if "--" in sublist[i]:
                        if list:
                                dict[dictstr] = list
                                list = []
                        dictstr = sublist[i]
                else:
                        list.append(sublist[i])
        dict[dictstr] = list
        return dict

def find(list, substr):
        for i, s in enumerate(list):
                if substr in s:
                        return i
        return -1
