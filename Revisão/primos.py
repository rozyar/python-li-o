primo = "S"
for numero in range (1, 101):
    for divisor in range (1, numero+1):
        resto = numero%divisor
        if  (resto == 0 and (divisor != 1 and divisor != numero)):
            primo = "N"
    if primo == "S":
        print("O Numero " + str(numero) + " é Primo!")
        primo = "S"
    #elif primo == "N":
    #    print("O Numero " + str(numero) + " não é Primo!")
            