def ist_teilbar(x,y):
    if x == y:
        print(str(x) +" und " + str(y) + " sind die selbe Zahl!")
    else:
        if y == 0:
            print("Es it nicht möglich durch 0 zu teilen!")
        else:
            if x%y == 0:
                print(str(x) + " ist durch " + str(y) + " teilbar")
            else:
                    print(str(x) + " ist nicht durch " + str(y) + " teilbar")
            
