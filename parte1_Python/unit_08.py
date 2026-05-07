print("This line will be printed.")

s=0
for i in range(1,11):
    s+=i
print('Sum of numbers from 1 to 10:',s)

nota = 5
if nota < 5:
    calificacion = "SUSPENSO"
elif nota < 7:
    calificacion = "APROBADO"
elif nota < 9:
    calificacion = "NOTABLE"
else:
    calificacion = "SOBRESALIENTE"

print(f'La nota es: {calificacion}')
