import matplotlib.pyplot as plt
import numpy as np


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
segurança da população.

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

    chuvas = np.linspace(0, 300, 100)
    riscos = 0.5 * chuvas + 10
    riscos = np.minimum(riscos, 100)

    plt.figure(figsize=(8, 5))
    plt.plot(chuvas, riscos, linewidth=2)

    plt.scatter(chuva, risco, s=80)

    plt.annotate(
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
    plt.grid(True)

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

def menu():
    while True:

        print("\n" + "=" * 9)
        print("ECOSHIELD")
        print("=" * 9)
        print("1 - Calcular risco de enchente")
        print("2 - Sobre a aplicação")
        print("3 - Simular cenários")
        print("4 - Sair")

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
            print("\nFim da operação!")
            break

        else:
            print("\nOpção inválida.")


menu()