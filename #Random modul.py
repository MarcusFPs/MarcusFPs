#Random modul
import random
import string

#1. Generer et tilfældigt heltal mellem 1 og 100 og udskriv det.
random_number = random.randrange (1, 100)
print(random_number)
#2. Generer og udskriv en tilfældig flydende værdi mellem 0 og 1.
print(random.random())
#3. Lav en liste med navne på farver (f.eks. "rød", "blå", "grøn", osv.). Brug random‐modulen til at vælge en tilfældig farve #fra listen og udskriv den.
farvelist = ["Rød", "Blå", "Grøn", "Gul", "Orange"]
print(random.choice(farvelist)) 
#4. Simuler kast af en mønt. Brug random‐modulen til at generere enten "hoved" eller "kron" og udskriv resultatet.
kastmønt = ["Kron", "Hoved"]
print(random.choice(kastmønt)) 
#5. Skriv et program, der genererer et tilfældigt kodeord bestående af store bogstaver, små bogstaver og tal.

def generer_tilfældigt_kodeord(længde):
    karakterer = string.ascii_letters + string.digits
    kodeord = ''.join(random.choice(karakterer) for i in range(længde))
    return kodeord

#Angiv længden af det ønskede kodeord
længde = 12  # Du kan ændre dette til din ønskede længde

tilfældigt_kodeord = generer_tilfældigt_kodeord(længde)
print("Dit tilfældige kodeord er:", tilfældigt_kodeord)

#6. Skriv et program, der simulerer kast af en terning. Du skal tage imod antallet af kast som parameter og returnere en liste #med resultaterne af hvert kast.
antal_kast = int(input("Hvor mange kast vil du have? "))
resultater = [random.randint(1, 6) for i in range(antal_kast)]
print("resultater af kast ", resultater)
#7. Generer og udskriv en tilfældig dato i formatet "DD‐MM‐ÅÅÅÅ" (f.eks. "15‐09‐2023").
dato = random.randrange(1,31)
month = random.randrange(1,12)
year = random.randrange(1, 2023)
#8.Skriv et program, der genererer og udskriver et tilfældigt password bestående af en kombination af store bogstaver, små #bogstaver og tal. Lad brugeren angive længden af passwordet.

#9. Simuler et tilfældigt valg af en vinder blandt en liste med deltagere. Brug random‐modulen til at vælge en tilfældig #deltager fra listen og udskriv vinderen.