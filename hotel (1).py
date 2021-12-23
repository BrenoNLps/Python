#Lucas Celestino e Breno Lopes

from datetime import date
from datetime import datetime

#Listas
clientesL = []
reservasL = []
apartamentosL = []
reservas_apartamentosL = []

#Dicionarios
cliente = {}
reserva = {}
apartamento = {}
reserva_apartamento = {}

escolha = 0
print("----------------------")
print("Bem-vindo ao Hotel")
print("----------------------")

#Cliente
def IncluirCliente(cliente, clientesL):
    cpf = input("CPF: ")
    checar = True
    x = 0
    while x < len(clientesL):
        if(cpf == clientesL[x]['cpf']):
            checar = False
        x = x + 1
    if(checar):
        cliente['cpf'] = cpf
        nome = input("Nome: ")
        cliente['nome'] = nome
        endereco = input("Endereço: ")
        cliente['endereco'] = endereco
        telefone = input("Telefone fixo: ")
        cliente['telefone'] = telefone
        celular  = input("Celular: ")
        cliente['celular'] = celular
                
        clientesL.append(cliente.copy())
        cliente.clear()
        print("-----------")
        print("Cliente inserido")
        print("-----------")
    else:
        print("\n Usuário com CPF já cadastrado. \n")

        
def AlterarCliente(cliente, clientesL):
    cpf = input("CPF do cliente: ")
    checar = False
    x = 0
    posicao = 0
    while x < len(clientesL):
        if(cpf == clientesL[x]['cpf']):
            posicao = x
            cliente_alterar = clientesL[x]
            checar = True
        x = x + 1
    if(checar):
        propriedade = input("Deseja alterar qual propriedade do cliente? ")
        if(propriedade == 'cpf'):
            print("\n Não é possível alterar o CPF. \n")
        elif(propriedade not in cliente_alterar.keys()):
            print("\n Essa propriedade não existe. \n")
        else:
            dado = input("Forneça o novo dado para substituir: ")
            cliente_alterar[propriedade] = dado
            clientesL[posicao] = cliente_alterar
            print("-----------")
            print("Cliente alterado")
            print("-----------")
    else:
        print("\n Este CPF não está cadastrado \n")

        
def ExcluirCliente(clientesL):
    cpf = input("CPF do cliente para excluir:")
    checar = False
    x = 0
    while x < len(clientesL):
        if(cpf == clientesL[x]['cpf']):
            posicao = x
            checar = True
            del clientesL[x]
            print("-----------")
            print("Cliente excluído")
            print("-----------")
        x = x + 1
    if(checar == False):
        print("\n Este CPF não está cadastrado. \n")

        
def ListarCliente(clientesL):
    cpf = input("\n CPF do cliente para listar: \n")
    checar = False
    x = 0
    posicao = 0
    while x < len(clientesL):
        if(cpf == clientesL[x]['cpf']):
            cliente_listar = clientesL[x]
            print("++++ Cliente ++++")
            print(f"CPF: {cliente_listar['cpf']}")
            print(f"Nome: {cliente_listar['nome']}")
            print(f"Endereço: {cliente_listar['endereco']}")
            print(f"Telefone: {cliente_listar['telefone']}")
            print(f"Celular: {cliente_listar['celular']}")
            print("++++++++++++++++")
                    
            checar = True
        x = x + 1
    if(checar == False):
        print("\n Este CPF não está cadastrado. \n")

        
def ListarClientes(clientesL):
    if(len(clientesL) == 0):
        print("\n Não há clientes no cadastro \n")
    else:
        x = 0
        while x < len(clientesL):
            cliente_listar = clientesL[x]
            print(cliente_listar)
            print("++++ Cliente ++++")
            print(f"CPF: {cliente_listar['cpf']}")
            print(f"Nome: {cliente_listar['nome']}")
            print(f"Endereço: {cliente_listar['endereco']}")
            print(f"Telefone: {cliente_listar['telefone']}")
            print(f"Celular: {cliente_listar['celular']}")
            print("++++++++++++++++")
            x = x + 1

