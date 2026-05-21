usuarios = []

def mostrar_menu():
    print("\n=== SISTEMA DE LOGIN ===")
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Listar usuários")
    print("4 - Sair")
    print("5 - encerrar conta")
    

while True:

    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ")
        
        if nome in [u["nome"] for u in usuarios]:
            print("usuario já existe, tente outro nome.")

        else:
            usuario = {
                "nome": nome,
                "senha": senha,
                "status": "ativo"
            }

            usuarios.append(usuario)

            print("Usuário cadastrado com sucesso!")

    elif opcao == "2":

        nome_login = input("Digite seu nome: ")
        senha_login = input("Digite sua senha: ")

        login_feito = False

        for usuario in usuarios:
            
            

            if usuario["nome"] == nome_login and usuario["senha"] == senha_login:
                if usuario["status"] == "encerrado":
                    
                    print(" conta encerrada, entre em contato com o suporte para mais infomações.")
                    
                else:
                    print("bem vindo, Estamos muito felizes em recebê-lo!")
                login_feito = True

        if login_feito == False:

            print("Usuário ou senha incorretos.")

    elif opcao == "3":

        print("\n=== USUÁRIOS CADASTRADOS ===")

        if len(usuarios) == 0:

            print("Nenhum usuário cadastrado")

        else:
            
            for usuario in usuarios:

                print(f"Nome: {usuario['nome']}")
                print(f"status: {usuario['status']}")
                print("----------------------")

    elif opcao == "4":

        print("Saindo do sistema...")
        break
    elif opcao == "5":
        
        nome_encerrar = input("Digite seu nome para encerrar a conta: ")
        senha_encerrar = input("Digite sua senha: ")

        for usuario in usuarios:
            if usuario["nome"] == nome_encerrar and usuario["senha"] == senha_encerrar:
                usuario["status"] = "encerrado"
                print("Conta encerrada com sucesso!")
                break
        else:
            print("Usuário ou senha incorretos.")