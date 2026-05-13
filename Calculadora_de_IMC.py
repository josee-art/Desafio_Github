import os

pacientes = []

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(DIRETORIO_ATUAL, "pacientes.txt")

def Menu(): 
    print("\nCalculadora de IMC - Índice de Massa Corporal\n")
    print("Escolha uma das opções: ")
    print("1 - Cadastrar paciente ")
    print("2 - IMC dos pacientes cadastrados")
    print("3 - Salvar dados")
    print("4 - Sair do programa\n")
    try:
        opcao = int(input("Digite o número da opção que deseja: "))
        return opcao
    except ValueError:
        return 0
    
def Carregar_Dados():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(" | ")

            nome = dados[0]
            peso = float(dados[1])
            altura = float(dados[2])

            paciente = {
                "nome": nome,
                "peso": peso,
                "altura": altura
            }

            pacientes.append(paciente)

    print("\n[SUCESSO] Dados carregados!")

def Cadastro():
    print("\n====Cadastro de Pacientes====\n")
    nome = str(input("Digite o nome do paciente: "))
    peso = float(input("Digite o peso do paciente (Kg): "))
    altura = float(input("Digite a altura do paciente (m): "))
    if peso <= 0:
        print("\nDigite um peso válido!")
        return
    if altura <= 0:
        print("\nDigite uma altura válida!")
        return
    
    paciente = {
        "nome": nome,
        "peso": peso,
        "altura": altura
    }

    pacientes.append(paciente)
    print("\nPaciente Cadastrado com sucesso!")

def Calculo_IMC(peso,altura):
    return peso / (altura * altura)

def Mostrar_pacientes():
    print("\n==== Pacientes Cadastrados ====\n")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return
    
    for paciente in pacientes:
        imc = Calculo_IMC(paciente["peso"], paciente["altura"])

        print(f"Nome: {paciente['nome']}")
        print(f"Peso: {paciente['peso']} Kg")
        print(f"Altura: {paciente['altura']} m")
        print(f"IMC: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso")
            print("================================")

        elif imc < 25:
            print("Classificação: Peso normal")
            print("================================")

        elif imc < 30:
            print("Classificação: Sobrepeso")
            print("================================")
        else:
            print("Classificação: Obesidade")
            print("================================")

def Salvar_Dados():

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        linha = f"Dados dos pacientes (Nome, Peso, Altura, IMC):\n"
        arquivo.write(linha + "\n")
        for paciente in pacientes:
            imc = Calculo_IMC(paciente['peso'], paciente['altura'])
            if imc < 18.5:
             abaixo = str("Classificação: Abaixo do peso")
             linha = f"--> {paciente['nome']} | {paciente['peso']} | {paciente['altura']} | {abaixo}\n"
             arquivo.write(linha)

            elif imc < 25:
             normal = str("Classificação: Peso normal")
             linha = f"--> {paciente['nome']} | {paciente['peso']} | {paciente['altura']} | {normal}\n"
             arquivo.write(linha)

            elif imc < 30:
             sobrepeso = str("Classificação: Sobrepeso")
             linha = f"--> {paciente['nome']} | {paciente['peso']} | {paciente['altura']} | {sobrepeso}\n"
             arquivo.write(linha)

            elif imc >= 30:
             obesidade = str("Classificação: Obesidade")
             linha = f"--> {paciente['nome']} | {paciente['peso']} | {paciente['altura']} | {obesidade}\n"
             arquivo.write(linha)

    print(f"\n[SUCESSO] Dados gravados em: {CAMINHO_ARQUIVO}")

Carregar_Dados()
while True:
    opcao = Menu()
    if opcao == 1:
        Cadastro()
    elif opcao == 2:
        Mostrar_pacientes()
    elif opcao == 3:
        Salvar_Dados()
    elif opcao == 4:
        print("\nEncerrando o sistema de IMC. Até logo!")
        break
    else:
        print("\nEscolha uma opção válida!")

