budget=int(input("enter your budget: "))
season=input("enter the season: ")
if season=="summer":
   if budget<=100:
       place="Bulgaria"
       spent=budget*0.3
   elif budget<=1000:
         place="Balkans"
         spent=budget*0.4
   else:
        place="Europe"
        spent=budget*0.9
elif season=="winter":
    if budget<=100:
        place="Bulgaria"
        spent=budget*0.7
    elif budget<=1000:
          place="Balkans"
          spent=budget*0.8
    else:
         place="Europe"
         spent=budget*0.9
print("Place: ",place)
print("budget spent : ",spent)