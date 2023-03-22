resp = "S"
qtd = 0
soma = 0

while resp == "S":
    soma = soma + float(input("Digite a nota " + str(qtd + 1)))
    qtd += 1
    resp = input("Desejo continuar?(S ou N) ").upper()
    while resp != "S" and resp != "N":
        print("opção invalida!")
        resp = input("Desejo continuar?(S ou N) ").upper()


media = soma/qtd
print(media)

