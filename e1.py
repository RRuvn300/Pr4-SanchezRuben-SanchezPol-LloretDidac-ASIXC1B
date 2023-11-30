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

try:
    numeros = input("Introdueix 10 nombres sencers separats per espais: ")
    numeros_lista = [int(num) for num in numeros.split()]

    for nombre in numeros_lista:
        if nombre > 0:
            positius += 1
        elif nombre < 0:
            negatius += 1
        else:
            zeros += 1

    print(f"\nResultats:\nPositius: {positius}\nNegatius: {negatius}\nZeros: {zeros}")

except ValueError:
    print("Has d'introduir 10 nombres sencers separats per espais.")


