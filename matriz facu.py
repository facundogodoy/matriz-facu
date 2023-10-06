matriz=[[1,2],
       [4,5],
       [7,8],
       ]
fila=0
columna=0
fila=int(input("que fila quieres ver ?"))
columna=int(input("que columna quieres ver?"))
print("su num es",matriz[fila][columna])
op=input("quieres cambiar de num? si/no")
if op == "si":
    num=int(input("ingrese su num"))
    matriz[fila][columna]=num
    
for fil in range (1,3):
    print(matriz[fila])
