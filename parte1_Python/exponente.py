exponente = 3 # int(input("Introduce el exponente: "))
print("\nTabla de potencias (base^{exponente}) para bases del 1 al 10:")
for base in range(1, 11):
    resultado = base ** exponente
    print(f"{base} ^ {exponente} = {resultado}")