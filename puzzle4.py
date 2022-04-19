# My code
'''
piles = int(input('How much piles are you lookin for? '))
pile = []

for i in range(0, piles):
	pile.append(piles + 2 * i)
print(pile)
'''

# Better one

def check(x):
	# 4 + 2 * 0 = 4
	# 4 + 2 * 1 = 6
	# 4 + 2 * 2 = 8
	return [x + 2 * i for i in range(x)]

piles = int(input('How much piles are you lookin for? \n'))
print(check(piles))
