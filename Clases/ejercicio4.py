def ejercicio4():    
    #VECTOR

    t=[3,4,8,9,7,6,5,2,1]
    print("Tabla inicial:")
    print(t)

    tmp=0

    h=int(len(t))

    for i in range(1,h):
        tmp=t[i]
        j=i-1
        while(j>=0 and t[j]>=tmp):
           t[j+1]=t[j]
           j=j-1
        t[j+1]=tmp
    print("Tabla ordenada:")
    print(t)