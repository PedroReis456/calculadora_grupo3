def somaF (n1,n2):
    soma = n1 + n2
    return soma

def main():
    assert somaF(2,5) == 7
    assert somaF(2.7,6.7) == 9.4
    assert somaF(-3,5) == 2
    assert somaF(0,5) == 5
    assert somaF(5,0) == 5
    assert somaF(2.2,2.2) == 4.4
    print('Todos os testes passaram com sucesso!')
    return

main()
   