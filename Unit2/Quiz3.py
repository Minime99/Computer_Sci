# list # # REVIEW:
thislist = ["apple", "cookie", "knife"]
thislist.append("me")
thislist.remove("cookie")
print(thislist)
print(thislist[1])
thislist.insert(1, "smg")
print(thislist)
thislist[0] = "new"
print(thislist)
print(len(thislist))

# tuple # REVIEW:
a = (1, 2, 3)
print(a[1])
# can not be changed
print(len(a))
# you would use a tuple if you never wanted a list of things to change

# sets # REVIEW:
x = {1, 5, 4}
print(x)
x.add(6)
print(x)
x.add(6)
print(x)
# did not change
x.remove(1)
print(x)
# can not replace

# dictionarie # REVIEW:
thisdict = {"noah": 'fedosoff', "gun": 'ammo', "knife": 'blood'}
print(thisdict)
print(thisdict["noah"])
thisdict.update({"noah": 'star'})
print(len(thisdict))
thisdict.update({"smg": '3'})
#thisdict["smg"] = "3"
print(thisdict)
del thisdict["noah"]
print(thisdict)
