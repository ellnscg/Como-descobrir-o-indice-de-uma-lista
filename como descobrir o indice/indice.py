#como descobrir o indice de uma lista?

#para isso vamos utilizar o i=lista.index("item")

produtos = ['tv', 'celular', 'tablet','mouse', 'teclado', 'geladeira', 'forno',]
estoque = [100, 150, 100, 120,70,180, 80]

#Nesse caso a lista é "pequena" para fins didaticos, mas essa lista poderia ter dezenas de milhares de produtos diferentes.
#E agora, como eu faço para descobrir a quantidade em estoque do produto geladeira?

i = produtos.index('geladeira')
qtde_estoque = estoque [i]

print('Quantidade em estoque da geladeira é de {}'.format(qtde_estoque))