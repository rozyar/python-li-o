def calcular_media(numero1, numero2):
    #Calcular uma media simples
    media = (numero1 + numero2)/2

    print("A media é igual a:" + str(media))

resp = "S"
while resp == "S":
    nota1 = float(input("Digite o primeiro Numero: "))
    nota2 = float(input("Digite o segundo Numero: "))

    calcular_media(nota1, nota2)
    resp = input("Desejo continuar?(S ou N) ").upper()