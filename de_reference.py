print("Simple Assignment")
shoplist=["apple","mango","carrot","banana"]
mylist=shoplist
del shoplist[0]
print("shoplist is",shoplist)
print("mylist is", mylist)

print("Copy by making a full slice")
# mylist=shoplist[:]
mylist=sorted(shoplist)
del mylist[0]
print("shoplist is",shoplist)
print("mylist is",mylist)
# help(str)
# st="   Lmc will find love   "
# st.strip()
# print(st,"\n\n",st.strip())
# help(str.join)
name="Swaroop"


if name.startswith("Swa"):
	print("Yes, the string starts with \"Swa\"")
	a="    a "
if "a" in name:
	print("Yes, the string contains\
 \"{}\"".format(a.strip()))
if name.find("roo")!=-1:
	print("Yes, it contains the string \"roo\"","   ",name.find("roo"))
delimeter="___h*h___"
mylist=["L","M","C","JI","UM"]
print(delimeter.join(mylist))