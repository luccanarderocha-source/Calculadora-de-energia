print("Camculadora de Média de Consumo de Energia de Eletrodomésticos (CMCEE)")

nomeDoAparelho = input("Qual o nome do aparelho? ")
potenciaDoAparelho = float(input("Qual a potência do aparelho em watts(W)? "))
tempoDeUso = float(input("Qual o tempo médio de uso em horas? "))

consumoMensal = (potenciaDoAparelho * tempoDeUso * 30) / 1000

print("O consumo mensal médio de seu(sua)", nomeDoAparelho, "é de:", consumoMensal, "KWh")