"""
Pol Sánchez
Dídac Lloret
Rubén Sánchez
ASIXc1B
Programa que mostra un triangle amb nombres a les cantonades.  Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
"""

try:
    #Definim el valor de sumsenar i sumparell a 0 i posem el input del número.
    sumsenar = 0
    sumparell = 0
    num = int(input("Escriu un número:"))
    #creem un bucle en el que es comproba número a número si es parell o senar i fem que depenen el que sigui es sumi a un lloc o al altre.
    for i in range (num):
        if i % 2 == 0:
            sumparell += i
        else:
            sumsenar += i

    print(f"La suma de números parells és {sumparell} y la suma de números imparells es {sumsenar}")
except:
    print("Hi ha hagut un error proba a escriure un número sencer")