#Reserva
def IncluirReserva(clientesL, reservasL, reserva):
    cpf = input("CPF do cliente para reserva: ")
    checar_cpf = False
    checar = True
    x = 0
    while x < len(clientesL):
        if(cpf == clientesL[x]['cpf']):
            checar_cpf = True
        x = x + 1
                
    if (checar_cpf == False):
        print("\n CPF não encontrado. \n")
    else: 
        y = 0
        codigo = input("Código da reserva: ")
        while y < len(reservasL):
            if(codigo == reservasL[y]['codigo']):
                checar = False
            y = y + 1
                        
        if(checar and checar_cpf):
            reserva['codigo'] = codigo
            reserva['cpf_cliente'] = cpf

            reservasL.append(reserva.copy())
            reserva.clear()
            print("\n Reserva incluída \n")
        else:
            print("\n Código já cadastrado. \n")
            
def AlterarReserva(reservasL, clientesL, reserva):
    codigo = input("Código da reserva: ")
    checar = False
    x = 0
    posicao = 0
    while x < len(reservasL):
        if(codigo == reservasL[x]['codigo']):
            posicao = x
            reserva_alterar = reservasL[x]
            checar = True
        x = x + 1
                
    if(checar):
        propriedade = input("Deseja alterar qual propriedade da reserva? ")
        if(propriedade == 'codigo'):
            print("\n Não é possível alterar o código. \n")
        elif(propriedade not in reserva_alterar.keys()):
            print("\n Essa propriedade não existe. \n")
        else:
            dado = input("Forneça o novo dado para substituir: ")
            y = 0
            checar_cliente = False
            while y < len(clientesL):
                if(dado == clientesL[y]['cpf']):
                    checar_cliente = True
                            
                    reserva_alterar[propriedade] = dado
                    reservasL[posicao] = reserva_alterar
                            
                    print("-----------")
                    print("Reserva alterada")
                    print("-----------")
                y = y + 1
            if(checar_cliente == False):    
                print("\n Este CPF não está cadastrado \n")
                    
    else:
        print("\n Este código de reserva não está cadastrado \n")
def ExcluirReserva(reservasL):
    codigo = input("Código da reserva para excluir: ")
    checar = False
    x = 0
    while x < len(reservasL):
        if(codigo == reservasL[x]['codigo']):
            checar = True
            del reservasL[x]
            print("-----------")
            print("Reserva excluída")
            print("-----------")
        x = x + 1
    if(checar == False):
        print("\n Este código de reserva não está cadastrado. \n")
        
def ListarReserva(reservasL):
    codigo = input("Código da reserva para listar: ")
    checar = False
    x = 0
    posicao = 0
    while x < len(reservasL):
        if(codigo == reservasL[x]['codigo']):
            reserva_listar = reservasL[x]
            print("++++ Reserva ++++")
            print(f"Código: {reserva_listar['codigo']}")
            print(f"CPF do cliente: {reserva_listar['cpf_cliente']}")
            print("++++++++++++++++")  
            checar = True
        x = x + 1
    if(checar == False):
        print("\n Este código não está cadastrado. \n")

        
def ListarReservas(reservasL):
    if(len(reservasL) == 0):
        print("\n Não há reservas cadastradas \n")
    else:
        x = 0
        while x < len(reservasL):
            listar = reservasL[x]
            print("++++ Reservas ++++")
            print(f"Código: {listar['codigo']}")
            print(f"CPF do cliente: {listar['cpf_cliente']}")
            print("++++++++++++++++")
            x = x + 1

#Apartamento
def IncluirApartamento(apartamentosL, apartamento):
    codigo = input("Código do apartamento: ")
    checar = True
    x = 0
    while x < len(apartamentosL):
        if(codigo == apartamentosL[x]['codigo']):
            checar = False
        x = x + 1
    if(checar):
        apartamento['codigo'] = codigo
        descricao = input("Descrição: ")
        apartamento['descricao'] = descricao
        adultos = int(input("Quantidade de adultos: "))
        apartamento['adultos'] = adultos
        criancas = int(input("Quantidade de crianças: "))
        apartamento['crianças'] = criancas
        valor = float(input("Valor do apartamento: "))
        apartamento['valor'] = valor
                
        apartamentosL.append(apartamento.copy())
        apartamento.clear()
        print("-----------")
        print("Apartamento incluído")
        print("-----------")
                
    else:
        print("\n Código de apartamento já cadastrado. \n")

        
