import os             ## -------- "os" arquivo dentro do phyton para executar comandos externos do nosso arquivo
import cadastro       ## -------- USAMOS O "IMPORT" para realmente importar coisas para dentro desse arquivo ---- ai nesse caso eu to importando o arquivo "cadastro" para dentro desse aqui, deixando os codigos mais separados e organizados!!

banco_dados = []

def menu () :
    while True:
        print ("1 - Cadastro cliente")
        print ("2 - Listar Clientes")
        print ("3 - Atualizar cliente")
        print ("4 - Excluir cliente")
        print ("-" * 50)

        opcao = input ("Escolha uma opção:")

        os.system ("cls") ## --------------- esse ".system" serve para manipular as coisas dentro do terminal // e o "cls" serve para limpar o terminal depois do loop
        if opcao == "1":
            print ("Cadastro")
            cadastro.cadastro_cliente (banco_dados)
        elif opcao == "2":
            print (banco_dados)
        elif opcao == "3":
            print ("Atualizar")
        elif opcao == "4":
            print ("Excluir")
        elif opcao == "5":
            print ("Sistema encerrado")
            break
        else: 
            print ("ERRO: Opção inválida.")

menu ()
