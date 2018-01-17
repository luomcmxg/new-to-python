import os
import time
import tensorflow as tf
from functools import reduce
import sys
import zipfile
target_dir = "E:\\\\Backup"
source = ['"G:\\\\test"']
today = target_dir + os.sep + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")
comment = input("Enter a comment --> ")
if len(comment) == 0:
    target = today + os.sep + now + ".zip"
else:
    target = today + os.sep + now + "_" + comment.replace(" ", "_") + ".zip"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
if not os.path.exists(today):
    os.mkdir(today)
    print("Successfully created directory", today)


# target =today+os.sep+now+".zip"
zip_command = "zip -r {0}  {1}".format(target, " ".join(source))

print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print("Successfully backup to", target)

else:
    print("Backup FAILED")
help(tf.Session)
print(int(reduce(lambda x, y: x * y, [8, 9, -1, -10])))
print(sys.argv)
help(list.append)
help(zipfile)
help(int)
