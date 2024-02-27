import random
#Importerer Random og spørger hvor mange runder spilleren vil have, samt hvor mange point spilleren og computeren har
antal_runder = int(input("Hvor mange runder vil du spille? "))

spiller_point = 0
computer_point = 0

#Her er selve koden, det starter med at  ens input bliver antal runder, og som kører runden rundt. herud over, spørger jeg om sten saks papir, 
# og så vælger computeren en random en
#så laver jeg en if for hvad computeren valgte og hvad der skal ske ved de forskellige input. samt et point system
for _ in range(antal_runder):
    valg = input("Vælg Sten, Saks eller Papir: ").lower()
    computer_valg = random.choice(["sten", "saks", "papir"])
    print(f"Computeren valgte: {computer_valg}")

    if valg == computer_valg:
        print("Uafgjort!")
    elif (valg == "sten" and computer_valg == "saks") or \
         (valg == "saks" and computer_valg == "papir") or \
         (valg == "papir" and computer_valg == "sten"):
        print("Spilleren vinder denne runde!")
        spiller_point += 1
    else:
        print("Computeren vinder denne runde!")
        computer_point += 1
#her får jeg den til at printe mængden af point
print(f"\nSlutresultat:\nSpiller: {spiller_point} point\nComputer: {computer_point} point")

#og her spørger jeg om spilleren vil spille igen.
spil_igen = input("Vil du spille igen? (ja/nej): ").lower()
if spil_igen == "ja":
    exec(open(__file__).read())
