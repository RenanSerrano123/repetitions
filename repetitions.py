lista=[]
soma=0.0
x=int(input())
for indice in range(1,x+1):
  r=int(input())
  if r>=0:
    lista.append(r)
    soma=soma+r
lista2=list(reversed(lista))
print(*lista2, sep = " ")
print(int(soma))