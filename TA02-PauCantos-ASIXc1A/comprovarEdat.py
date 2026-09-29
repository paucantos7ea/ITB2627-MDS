"""

Pau CAntos

ASIXc 0373 Llenguatges de marques

Descripció: Programa que diu si ets major d'edat o no segons l'edat que introdueixis.

"""
# Programa que demana l'edat i diu si ets major
edad = int(input("Quina edat tens? "))

if edad >= 18:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")

#Funció 1: edad d'aqui a 10 anys
print (f"En 10 anys tindràs {edad + 10} anys")

#Funció 2: edad d'aqui als 18 anys
if edad < 18:
    print(f"Et falten {18 - edad} anys per ser major d'edat")

print("Fi del programa")