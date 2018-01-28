a=[]
list(map(a.append,list(filter(lambda a:a>3,[2,3,4,5,6]))))
print(a)
if True:print("yes")
zet=[{'x':2,'y':3},{'x':4,'y':1}]
zet.sort(key=lambda z: z['x'],reverse=True)
print(zet)
help(list.sort)
print(list(map(lambda x:x**2,list(filter(lambda y:y>2,range(1,9))))))
listtwo=[i**2 for i in range(1,9) if i>2]
print(listtwo)
def sump(power,*ll):
	total=0
	for i in ll:
		total+=pow(i,power)
	return total
print(sump(2,3,4))
