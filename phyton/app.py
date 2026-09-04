# Importamos a biblioteca sys para encerrar o programa em caso de erro
import sys

# Função responsável por calcular o IMC
def calcular_imc(peso, altura):
    # Verifica se os valores são válidos
    if altura <= 0:
        return "Erro: a altura deve ser maior que zero."
    if peso <= 0:
        return "Erro: o peso deve ser maior que zero."

    # Fórmula do IMC: peso dividido pela altura ao quadrado
    imc = peso / (altura ** 2)

    # Classificação do IMC de acordo com os valores
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 24.9:
        classificacao = "Peso normal"
    elif imc < 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    # Retorna o resultado formatado com duas casas decimais
    return f"Seu IMC é {imc:.2f} ({classificacao})."


# Função principal do programa
def main():
    print("=== Calculadora de IMC ===")  # título do programa
    print("Este programa calcula o Índice de Massa Corporal (IMC).")
    print("Você precisa informar seu peso em kg e sua altura em metros.\n")

    # Solicita o peso ao usuário
    try:
        peso = float(input("Digite seu peso (kg): "))
    except ValueError:
        print("Entrada inválida! O peso deve ser um número.")
        sys.exit()  # encerra o programa

    # Solicita a altura ao usuário
    try:
        altura = float(input("Digite sua altura (m): "))
    except ValueError:
        print("Entrada inválida! A altura deve ser um número.")
        sys.exit()  # encerra o programa

    # Chama a função calcular_imc e guarda o resultado
    resultado = calcular_imc(peso, altura)

    # Exibe o resultado final
    print("\nResultado:")
    print(resultado)


# Executa o programa principal
if __name__ == "__main__":
    main()