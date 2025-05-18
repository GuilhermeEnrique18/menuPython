def adicionarItem(lista):
    item = input("Digite o item que quer adicionar: ")
    lista.append(item)
    print(f"{item} foi adicionado na sua lista.")

def listarItens(lista):
    if len(lista) == 0:
        print("Lista Vazia, impossível verificar. Adicione algo para listar.")
    else:
        print("Sua lista de tarefas:")
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")

def deletarItem(lista):
    if len(lista) == 0:
        print("Lista Vazia, impossível apagar algo. Adicione algo na lista.")
    else:
        print("1.Deletar item específico\n2.Limpar lista")
        opcao = input("Deseja deletar um item específico ou limpar a lista inteira? ")

        if opcao == "1":
            item = input("Digite o item que quer apagar da lista: ")
            if item in lista:
                lista.remove(item)
                print(f"{item} apagado.")
            else:
                print("Item não encontrado na lista.")
        elif opcao == "2":
            lista.clear()
            print("Lista completamente apagada.")
        else:
            print("Opção inválida.")

def atualizarItem(lista):
    if  len(lista) == 0:
        print("Lista Vazia, impossível Atualizar um item inexistente. Adicione algo na lista.")
    else:
        item_antigo = input("Digite o item que deseja modificar: ")
        if item_antigo in lista:
            novo_item = input("Digite o novo item a ser adicionado no lugar: ")
            indice = lista.index(item_antigo)
            lista[indice] = novo_item
            print("Item atualizado com sucesso!")
        else:
            print("Item não encontrado na lista. :(")
