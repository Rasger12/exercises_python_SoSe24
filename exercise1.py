def hello():
    print("hello du typ!")
    

name = "Richard"
def mein_name(name, alter, ort):
    print("Hello "+ name + " und ich bin cool und " + alter + " Jahre alt und wohne in " + ort)


    
#mein_name("Richard", "18", "Berlin")

def mein_zahl(input, input2):
    zahl = input * input2
    return zahl
zahl = mein_zahl(3,4)
#print(zahl)
#print(mein_zahl(4,4))



def quadrat_funktion(x):
    x_quadrat = x**2
    print(x_quadrat)
    
#quadrat_funktion(2)

#def quadrat_funktion_neu(x):
    x_quadrat = x**2
    return x_quadrat
    
#print(quadrat_funktion_neu(2)*8)




#___________________
#Aufgabe

def cagr_berechnung(AK, EK, t):

    if AK <= 0 or t <= 0:
        
        return "Error! AK darf nicht <= 0 und t auch nicht!!"
    return (((EK/AK)**(1/t))-1)*100
AK= 120
t = 30
cagr= cagr_berechnung(100, 700, 30)
EK = AK * ( cagr/100)**t

print(EK)
print(cagr)
            
    



