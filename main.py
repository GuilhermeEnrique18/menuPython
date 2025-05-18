from biblioteca import adicionarItem, listarItens, deletarItem, atualizarItem

listaTarefas = []
continuar = "s"

while continuar.lower() == "s":
    print("\nBem vindo a sua lista!")
    print("1. Adicionar item na lista")
    print("2. Listar")
    print("3. Deletar item da lista")
    print("4. Atualizar algum item")
    print("5. Sair")

    try:
        opcao = int(input("O que deseja fazer? "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if opcao == 1:
        adicionarItem(listaTarefas)
    elif opcao == 2:
        listarItens(listaTarefas)
    elif opcao == 3:
        deletarItem(listaTarefas)
    elif opcao == 4:
        atualizarItem(listaTarefas)
    elif opcao == 5:
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida.")

    continuar = input("\nDeseja continuar? Digite S para sim ou qualquer tecla para não: ")
