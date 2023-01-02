import time

print("SEJA BEM VINDO AO BANCO ")

nome = str(input('Por favor informe o seu nome: '))
resp = int(input("sr(a) {} o senhor(a) possui cadastro no banco? \n[0]Não \n[1]Sim \nResposta: ".format(nome)))

if resp == 0:
    x = int(input("sr(a) {} gostaria de realizar o cadastro? \n[0]Não \n[1]Sim \nResposta: ".format(nome)))
    while x == 0:
        print("sr(a) {} agradeçemos o contato, mas não podemos continuar !!".format(nome))
        break
    while x == 1:
        str(input("Ok sr(a) Por favor informe o seu nome completo: ".format(nome)))
        str(input("Informe o seu Bairro: "))
        str(input("Informe a cidade onde reside: "))
        str(input("Informe o seu endereço residencial: "))
        int(input("Informe o DDD: "))
        float(input("Informe o numero de telefone: "))
        str(input("Informe o seu sexo: "))
        str(input("Informe a sua nacionalidade: "))
        str(input("informe a cidade do seu nascimento: "))
        str(input("informe o seu estado de nascimento: "))
        print('Aguarde um instante.....')
        time.sleep(2)
        doc = int(input("sr(a) {} escolha um documento para informar:\n"
                        "[0]RG \n[1]CPF \ninforme a sua escolha:".format(nome)))
        while doc == 0:
            rg = float(input("sr(a) {} informe aqui o numero do seu RG (somente numero): ".format(nome)))
            break
        while doc == 1:
            cpf = float(input("sr(a) {} informe aqui o numero do seu CPF (somente numero): ".format(nome)))
            break
        while doc >= 2:
            print("Opção Invalida !")
            break
        if doc <= 1:

            t = int(input("sr(a) {} informe o tipo de conta que gostaria de abrir:"
                          "\n[1] Conta correte \n[2] Conta poupança \n[3] Conta sálario \nResposta:"))

            if t == 1:
                print("sr {} em instantes estaremos abrindo a sua conta corrente !".format(nome))
                time.sleep(2)
                print("sr {} a sua Agencia é 1440 e sua conta corrente é a 12345-6".format(nome))
            if t == 2:
                print("sr {} em instantes estaremos abrindo a sua conta poupança !".format(nome))
                time.sleep(2)
                print("sr {} a sua Agencia é 1476 e sua conta corrente é a 15685-6".format(nome))
            if t == 3:
                print("sr {} em instantes estaremos abrindo a sua conta salário !".format(nome))
                time.sleep(2)
                print("sr {} a sua Agencia é 1420 e sua conta corrente é a 22435-7".format(nome))
            print("Agradeçemos volte sempre !")
            break

