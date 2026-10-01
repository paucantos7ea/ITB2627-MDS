edad = int(input("Introduce tu edad: "))
vestido = input("¿Vas vestido adecuadamente y de blanco? (si/no): ").lower()
entrada = input("¿Tienes entrada? (si/no): ").lower()

if edad >= 18 and vestido == "si" and entrada == "si":
    print("Puedes entrar a la discoteca.")
else:
    print("No puedes entrar a la discoteca.")