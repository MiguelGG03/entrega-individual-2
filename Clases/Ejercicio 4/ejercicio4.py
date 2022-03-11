#VECTOR
t=[3,4,8,9,14,21,18,22,1]

cont=0
max=0

letras=[]
h=int(len(t))

for j in range(0,h):
    if(t[j:j+1]!=' '):
        letras.append(t[j:j+1])
        max=max+1

#max es la longitud de la lista sin blancos

while(letras[cont]==letras[max-1-cont] and cont<max/2):
    print(str(cont)+letras[cont]+letras[max-1-cont])
    cont=cont+1

if(cont==int(max/2)):
    print('Es palindromo '+str(t))
else:
    print('No es palidromo '+str(t))