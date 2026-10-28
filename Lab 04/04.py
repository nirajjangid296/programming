hour=int(input("hours: "))
minute=int(input("minutes: "))
m=minute+15
h=hour+(m//60)
if m>59:
    if m%60<10:
        print(h,":","0"+str(m%60))
    else:
        print(h,":",m%60)
else:
    print(h,":",m)