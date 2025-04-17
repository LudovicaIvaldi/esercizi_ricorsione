from functools import lru_cache


def quadrato_magico(N):
    rimanenti= []
    for i in range(1,N*N+1):
        rimanenti.append(i)
    ricorsione ([],rimanenti,N)




def ricorsione(parziale, rimanenti,N):
    #codizione terminale
    if len(parziale) == N*N:
        # qui calcoli le somme sulle righe colonne e diagonali
        # scandici n alla volta e sommi per le righe
        # for col in N -> col+N*riga
        # col=0 e n=3 -> 0+0, 0+3, 0+3*2 ...
        # verifca le due diagonali principali  -> cerca su internet la soluzione
        if verifica_righe(parziale,N) and verifica_colonne(parziale,N) and verifica_diag(parziale,N):
         print(parziale)
    #caso non terminale
    else:
        for i in range(len(rimanenti)):
            numero=rimanenti[i]
            parziale.append(numero)
            nuovi_rimanenti=rimanenti[:i]+rimanenti[i+1:]
            ricorsione (parziale, nuovi_rimanenti,N)
            parziale.pop()


def verifica_righe(parziale,N):
    lista_somme=[]
    for i in range(N):
        somma_righe=0
        for j in range(i*N,(i+1)*N):
            somma_righe+=parziale[j]
        lista_somme.append(somma_righe)
    for i in range(1,len(lista_somme)):
        if lista_somme[i] != lista_somme[i-1]:
            return False
    return True

def verifica_colonne(parziale,N):
    lista_colonne= []
    for col in range(N):
        somma_colonne = 0
        for r in range(N):
            indice =col+N*r
            somma_colonne+=parziale[indice]
        lista_colonne.append(somma_colonne)
    for i in range(1, len(lista_colonne)):
        if lista_colonne[i] != lista_colonne[i - 1]:
            return False
    return True

def verifica_diag(parziale,N):
    somma_diag_1 = 0
    for r in range(N):
        indice=r*N+r
        somma_diag_1 += parziale[indice]
    somma_diag_2 = 0
    for r in range(1,N+1):
        indice=(N-1)*r
        somma_diag_2 += parziale[indice]
    if somma_diag_1 != somma_diag_2:
        return False
    return True



if __name__ == '__main__':
    quadrato_magico(4)
