"""

Pol Sánchez
Dídac Lloret
Rubén Sánchez
ASIXc1B
PPrograma que mostra per pantalla la suma de tots els nombres senars i de tots els nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.

"""


try:

    sumsenar = 0
    sumparell = 0
    num = int(input("Escriu un número:"))

    for i in range (num):
        if i % 2 == 0:
            sumparell += i
        else:
            sumsenar += i

    print(f"La suma de números parells és {sumparell} y la suma de números imparells es {sumsenar}")
except:
    print("Hi ha hagut un error proba a escriure un número sencer")