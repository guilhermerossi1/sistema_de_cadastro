def cadastro_cliente (banco_dados):
    nome = input ("Nome: ").strip()               ## --------- STRIP() remove espaços do fim e inicio da string
    idade = input ("Idade: ").strip() 
    telefone = input ("Telefone: ").strip() 
    email = input ("Email: ").strip() 


    if nome == "" or idade == "" or  telefone == "" or email == "" :
        print ("ERRO: Todos os campos são obrigatórios.")
        return

    cliente = {                                        ## ------------- isso é um dicionário! ---- é uma estrutura de dados que armazena informações em pares de é uma estrutura de dados que armazena informações em pares de é uma estrutura de dados que armazena informações em pares de é uma estrutura de dados que armazena informações em pares de chave e valor  
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "email": email
    }
    banco_dados.append(cliente)


    ## input ------- serve para captar futuramente os dados que o USUARIO vai inserir no site/aplicativo sei la