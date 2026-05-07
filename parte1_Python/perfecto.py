perfecto=8128
div = []
suma=0
for i in range (1, perfecto):
    if perfecto % i == 0:
        div.append(i)
        suma +=i
 
print("Divisores de", perfecto, ":", div)   
if suma == perfecto:
    print("La suma de los divisores propios es igual al número, por lo tanto, es un número PERFECTO!")
else:
    print("La suma de los divisores propios no es igual al número, por lo tanto, no es un número perfecto.")