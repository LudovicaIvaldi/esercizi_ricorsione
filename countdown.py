from time import sleep

def countdown(n):
    while(n>=0):
        print(n)
        sleep(0.5)
        n-=1
#rimango sempre nella stessa riga di debag dentro la sessa istanza del metodo

def countdown_recursive(n):
    if n<=0:
        print("stop")
    else:
        print(n)
        sleep(0.5)
        counter=n-1
        countdown_recursive(counter)
#quando lanci questo lanci proprio più vole il metodo, fai più isteanze del metodo countive_recursive su argomenti diversi,
#non stai ciclando sulla stessa funzione ma stai chiamando più volte il metodo con argomenti diversi
#nei cicli rimani dentro la stessa istanza del metodo, con la ricorsioni crei tante istanze deiverso dello stesso metodo
#fai crescere lo stack di chiamate
#quando esegui l'ultima chiamata chude tutte le istanze del metodo aperte prima -> unwinding (per effetto a catena tutte le chiamate fatte priam si chiudono)


if __name__ == '__main__':
    #countdown(10)
    countdown_recursive(10)

