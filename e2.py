"""
Pol Sánchez
Dídac Lloret
Rubén Sánchez
ASIXc1B
Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle. Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
"""

cont = 0

try:
    n = int (input("Introduce el número de filas: "))

    if n < 2 or n > 9:
        print("Entre 2 y 9")
        exit()

    for i in range(n):
            for j in range(i + 1):
                if i == n - 1 or (j == 0 or j == i):
                    print(f"{i + 1}", end = " ")
                else:
                    print(" ", end=" ")
            if i != n - 1:
                print()
except:
    print("!Escribe número entero¡")