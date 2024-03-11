from math import *

#input des valeurs de a, b et c
a = float(input("entrez la valeur de a: "))
b = float(input("entrez la valeur de b: "))
c = float(input("entrez la valeur de c: "))

#calcul de alpha
alpha = float(-1*b)
alpha = alpha/2
alpha = alpha/a	

#calcul de beta
beta1 = float(a*alpha*alpha)
beta2 = float(b*alpha)
beta3 = c
beta3 = float(beta3)
beta = beta1+beta2+beta3

#print du résultat
print(f"alpha = {alpha}")
print(f"beta = {beta}")
if alpha <= 0:
	if beta <= 0:
		print(f"{a}(x{alpha}){beta}")
	elif beta >= 0:
		print(f"{a}(x{alpha})+{beta}")
elif alpha >= 0:
	if beta <= 0:
		print(f"{a}(x+{alpha}){beta}")
	elif beta >= 0 :
		print(f"{a}(x{+alpha})+{beta}")
