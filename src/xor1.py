#if __name__ == '__main__': 

from random import randint

no1 = randint(15,125)
no2 = randint(15,125)

while no2 == no1:
	no2 = randint(15,125)

no3 = randint(15,125)
while no3 == no1 or no3 == no2:
	no3 = randint(15,125)

print('first no. %d     second no. %d     third no. %d' % (no1,no2,no3))



"""
numb1=[]

for i in range (6,-1,-1):
    no = no1//2**i
    numb1.append(no)
    no1 = no1 % 2**i
print(numb1)

"""
"""
if __name__ == '__main__': 

	no1 = 36
	no2 = 19
	no3 = 56
	print('first no. %d     second no. %d     third no. %d' % (no1,no2,no3))
	no = no1 ^ no2 ^no3
	if no == 0:
		
		print(no)
	
"""	
	
"""
	
	if no < no3:
		no3 = no
		print('i have changed the third no to %d' % (no3))
		print('first no. %d     second no. %d     third no. %d' % (no1,no2,no3))
		print('now it is your turn to changd the number.' )
		print(no)
"""