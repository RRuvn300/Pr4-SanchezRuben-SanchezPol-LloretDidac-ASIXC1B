altura = int(input("Escribe la altura de tu triangulo: "))
try:
    for i in range(altura):
        for j in range (1+1):
            if 1 == altura+1 or (j == 0 or j ==1):
                    print(f"{1+1}", end="")
            else:
                    print("", end="")
        if i != altura-1:
                print()
except:
    print("Escribe número entero")
