def ejercicio5():    
    # Nº DE TAREAS
    N=10
    # TABLA DE RELACIONES 
    T=[[0,7],[7,9],[9,4],[4,6],[6,1],[1,3],[3,2],[5,8],[2,5]]
    # TABLA DE CONTROL
    u=[0,0,0,0,0,0,0,0,0,0]
    # TABLA DE RESULTADO
    r=[]
    # INICIALIZACION
    r.append(0)
    b=0
    u[0]=1
    # CALCULO CAMINO
    for i in range(0,9):
        j=T[0]
        x=0
        while(j[0]!=b and x<=N-3):
            x=x+1
            j=T[x]
        r.append(j[1])
        u[j[1]]=1
        b=j[1]
    # CONTROL DE CAMINO COMPLETO
    i=0
    while (i < 9 and u[i]==1):
        i=i+1
    # PRINT RESULTADO
    if (i<9):
        print("NO TIENE SOLUCION") 
    else:
        print("LA SOLUCION ES:") 
        print (r)