def AlterarApartamento(apartamentosL):
    codigo = input("Código do apartamento: ")
    checar = False
    x = 0
    posicao = 0
    while x < len(apartamentosL):
        if(codigo == apartamentosL[x]['codigo']):
            posicao = x
            apartamento_alterar = apartamentosL[x]
            checar = True
        x = x + 1
                
    if(checar):
        propriedade = input("Deseja alterar qual propriedade do apartamento? ")
        if(propriedade == 'codigo'):
            print("\n Não é possível alterar o Código. \n")
        elif(propriedade not in apartamento_alterar.keys()):
            print("\n Essa propriedade não existe. \n")
        else:
            if(propriedade == 'adultos' or propriedade == 'criancas'):                        
                dado = int(input("Forneça o novo dado para substituir: "))                            
                apartamento_alterar[propriedade] = dado
                apartamentosL[posicao] = apartamento_alterar
                print("-----------")
                print("Apartamento alterado")
                print("-----------")
            elif(propriedade == 'valor'):                        
                dado = float(input("Forneça o novo dado para substituir: "))                            
                apartamento_alterar[propriedade] = dado
                apartamentosL[posicao] = apartamento_alterar
                print("-----------")
                print("Apartamento alterado")
                print("-----------")
            else:
                dado = float(input("Forneça o novo dado para substituir: "))                            
                apartamento_alterar[propriedade] = dado
                apartamentosL[posicao] = apartamento_alterar
                print("-----------")
                print("Apartamento alterado")
                print("-----------")
    else:
        print("\n Código não encontrado \n")
        
def ExcluirApartamento(apartamentosL):
    
    codigo = input("Código do apartamento para excluir: ")
    checar = False
    x = 0
    while x < len(apartamentosL):
        if(codigo == apartamentosL[x]['codigo']):
            checar = True
            del apartamentosL[x]
            print("-----------")
            print("Apartmento excluído")
            print("-----------")
        x = x + 1
    if(checar == False):
        print("\n Este código de reserva não está cadastrado. \n")

  
def ListarApartamento(apartamentosL):
    
    codigo = input("Código do apartamento para listar: ")
    checar = False
    x = 0
    posicao = 0
    while x < len(apartamentosL):
        if(codigo == apartamentosL[x]['codigo']):
            apartamento_listar = apartamentosL[x]
            print("++++ Reserva ++++")
            print(f"Código: {apartamento_listar['codigo']}")
            print(f"Descrição do apartamento: {apartamento_listar['descricao']}")
            print(f"Número de adultos no apartamento: {apartamento_listar['adultos']}")
            print(f"Número de crianças no apartamento: {apartamento_listar['crianças']}")
            print(f"Valor apartamento: {apartamento_listar['valor']}")
            print("++++++++++++++++")  
            checar = True
        x = x + 1
    if(checar == False):
        print("\n Este código não está cadastrado. \n")
    
def ListarApartamentos(apartamentosL):
    
    if(len(apartamentosL) == 0):
        print("\n Não há apartamentos cadastrados \n")
    else:
        x = 0
        while x < len(apartamentosL):
            apartamento_listar = apartamentosL[x]
            print("++++ Reserva ++++")
            print(f"Código: {apartamento_listar['codigo']}")
            print(f"Descrição do apartamento: {apartamento_listar['descricao']}")
            print(f"Número de adultos no apartamento: {apartamento_listar['adultos']}")
            print(f"Número de crianças no apartamento: {apartamento_listar['crianças']}")
            print(f"Valor apartamento: {apartamento_listar['valor']}")
            print("++++++++++++++++") 
            x = x + 1

