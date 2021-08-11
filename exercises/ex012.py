p = float(input('Preço: R$'))
d = p*(5/100)
f = p-d
print('O produto de R${:.2f} com desconto de 5% sai a R${:.2f}'.format(p,f))