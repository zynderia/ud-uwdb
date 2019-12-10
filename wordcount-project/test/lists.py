locations = ["Stage A", "Bar Lounge", "Post Apocalyptic", "Stage G: Aurora"]
locations.insert(0, "Stage C")

## print(locations)

for location in locations:
	if location != "Stage A":
		print(location)

##while location in locations != "Stage B":
	##print (location)

class Property:
	def __init__(self, name="", address="", type="", cat=""):
		self.name = "Stage A"
		self.address = "741 Naud STreet, Los ANgeles, CA 90012"
		self.type = "Filming"
		self.cat = "Industrial, Raw Warehouse, Grafitti"

	def rent(self, data):
		print("Thank you for your inquiry for " + data)

myProperty = Property()

print(myProperty.type)

myProperty.rent("Wednesday Dec 10, 2019")