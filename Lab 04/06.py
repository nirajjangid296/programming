holidays=int(input("enter no. of holidays: "))
workdays=365-holidays
game=holidays*127+workdays*63
diff=30000-game
if game<30000:
    print("Tom can sleep well")
    print(diff)
else:
    print("Tom can't sleep well")
    