"""
Pol Sánchez
Dídac Lloret
Rubén Sánchez
ASIXc1B
Programa que imprimeix un tauler d’escacs per pantalla. Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre ;-)
"""

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("⬜️", end=" ")
        else:
            print("⬛️", end=" ")
    print()
