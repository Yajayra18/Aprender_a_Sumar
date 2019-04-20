print ("Escribe dos numeros")
numero_intentos = 0 
num_1 = int (input("numero 1:"))
num_2 = int (input("numero 2:"))
respuesta_incorrecta = True

while (numero_intentos < 3 and  respuesta_incorrecta):
    print ("ahora suma los dos numeros")
    resp  = int (input("respuesta:"))
    if resp == num_1 + num_2:
        print ("Muy Bien!")
        respuesta_incorrecta = False
    else:
        print ("La respuesta es incorrecta, intenta nuevamente")
        numero_intentos += 1 