if resp == 1:
    y = int(input("Ok sr(a) {} qual seria o seu cadastro: \n[1] Cliente \n[2] Funcionario \nResposta: ".format(nome)))
    if y == 2:
        us = str(input("Informe o seu usuario: "))
        sh = int(input("sr(a) {} informe a sua senhar: ".format(us)))
        if sh != 123456:
            print("sr(a) {} a sua senha está errada ! \nACESSO RECUSADO!!" .format(us))
        else:
            print("sr{} seja bem vindo ".format(us))
            sv = int(input("sr {} informe o tipo de serviço que será executado.\n[1]Correção no sistema"
                           "\n[2]Correção no hardware\n[3]Manutenção na rede"
                           "\npor favor informe a opção escolhida: ".format(us)))
            time.sleep(2)
            if sv == 1:
                print("{} Acesso liberado para correção no sistema".format(us))
            time.sleep(2)
            if sv == 2:
                print("{} Acesso liberado para correção do hardware".format(us))
            time.sleep(2)
            if sv == 3:
                print("{} Acesso liberado a manutenção de Rede".format(us))

    elif y == 1:
        card = int(input("sr(a) {} Gostaria de iniciar com o cartão ou sem o cartão "
                         "\n[1]Com cartão \n[2]Sem Cartão \nResposta: ".format(nome)))
        time.sleep(2)
        if card == 1:
            print("sr(a) {}, Ok Vamos continuar o acesso com o cartão".format(nome))
            time.sleep(2)
        elif card == 2:
            print("sr(a) {}, Ok Vamos continuar o acesso sem o cartão".format(nome))
            time.sleep(2)
        else:
            print("sr(a) {},Esta opção escolhida é invalida !! ".format(nome))

        fun = int(input("Seja bem vindo(a) sr(a) {} o que gostaria de realizar?\n[1]Saque \n[2]Deposito"
                        "\n[3]Consultar cambio \n[4]Emprestimo \n[5]Transferencia \n[6]Saldo"
                        "\n[7]Extrato \n[8]Consultar Conta \n[9]Solicitação\informativos"
                        "\nsr(a) {} Informe a sua escolha: ".format(nome, nome)))
        si = int(input("Informe a sua senha de 6 digitos:"))
        time.sleep(2)
        if si == 123456:
            if fun == 1:
                vc = float(input("Informe o valor em reais que voce tem na sua conta hoje R$ "))
                vs = float(input("Informe o valor que gostaria de sacar da sua conta R$ "))
                if vs <= 1000.00:
                    sub = vc-vs
                    print("sr(a) {} valor de saque for de R$ {}"
                          " e atualmente consta R$ {} na sua conta bancaria.".format(nome, vs, sub))
                if vs >= 1000.01:
                    print("Saque recusado.\nValor escolhido foi de R$ {} maior que R$ {}".format(vs, 1000.01))
                    print("Obrigado Volte Sempre")

                elif fun == 6:
                    input("Informe o seu nome completo: ")
                    print("sr(a) {} o saldo na sua conta é de R$ {} ".format(nome, 1000.00))
                    i = int(input("sr(a) {} gostaria de imprimir [1]Sim ou [2]Não \nResposta:".format(nome)))
                    if i == 1:
                        print("O saldo da sua conta esta sendo impresso..........")
                    elif i == 2:
                        print("Obrigado Volte Sempre")

            elif fun == 7:
                print("sr(a) {} o extrato da sua conta é de R$ {} e não"
                      "Houve movimentação até a data atual.".format(nome, 1000.00))

            elif fun == 2:
                d = float(input("sr(a) {} informe o valor que voce deseja adicionar a sua conta R$ ".format(nome)))
                valoc = float(input("sr(a) {} informe o valor em reais que voce já "
                                    "tinha na sua conta hoje R$ ".format(nome)))
                soma = d + valoc
                print("Sr(a) {} o valor na sua conta atual é de R$ {}".format(nome, soma))
                print("Obrigado, Volte sempre !!")

            elif fun == 3:
                r = float(input("sr {} iremos consultar o cambio do dolar "
                                "\ninforme o valor em reais que o senhor tem hoje R$ ".format(nome)))
                cal = (r / 5.71)
                print("sr(a) {} o valor em dolar será de ${:.2f}\nMuito obrigado!!".format(nome, cal))
                b = int(input("Sr(a) {} gostaria de imprimir  [1]SIM [2]NÃO\n Resposta:".format(nome)))
                if b == 1:
                    print("O seu recibo está sendo impresso .......")
                if b == 2:
                    print("Agradeçemos, Volte Sempre")
                while b != 1:
                    print("Opção Invalida !!")
                    break
                while b == 1:
                    print('Opção Invalida !!')
                    break
            elif fun == 4:
                emp = float(input("sr {} Favor informar o valor do emprestimo requerido R$ ".format(nome)))
                div = float(input("sr{} informe em quantas vezes gostaria de dividir o valor: ".format(nome)))
                cal = (div * 0.102) + div
                print("sr{} pagara R${} por {} meses sendo que há 1,25% de juros por mes ! ".format(nome, cal, div))
                print("Obrigado Volte sempre !!!")

            elif fun == 8:
                print("ok sr(a) {} a sua agencia é a 1440\na sua conta é 12259-8 \n"
                      " e o seu tipo de conta corrente!".format(nome))

            elif fun == 9:
                str(input("sr {} Faça a sua solicitação em texto".format(nome)))

            elif fun == 5:
                ty = int(input('Informe o tipo de transferencia [1]Ted [2]DOC [3]TRANSFERENCIA [4]PIX :'))
                if ty == 1 or 2 or 3:
                    str(input("Informe o banco destinadario: "))
                    float(input("Informe a conta bancaria sem digito: "))
                    int(input("Infome a agencia sem digito: "))
                    float(input("Informe o valor de Tranferencia R$ "))
                    str(input("Informe o nome do destinatario: "))
                    print("OK, Tranferencia concluida com sucesso !!\nVolte sempre!!")
                elif ty == 4:
                    str(input("Transferencia PIX, Informe O nome do destinatario: "))
                    n = int(input("Infome o tipo de documento [5]RG [6]CPF "))
                    while n == 5:
                        input("Informe o numero do seu RG: ")
                    while n == 6:
                        input("Infome o numero do seu Cpf: ")
                        break
                    else:
                        print("Opção Invalida")

        else:
            print("Opção invalida !!!\nTente Novamente!!!")
    else:
        print("Opção invalida !!!\nTente novamente!!!")
while resp >= 2:
    print("Opção invalida !!\nTente Novamente !!")
    break