def IncluirReservaApartamentos(apartamentosL,reservasL,reservas_apartamentosL,reserva_apartamento):
    
    codigo_apartamento = input("Código do apartamento: ")
    checar_apartamento = False
    x = 0

    #Checa se o apartamento existe
    while x < len(apartamentosL):
        if(codigo_apartamento == apartamentosL[x]['codigo']):
            checar_apartamento = True
        x = x + 1

        
    codigo_reserva = input("Código da reserva: ")
    checar_reserva = False
    x = 0
    
    #Checa se a reserva existe
    while x < len(reservasL):
        if(codigo_reserva == reservasL[x]['codigo']):
            checar_reserva = True
        x = x + 1

    entrada = input("Data de entrada dd/mm/yy: ")
    entrada_input = datetime.strptime(entrada, '%d/%m/%Y').date()
    saida = input("Data de saída dd/mm/yy: ")
    saida_input = datetime.strptime(saida, '%d/%m/%Y').date()

    checar_reserva2 = True
    x = 0
    #Checa se a reserva ja foi incluida no ReservaApartamentos
    while x < len(reservas_apartamentosL):
        if(codigo_reserva == reservas_apartamentosL[x]['codigo_reserva']):
            checar_reserva2 = False
        x = x + 1

    
    if(checar_reserva2 == False):
        print("\n Essa reserva já foi feita. \n")

    checa_datas = True
    x = 0
    #Checa se as datas de entrada e saída para um mesmo apartamento são diferentes
    while x < len(reservas_apartamentosL):
        if(codigo_apartamento == reservas_apartamentosL[x]['codigo_apartamento']):
            
            data_entrada = reservas_apartamentosL[x]['entrada']
            dataE = datetime.strptime(data_entrada, '%d/%m/%Y').date()

            data_saida = reservas_apartamentosL[x]['saida']
            dataS = datetime.strptime(data_saida, '%d/%m/%Y').date()
            
            if(entrada_input >= dataE and entrada_input <= dataS or saida_input >= dataE and saida_input <= dataS):
                checa_datas = False
        x = x + 1
                
    if(checar_apartamento):
        reserva_apartamento['codigo_apartamento'] = codigo_apartamento
        if(checar_reserva and checar_reserva2):
            reserva_apartamento['codigo_reserva'] = codigo_reserva
            if(checa_datas):
                reserva_apartamento['entrada'] = entrada
                reserva_apartamento['saida'] = saida
                reservas_apartamentosL.append(reserva_apartamento.copy())
                reserva_apartamento.clear()
                print("\n Reserva de apartamento cadastrada. \n")
            else:
                print("\n Datas inválidas \n")
        else:
            print("\n Código de reserva inexistente \n")
    else:
        print("\n Código de apartamento inexistente \n")

        
        
def ExcluirReservaApartamentos(reservas_apartamentosL):
    
    codigo = input("Código da reserva para excluir: ")
    checar = False
    x = 0
    while x < len(reservas_apartamentosL):
        if(codigo == reservas_apartamentosL[x]['codigo_reserva']):
            checar = True
            del reservas_apartamentosL[x]
            print("-----------")
            print("Reserva excluída")
            print("-----------")
        x = x + 1
    if(checar == False):
        print("\n Este código de reserva não está cadastrado. \n")
        
def ListarReservaApartamentos(reservas_apartamentosL):
    codigo = input("Código da reserva para listar: ")
    checar = False
    x = 0
    posicao = 0
    while x < len(reservas_apartamentosL):
        if(codigo == reservas_apartamentosL[x]['codigo_reserva']):
            reserva_listar = reservas_apartamentosL[x]
            print("++++ Reserva ++++")
            print(f"Código do apartamento: {reserva_listar['codigo_apartamento']}")
            print(f"Código da reserva: {reserva_listar['codigo_reserva']}")
            print(f"Entrada: {reserva_listar['entrada']}")
            print(f"Saída: {reserva_listar['saida']}")
            print("++++++++++++++++")  
            checar = True
        x = x + 1
    if(checar == False):
        print("\n Esta reserva não está cadastrada. \n")
    
def ListarTodasReservasApartamentos(reservas_apartamentosL):
    if(len(reservas_apartamentosL) == 0):
        print("\n Não há reservas cadastradas \n")
    else:
        x = 0
        while x < len(reservasL):
            reserva_listar = reservas_apartamentosL[x]
            print("++++ Reserva ++++")
            print(f"Código do apartamento: {reserva_listar['codigo_apartamento']}")
            print(f"Código da reserva: {reserva_listar['codigo_reserva']}")
            print(f"Entrada: {reserva_listar['entrada']}")
            print(f"Saída: {reserva_listar['saida']}")
            print("++++++++++++++++")  
            x = x + 1
            
def ReservasDoApartamento(reservas_apartamentosL):
    codigo = input("Código do apartamento para listar: ")
    checar = False
    x = 0
    posicao = 0
    while x < len(reservas_apartamentosL):
        if(codigo == reservas_apartamentosL[x]['codigo_apartamento']):
            reserva_listar = reservas_apartamentosL[x]
            print("++++ Reserva ++++")
            print(f"Código do apartamento: {reserva_listar['codigo_apartamento']}")
            print(f"Código da reserva: {reserva_listar['codigo_reserva']}")
            print(f"Entrada: {reserva_listar['entrada']}")
            print(f"Saída: {reserva_listar['saida']}")
            print("++++++++++++++++")  
            checar = True
        x = x + 1
    if(checar == False):
        print("\n Este apartamento não tem reservas. \n")
