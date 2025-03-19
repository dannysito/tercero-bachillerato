###
#convertir una cadena de texto a un número entero
###

print("Conversión de tipos:")

print(type("100"))
print(type(int("100")))

print(int("100") + 2)
print(2 + int("100"))

print("100" + "2")

print(type(float("3.141592")))

print(bool(3))
print(bool(0))
print(bool(-1))

print(bool(""))
print(bool(" "))
print(bool("False"))
print(bool("True"))

#print(int("Hola mundo"))#no puede transformar
print(int(2.5))#no redondea al número 3 - se usa round para redondear

print(round(2.5))
print(round(2.51))
print(round(3.5)) #redondea al par más cercano