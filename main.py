from click import clear

listaTarefas = []

continuar = "s"

opcaoEscolhida = 0

while continuar == "s":
    print("1.Adicionar item na lista\n"
              "2.Listar\n"
              "3.Deletar item da lista\n"
              "4.Atualizar algum item\n"
              "5.Sair")
    opcaoEscolhida = int(input("O que deseja fazer?\n"))
    if opcaoEscolhida == 1 or opcaoEscolhida == 2 or opcaoEscolhida == 3 or opcaoEscolhida == 4:

        if opcaoEscolhida == 1:
            itemLista = input("Digite o item que quer adicionar: ")
            listaTarefas.append(itemLista)
            print(f"{itemLista} foi adicionado na sua lista.")

        elif opcaoEscolhida == 2:
            if len(listaTarefas) == 0 :
                    print("Lista Vazia, impossível verificar. Adicione algo para listar.")
            else:
                print(listaTarefas)

        elif opcaoEscolhida == 3:
            if len(listaTarefas) == 0 :
                    print("Lista Vazia, impossível apagar algo. Adicione algo na lista.")
            elif len(listaTarefas) != 0:
                print("1.Deletar item específico\n"
                      "2.Limpar lista")
                opcaoDeletar = int(input("Deseja deletar um item específico ou limpar a lista inteira? "))

                if opcaoDeletar == 1:
                    itemApagado = input("Digite o item que quer apagar da lista")
                    listaTarefas.remove(itemApagado)
                    print(f"{itemApagado} apagado.")
                else:
                    listaTarefas.clear()

        elif opcaoEscolhida == 4:
            if len(listaTarefas) == 0 :
                    print("Lista Vazia, impossível Atualizar um item inexistente. Adicione algo na lista.")
            else:
                itemAntigo = input("Digite o item que deseja modificar: ")
                if itemAntigo in listaTarefas:
                    novoItem = input("Digite o novo item a ser adicionado no lugar: ")
                    indice = listaTarefas.index(itemAntigo)
                    listaTarefas[indice] = novoItem
                    print("Item atualizado com sucesso!")
                else:
                    print("Item não encontrado na lista. :(")

    else:
        print("Opcao inválida. Digite uma opcao valida para seguir.")

        continuar = input("Deseja continuar? Digite S para sim ou qualquer tecla para nao: ")