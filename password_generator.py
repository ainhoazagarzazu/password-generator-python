import random
password = ""
caracteres = ""
letras_minuscula = "abcdefghijklmnopqrstuvwxyz"
letras_mayuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%"
longitud = int(input("¿Cuántos caracteres quieres? "))
if longitud < 6:
    print("La contraseña debe tener al menos 6 caracteres")
else:
    quiere_minuscula = input("¿Quieres incluír letras en minúscula? (s/n)" )
    quiere_mayuscula = input("¿Quieres incluír letras en mayúscula? (s/n)" )
    usar_numeros = input("¿Quieres incluír números? (s/n)" )
    usar_simbolos = input("¿Quieres incluír símbolos? (s/n):" )
    if quiere_minuscula == "s":
        caracteres += letras_minuscula
    if quiere_mayuscula == "s":
        caracteres += letras_mayuscula
    if usar_numeros == "s":
        caracteres += numeros
    if usar_simbolos == "s":
        caracteres += simbolos
    else:
        print("Debes seleccionar al menos un tipo de caracter.")
    for i in range(longitud):password += random.choice(caracteres)
    print(" 🔐 Tu nueva contraseña es:", password)
