import tensorflow as tf
import numpy
import PIL
shoplist = ["apple", "mango", "carrot", "banana"]
print("I have", len(shoplist), "items to purchase")
print("These items are:", end=" ")
for item in shoplist:
    print(item, end=" ")
print("\nI also have to buy rice.")
shoplist.append("rice")
print("My shoplist is now", shoplist)

print("I will sort my lsit now")
shoplist.sort()
print("Sorted shopping list is", shoplist)
print("The first item I will buy is", shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print("I bought the", olditem)
print("My shopping list is now", shoplist)
olditem2 = shoplist[0]
print("I also bought the", olditem2)
del shoplist[0]
olditem3 = []
print("My shopping list is now", shoplist)
for i in range(1, len(shoplist) + 1):
    olditem3.append(shoplist[0])
    print("I bought", olditem3[i - 1])
    del shoplist[0]
    print("My shopping list is now", shoplist)
    i + 1
print(dir(list))
help(list)
print(numpy.__version__)
help(PIL)
