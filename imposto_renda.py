salario_bruto = float(input())
dependentes = int(input())

if salario_bruto <= 720:
    inss = 720 * 0.0765

elif salario_bruto <=1200:
    inss = salario_bruto * 0.09

elif salario_bruto <= 2400:
    inss = salario_bruto * 0.11

elif salario_bruto > 2400:
    inss = 2400 * 0.11


if salario_bruto >= 1372.82 and salario_bruto <= 2743.25:
    aliquota = 0.15
    dedução = 205.92

elif salario_bruto > 2743.25:
    aliquota = 0.275
    dedução = 548.82

else:
    aliquota = 0
    dedução = 0

irrf = (salario_bruto - (137.99 * dependentes) - inss) * aliquota - dedução

if irrf < 0 :
    irrf = 0

print(round(irrf , 2))