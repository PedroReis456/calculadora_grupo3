def subtracaof(x, y):
    return x - y

def main():
      
    assert subtracaof(3, 2) == 1, "Erro: 3 - 2 deveria ser 1"
    assert subtracaof(2.5, 0.5) == 2, "Erro: 2.5 - 0.5 deveria ser 2.0"
    assert subtracaof(-1.5, 4.5) == -6.0, "Erro: -1.5 - 4.5 deveria ser -6.0"
    assert subtracaof(5, 0) == 5, "Erro: 5 - 0 deveria ser 5"
    assert subtracaof(0, 8) == -8, "Erro: 0 - 8 deveria ser -8"
    assert subtracaof(1.1, 1.1) == 0, "Erro: 1.1 - 1.1 deveria ser 0"
    print("Todos os testes passaram com sucesso!")
    return

print(main())