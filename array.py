horde = ["Garrosh", "Thrall", "Grommash", "Vol'jin"]
ally = ["Garrosh", "Varian", "Anduin", "Jaina", "Malfurion"]

print(horde)
print(ally[2])
print(len(ally))

print("")
for item in ally:
	print(item)
print("")

horde.append("Sylvannas") #add item to array's end
for item in horde:
	print(item)
print("")

index = 0
if "Garrosh" in ally:
	print("Betrayer!!!")
	print("")

	for item in horde:
		if item == "Garrosh":
			del horde[index]
		index += 1

	print("New horde:\n", horde)
	print("")
else:
	print("Not a Betrayer")

#Arr2

number_list = [23, 3902, 3203, 310293, 0, 2303, 21, 2, 3, 5]

number_list.sort() #will sort from smaller to greater
sorted_list = sorted(number_list) #same thing as sort but needs to be stored
print(sorted_list)
print(number_list)

number_list.sort(reverse=True) #will sort from greater to smaller
print(number_list)
number_list.reverse() #will flip array
print(number_list)

horde.sort() #will sort A-Z
print(horde)

horde.sort(reverse=True)
print(horde) #will sort Z-A