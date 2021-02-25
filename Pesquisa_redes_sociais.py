def linha():
    print("="*35)


linha()
print ("1. Facebook")
print("2. Instagram")
print("3. Twitter")
print("4. Watssap")
print("5. Tik Tok")
pergunta = int(input("Qual a sua rede social favorita? "))


if pergunta == 1:
    print("Obrigado pela sua participação! Hoje esta plataforma conta com 2,6 bilhões de usuários.")
elif pergunta == 2:
    print("Obrigado por sua participação! Hoje esta plataforma conta com 1 bilhão de usuários.")
elif pergunta == 3:
    print("Obrigado pela sua participação! Hoje esta plataforma conta com 186 milhões de usuários.")
elif pergunta == 4:
    print ("Obrigado pela sua participação! Hoje esta plataforma conta com 2 bilhões de usuários.")
elif pergunta == 5:
    print("Obrigado pela sua participação! Hoje esta plataforma conta com  7 milhões no Brasil.")
else:
    print("ERRO! DIGITE UM NÚMERO DE 1 A 5")
