###
# 04 - variables
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinámico y de tipado fuerte
###

#asignar una variable 
#solo hace falta poner

my_name = "Fernando"
print(my_name)

age = 32
print(age)

age = 39
print(age)

#Tipado dinámico: el tipo de dato se detrermina en tiempo de ejecución
# que no tiene que declararlo explícitamente

name = "Fernando"
print(type(name))

#name = 32
#print(type(name))

# Tipado fuerte: no realiza conversiones de tipo automático

#f-string (literal de cadena de formato)
print(f"hola {name}, tengo {age + 5} años")

# no recomendada forma de asignar variables
name, edad, city = "Ferndando", 32, "Madrid"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok" #snake_case
nombre = "ok"

MI_CONSTANTE = 3.14 # UPPER_CASE -> constantes

# nombres no validos de variables
# 123412341234_variable = "ok" 
# mi-variable = "ko"
# mi variable = "ko"

#No se puede usar las palabras reservadas de Python como nombres de variables
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']