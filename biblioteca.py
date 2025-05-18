
def adicionarLista(itemLista):
    listaTarefas.append(itemLista.upper())


def deletarItemLista(itemLista):
    listaTarefas.remove(itemLista.upper())


def listarLista():
    return listaTarefas