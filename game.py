import random


size = 3

def is_way(matrice):
	

#def sort(raw_matrice):

		


matrice = [ [random.randint(0, 1) for i in range( size)] for j in range( size) ]
matrice[0][0] = 1
matrice[size - 1][size - 1] = 1
print(matrice)
#sort(matrice)
input()