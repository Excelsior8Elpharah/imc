print("Cálculo de IMC")

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))

imc = peso / (altura**2)

if imc < 18.5:
    categoria = "Baixo peso"
elif imc < 25:
    categoria = "Peso adequado"
elif imc < 30:
    categoria = "Sobrepeso"
elif imc < 35:
    categoria = "Obesidade Grau I"
elif imc < 40:
    categoria = "Obesidade Grau II"
else:
    categoria = "Obesidade Grau III"

print(f"Seu IMC é {imc:.2f} e sua categoria é {categoria}")
