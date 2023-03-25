from time import sleep

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print("-=-" * 11)
print("    Gerenciador de pagamentos")
print("-=-" * 11)

preco_compras = float(input("Por favor, informe o valor total de suas compras: R$"))

print("""FORMAS DE PAGAMENTO: 
[ 1 ] à vista dinheiro/cheque, com 10% de desconto
[ 2 ] à vista no cartão, com 5% de desconto
[ 3 ] em 2x no cartão, sem juros
[ 4 ] 3x ou mais no cartão, com 20% de juros
""")

opcao = input("Selecione a opção desejada: ")

if opcao == "1":
    preco_final = preco_compras * (1 - 0.10)
elif opcao == "2":
    preco_final = preco_compras * (1 - 0.05)
elif opcao == "3":
    preco_final = preco_compras
    parcelas = preco_compras / 2
    print("\nProcessando...\n")
    sleep(2)
    print("Foram geradas 2 parcelas de R${:.2f}.".format(parcelas))
elif opcao == "4":
    preco_final = preco_compras * 1.20
    quant_parcelas = int(input("Em quantas vezes gostaria de efetuar o pagamento?\nInforme quantas parcelas: "))
    parcelas = preco_final / quant_parcelas
    print("\nProcessando...\n")
    sleep(2)
    print("Foram geradas {} parcelas de R${:.2f}.".format(quant_parcelas, parcelas))
print("Sua compra no valor de R${:.2f} ficará no valor de R${:.2f}.".format(preco_compras, preco_final))
sleep(4)
print("\nAgradecemos a preferência!")
sleep(2)
print("Atendimento finalizado.")