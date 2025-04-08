def palyndrome(word):
    if len(word)<=1 : #quando arrivi alla fine o a 0 o hai 1 lettera ed è sempre palundroma
        return True
    else:
        return (word[0]==word[-1] and palyndrome(word[1:-1])) #da 1 incluso a -1 esluso

def palyndrome_banale(word):
    return word==word[::-1] #sia appoggia sul fato che in python esiste l'inversione della stronga se no eri fottuto

if __name__ == '__main__':
    print(palyndrome("casa"))
    print(palyndrome("civic"))
    print(palyndrome_banale("casa"))
    print(palyndrome_banale("civic"))