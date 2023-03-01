print('{:=^40}'.format(' loja arthur '))
preco = float(input('qual valor da compra ? R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] A vista no dinheiro
[ 2 ] A vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão com juros de 20% ''')
opcao = int(input('qual é a opção'))
if opcao == 1:
    p1=preco-(preco*0.10)
    print('sua compra de {} vai custar {} no final'.format(preco,p1))
elif opcao == 2:
    p2 =preco-(preco*0.05)
    print('sua compra de {} vai custar {} no final'.format(preco,p2))
elif opcao ==3:
    p3 = preco/2
    print('sua compra de {} parcelada em  2x ficara {} cada parcela '.format(preco,p3))
elif opcao == 4:
    parcelas = int(input('quantas parcelas'))
    juros = (preco*0.20)+preco
    vez = juros / parcelas
    print('sua compra de {} parcelada em  {}x ficara {} cada parcela '.format(preco,parcelas,vez))



