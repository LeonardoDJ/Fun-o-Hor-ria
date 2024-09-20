So = float(input("Coloque um número de valor inicial da formula: S = S° + v.t "))
V = float(input("Coloque a velocidade que deseja da formula: S = S° + v.t "))
T = float(input("Coloque um tempo(hora) da formula: S = S° + v.t "))

def funcao(So, V, T):
    return (So + V * T)

print("Total de KM percorrido é de",  funcao(So, V, T))