def ReservasPorCliente(reservasL, reservas_apartamentosL):
    cpf = input("CPF do cliente para checar reserva: ")
    checar_cpf = False
    codigo = ""
    x = 0
    codigos_de_reserva = []
    while x < len(reservasL):
        if(cpf == reservasL[x]['cpf_cliente']):
            checar_cpf = True
            codigos_de_reserva.append(reservasL[x]['codigo'])
        x = x + 1
                
    if (checar_cpf == False):
        print("\n CPF não encontrado. \n")
    else:
        x = 0
        while (x < len(reservas_apartamentosL)):
            codigo_atual = reservas_apartamentosL[x]['codigo_reserva']
            reserva_listar = reservas_apartamentosL[x]
            y = 0
            while y < len(codigos_de_reserva):
                if(codigo_atual == codigos_de_reserva[y]):
                    print("++++ Reserva ++++")
                    print(f"Código do apartamento: {reserva_listar['codigo_apartamento']}")
                    print(f"Código da reserva: {reserva_listar['codigo_reserva']}")
                    print(f"Entrada: {reserva_listar['entrada']}")
                    print(f"Saída: {reserva_listar['saida']}")
                    print("++++++++++++++++")  
                y = y + 1
            x = x + 1
def ClientesEntreDatas(reservas_apartamentosL,reservasL,clientesL):
    entrada = input("Data de entrada dd/mm/yy: ")
    entrada_input = datetime.strptime(entrada, '%d/%m/%Y').date()
    saida = input("Data de saída dd/mm/yy: ")
    saida_input = datetime.strptime(saida, '%d/%m/%Y').date()
    check = False
    x = 0
    while x < len(reservas_apartamentosL):
        cpf_cliente = ""
        nome_cliente = ""
        reserva_listar = reservas_apartamentosL[x]
        data_entrada = reservas_apartamentosL[x]['entrada']
        dataE = datetime.strptime(data_entrada, '%d/%m/%Y').date()

        data_saida = reservas_apartamentosL[x]['saida']
        dataS = datetime.strptime(data_saida, '%d/%m/%Y').date()
            
        if(dataE >= entrada_input and dataE <= saida_input):
            codigo_reserva = reservas_apartamentosL[x]['codigo_reserva']
            y = 0
            while y < len(reservasL):
                if(codigo_reserva == reservasL[y]['codigo']):
                    cpf_cliente = reservasL[y]['cpf_cliente']
                y = y + 1
                
            z = 0
            while z < len(clientesL):
                if(cpf_cliente == clientesL[z]['cpf']):
                    nome_cliente = clientesL[z]['nome']
                
                    print("++++ Dados ++++")
                    print(f"Nome: {nome_cliente}")
                    print(f"CPF: {cpf_cliente}")
                    print("++++++++++++++++")
                    check = True
                z = z + 1
        x = x + 1

    if(check == False):
        print("\n Não há reservas dentro desse período \n")

        
