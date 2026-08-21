def multiplica(n1: float, n2: float) -> float:

    return round(n1 * n2,2)


def main():
    assert multiplica(2, 3) == 6
    assert multiplica(2.5, 3.7) == 9.25
    assert multiplica(-1.5, 4.0) == -6.0
    assert multiplica(0, 5) == 0
    assert multiplica(-2, -3) == 6
    assert multiplica(1.1, 1.1) == 1.21, "testando"

    print("Todos os testes passaram com sucesso!")
    return

if __name__ == "__main__":
main()

    