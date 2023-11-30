"""
Pol Sánchez
Dídac Lloret
Rubén Sánchez
1-B
Programa que mostra un triangle amb nombres a les cantonades.  Cal demanar quina alçada ha de tenir el triangle. Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
"""
cont = 0


n = int (input("Introduce el número de filas: "))

if n < 2 or n > 9:
    print("entre 2 y 9")
    exit()

for i in range (1, 1 + n):
  cont = cont + 1
  print(" ")
  for j in range(1, i + 1):
     print(cont, " ", end=" ")


