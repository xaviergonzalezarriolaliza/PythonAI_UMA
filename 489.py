#Javi
n = int(input("Introduzca el tamaño de columna/fila: "))

for fila in range(n):  
    for col in range(n):  
        if fila % 2 == 0: #izquierda a derecha
            print(fila * n + col + 1, end=" ")
        else: #derecha a izquierda
            print(fila * n + n - col, end=" ")
    print()