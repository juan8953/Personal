diccionario={"letras":["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],"numero":[1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]}
str_p1=str(input("Ingrese la palabra número uno "))
str_p2=str(input("Ingrese la palabra número dos "))
str_1 = str_p1.upper()
str_2 = str_p2.upper()
def busqueda(str_p1,str_p2):
    int_pt=0
    for i in(str_1):
        p=0
        for j in (diccionario["letras"]):
            if i==j:
                int_pt=int_pt+diccionario["numero"][p]
                break
            else:
                p+=1
    print(int_pt)
print(busqueda(str_p1,str_p2))