def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    password1=input()
    largo_pass=int(len(password1))
    contiene_num= ("0" in password1) or ("1" in password1) or ("2" in password1) or ("3" in password1) or ("4" in password1) or ("5" in password1) or ("6" in password1) or ("7" in password1) or ("8" in password1) or ("9" in password1)
    if largo_pass>=8 and contiene_num==True:
        print("Contraseña valida")
    elif largo_pass>=8 and contiene_num==False:
        print("Debe contener un numero")
    elif largo_pass<8 and contiene_num==True:
        print("Contraseña muy corta")
    else:
        print("Contraseña muy corta")
        print("Debe contener un numero")
