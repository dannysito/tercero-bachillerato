###
# 05 - Entrada de usuario (input()) - version simplificada
#  la función input() permite obtener datos del usuario a través de la consola
###

#print("Hola como te llamas?")
#nombre = input()

nombre = input(f"Hola como te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("Cuantos años tienes?\n")
print(type(age))
print(f"Tienes {age} años")

print("Obtener múltiples datos del usuario")
country, city = input("¿En qué país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")