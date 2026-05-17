import os

pacientes = []

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(DIRETORIO_ATUAL,"pacientes.txt")
CAMINHO_HISTORICO = os.path.join(DIRETORIO_ATUAL,"historico_imc.txt")

def Menu():
    print("\n===== CALCULADORA DE IMC =====\n")

    print("1 - Cadastrar paciente")
    print("2 - Mostrar pacientes")
    print("3 - Salvar dados")
    print("4 - Apagar paciente")
    print("5 - Ver histórico")
    print("6 - Sair\n")

    try:
        opcao = int(input("Digite a opção desejada: "))
        return opcao

    except ValueError:
        return 0


def Carregar_Dados():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas[1:]:

            dados = linha.strip().split(" | ")

            if len(dados) < 3:
                continue

            paciente = {
                "nome": dados[0],
                "peso": float(dados[1]),
                "altura": float(dados[2])
            }

            pacientes.append(paciente)

    print("\n[SUCESSO] Dados carregados!")

def Calculo_IMC(peso, altura):
    return peso / (altura ** 2)


def Classificacao_IMC(imc):
    if imc < 18.5:
        return "Abaixo do peso"

    elif imc < 25:
        return "Peso normal"

    elif imc < 30:
        return "Sobrepeso"

    else:
        return "Obesidade"

def Salvar_Historico(paciente):
    imc = Calculo_IMC(paciente["peso"],paciente["altura"])

    classificacao = Classificacao_IMC(imc)

    with open(CAMINHO_HISTORICO, "a", encoding="utf-8") as arquivo:

        linha = (
            f"{paciente['nome']} | "
            f"{paciente['peso']} Kg | "
            f"{paciente['altura']} m | "
            f"IMC: {imc:.2f} | "
            f"{classificacao}\n"
        )

        arquivo.write(linha)

def Cadastro():
    while True:

        print("\n===== CADASTRO DE PACIENTE =====\n")

        nome = input("Digite o nome do paciente: ")

        try:

            peso = float(input("Digite o peso (Kg): "))

            altura = float(input("Digite a altura (m): "))

        except ValueError:

            print("\nDigite apenas números!")
            continue

        if peso <= 0 or altura <= 0:

            print("\nPeso e altura devem ser maiores que zero!")
            continue

        paciente = {
            "nome": nome,
            "peso": peso,
            "altura": altura
        }

        pacientes.append(paciente)

        print("\nPaciente cadastrado com sucesso!")

        opcao = input(
            "\nDigite 1 para cadastrar outro paciente "
            "ou qualquer tecla para voltar ao menu: "
        )

        if opcao == "1":

            continue

        else:

            return

def Mostrar_pacientes():
    print("\n===== PACIENTES CADASTRADOS =====\n")

    if len(pacientes) == 0:

        print("Nenhum paciente cadastrado.")
        return

    indice = 1

    for paciente in pacientes:

        imc = Calculo_IMC(paciente["peso"],paciente["altura"])

        classificacao = Classificacao_IMC(imc)

        print(f"Paciente {indice}")
        print(f"Nome: {paciente['nome']}")
        print(f"Peso: {paciente['peso']} Kg")
        print(f"Altura: {paciente['altura']} m")
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        print("==================================")

        indice += 1

    input("Digite qualquer valor para voltar ao menu: ")

def Salvar_Dados():
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:

        arquivo.write(
            "Nome | Peso | Altura | Classificação\n\n"
        )

        for paciente in pacientes:

            imc = Calculo_IMC(
                paciente["peso"],
                paciente["altura"]
            )

            classificacao = Classificacao_IMC(imc)

            linha = (
                f"{paciente['nome']} | "
                f"{paciente['peso']} | "
                f"{paciente['altura']} | "
                f"{classificacao}\n"
            )

            arquivo.write(linha)

    with open(CAMINHO_HISTORICO, "a", encoding="utf-8") as arquivo:

        for paciente in pacientes:

            Salvar_Historico(paciente)

    print(f"\n[SUCESSO] Dados salvos em {CAMINHO_ARQUIVO}")

def Apagar_paciente():
    if len(pacientes) == 0:

        print("Nenhum paciente cadastrado.")
        return

    indice = 1

    for paciente in pacientes:

        imc = Calculo_IMC(paciente["peso"],paciente["altura"])

        classificacao = Classificacao_IMC(imc)

        print(f"Paciente {indice}")
        print(f"Nome: {paciente['nome']}")
        print(f"Peso: {paciente['peso']} Kg")
        print(f"Altura: {paciente['altura']} m")
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        print("==================================")

        indice += 1

    try:

        indice = int(
            input(
                "\nDigite o número do paciente que deseja apagar: "
            )
        )

        if 1 <= indice <= len(pacientes):

            removido = pacientes.pop(indice - 1)
            Salvar_Dados()

            print(
                f"\nPaciente "
                f"{removido['nome']} removido com sucesso!"
            )

        else:

            print("\nNúmero inválido!")

    except ValueError:

        print("\nDigite um número válido!")

def Mostrar_Historico():
    print("\n===== HISTÓRICO GERAL =====\n")

    if not os.path.exists(CAMINHO_HISTORICO):

        print("Nenhum histórico encontrado!")
        return

    with open(CAMINHO_HISTORICO, "r", encoding="utf-8") as arquivo:

        linhas = arquivo.readlines()

        if len(linhas) == 0:

            print("Histórico vazio!")
            return

        for linha in linhas:

            print(linha.strip())

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
        Apagar_paciente()

    elif opcao == 5:
        Mostrar_Historico()

    elif opcao == 6:
        print("\nEncerrando sistema...")
        break

    else:
        print("\nDigite uma opção válida!")
