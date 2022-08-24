
def f_calBin (s_num):
    s_residuo=0
    list=[]
    while s_num!=0:
        s_residuo =s_num % 2
        s_num=s_num//2
        print(s_num)

        list.append(s_residuo)
    print(list)
    idx = len(list) - 1
    newList = []
    while (idx >= 0):
        newList.append(list[idx])
        idx = idx - 1

    print(newList)



    '''
    Calculadora que permite encontrar la representación en binario de un número entero o decimal que ingresa por parametro
    :param s_num: número que se desea convertir a binario int o float
    :return: valor número en binario
    '''

    #TODO: escribir la sección del codigo para las conversiones
    #NOTA: puede hacer uso de tantas funciones como necesite (diseñadas por el estudiante)
    # #deben asignal el valor binario en esta variable
    return s_bin

print(f_calBin(126))
