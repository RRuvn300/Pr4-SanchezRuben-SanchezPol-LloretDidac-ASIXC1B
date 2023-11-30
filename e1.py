"""
Pol Sánchez
Dídac Lloret
Rubén Sánchez
1-b
Programa que demana a l'usuari la introducció de 10 nombres sencers (que també podrien ser 10000000 😱😳😈) i ha de mostrar, al final i per pantalla, quants són positius, quants negatius i quants zero.

"""
positius = 0
negatius = 0
zeros = 0

for i in range(10):
    try:
        nombre = int(input("Introdueix un nombre sencer: "))

        if nombre > 0:
            positius += 1
        elif nombre < 0:
            negatius += 1
        else:
            zeros += 1

    except ValueError:
        print("Has d'introduir un nombre sencer. Torna-ho a provar.")

print(f"\nResultats:\nPositius: {positius}\nNegatius: {negatius}\nZeros: {zeros}")

