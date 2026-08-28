def dividef (nume,deno):
    return nume/deno

def main():

    assert dividef(10, 2) == 5, "Erro: 10/2 deveria ser 5"
    assert dividef(5.5, 2.5) == 2.2, "Erro: 5.5/2.5 deveria ser 2.2"
    assert dividef(-4.5, 1.5) == -3.0, "Erro: -4.5/1.5 deveria ser -3.0"
    assert dividef(0, 5) == 0, "Erro: 0/5 deveria ser 0"
    assert dividef(5, 0) == ZeroDivisionError, "Erro: 5/0 deveria ser "ZeroDivisionError"
    assert dividef(1.1, 1.1) == 1, "Erro: 1.1/1.1 deveria ser 1"
    print("Todos os testes passaram com sucesso!")
    return
    
if __name__ == "__main__":

    main()
