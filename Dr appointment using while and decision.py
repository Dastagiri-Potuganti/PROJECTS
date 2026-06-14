Dr1='1.DR.Ramesh-Sr.Homeopathy Doctor'
Dr2='2.Dr.Thanuja-Jr Homeopathy Doctor'
Dr3='3.Dr.Sai Sritha- Jr Homeopathy Doctor'
while True:
    print("\n1.Select Doctors\n2.Patient Appointment\n3.Exit")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        print("Doctors Available are:")
        print('Dr.Ramesh-Sr.Homeopathy Doctor')
        print('2.Dr.Thanuja-Jr Homeopathy Doctor')
        print('3.Dr.Sai Sritha- Jr Homeopathy Doctor')
    elif ch==2:
        print("Welcome for Patient Appointment")
        p_name=input("Enter Your name:")
        dr_ch=int(input("Choose a doctor:"))
        if dr_ch==1:
            print(p_name,"appointment is approved for the doctor ",Dr1)
        elif dr_ch==2:
            print("Your appointment is approved for the doctor",Dr2)
        elif dr_ch==3:
            print("Your appointment is approved for the doctor",Dr3)
        else:
            print("Choose an available doctor:")
    elif ch==3:
        print("Appointments Over")
        break
    else:
        print("Invalid choice")
    
