print('olá cliente sou o Assistente virtual do Assái atacadista, vamos iniciar nossa pesquisa de satisfação')
nome=input('para iniciarmos me diga qual o seu primeiro nome, por gentileza. ')
idade=input('agora qual é a sua idade ')
print('muito obrigado',nome,'por suas informações agora vamos para a proxima etapa.')

organizacao=input('o que você achou da organização do assaí atacadista? ')

limpeza=input('e sobre a limpeza o que você achou? ')

qprodutos=input ('e sobre a qualidade dos produtos ? de 0 a 10 informe o que você achou da variedade dos mesmos')    #qualidade dos produtos

print('perfeito',nome, 'agora que sei sua opinião em algumas de nossas pesquisas nos informe qual produto vocẽ mais se surpreendeu em vê em nossa loja. ')

sproduto=input('') #surpresa de pproduto

print('agora para terminar irei informar todos as respostas para você confirmar comigo tudo bem?')
print('suas respostas foram:{} {} na organização você colocou:{} na limpeza você colocou: {} e na qualidade dos nossos produtos você colocou {}'.format(nome,idade,organizacao,limpeza,qprodutos))

n1=int(input('para finalizar informe um numero qualquer'))
n2=int(input('agora apenas mais um numero para confirmarmos sua participação'))

print('o resultado dos numeros a cima foi',int(n1)+(n2))