poem = """\
Prgramming is fun
When the work is done 
if you wanna make your life work also fun:
	 	use Python!
"""
for i in range(2, 10):
    t = open("{}.txt".format(i), "w")
    s = list(map(float, map(lambda x: x**i, (a for a in range(2, i + 1)))))
    t.write(str(s))
    t.close()
for i in range(2, 10):
    with open("{}.txt".format(i),"r") as t:
        for line in t.readlines():
            print(line.strip())
f = open("poem.txt", "w")
f.write(poem)

f.close()

f = open("poem.txt")
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line.rstrip())

f.close()
