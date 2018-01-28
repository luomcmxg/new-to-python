import sys
import time

f = None
try:
    with open("poem.txt") as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print(line, end=" ")
            sys.stdout.flush()
            print("Press ctrl+c now")
            time.sleep(0.2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
# finally:
# 	if f:
# 		f.close()
a={}
i=0
for items in tuple(sys.version_info):
	a[i]=items
	i+=1
print(a)

print(sys.version_info)
print(dir(sys.version_info))
