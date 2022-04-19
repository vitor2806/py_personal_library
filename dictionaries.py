car = {
	"identifier": "ABC-9823",
	"brand": "Porsche",
	"model": "911 GT3 RS2",
	"power": "650HP",
	"price": "R$ 785.000,00"
}

print("\t\tCar: \n")
for info in car:
	print(info+": "+car[info])
print('')

for i in car.keys(): #default
	print(i)