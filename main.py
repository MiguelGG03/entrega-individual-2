from Clases.ejercicio4 import ejercicio4
from Clases.ejercicio5 import ejercicio5
from Clases.ejercicio6 import ejercicio6

def main():
    acabar=False
    while(acabar==False):
        seguir=str(input('Quieres seguir viendo ejercicios(S/N)?:'))    
        if(seguir=='s' or seguir=='S'):
            cual=str(input('Que ejercicio quieres ver (4,5,6)?:'))
            if(cual=='4'):
                print('Ejercicio 4:\n')
                ejercicio4()
            if(cual=='5'):
                print('Ejercicio 5:\n')
                ejercicio5()
            if(cual=='6'):
                print('Ejercicio 6:\n')
                ejercicio6()
        if(seguir=='n' or seguir=='N'):
            acabar=True
        else:
            print('Introduzca una N o una S')


if __name__=='__main__':
    main()