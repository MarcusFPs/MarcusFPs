import math
print("Trekant udregner")

a = 0
b = 0
c = 0
A = 0
B = 0
C = 0
Omkreds = 0
Højde_a = 0
Areal = 0
Median_a = 0
Median_b = 0
Median_c = 0
Semiperimeter = 0
In_radius = 0
Circumradius = 0

while True:
    sss = input("Kender du alle sider i trekanten? Ja/Nej: ")
    if sss.lower() == "ja":
        a = int(input("Hvor lang er siden a? "))
        if a < 0:
            print("Siden a kan ikke være negativ. Prøv igen.")
            continue
        b = int(input("Hvor lang er siden b? "))
        if b < 0:
            print("Siden b kan ikke være negativ. Prøv igen.")
            continue
        c = int(input("Hvor lang er siden c? "))
        if c < 0:
            print("Siden c kan ikke være negativ. Prøv igen.")
            continue

        C = (a**2 + b**2 - c**2) / (2 * a * b)
        B = (a**2 + c**2 - b**2) / (2 * a * c)
        A = 180 - C - B
        
        Omkreds = a + b + c
        Højde_a = a * math.sin(B)
        Areal = 1/2 * Højde_a * a
        
        Median_a = 0.5 * math.sqrt(2 * b**2 + 2 * c**2 - a**2)
        Median_b = 0.5 * math.sqrt(2 * a**2 + 2 * c**2 - b**2)
        Median_c = 0.5 * math.sqrt(2 * a**2 + 2 * b**2 - c**2)

        Semiperimeter = Højde_a/2
        In_radius =Areal/Semiperimeter
        Circumradius = a / (2*math.sin(A))

        print(f"Dine sider har Maalende: a,{a}, b,{b}, c,{c}")
        print(f"Dine vinkler har Maalende: A,{A}, B,{B}, C,{C}")
        print(f"Din omkreds er: {Omkreds}")
        print(f"Din højde er: {Højde_a}")
        print(f"Dit areal er: {Areal}")
        print(f"Dine medianer er: a,{Median_a}, b, {Median_b}, c, {Median_c}")
        print(f"Din Inradius er: {In_radius}")
        print(f"Din circumradius er: {Circumradius}")
        break

    sas = input("Kender du 2 sider og den inkluderet vinkel? (Ja)(Nej)")
    if sas.lower() == "ja":
        a = int(input("Hvor lang er siden a? "))
        if a < 0:
            print("Siden a kan ikke være negativ. Prøv igen.")
            continue
        b = int(input("Hvor lang er siden b? "))
        if b < 0:
            print("Siden b kan ikke være negativ. Prøv igen.")
            continue
        a = int(input("Hvor lang er siden c? "))
        if c < 0:
            print("Siden c kan ikke være negativ. Prøv igen.")
            continue        

        A = int(input("Hvor mange grader har A?"))
        if A < 0:
            print("Vinkel A kan ikke være negativ. Prøv igen.")
            continue

        B = int(input("Hvor mange grader har B?"))
        if B < 0:
            print("Vinkel B kan ikke være negativ. Prøv igen.")
            continue

        C = int(input("Hvor mange grader har C?"))
        if C < 0:
            print("Vinkel C kan ikke være negativ. Prøv igen.")
            continue

        if a > 0 and b > 0:
            c = math.sqrt(a**2 + b**2)
        elif b > 0 and c > 0:
            a = math.sqrt(c**2 - b**2)
        elif a > 0 and c > 0:
            b = math.sqrt(c**2 - a**2)

        C = (a**2 + b**2 - c**2) / (2 * a * b)
        B = (a**2 + c**2 - b**2) / (2 * a * c)
        A = 180 - C - B

        Omkreds = a + b + c
        Højde_a = a * math.sin(B)
        Areal = 1/2 * Højde_a * a
        
        Median_a = 0.5 * math.sqrt(2 * b**2 + 2 * c**2 - a**2)
        Median_b = 0.5 * math.sqrt(2 * a**2 + 2 * c**2 - b**2)
        Median_c = 0.5 * math.sqrt(2 * a**2 + 2 * b**2 - c**2)

        Semiperimeter = Omkreds/2
        In_radius =Areal/Semiperimeter
        Circumradius = a / (2*math.sin(A))

        print(f"Dine sider har Maalende: a,{a}, b,{b}, c,{c}")
        print(f"Dine vinkler har Maalende: A,{A}, B,{B}, C,{C}")
        print(f"Din omkreds er: {Omkreds}")
        print(f"Din højde er: {Højde_a}")
        print(f"Dit areal er: {Areal}")
        print(f"Dine medianer er: a,{Median_a}, b, {Median_b}, c, {Median_c}")
        print(f"Din Inradius er: {In_radius}")
        print(f"Din circumradius er: {Circumradius}")
        break






    asa = input("Kender du 2 vinkler og den inkludere side? (Ja)(Nej)")
    sss = input("Kender du alle sider i trekanten? Ja/Nej: ")
    if sss.lower() == "ja":
        a = int(input("Hvor lang er siden a? "))
        if a < 0:
            print("Siden a kan ikke være negativ. Prøv igen.")
            continue
        b = int(input("Hvor lang er siden b? "))
        if b < 0:
            print("Siden b kan ikke være negativ. Prøv igen.")
            continue
        c = int(input("Hvor lang er siden c? "))
        if c < 0:
            print("Siden c kan ikke være negativ. Prøv igen.")
            continue





    aas = input("Kender du 2 vinkler og en side der ikke er inkluderet ned den? (Ja)(Nej)")
    sss = input("Kender du alle sider i trekanten? Ja/Nej: ")
    if sss.lower() == "ja":
        a = int(input("Hvor lang er siden a? "))
        if a < 0:
            print("Siden a kan ikke være negativ. Prøv igen.")
            continue
        b = int(input("Hvor lang er siden b? "))
        if b < 0:
            print("Siden b kan ikke være negativ. Prøv igen.")
            continue
        c = int(input("Hvor lang er siden c? "))
        if c < 0:
            print("Siden c kan ikke være negativ. Prøv igen.")
            continue