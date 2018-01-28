import pickle
import json
import inspect
shoplistfile = "shoplist.txt"

shoplist = ["apple", "mango", "carrot", "banana", "pear"]
print(type(shoplist[0]))
for items in shoplist:
    items = items.encode("utf-8")

with open(shoplistfile, "wb") as f:
    pickle.dump(shoplist, f)


del shoplist
f = open(shoplistfile, "rb")
storedlist = pickle.load(f)
f.close()
storedlist.sort(key=lambda a: len(a))
print(storedlist)
