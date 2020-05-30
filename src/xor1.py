#if __name__ == '__main__': 
# description of game rules
print("")
print("")
print("the game starts with randomly generating three different integers. one of the two players,staring from you, should")
print("in turns choose only one from the three numbers and  replace it with a new smaller positive integer, which is to be ")
print("different from other two unchanged numbers. if any side fails to do so, the other one is winner. the game is over. ")

from random import randint

no1 = randint(15,125)
no2 = randint(15,125)

while no2 == no1:
	no2 = randint(15,125)

no3 = randint(15,125)
while no3 == no1 or no3 == no2 :
	no3 = randint(15,125)

print('first no. %d     second no. %d     third no. %d' % (no1,no2,no3))




nno1 = no1
nno2 = no2
nno3 = no3
for i in range (5,-1,-1):
	k = 2**i
    if noo1//k + noo2//k +noo3//k == 2:
		noo1 = nno1 % 2**i
		noo2 = nno2 % 2**i
		noo3 = nno3 % 2**i
		continue
	elif noo1//2**i + noo2//2**i +noo3//2**i == 1:
		if noo1//2**i == 1:
			print('i have changed the first no to %d' % (no2^^no3))
			print('first no. %d     second no. %d     third no. %d' % (no2^^no3,no2,no3))
		elif noo2//2**i == 1:
			print('i have changed the second no to %d' % (no1^^no3))
			print('first no. %d     second no. %d     third no. %d' % (no1,no1^^no3,no3))
		else:
			print('i have changed the third no to %d' % (no1^^no2))
			print('first no. %d     second no. %d     third no. %d' % (no1,no2,no1^^no2))
	else:
		no = randint(1,3)
		if no == 1: 
			no1 = no2^^no3
			print('i have changed the first no to %d' % (no1))			
		elif no == 2:
			no2 = no1^^no3
			print('i have changed the second no to %d' % (no2))
		else:
			no3 = no1^^no2
			print('i have changed the third no to %d' % (no3))
			
print('first no. %d     second no. %d     third no. %d' % (no1,no2,no3))

print('now it is your turn to changd the number.' )
		

