
def checkNumber(integer):
	return (
		integer > (4 ** 4)
		and
		(integer % 34) == 4
	)

x = int(input('Insert an integer number: '))

print("Result: ", checkNumber(x))

