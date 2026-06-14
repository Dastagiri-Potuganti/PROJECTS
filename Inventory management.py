#login details
user_name='Dastagiri'
password='giri@2468'
item=['tomato','onion','ladyfinger','carrot','beetroot','drum stick','brinjal','beans','potato']
quantity=[30,35,10,20,15,10,20,10,10]
selling_price=[35,25,40,50,40,45,30,20,15]
cost_price=[25,20,30,40,35,40,25,10,10]
sales_amt=[0,0,0,0,0,0,0,0,0]
purchase_amt=[]
for q,c in zip(quantity,cost_price):
    b=q*c
    purchase_amt.append(b)
total_amt=0
for i in purchase_amt:
    total_amt=total_amt+i
total_sales=0
while True:
    print("1.Owner \n2.Customer")
    section=int(input("Enter login section number:"))
    #Owner login
    if section==1:
        #Login Criteria(owner)
        i=1
        while i<=3:
            u_n=input("Enter user name:")
            pw=input("Enter password:")
            if u_n==user_name and password==pw:
                print("Login Successful")
                break
            elif u_n!=user_name and password!=pw:
                print("Incorrect login details")
            elif u_n!=user_name:
                print("Incorrect username")
            elif pw!=password:
                print("Incorrect password")
            i=i+1
        else:
            print("You are not the owner")
            continue
        #Owner Menu
        while True:        
            print('1.Add item to inventory\n2.remove item\n3.update item\n4.view inventory\n5.view report\n6.exit')
            menu=int(input("Enter the menu number to enter:"))
            #Add item to inventory
            if menu==1:
                veg=input("Enter new vegetable name:")
                if veg in item:
                    print("Vegetable is already in the list")
                else:
                    q=float(input("Enter quantity in kg's:"))
                    sp=int(input("Enter selling price:"))
                    cp=int(input("Enter Original price:"))
                    item.append(veg)
                    quantity.append(q)
                    selling_price.append(sp)
                    cost_price.append(cp)
                    sales_amt.append(0)
                    print(veg,"is added to the shop")
            #Remove item from inventory
            elif menu==2:
                print("Removing item")
                veg=input("Enter vegetable to remove:")
                if veg in item:
                    idx=item.index(veg)
                    item.remove(item[idx])    
                    quantity.remove(quantity[idx])
                    selling_price.remove(selling_price[idx])
                    cost_price.remove(cost_price[idx])
                    sales_amt.remove(sales_amt[idx])
                    print(veg,"is removed from the shop")
                else:
                    print(veg,'is not available')
            #Update item in inventory
            elif menu==3:
                print("Updating item")
                veg=input("Enter the vegetable do you want to update:")
                #checking vegetable in the list
                if veg in item:
                    idx=item.index(veg)
                    print("1.quantity\n2.sellingprice\n3.costprice")
                    ch=int(input("Enter what do you want to update:"))
                    #Quantity Update
                    if ch==1:
                        qty=int(input("How many kg's do you want to add :"))
                        quantity[idx]=quantity[idx]+qty
                    #Selling price update
                    elif ch==2:
                        print("1.Increase selling price\n2.Decrease price")
                        c=int(input("What do you want to update in selling price:"))
                        #Sp increase
                        if c==1:
                            sp=int(input("How much do you want to increase selling price in rupees:"))
                            selling_price[idx]=selling_price[idx]+sp
                        #sp Decrease
                        elif c==2:
                            sp=int(input("How much do you want to decrease selling price in rupees:"))
                            selling_price[idx]=selling_price[idx]-sp
                        else:
                            print("Not possible")
                    #Cost price update
                    elif ch==3:
                         print("1.Increase selling price\n2.Decrease price")
                         c=int(input("What do you want to update in selling price:"))
                        #Cp increase
                         if c==1:
                            cp=int(input("How much do you want to increase cost price in rupees:"))
                            cost_price[idx]=cost_price[idx]+cp
                        #Cp Decrease
                         elif c==2:
                            cp=int(input("How much do you want to decrease cost price in rupees:"))
                            cost_price[idx]=cost_price[idx]-cp
                         else:
                            print("Not possible")
                    else:
                        print("Update is not possible")
                    print(veg,"is updated")
                else:
                    print(veg,"is not available in the list")
            #View inventory
            elif menu==4:
                print("item-","qty-","sp-","cp")
                for i,q,s,c in zip(item,quantity,selling_price,cost_price):
                    print(i,'-',q,'-',s,'-',c)
            #View Report
            elif menu==5:
                print("Viewing report")
                p=total_sales-total_amt
                if p>0:
                    print("Profit amount is :",p)
                else:
                    print("Loss amount is:",p)
                print("Items left")
                for i,q in zip(item,quantity):
                    print(i,q,"kg's")
                print("Item wise purchase amount remained")
                for i,p,s in zip(item,purchase_amt,sales_amt):
                    print(i,'--',p,'\-',' -',s,'\-')
                print("Sales per item:")
                for i,s in zip(item,sales_amt):
                    print(i,'--',s,'Rs')
            #Log out
            elif menu==6:
                print("Coming out from the owner's section")
                break
            #Indefined Menu
            else:
                print("Invalid menu number")
    #customer login    
    elif section==2:
        #Customer menu
        while True:
            print("1.Add cart\n2.Remove cart \n3.Modify cart \n4.view cart\n5.billing \n6.Exiting")
            ch=int(input("Enter the menu number:"))
            #Add cart
            if ch==1:
                for i in item:
                    print(i)
                cart=[]
                cart_qty=[]
                cart_price=[]
                while True:
                    veg=input("What vegtable do you want:")
                    if veg in item:
                        idx=item.index(veg)
                        q=float(input("How much quantity do you want:"))
                        if q<=quantity[idx]:
                            cart.append(veg)
                            cart_qty.append(q)
                            quantity[idx]=quantity[idx]-q
                            price=q*selling_price[idx]
                            cart_price.append(price)
                            sales_amt[idx]=price
                        else:
                            print("Out of stock")
                    else:
                        print("Item is not available in the store")
                    again=input("Do You want to add another item(yes/no) :")
                    if again=='no':
                           break
                    elif again=='yes':
                        continue
                    else:
                        print("Wrong input")
            #Remove from cart
            elif ch==2:
                vege=input("What vegetable do you want to remove from the cart:")
                if vege in cart:
                    ind=cart.index(vege)
                    cart.remove(cart[ind])
                    cart_price.remove(cart_price[ind])
                    cart_qty.remove(cart_qty[ind])
                else:
                    print(vege,'is not available in the cart')
            #Modify cart
            elif ch==3:
                vegs=input("Enter what item do you want to modify :")
                if vegs in cart:
                    print("1.Increase quantity\n2.Decrease Quantity")
                    iq=int(input("Enter what to do you want to do:"))
                    cid=cart.index(vegs)
                    if iq==1:
                        kg=float(input("How many kgs do you want to add:"))
                        s_p=cart_price[cid]//cart_qty[cid]
                        cart_qty[cid]=cart_qty[cid]+kg
                        cart_price[cid]=s_p*cart_qty[cid]
                    elif iq==2:
                         kg=float(input("How many kgs do you want to decrease:"))
                         s_p=cart_price[cid]//cart_qty[cid]
                         cart_qty[cid]=cart_qty[cid]-kg
                         cart_price[cid]=s_p*cart_qty[cid]
                    else:
                        print("Modify is not possible")
                else:
                    print("The",vegs,'is not in the cart')
            #View Cart
            elif ch==4:
                for c,q,p in zip(cart,cart_qty,cart_price):
                    print(c,'-',q,'kgs',p,'/-')
            #Billing Section
            elif ch==5:
                bill=0
                for rs in cart_price:
                    bill=bill+rs
                print("Your total amount to be paid is :",bill,'rupees')
                total_sales=total_sales+bill
                break
            #Exiting
            elif ch==6:
                print("Exiting")
                break
            else:
                print("Invalid Menu")
    else:#login incorrect number
        print("Invalid login number:")
    ch=input("Do you want to close the shop(yes/no):")
    if ch=='yes':
        print("Closing shop")
        break
