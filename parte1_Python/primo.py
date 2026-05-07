primo = 137
divisores = 0
for i in range(1, primo + 1):      # range(1, primo+1) includes primo itself
    if primo % i == 0:
        divisores += 1

print("Número de divisores:", divisores)
if divisores == 2:
    print(primo, "SI es primo")
else:
    print(primo, "NO es primo")
    