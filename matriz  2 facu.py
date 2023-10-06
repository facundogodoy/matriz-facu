buscaminas=[[0,0,1,0,0,0],
            [0,0,1,0,0,0],
            [1,0,0,0,1,0],
            [0,0,1,0,0,0],
            [0,0,0,1,0,0]]
usuario=[["-","-","-","-","-","-"],
        ["-","-","-","-","-","-"],
        ["-","-","-","-","-","-"],
        ["-","-","-","-","-","-"],
        ["-","-","-","-","-","-"]]
fila=0
columna=0

def mostrar_tablero(tablero):
    for f in enumerate (tablero):
        print(f)
        
print("bienvenido al buscaminas")
print("este es su tablero")
mostrar_tablero(usuario)

fila=int(input("que fila quieres ver ?"))
columna=int(input("que columna quieres ver?"))

if buscaminas[fila][columna]==1:
    usuario[fila][columna]="x"
    mostrar_tablero(usuario)
    print("explotaste pelotudo")
else:
    usuario[fila][columna]="-"
    mostrar_tablero(usuario)
    print("casi que explotas zapallo")