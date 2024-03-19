#Lista

def retira_rep(lista):
    lista_sem_rep = []
    for elemt in lista:
        if not element in lista_sem_rep:
            lista_sem_rep.append(elemt)

    return lista_sem_rep

l = [1,2,2,3,2,1,4,7]
print(retira_rep(1))

def limpa_lista(lista):
    nova_lista = []
    for elemt in lista:
        if elemt < 3:
            nova_lista.append(elemt)
    return nova_lista

print(limpa_lista(1))
