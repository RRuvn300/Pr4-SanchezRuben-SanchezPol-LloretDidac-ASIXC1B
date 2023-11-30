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


