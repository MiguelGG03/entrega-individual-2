def ejercicio6():
    
    t=[4,3,8,9,7,6,5,2,1]
    print("Tabla inicial:")
    print(t)

    max=t[0]
    ini=0
    cont=1
    h=int(len(t))

    for i in range(1,h):
        if(t[i]<=max):
            t[i-1]=t[i]
        else:
            t[i-1]=max
            max=t[i]
            print("Segmento "+str(cont)+":")
            print(t[ini:i])
            ini=i
            cont=cont+1

    t[h-1]=max
    print("Segmento "+str(cont)+":")
    print(t[ini:h])

    print("Tabla ordenada:")
    print(t)