def mario(Num = 3):
    str_block1=''
    for i in range(Num):
        str_block='   '
        for j in range(i+1):
            str_block = str_block+'#'
        print(str_block)
    while Num == 3:
        for j in range(Num+1):
            str_block1+='#'
            for i in range(Num):
                str_block1+=' '
        print(str_block1)


mario(10)