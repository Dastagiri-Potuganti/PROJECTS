wallet=1200
print("MOBILE RECHAARGE SYSTEM")
while True:                                         
    print("1.Sim Brands\n2.Recharge Process\n3.check wallet balance\n4.Add wallet balance\n5.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("i.Jio\nii.Aitel\niii.VI\niv.Bsnl")
    elif ch==2:
        cho=int(input("Enter sim brand:"))
        #jio
        if cho==1:
            while True:
                ph=int(input("Enter your mobile number in integers:"))
                cnt=0
                while ph>0:
                    d=ph%10
                    cnt=cnt+1
                    ph=ph//10
                if cnt==10:
                    
                        print("Plans are:")
                        print("1.1gb packs\n2.2gb packs\n3.1.5 gb packs\n4.Yearly plans")
                        p=int(input("Enter your pack number:"))
                        #1gb
                        if p==1:
                            print("1.28 days-$290\n2.30 days-$320\n3.84 days-$700")
                            d=int(input("Choose number of days:"))
                            if wallet>290:
                                if d==1:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-290
                                
                            else:
                                print("Insufficient funds")
                            if wallet>320:
                                if d==2:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-320
                                
                            else:
                                print("Insufficient funds")
                            if wallet>700:
                                if d==3:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-700
                            else:
                                print("Insufficient funds")
                         
                        #2gb
                        elif p==2:
                            print("1.28 days-$350\n2.30 days-$390\n3.84 days-$900")
                            d=int(input("Choose number of days:"))
                            if wallet>350:
                                if d==1:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-350
                            else:
                                print("Insufficient funds")
                            if wallet>390:
                                if d==2:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-390
                            else:
                                print("Insufficient funds")
                            if wallet>900:
                                if d==3:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-900
                            else:
                                print("Insufficient funds")
                            
                        #1.5gb
                        elif p==3:
                            print("1.28 days-$320\n2.30 days-$360\n3.84 days-$820")
                            d=int(input("Choose number of days:"))
                            if wallet>320:
                                if d==1:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-320
                            else:
                                print("Insufficient funds")
                            if wallet>360:
                               if d==2:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-360
                            else:
                                print("Insufficient funds")
                            if wallet>820:
                                if d==3:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-820
                            else:
                                print("Insufficient funds")
                            
                        #yearly plans
                        elif p==4:
                            print("1.1gb pack-$2900\n2.1.5gb pack-$3300\n3.2gb pack-$3600")
                            d=int(input("Choose number of days:"))
                            if wallet>2900:
                                if d==1:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-2900
                            else:
                                print("Insufficient funds")
                            if wallet>3300:
                               if d==2:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-3300
                            else:
                                print("Insufficient funds")
                            if wallet>3600:
                                if d==3:
                                    print("You have completed Your recharge plan")
                                    wallet=wallet-3600
                            else:
                                print("Insufficient funds")
                            
                        else:
                            print("Choose Correct plan")
                        break
                else:
                    print("Enter Correct number")
        #Airtel
        elif cho==2:
            ph=int(input("Enter your mobile number:"))
            cnt=0
            while ph>0:
                d=ph%10
                cnt=cnt+1
                ph=ph//10
            if cnt==10:
                print("Plans are:")
                print("1.1gb packs\n2.2gb packs\n3.1.5 gb packs\n4.Yearly plans")
                p=int(input("Enter your pack number:"))
                #1gb plans
                if p==1:
                   print("No Plans available")
                #2gb plans
                elif p==2:
                    print("1.28 days-$350\n2.56 days-$650\n3.84 days-$980")
                    d=int(input("Choose number of days:"))
                    if wallet>=350:
                        if d==1:
                            print("You have completed Your recharge plan")
                            wallet=wallet-350
                    else:
                        print("Insufficient funds")
                    if wallet>=650:
                        if d==2:
                            print("You have completed Your recharge plan")
                            wallet=wallet-650
                    else:
                        print("Insufficient funds")
                    if wallet>=980:
                        if d==3:
                            print("You have completed Your recharge plan")
                            wallet=wallet-980
                    else:
                        print("Insufficient funds")
                #1.5gb plans
                elif p==3:
                    print("1.28 days-$300\n2.30 days-$320\n3.84 days-$860")
                    d=int(input("Choose number of days:"))
                    if wallet>300:
                        if d==1:
                            print("You have completed Your recharge plan")
                            wallet=wallet-300
                    else:
                        print("Insufficient funds")
                    if wallet>320:
                       if d==2:
                            print("You have completed Your recharge plan")
                            wallet=wallet-320
                    else:
                        print("Insufficient funds")
                    if wallet>860:
                        if d==3:
                            print("You have completed Your recharge plan")
                            wallet=wallet-860
                    else:
                        print("Insufficient funds")
                #Yearly plans
                elif p==4:
                    print("1.2gb pack(unlimited 5g +2.5gb data)-$4000\n2.365 days pack(abroad-5gb)-$5000")
                    d=int(input("Choose number of days:"))
                    if wallet>4000:
                        if d==1:
                            print("You have completed Your recharge plan")
                            wallet=wallet-4000
                    else:
                        print("Insufficient funds")
                    if wallet>5000:
                       if d==2:
                            print("You have completed Your recharge plan")
                            wallet=wallet-5000
                    else:
                        print("Insufficient funds")
                else:
                    print("Choose Correct plan") 
            else:
                print("Enter Correct number")
        #VI
        elif cho==3:
            ph=int(input("Enter your mobile number:"))
            cnt=0
            while ph>0:
                d=ph%10
                cnt=cnt+1
                ph=ph//10
            if cnt==10:
                print("Plans are:")
                print("1.1gb packs\n2.2gb packs\n3.1.5 gb packs")
                p=int(input("Enter your pack number:"))
                #1gb plan
                if p==1:
                    print("1.28 days-$150\n2.28 days with 5g unlimited+VI Movies&TV-$300\n3.28 days=1gb/day+1gb-$340")
                    d=int(input("Choose number of days:"))
                    if wallet>150:
                        if d==1:
                            print("You have completed Your recharge plan")
                            wallet=wallet-150
                    else:
                        print("Insufficient funds")
                    if wallet>300:
                        if d==2:
                            print("You have completed Your recharge plan")
                            wallet=wallet-300
                    else:
                        print("Insufficient funds")
                    if wallet>340:
                        if d==3:
                            print("You have completed Your recharge plan")
                            wallet=wallet-340
                    else:
                        print("Insufficient funds")
                #2gb plans
                elif p==2:
                    print("1.365days(VI Hero Unlimited)-$3600\n2.365 days(Extra 50gb+1yr jio hotstar)-$3700\n3.365days(Exclusive-jio hotstar+amazon prime)-$4000")
                    d=int(input("Choose number of days:"))
                    if wallet>3600:
                        if d==1:
                            print("You have completed Your recharge plan")
                            wallet=wallet-3600
                    else:
                        print("Insufficient funds")
                    if wallet>3700:
                        if d==2:
                            print("You have completed Your recharge plan")
                            wallet=wallet-3700
                    else:
                        print("Insufficient funds")
                    if wallet>4000:
                        if d==3:
                            print("You have completed Your recharge plan")
                            wallet=wallet-4000
                    else:
                        print("Insufficient funds")
                #1.5gb plan
                elif p==3:
                    print("1.28 days-$350\n2.56days-$580\n3.84 days-$860")
                    d=int(input("Choose number of days:"))
                    if wallet>350:
                        if d==1:
                            print("You have completed Your recharge plan")
                            wallet=wallet-350
                    else:
                        print("Insufficient funds")
                    if wallet>580:
                       if d==2:
                            print("You have completed Your recharge plan")
                            wallet=wallet-580
                    else:
                        print("Insufficient funds")
                    if wallet>860:
                        if d==3:
                            print("You have completed Your recharge plan")
                            wallet=wallet-860
                    else:
                        print("Insufficient funds")
                else:
                    print("Choose Correct plan") 
            else:
                print("Enter Correct number")
        #BSNL
        elif cho==4:
            ph=int(input("Enter your mobile number:"))
            cnt=0
            while ph>0:
                d=ph%10
                cnt=cnt+1
                ph=ph//10
            if cnt==10:
                print("Plans are:")
                print("1.calling packs\n2.2gb packs\n3.1.5 gb packs\n4.Yearly plans")
                p=int(input("Enter your pack number:"))
                #Calling packs
                if p==1:
                    print("1.14 days-$100\n2.22 days-$110\n3.24 days-$150")
                    d=int(input("Choose number of days:"))
                    if wallet>100:
                        if d==1:
                            print("You have completed Your recharge plan")
                            wallet=wallet-100
                    else:
                        print("Insufficient funds")
                    if wallet>110:
                        if d==2:
                            print("You have completed Your recharge plan")
                            wallet=wallet-110
                    else:
                        print("Insufficient funds")
                    if wallet>150:
                        if d==3:
                            print("You have completed Your recharge plan")
                            wallet=wallet-150
                    else:
                        print("Insufficient funds")
                #2gb plans
                elif p==2:
                    print("1.28 days-$200\n2.30 days-$230\n3.150 days-$1000")
                    d=int(input("Choose number of days:"))
                    if wallet>200:
                        if d==1:
                            print("You have completed Your recharge plan")
                            wallet=wallet-200
                    else:
                        print("Insufficient funds")
                    if wallet>230:
                        if d==2:
                            print("You have completed Your recharge plan")
                            wallet=wallet-230
                    else:
                        print("Insufficient funds")
                    if wallet>1000:
                        if d==3:
                            print("You have completed Your recharge plan")
                            wallet=wallet-1000
                    else:
                        print("Insufficient funds")
                #1.5gb plans
                elif p==3:
                    print("1.330 days-$2000")
                    d=int(input("Choose number of days:"))
                    if wallet>2000:
                        if d==1:
                            print("You have completed Your recharge plan")
                            wallet=wallet-2000
                    else:
                        print("Insufficient funds")
                #yearly plans
                elif p==4:
                    print("1.2gb pack(Unlimited voice calls+unlimited data-$2400\n2.2.6gb pack-$2630\n3.3gb pack-$2800")
                    d=int(input("Choose number of days:"))
                    if wallet>2400:
                        if d==1:
                            print("You have completed Your recharge plan")
                            wallet=wallet-2400
                    else:
                        print("Insufficient funds")
                    if wallet>2630:
                       if d==2:
                            print("You have completed Your recharge plan")
                            wallet=wallet-2630
                    else:
                        print("Insufficient funds")
                    if wallet>2800:
                        if d==3:
                            print("You have completed Your recharge plan")
                            wallet=wallet-2800
                    else:
                        print("Insufficient funds")

                else:
                    print("Choose Correct plan") 
            else:
                print("Enter Correct number")
        elif cho==5:
            print("Invaild sim brand")
    elif ch==3:
        print('Your balance is:',wallet)
    elif ch==4:
        bal=int(input("Enter add balance amount"))
        wallet=wallet+bal
        print("Your balance is:",wallet)
    elif ch==5:
        print("Exiting")
        break
    else:
        print("Choose correct option")
