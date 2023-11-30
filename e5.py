"""
Pol Sánchez
Dídac Lloret
Rubén Sánchez
ASIX1cB
Programa que realitza la multiplicació, de dos nombres sencers,  mitjançant sumes
"""
try:
    primer_numero = int(input("Escriu el primer nombre: "))
    segon_numero = int(input("Escriu el segon nombre: "))
    resultat = 0

    for i in range (segon_numero):
        resultat += primer_numero
        print (f"{primer_numero} + {resultat} = {resultat}")

except ValueError:
    print("Introdueix un nombre sencer només")