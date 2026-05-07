for i in range(100):
    print("no se habla en clase ", i)

n = int(input("Introduce un número: "))
for i in range(1, n+1):
    print("Avanzo una calle")

print("Giro a la izquierda")


try:
    exponente = 2 # int(input("Introduce el exponente: "))
    print(f"\nTabla de potencias (base^{exponente}) para bases del 1 al 10:")
    for base in range(1, 11):
        resultado = base ** exponente
        print(f"{base} ^ {exponente} = {resultado}")
except ValueError:
    print("Error: Debes ingresar un número entero válido.")