









def menu () :
    while True:
        print ("1 - Cadastro cliente")
        print ("2 - Listar Clientes")
        print ("3 - Atualizar cliente")
        print ("4 - Excluir cliente")
        print ("-" * 50)

        opcao = input ("Escolha uma opção:")

        if opcao == "1":
            print ("Cadastro")
        elif opcao == "2":
            print ("Listar")
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

## while --------- enquanto for verdadeiro vai continuar executando o codigo


## "cls" ------ comando para limpar tudo do terminal
