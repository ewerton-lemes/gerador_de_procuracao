#pacotes
import func_procuracao
import sqlite3

con = sqlite3.connect("escritorio.db")

cur = con.cursor()

cadastrados = list(cur.execute("select * from cadastro"))

print("*************** Doc Factory ***************\n")

cpf = input("Digite o CPF do cliente: ")

def encontra_cliente(x):
    encontrado = False
    dados_do_cliente = ()
    for cad in cadastrados:
        if cad[1] == x:
            dados_do_cliente = cad
            encontrado = True
    if encontrado == True:
        return [True, dados_do_cliente]
    else:
        return [False, 0]

encontra_cliente(cpf)

resultado = encontra_cliente(cpf)

if resultado[0] == True:
    print("\nDados do cliente:\n")
    print("Nome: " + resultado[1][0])
    print("CPF: " + resultado[1][1])
    print("Nacionalidade: " + resultado[1][2])
    print("Estado civil: " + resultado[1][3])
    print("Profissão: " + resultado[1][4])
    print("Endereço: " + resultado[1][5])
    print("Cidade: " + resultado[1][6])
    print("Estado: " + resultado[1][7])
else:
    print("\nCliente não encontrado.")

if resultado[0] == False:
    print("Não é possível gerar a procuração.")
else:
    gerar = input("\nGerar procuração (s/n)?")
    if gerar == "s":
        func_procuracao.procuracao_aut(resultado[1][0], resultado[1][1], resultado[1][2], resultado[1][3], \
                       resultado[1][4], resultado[1][5], resultado[1][6], resultado[1][7], resultado[1][8])