while escolha != 6:
    print("1. Submenu de Clientes")
    print("2. Submenu de Reservas")
    print("3. Submenu de Apartamentos")
    print("4. Submenu de Reserva Apartamentos")
    print("5. Submenu Relatórios")
    print("6. Sair")
    escolha = int(input("Escolha: "))
    print("----------------------")
    if(escolha == 1):
        print("Submenu de Clientes")
        print("----------------------")
        print("1. Incluir cliente")
        print("2. Alterar dados do cliente")
        print("3. Excluir cliente")
        print("4. Listar um cliente")
        print("5. Listar todos os clientes")
        sub_escolha = int(input("Escolha: "))
        print("----------------------")
        
        if(sub_escolha == 1):

            
            #Incluir cliente
            IncluirCliente(cliente, clientesL)

            
        elif(sub_escolha == 2):

            
            #Alterar dados de um cliente
            AlterarCliente(cliente, clientesL)

            
        elif(sub_escolha == 3):

            
            #Excluir cliente
            ExcluirCliente(clientesL)

            
        elif(sub_escolha == 4):

            
            #Listar UM cliente
            ListarCliente(clientesL)

            
        elif(sub_escolha == 5):

            
            #Listar todos os clientes
            ListarClientes(clientesL)
            
        else:
            print("\n Opção inválida\n Tente novamente \n")    

            
    elif(escolha == 2):
        print("Submenu de Reservas")
        print("----------------------")
        print("1. Fazer reserva")
        print("2. Alterar dados da reserva")
        print("3. Excluir reserva")
        print("4. Listar uma reserva")
        print("5. Listar todas as reservas")
        sub_escolha = int(input("Escolha: "))
        print("----------------------")
        
        if(sub_escolha == 1):

            
            #Incluir reserva
            IncluirReserva(clientesL, reservasL, reserva)

                
        elif(sub_escolha == 2):

            
            #Alterar dados de uma reserva
            AlterarReserva(reservasL, clientesL, reserva)

            
        elif(sub_escolha == 3):

            
            #Excluir reserva
            ExcluirReserva(reservasL)


            
        elif(sub_escolha == 4):

            
            #Listar UMA reserva
            ListarReserva(reservasL)

                
        elif(sub_escolha == 5):

            
            #Listar todas as reservas
            ListarReservas(reservasL)

            
        else:
            print("\n Opção inválida\n Tente novamente \n")
            
    elif(escolha == 3):
        print("Submenu de Apartamentos")
        print("----------------------")
        print("1. Incluir apartamento")
        print("2. Alterar dados do apartamento")
        print("3. Excluir apartamento")
        print("4. Listar um apartamento")
        print("5. Listar todos os apartamento")
        sub_escolha = int(input("Escolha: "))
        print("----------------------")

        if(sub_escolha == 1):

            
            #Incluir apartamento
            IncluirApartamento(apartamentosL, apartamento)

            
        elif(sub_escolha == 2):

            
            #Alterar apartamento
            AlterarApartamento(apartamentosL)

            
        elif(sub_escolha == 3):

            
            #Excluir apartamento
            ExcluirApartamento(apartamentosL)

            
        elif(sub_escolha == 4):

            
            #Listar UM apartamento
            ListarApartamento(apartamentosL)
            
            
        elif(sub_escolha == 5):

            
            #Listar todos os apartamentos
            ListarApartamentos(apartamentosL)

            
        else:
            print("Opção inválida\n Tente novamente")
            
            
    elif(escolha == 4):
        print("Submenu de Reserva de Apartamentos")
        print("----------------------")
        print("1. Incluir reserva de apartamento")
        print("2. Excluir reserva do apartamento")
        print("3. Listar uma reserva de apartamento")
        print("4. Listar todas as reservas de apartamentos")
        sub_escolha = int(input("Escolha: "))
        print("----------------------")

        if(sub_escolha == 1):
            #Incluir reserva de apartamentos
            IncluirReservaApartamentos(apartamentosL,reservasL,reservas_apartamentosL,reserva_apartamento)
        elif(sub_escolha == 2):
            #Excluir reserva de apartamentos
            ExcluirReservaApartamentos(reservas_apartamentosL)
        elif(sub_escolha == 3):
            #Listar uma reserva de apartamentos
            ListarReservaApartamentos(reservas_apartamentosL)
        elif(sub_escolha == 4):
            #Listar todas as reservas de apartamentos
            ListarTodasReservasApartamentos(reservas_apartamentosL)
        else:
            print("Opção inválida\n Tente novamente")
            
    elif(escolha == 5):
        print("Submenu de Relatórios")
        print("----------------------")
        print("1. Mostrar todas as reservas de um apartamento")
        print("2. Mostrar todas as reservas de determinado cliente")
        print("3. Mostrar o CPF e nome de cada cliente que fizeram reservas para o período entre as datas X e Y")
        sub_escolha = int(input("Escolha: "))
        print("----------------------")

        if(sub_escolha == 1):
            ReservasDoApartamento(reservas_apartamentosL)
        elif(sub_escolha == 2):
            ReservasPorCliente(reservasL, reservas_apartamentosL)
        elif(sub_escolha == 3):
            ClientesEntreDatas(reservas_apartamentosL,reservasL,clientesL)
        else:
            print("Opção inválida\n Tente novamente")
    elif (escolha > 6 or escolha < 1):
        print("Opção inválida")
        print("--------------")
    else:
        print("Desligando...")
