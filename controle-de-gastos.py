descricoes = []
valores = []

while True: 
    print("\n1 - Cadastrar  2 - Listar  3 - Somar  0 - Sair")
    opcao = input("Escolha uma opção: ")

    # caso o usuario escolha 1
    if opcao == "1":
        descricao = input("Descrição: ")
        descricoes.append(descricao)
        valor = float(input("Valor: "))
        valores.append(valor)
    # caso o usuario queira listar os gastos
    elif opcao == "2": 
        for indice in range(len(descricoes)):
            print(f"{indice+1} - Descrição: {descricoes[indice]}   Valor: {valores[indice]}")
    #caso o usuario escolha somar o total
    elif opcao == "3":
        soma_total = sum(valores)
        print(f"O total de gastos da lista é: {soma_total}")
    #caso nao seja nenhuma das opcoes anteriores
    else:
        print("Fim do programa.")
        break

# range = define um intervalo