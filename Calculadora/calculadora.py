import soma
import divisao
import multiplica
import subtracao


def pergunta_operacao():
    op = input("Digite o símbolo da operação desejada (+,-,*, /): ")
    if op not in ["+", "-", "*", "/", "0"]:
        print("Insira uma operação válida...")
        return False
    else:
        return op

def pergunta_2numeros():

    n1 = input("Insira o primeiro valor: ")
    n2 = input("Insira o segundo valor: ")    

    return float(n1), float(n2)

is_running = True
op = 0

while is_running == True:

    checa_input = False
    while checa_input == False:
        op = pergunta_operacao()
        if op != False:
            checa_input = True

    n1,n2 = pergunta_2numeros()

    if op == "+":
        result = soma.somaF(n1, n2)
        print("%.2f + %.2f = %.2f" % (n1, n2, result))

    elif op == "-":
        result = subtracao.subtracaof(n1, n2)
        print("%.2f - %.2f = %.2f" % (n1, n2, result))

    elif op == "*":
        result = multiplica.multiplicaf(n1, n2)
        print("%.2f * %.2f = %.2f" % (n1, n2, result))

    elif op == "/":
        result = divisao.dividef(n1, n2)
        print("%.2f / %.2f = %.2f" % (n1, n2, result))
    elif op == "0":
        is_running = False





    
        





        
