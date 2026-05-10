print("\nCalculadora de IMC - Índice de Massa Corporal\n")
print("Escolha uma das opções: ")
print("1 - Cadastrar paciente ")
print("2 - IMC dos pacientes cadastrados\n")
opcao = int(input("Digite o número da opção que deseja: "))

def Cadastro():
    print("\n====Cadastro de Pacientes====\n")
    nome = str(input("Digite o nome do paciente: "))
    peso = float(input("Digite o peso do paciente (Kg): "))
    altura = float(input("Digite a altura do paciente: "))
    if peso <= 0:
        print("\nDigite um peso válido!")
    else:
        return print(f"\nO nome do paciente é {nome}, seu peso é igual a {peso} Kg e sua altura é igual a {altura}\n")

if opcao == 1:
    Cadastro()
elif opcao == 2:
    print("\nVocê escolheu 2!")
else:
    print("Escolha uma opção válida!")




