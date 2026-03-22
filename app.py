print("Camculadora de Média de Consumo de Energia de Eletrodomésticos (CMCEE)") # Título do programa.

nomeDoAparelho = input("Qual o nome do aparelho? ") # Entrada do nome do aparelho.
potenciaDoAparelho = float(input("Qual a potência do aparelho em watts(W)? ")) # Entrada da potência do aparelho
tempoDeUso = float(input("Qual o tempo médio de uso em horas? ")) # Entrada do tempo de uso.

consumoMensal = (potenciaDoAparelho * tempoDeUso * 30) / 1000 # Processamento do consumo mensal do aparelho.

print("O consumo mensal médio de seu(sua)", nomeDoAparelho, "é de:", consumoMensal, "KWh") # Saída do consumo mensal do aparelho.