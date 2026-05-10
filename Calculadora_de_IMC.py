pacientes = []

def Menu(): 
    print("\nCalculadora de IMC - Índice de Massa Corporal\n")
    print("Escolha uma das opções: ")
    print("1 - Cadastrar paciente ")
    print("2 - IMC dos pacientes cadastrados\n")
    opcao = int(input("Digite o número da opção que deseja: "))
    return opcao

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
            print("Classificação: Abaixo do peso\n")

        elif imc < 25:
            print("Classificação: Peso normal\n")

        elif imc < 30:
            print("Classificação: Sobrepeso\n")
        else:
            print("Classificação: Obesidade\n")

while True:
    opcao = Menu()
    if opcao == 1:
        Cadastro()
    elif opcao == 2:
        Mostrar_pacientes()
    else:
        print("Escolha uma opção válida!")




