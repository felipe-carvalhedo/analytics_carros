from main import AnaliseDados

analise_dados = AnaliseDados()

while True:
    print("\nEscolha uma opção:")
    print("1. Quantidade de carros por marca")
    print("2. Quantidade de carros por ano")
    print("3. Listar carros disponíveis")
    print("4. Gerar gráfico de total por marca")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        marca = input("Digite a marca para verificar a quantidade de carros: ")
        analise_dados.quantidade_carro_marca(marca)
    elif opcao == "2":
        ano = (input("Digite o ano para verificar a quantidade de carros: "))
        analise_dados.quantidade_carro_ano(ano)
    elif opcao == "3":
        analise_dados.carros_disponiveis()
    elif opcao == "4":
        analise_dados.total_por_marca()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
