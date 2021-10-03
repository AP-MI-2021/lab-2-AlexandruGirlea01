def get_largest_prime_below(n):
    '''
    Functia afiseaza cel mai mare numar prim, mai mic decat numarul dat
    :param n: Parametru fata de care numarul prim trebuie sa fie mai mic
    :return: int; Un numar prim mai mic decat parametrul n
    '''
    if n<=2:
        print("Numarul trebuie sa fie mai mare decat 2")
    else:
        for Numar in range(n-1,-1,-1):
            NrDivizori = 0
            for i in range(2, Numar//2+1):
                if Numar % i == 0:
                    NrDivizori+=1
            if NrDivizori == 0:
                print(Numar)
                break


def test_get_largest_prime_below():
    assert(get_largest_prime_below(12)) == 11
    assert(get_largest_prime_below(3)) == 2



def is_palindrome(n):
    '''
    Functia determina daca un numar este sau nu palindrom
    :param n: Numarul care trebuie sa fie testat
    :return: bool; True daca este palindrom sau False in caz contrar
    '''
    auxiliar = n
    invers = 0
    while n>0:
        invers = invers*10+n%10
        n = n//10
    if auxiliar == invers:
        return True
    else:
        return False


def test_is_palindrome():
    assert(is_palindrome(121)) == True
    assert(is_palindrome(122)) == False





isRunning = True
while isRunning == True:
    n1 = int(input("Introduceti datele pentru Problema 1(Cel mai mare numar prim mai mic decat numarul dat):"))
    print(get_largest_prime_below(n1))
    n2 = int(input("Introduceti datele pentru Problema 2(Verificati daca numarul este palindrom):"))
    print(is_palindrome(n2))
    opt = int(input("Daca doriti sa opriti aplicatia apasati tasta 0, iar daca doriti sa continuati apasati orice alta tasta:"))
    if opt == 0:
        isRunning=False
    else:
        isRunning = True