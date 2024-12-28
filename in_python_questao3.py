def Calculalar_hora(valor, quantida):
  return valor * quantida
def calcular_desconto(porcetagem, salario):
  return salario - ((porcetagem / 100) * salario)

horas = float(input("Digite quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada:"))

salario_bruto = Calculalar_hora(valor_hora, horas)
print(f"Salario Bruto: R${salario_bruto}")

if salario_bruto > 1800 :
  salario = calcular_desconto(8, salario_bruto)
  print(f"Salario liquido: R${salario}")
else:  # Correct indentation here
  print(f"Salario liquido: R${salario_bruto}")
