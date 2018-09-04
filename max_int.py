num_int = int(input("Input a number: "))    # Do not change this line
max_int=0  # Búum til max_int breytuna.
if num_int<0:  #Þegar að talan er minni en núll prentast út talan.
    print(num_int)
else:              # Annars ef talan er stærri eða = 0, 
    while num_int>=0:       #Þá tekur talan gildið sem er stærra
        if num_int>max_int:   #Talan tekur alltaf stærsta gildið
            max_int=num_int   #Þangað til það kemur mínustala
        num_int = int(input("Input a number: "))
print("The maximum is", max_int)    # Do not change this line