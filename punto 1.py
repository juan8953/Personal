l_paises = ['Colombia','Mexico','Turquia','Polonia','serbia','dinamarca','holanda','Alemania']
l_paises1=""
for i in range(0,8,1):
    l_paises1+=l_paises[i].capitalize()
    l_paises1+="\n"
archi1=open("datos.txt","w")
with open('datos.txt', 'w') as temp_file:
    for item in l_paises1:
        temp_file.write("%s" % item)
file = open('datos.txt', 'r')
print(file.read())