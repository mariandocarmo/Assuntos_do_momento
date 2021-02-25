def linha():
    print("="*35)


linha()
pergunta = input("Você sabe o que significa Segurança da Informação? ")


if pergunta == "Sim":
    print(" Que bom que entende do assunto! Cuide das suas informações pessoais!")
elif pergunta == "Não":
    print("SEGURANÇA DA INFORMAÇÃO: A segurança da informação está diretamente relacionada\n\
com proteção de um conjunto de informações, no sentido de preservar o valor que possuem\n\
para um indivíduo ou uma organização.")
else:
    print("ERRO! DIGITE: Sim ou Não!")

