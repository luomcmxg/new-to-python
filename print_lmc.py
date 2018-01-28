import io
f=io.open("abc.txt","wt",encoding="utf-8")
f.write(u"Imagine non-English language here, like 我爱你")
f.close()

with io.open("abc.txt",encoding="utf-8") as t:
	text=t.read()

print(text)
