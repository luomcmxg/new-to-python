ab={
	"Swaroop":"swaroop@swaroopch.com",
	"Larry":"lary@wall.org",
	"Matsumoto":"matz@rybu-lang.org",
	"Spammer":"spammer@hotmial.com"
}

print("Swaroop's address is",ab["Swaroop"])

del ab["Spammer"]

print("\nThere are {} contacts in the address-book\n".format(len(ab)))

for name,address in ab.items():
	print("Contact {} at {}".format(name,address))

ab['Guido']="guido@pyton.org"

if 'Guido' in ab:
	print("\nGuido's address is", ab['Guido'])
shoplist=["a","b","c","d","e","f"]
print(shoplist[1:10])