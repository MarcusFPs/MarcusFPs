#importering af turtle som t, så input kan starte med t
import turtle as t

#definering af antal kollonner, rækker og cirkelradius for at lave pladen
Kolonne = 7
Række = 6
Cirkelradius = 60

#her laver jeg et setup til skærmen, giver den koordinater samt titel og baggrundsfarve
Screen = t.Screen()
Screen.setup (500,500)
Screen.setworldcoordinates(-500, -500, 500, 500)
Screen.title("4 på stribe")
Screen.bgcolor("Light Blue")

#opretter lister for, felter, fyldte cirkeler, og jeg kunne ikke sammeligne koordinaterne, så jeg lavede en saperat liste hvor den runder op til de sidste 3 decimaler
felter = []
fyldte_cirkler = []
rundet_cirkler = []

#her laver jeg en funktion om at den skal lave min plade
def get_felt(xpos, ypos): return felter[(xpos*ypos-1)]
t.speed(0)
for x in range(Kolonne):
    for y in range(Række):
       
       #siden at worldmappet har en længde og bredde på 1000, så bliver der divideret med antal cirkeler per række og kolonne, så hvis jeg vil have en større plade var det muligt
        delty = 1000/Række
        deltx = 1000/Kolonne
        
        #her får jeg den til at tegne pladen og fylder dem med hvid, og laver dem som den defineret cirkelradius
        t.penup()
        t.goto(deltx*x -440, delty*y -465)
        tilt = [deltx*x -440, delty*y -465 + Cirkelradius/2]
        felter.append(tilt)
        t.pendown()
        t.fillcolor("White")
        t.begin_fill()
        t.circle(Cirkelradius)
        t.penup()
        t.end_fill()
        
#her sætter jeg den så den skifter mellem rød og blå via:
#true = rød
#false = blå
skift = True

#her opretter jeg funktion til at klikke på cirklen, og laver en float med en mindste afstand så man skal klikke på den.
def fyld_felt(x, y):
    global skift
    nær_af = None
    cirkel = None
    mindste_afstand = float('inf')

    for i in range(len(felter)):

#her laver jeg nogen list, med en current på x og y aksen, så man ikke kan sætte den på en tilfældig y-akse, men nederst.
        current_list = felter[i]
        current_x = current_list[0]
        current_y = current_list[1]

#sætter distance for at clicke på cirklen.
        distance = ((x - current_x)**2 + (y - current_y)**2)**0.5

#Her gør jeg det muligt for at klikke på enkelte cirkler og herefter give et signal til hvis cirklen ikke allerede har en farve
        if distance < mindste_afstand and distance < 60 and not current_list in fyldte_cirkler:
            if current_y == -435:
                afrund_x = round(current_x, 3)
                afrund_y = round(current_y, 3)
                mindste_afstand = distance
                cirkel = current_list
                nær_af = [afrund_x, afrund_y]
                #Den afrunder x- og y-aksen til hele decimaler så det bliver den cirkel som bliver clicket på.
            else:
                neden_under = [round(current_x, 3), round(current_y - 166.666666666666663, 3)]
                if neden_under in rundet_cirkler:
                   afrund_x = round(current_x, 3)
                   afrund_y = round(current_y, 3)
                   mindste_afstand = distance
                   cirkel = current_list
                   nær_af = [afrund_x, afrund_y]

#her begynder jeg en funktion til at farve cirklen
    if cirkel is not None:
        fyldte_cirkler.append(cirkel)
        rundet_cirkler.append(nær_af)
        print(cirkel)
        t.goto(cirkel[0], cirkel[1] - 30)
    
    #her skifter den farven til blå eller rød and på om skift er true eller false
        if skift == True:
            t.fillcolor("blue")
        else:
            t.fillcolor("Red")
        t.begin_fill()
        t.pendown()
        t.circle(60)
        t.penup()
        t.end_fill()
        if skift == True:
        
            skift = False
        elif skift == False:
            skift = True

#her gør jeg det muligt og klikke på cirklen
Screen.onclick(fyld_felt)
t.mainloop() 


