l_valores = [9,2, 9, 4, 5, 1, 8, 7, 8, 8, 9, 10,3]
def f_stat(l_valores):
    s_mean, s_median, s_STD = 0, 0, 0
    print(l_valores)
    int_contadora=0
    int_divisor=len(l_valores)
    for i in range (0,int_divisor):
        int_contadora+=l_valores[i]
    s_mean=int_contadora/int_divisor
    if int_divisor%2==0:
        s_median=((l_valores[(round((len(l_valores) / 2)+0.5))])+(l_valores[(round((len(l_valores) / 2)-1))]))/2
    else:
        s_median=l_valores[(round((len(l_valores) / 2)+0.5)-1)]
    return (f"la media es:{s_mean}, y la mediana es: {s_median}")
print(f_stat(l_valores))
    #función que toma una lista de valores y retorna el promedio, la mediana y la desviación estandar
    #:param l_valores: lista con los valores a utilizar
    #:return:
    #s_mean, s_median, s_STD = 0,0,0
    #TODO: realizar las modificaciones necesarias a partir de esta sección
    #return s_mean,s_median,s_STD
