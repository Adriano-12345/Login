import os
import time

Cadastros = {}

while True:
    try:
        inicio = int(input("Bem vindo! O que deseja realizar?\n1 - Login\n 2 - Cadastrar"))
        os.system("cls")
        if inicio == 1:
            UserInput = input("Qual seu usuário?\n")
            PasswordInput = input("Qual a sua senha?\n")
            os.system("cls")
            if UserInput in Cadastros and PasswordInput == Cadastros[UserInput]["senha"]:
                print(f"Seja bem vindo, {UserInput}!")
                break
            else:
                print("Usuário ou senha incorretos.")
                esqueceu = input("Esqueceu sua senha? (S/N)")
                os.system("cls")
                if esqueceu.lower() == "s":
                    Esqueceu_User = input("Qual o usuário?")
                    Esqueceu_Email = input("Qual o seu E-Mail (Registrado na conta)")
                    if Esqueceu_User in Cadastros and Esqueceu_Email in (Cadastros[Esqueceu_User]["email"]):
                        print("Verifique o código no seu E-Mail.")
                        ConfimarEmail = input("Insira o código de verificação: (Por padrão para teste, é 2222)\n")
                        if ConfimarEmail == "2222":
                            while True:
                                RedefinirSenha = input("Insira sua nova senha.\n")
                                os.system("cls")
                                ConfirmarRedefinicao = input("Confirme sua nova senha.\n")
                                os.system("cls")
                                if RedefinirSenha == ConfirmarRedefinicao:
                                    Cadastros[Esqueceu_User] = {
                                        "senha": RedefinirSenha
                                        }
                                    print("Senha redefinida com sucesso!")
                                    time.sleep(3)
                                    os.system("cls")
                                    break
                    else:
                        print("Usuário ou email não cadastrado.")
        elif inicio == 2:
            print("Bem vindo a central de cadastro!")
            while True:
                EmailInput = input("Insira seu Email\n")
                NewUserInput = input("Qual seu novo usuário?\n")
                NewPasswordInput = input("Qual a senha do seu usuário?\n")
                os.system("cls")
                ConfirmPasswordInput = input("Confirme sua senha.\n")
                if NewPasswordInput == ConfirmPasswordInput and NewUserInput not in Cadastros:
                    ConfirmEmailInput = input("Insira o código enviado em seu E-Mail (por padrão para teste, o código é 1111)\n")
                    if ConfirmEmailInput == "1111":
                        Cadastros[NewUserInput] = {
                            "senha": NewPasswordInput,
                            "email": EmailInput
                        }
                        print("Você foi cadastrado com sucesso! Faça seu login após 7 segundos.")
                        time.sleep(7)
                        break
                    else:
                        print("Código de verificação inválido!")
                        Esqueceuv2 = input("Reiniciar processo? (S/N)")
                        if Esqueceuv2.lower() == "s":
                            break
                        elif Esqueceuv2.lower() == "n":
                            continue
                else:
                    print("Nome de usuário já cadastrado ou senhas incoerentes.")
                    os.system("cls")
        else:    
            print("Digite um valor válido entre as opções.")
            time.sleep(3)
            os.system("cls")
    except:
        print("Erro indentificado! Tente novamente.")
        time.sleep(3)
        print("DEBUG")
        print(f"\n\n{Cadastros}\n\n")
        time.sleep(5)
        os.system("cls")
        import os
import time

Cadastros = {}

while True:
    try:
        inicio = int(input("Bem vindo! O que deseja realizar?\n1 - Login\n 2 - Cadastrar"))
        os.system("cls")
        if inicio == 1:
            UserInput = input("Qual seu usuário?\n")
            PasswordInput = input("Qual a sua senha?\n")
            os.system("cls")
            if UserInput in Cadastros and PasswordInput == Cadastros[UserInput]["senha"]:
                print(f"Seja bem vindo, {UserInput}!")
                break
            else:
                print("Usuário ou senha incorretos.")
                esqueceu = input("Esqueceu sua senha? (S/N)")
                os.system("cls")
                if esqueceu.lower() == "s":
                    Esqueceu_User = input("Qual o usuário?")
                    Esqueceu_Email = input("Qual o seu E-Mail (Registrado na conta)")
                    if Esqueceu_User in Cadastros and Esqueceu_Email in (Cadastros[Esqueceu_User]["email"]):
                        print("Verifique o código no seu E-Mail.")
                        ConfimarEmail = input("Insira o código de verificação: (Por padrão para teste, é 2222)\n")
                        if ConfimarEmail == "2222":
                            while True:
                                RedefinirSenha = input("Insira sua nova senha.\n")
                                os.system("cls")
                                ConfirmarRedefinicao = input("Confirme sua nova senha.\n")
                                os.system("cls")
                                if RedefinirSenha == ConfirmarRedefinicao:
                                    Cadastros[Esqueceu_User] = {
                                        "senha": RedefinirSenha
                                        }
                                    print("Senha redefinida com sucesso!")
                                    time.sleep(3)
                                    os.system("cls")
                                    break
                    else:
                        print("Usuário ou email não cadastrado.")
        elif inicio == 2:
            print("Bem vindo a central de cadastro!")
            while True:
                EmailInput = input("Insira seu Email\n")
                NewUserInput = input("Qual seu novo usuário?\n")
                NewPasswordInput = input("Qual a senha do seu usuário?\n")
                os.system("cls")
                ConfirmPasswordInput = input("Confirme sua senha.\n")
                if NewPasswordInput == ConfirmPasswordInput and NewUserInput not in Cadastros:
                    ConfirmEmailInput = input("Insira o código enviado em seu E-Mail (por padrão para teste, o código é 1111)\n")
                    if ConfirmEmailInput == "1111":
                        Cadastros[NewUserInput] = {
                            "senha": NewPasswordInput,
                            "email": EmailInput
                        }
                        print("Você foi cadastrado com sucesso! Faça seu login após 7 segundos.")
                        time.sleep(7)
                        break
                    else:
                        print("Código de verificação inválido!")
                        Esqueceuv2 = input("Reiniciar processo? (S/N)")
                        if Esqueceuv2.lower() == "s":
                            break
                        elif Esqueceuv2.lower() == "n":
                            continue
                else:
                    print("Nome de usuário já cadastrado ou senhas incoerentes.")
                    os.system("cls")
        else:    
            print("Digite um valor válido entre as opções.")
            time.sleep(3)
            os.system("cls")
    except:
        print("Erro indentificado! Tente novamente.")
        time.sleep(3)
        print("DEBUG")
        print(f"\n\n{Cadastros}\n\n")
        time.sleep(5)
        os.system("cls")
        
