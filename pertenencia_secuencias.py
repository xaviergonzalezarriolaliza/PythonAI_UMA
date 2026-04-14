# --- Uso con cadenas de texto (str) ---
# En strings, 'in' busca sub-cadenas (substrings)
mensaje = "Aprendiendo Python en la UMA"

print("--- Pertenencia en Strings ---")
print(f"¿Está 'Python' en el mensaje?: {'Python' in mensaje}")      # True
print(f"¿Está 'Java' en el mensaje?: {'Java' in mensaje}")          # False
print(f"¿NO está 'error' en el mensaje?: {'error' not in mensaje}") # True

# --- Uso con rangos (range) ---
# En rangos, 'in' verifica si un número pertenece a la progresión aritmética
numeros_pares = range(0, 20, 2) # 0, 2, 4, ..., 18

print("\n--- Pertenencia en Rangos ---")
print(f"Rango definido: {list(numeros_pares)}")

# Es True porque el 4 está dentro del inicio/fin y coincide con el paso (step)
print(f"¿Está el 4 en el rango?: {4 in numeros_pares}") 

# Es False porque, aunque 5 está entre 0 y 20, no forma parte de los saltos de 2
print(f"¿Está el 5 en el rango?: {5 in numeros_pares}") 

# Es True porque 21 está fuera del límite superior
print(f"¿NO está el 21 en el rango?: {21 not in numeros_pares}")

# Nota de ingeniería: 
# 'x in range(...)' en Python 3 es extremadamente eficiente O(1), 
# ya que Python calcula matemáticamente si el número debería estar ahí 
# en lugar de recorrer toda la lista de números.
