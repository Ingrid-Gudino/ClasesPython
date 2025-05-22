password = "holiwis"
incorrecta = True
intentos = 0
nombre = input("Ingrese su nombre: ")

while incorrecta :
    password2 = input("Ingrese su contraseña: ")
    if password == password2: 
        incorrecta = False
        
    intentos += 1

print (f"Hola {nombre}, ingresaste al sistema luego de {intentos} intentos fallidos ")       