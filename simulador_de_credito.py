from time import sleep

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
# (Acrescentei a possibilidade de compor renda com mais pessoas)

print("-=-" * 13)
print("   Bem-vindo(a) ao seu Home Banking")
print("-=-" * 13)

print("Simulador de Crédito Habitação\n")

preco_imovel = float(input("Preço do imóvel: R$"))
pessoas = int(input("Número de pessoas que irão compor renda: "))

renda = 0

for i in range(1, pessoas + 1):
    salario = float(input(f"Informe o salário da {i} pessoa: R$"))
    renda += salario


anos = int(input("Prazo em anos: "))
meses = anos * 12

parcelas = preco_imovel / (anos * 12)
parcela_max = renda * 30 / 100

print("\nGerando o limite mensal...\n")
sleep(2)
print("De acordo com a renda informada, a parcela máxima mensal poderá ser no valor R${:.2f}".format(parcela_max))

print("\nAguarde...\n")
sleep(3)

print("Para pagar uma casa no valor de R${:.2f}, em {} anos, a prestação será de R${:.2f}.".format(preco_imovel, anos, parcelas))
if parcelas < parcela_max:
    print("Parabéns! O seu financiamento foi APROVADO!")
else:
    print("Financiamento NEGADO.\nO valor mensal ultrapassa 30% da renda informada.")
print("\nPara maiores informações, dirija-se à sua agência.")

print("O Home Banking agradece a preferência!\n")
print("Atendimento finalizado.")
