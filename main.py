import matplotlib.pyplot as plt # Biblioteca para criar gráficos e exibí-los
import numpy as np # Biblioteca para realizar cálculos matemáticos e gerar intervalos de valores

############################################################################################
# ATENÇÃO! PARA A APLICAÇÃO FUNCIONAR CORRETAMENTE, É NECESSÁRIO BAIXAR AS BIBLIOTECAS ACIMA
############################################################################################

def exibirSobre():
    print("=" * 67)
    print("     SISTEMA DE PREVISÃO DE ENCHENTES POR SATÉLITE - ECOSHIELD")
    print("=" * 67)

    print("""
Esta aplicação utiliza uma função matemática para estimar
o risco de enchentes com base no volume de chuva registrado.

Os dados de precipitação podem ser obtidos por satélites
meteorológicos, permitindo o monitoramento de regiões com
maior probabilidade de alagamentos e enchentes.

O objetivo é auxiliar sistemas de alerta antecipado,
contribuindo para a prevenção de desastres e para a
segurança da população usando tecnologias espaciais.

Função utilizada:

R(x) = 0.5x + 10
R(x) = risco de enchente
x = nível de chuva


""")


def calcularRisco(chuva):
    risco = 0.5 * chuva + 10

    if risco > 100:
        risco = 100

    print(f"\nRisco estimado: {risco:.1f}%")

    if risco < 40:
        print("Status: Baixo risco")
    elif risco < 70:
        print("Status: Alerta Amarelo")
    else:
        print("Status: Alerta Vermelho")

    # Gráfico

    chuvas = np.linspace(0, 300, 100) # Cria valores de chuva entre 0 e 300 mm
    riscos = 0.5 * chuvas + 10 # Aplica a função matemática para calcular o risco
    riscos = np.minimum(riscos, 100) # Limita o risco máximo em 100%

    plt.figure(figsize=(8, 5)) # Cria a área do gráfico
    plt.plot(chuvas, riscos, linewidth=2) # Desenha a linha da função

    plt.scatter(chuva, risco, s=80) # Marca o ponto correspondente ao valor informado pelo usuário

    plt.annotate( # Exibe as coordenadas do ponto no gráfico
        f"({chuva:.0f} mm, {risco:.0f}%)",
        (chuva, risco),
        xytext=(10, 10),
        textcoords="offset points"
    )

    plt.title("Risco de Enchente em Função do Volume de Chuva")
    plt.xlabel("Volume de Chuva (mm)")
    plt.ylabel("Risco Estimado (%)")
    plt.xlim(0, 300)
    plt.ylim(0, 110)
    plt.grid(True) # Adiciona grade para facilitar a leitura

    plt.show()

def simular():
    print("\nSIMULAÇÃO DE CENÁRIOS\n")

    for chuva in range(0, 301, 50):

        risco = 0.5 * chuva + 10

        if risco > 100:
            risco = 100

        print(
            f"Chuva: {chuva:3} mm | "
            f"Risco: {risco:5.1f}%"
        )

def analiseMatematica():
    print("=" * 28)
    print("ANÁLISE MATEMÁTICA DA FUNÇÃO")
    print("=" * 28)

    print("""
R(x) = 0,5x + 10

Domínio:    x ∈ [0, 300] mm
Imagem:     R(x) ∈ [10, 100] %
Crescimento: estritamente crescente (a = 0,5 > 0)
Zero:        x = -20 (fora do domínio — risco nunca é nulo)
R(0) = 10%  (risco base mesmo sem chuva)

""")

def menu():
    while True:

        print("\n" + "=" * 9)
        print("ECOSHIELD")
        print("=" * 9)
        print("1 - Calcular risco de enchente")
        print("2 - Sobre a aplicação")
        print("3 - Simular cenários")
        print("4 - Análise matemática da função")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            while True:
                chuva = float(input("\nDigite o volume de chuva (mm): "))

                if chuva < 0:
                    print("O volume mínimo é 0 mm.")
                elif chuva > 300:
                    print("O volume máximo é 300 mm.")
                else:
                    break

            if chuva == 0:
                print("\nNão há risco de enchente pois não houve chuva.")
            else:
                calcularRisco(chuva)

        elif opcao == "2":
            exibirSobre()

        elif opcao == "3":
            simular()

        elif opcao == "4":
            analiseMatematica()

        elif opcao == "5":
            print("\nFim da operação!")
            break

        else:
            print("\nOpção inválida.")


menu()