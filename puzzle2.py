
import random

# Receives an array
def check(arr):
	# Returns true if array length is 8 or the element 5 occuries 3 or more times
	return len(arr) == 8 or arr.count(5) >= 3

# Randomize a number between 2 and 10 to uses as array length
arr_len = random.randint(2, 10)
arr = []

# Fills array with random numbers between 1 and 20
for i in range(0, arr_len):
	arr.append(random.randint(1, 20))

print(arr)
# Check if array matches with the propose
print(check(arr))