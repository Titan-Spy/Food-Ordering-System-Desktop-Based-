from tkinter import *
# from typing import final
from PIL import Image, ImageTk
from tkinter import messagebox
import math,random 
import datetime
from pdf_mail import sendpdf
from fpdf import FPDF
import mysql.connector as mc
from mysql.connector import DatabaseError
from mysql.connector.errors import DataError, Error
import re


#This all function is used to show information of fooditems with pop-up message when Admin will click on the particular fooditem
def btn_is_clicked():
    messagebox.showinfo("ALOO TIKKI BURGER", "It consists of a toasted bun with a potato patty topped fresh tomato,and tandoori Mayo!")

def btn_is_clicked2():
    messagebox.showinfo("VEGGIE BURGER", "It consists of a fried patty of ground vegetables, with lettuce,ketchup and mayo in a wholewheat bun!")

def btn_is_clicked3():
    messagebox.showinfo("CHICKEN BURGER", "Crispy seasoned chicken breast, topped with melted cheese and piled on wholewheat bun with onion, lettuce, tomato and garlic mayo!")

def btn_is_clicked5():
    messagebox.showinfo("CHICKEN POPCORN", "It consists of small, bite-sized pieces of chicken breast that have been breaded and fried!")

def btn_is_clicked4():
    messagebox.showinfo("FRIES", "These are thin, salted slices of deep fried potatoes served at room temperature!")

def btn_is_clicked6():
    messagebox.showinfo("COLD mojito", "It is a beverage served chilled and includes cream,coco powder or mojito beans!")

def btn_is_clicked7():
    messagebox.showinfo("COLD DRINKS", "750ml of COKE,SPRITE,PEPSI,MOUNTAIN DEW,FANTA,APPY FIZ ETC. ask the counter for available options!")

def btn_is_clicked8():
    messagebox.showinfo("ICE CREAM FLOAT", "IT is a chilled beverage that consists of ice cream in either COKE,SPRITE OR FANTA!")

def btn_is_clicked9():
    messagebox.showinfo("MOJITO", "It is a chilled combination of sweetness,citrus and herbaceous mint flavors and consists of lime juice,soda water,and mint!")

def btn_is_clicked10():
    messagebox.showinfo("ICE CREAM", "200ml of vanilla or strawberry ice cream served in cup or choco cone with customizable toppings!")

user_entry_login = []
user_entry_register = []
mytuple = tuple(user_entry_register)
# user_entry_login = []
food_items = []

#This function is used to clear all content(quantity) of fooitems when Admin will clear on clear button  
def clear_entry():
    value1.set(0)
    value2.set(0)
    value3.set(0)
    value4.set(0)
    value5.set(0)
    value6.set(0)
    value7.set(0)
    value8.set(0)
    value9.set(0)
    value10.set(0)
    Lbl_bill.pack_forget()
    return()


#This function is used to show the total amount of selected fooditems when admin will click on Total Button 
def calculate_bill():
    global Lbl_bill
    aloo_tikki_burger=entry_atburger.get()
    veggie_burger=entry_vegburger.get()
    chicken_burger=entry_chickenburger.get()
    fries=entry_fries.get()
    chicken_popcorn=entry_chickenpopcorn.get()
    cold_mojito=entry_coldcoffee.get()
    cold_drink=entry_colddrink.get()
    icecream_float=entry_float.get()
    mojito=entry_mojito.get()
    icecream=entry_icecream.get()
    total=((int(aloo_tikki_burger)*30)+(int(veggie_burger)*50)+(int(chicken_burger)*70)+(int(fries)*40)+(int(chicken_popcorn)*70)+(int(cold_mojito)*50)+(int(cold_drink)*40)+(int(icecream_float)*50)+(int(mojito)*40)+(int(icecream)*40))
    Lbl_bill = Label(btnrow5, text=total,width=10, bg="#262525", fg="gold", font=("seoge ui black bold", 20))
    Lbl_bill.pack(side=LEFT, anchor="center", pady=30)


def adlogin():
    top = Toplevel()
    top.title("LOGIN")
    top.geometry("700x500")
    framelogin1 = Frame(top, bg="#262525")
    framelogin1.pack(fill="both")
    framelogin2 = Frame(top, bg="#262525")
    framelogin2.pack(fill="both")
    framelogin3 = Frame(top, bg="#262525")
    framelogin3.pack(fill="both", expand=True)
    Lbl_bill = Label(framelogin1, text="USER-ID", bg="#262525", fg="gold", font=("eras bold itc", 20))
    Lbl_bill.pack(side=LEFT, anchor="nw", pady=20)
    Lbl_bill = Label(framelogin2, text="PASSWORD",bg="#262525", fg="gold", font=("eras bold itc", 20))
    Lbl_bill.pack(side=LEFT, anchor="nw", pady=20)

    def login_database():
        try:
            global mydb
            mydb = mc.connect(host= "localhost", user= database_userid.get(), password= database_pass.get(), database= "register")
            global mycursor
            mycursor = mydb.cursor()
            
        except:
            messagebox.showerror("Database Error", "Invalid username or password, Not connected to database", parent= top)
        else:
            messagebox.showinfo("Database", "Connection sucessfull", parent= top)

    for x in range(1):
        value1 = StringVar()
        database_userid = Entry(framelogin1, textvariable=value1, width=40)
        database_userid.pack(side=LEFT, anchor="nw", padx=90, pady=35)
        user_entry_login.append(database_userid)

    for x in range(1):
        value1 = StringVar()
        database_pass = Entry(framelogin2, show="*",textvariable=value1, width=40)
        database_pass.pack(side=LEFT, anchor="nw", padx=41, pady=35)
        user_entry_login.append(database_pass)

    btnlogin = Button(framelogin3, border=0, text="LOG-IN", bg="#262525", fg="gold", compound=TOP,
                   font=("gill sans ultra bold condensed", 20),borderwidth=5, command=login_database)
    btnlogin.pack(side=TOP, anchor="sw", padx=200, pady=0)

def register():
    top = Toplevel()
    top.title("REGISTER")
    top.geometry("700x500")
    framelogin1 = Frame(top, bg="#262525")
    framelogin1.pack(fill="both")
    framelogin2 = Frame(top, bg="#262525")
    framelogin2.pack(fill="both")
    framelogin3 = Frame(top, bg="#262525")
    framelogin3.pack(fill="both")
    framelogin4 = Frame(top, bg="#262525")
    framelogin4.pack(fill="both")
    framelogin5 = Frame(top, bg="#262525")
    framelogin5.pack(fill="both", expand=True)
    framelogin6 = Frame(top, bg="#262525")
    framelogin6.pack(fill="both", expand=True)
    framelogin7 = Frame(top, bg="#262525")
    framelogin7.pack(fill="both", expand=True)
    framelogin8 = Frame(top, bg="#262525")
    framelogin8.pack(fill="both", expand=True)
    # framelogin9 = Frame(top, bg="#262525")
    # framelogin9.pack(fill="both", expand=True)


    Lbl_bill = Label(framelogin1, text="FIRST NAME", bg="#262525", fg="gold", font=("eras bold itc", 20))
    Lbl_bill.pack(side=LEFT, anchor="nw", pady=20)
    Lbl_bill = Label(framelogin2, text="LAST NAME", bg="#262525", fg="gold", font=("eras bold itc", 20))
    Lbl_bill.pack(side=LEFT, anchor="nw", pady=20)
    Lbl_bill = Label(framelogin3, text="PHONE NO",bg="#262525", fg="gold", font=("eras bold itc", 20))
    Lbl_bill.pack(side=LEFT, anchor="nw", pady=20)
    Lbl_bill = Label(framelogin4, text="EMAIL ID",bg="#262525", fg="gold", font=("eras bold itc", 20))
    Lbl_bill.pack(side=LEFT, anchor="nw", pady=20)
    Lbl_bill = Label(top, text="The generated bill will delivered on this Email ID", bg="#262525", fg="gold", font=("eras bold itc", 12))
    Lbl_bill.place(x=545,y=262)
    Lbl_bill = Label(framelogin5, text="ADDRESS",bg="#262525", fg="gold", font=("eras bold itc", 20))
    Lbl_bill.pack(side=LEFT, anchor="nw", pady=20)
    res = Label(framelogin7,bg="#262525")
    res.pack(side=TOP)
    
    # Callback Function for username 
    def firstname(fname):
        if fname.isalpha():
            return True
        if fname == "":
            return True
        else:
            messagebox.showerror(f"Username Error", "Numbers, Space & Special character are not allowed in username",parent= top)
            return False
            
    # Callback Function for lastname 
    def lastname(lname):
        if lname.isalpha():
            return True
        if lname == "":
            return True
        else:
            messagebox.showerror("Username Error", "Numbers, Space & Special character are not allowed in username",parent= top)
            return False
        
    # Callback Function for contact number
    def contactnum(contact):
        if contact.isdigit():
            return True
        if len(str(contact))== 0:
            return True 
        else:
            messagebox.showerror("Invalid","Alphabets are not allowed in Contact number",parent= top)
            return False

    # Callback Function for whatsapp number
    def checkemail(email):
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                messagebox.showwarning("Input Error","Invalid E-mail enter by user", parent=top)
                return False
        else:
            pass
            # messagebox.showwarning("Input Error","Email length is too small", parent=top)
            # return True

    def register_database():
        try:
            mycursor.execute("use register")
            # command = "insert into user (Firstname, Lastname, Contactnumber, whatsappnum, address) values (%s,%s,%d,%d,%s)"   '"+num+"',
            mycursor.execute("INSERT INTO user(Firstname, Lastname, Contactnumber, Emailid, Address) values('"+fname_var.get().capitalize()+"','"+lname_var.get().capitalize()+"','"+phone_var.get()+"','"+mail_var.get()+"','"+add_var.get()+"')")
            mydb.commit()
            # mycursor.execute("commit")
            messagebox.showinfo("Registration Success", "User registration completed sucessfully!!", parent=top)
            mycursor.execute("select * from user")
            for i in mycursor:
                print(i)

        except Error as err:
            print("Error", err)
            mydb.close()

          
    #validation at submit time        
    def validation():
        # mail = mail_var.get()
        # alp = ["gmail", "yahoo", "bing"]
        # alp = any(alp)
        # alp1 = str(alp)
        # alp.fullmatch(mail_var.get()) 
        if fname_var.get() == "" and lname_var.get() == "" and phone_var.get() == "" and mail_var.get() == "" and add_var.get() == "":
            messagebox.showerror("Input Error", "All fields are necessary", parent=top)
        elif fname_var.get() == "":
            messagebox.showerror("Input Error","Enter the First name", parent=top)
        elif len(fname_var.get()) > 10:
            messagebox.showerror("Input Error","First name is too long", parent=top)
        elif lname_var.get() == "":
            messagebox.showerror("Input Error","Enter the Last first", parent=top)
        elif len(lname_var.get()) > 10:
            messagebox.showerror("Input Error","Last name is too long", parent=top)
        elif phone_var.get() == "": 
            messagebox.showerror("Input Error","Contact number is empty", parent=top)
        elif len(phone_var.get())!=10:
            messagebox.showerror("Input Error","Contact number is not equal to 10 digit", parent=top)
        elif mail_var.get() =="":
            messagebox.showinfo("Input Error","Enter Email", parent=top) 
        elif len(mail_var.get()) < 7:
            messagebox.showwarning("Input Error","Email length is too small", parent=top)
        elif "@" not in mail_var.get():
            messagebox.showerror("Input Error","\"@\" is not found!! Please enter the valid Email", parent=top)
        elif ".com" not in mail_var.get():
            messagebox.showerror("Input Error", "Email does not end with \".com\", Please enter the valid Email", parent=top)
        # elif "gmail" or "yahoo" or "bing" not in mail_var.get():
        #     messagebox.showerror("Input Error", "Something is missing betwen \"@\" and \".com\"", parent= top)
        elif add_var.get() == "" or len(add_var.get()) < 30:
            messagebox.showerror("Input Error","Enter the valid Address ", parent=top)
        else:
            register_database()

    

    for x in range(1):
        global fname_var
        fname_var = StringVar()
        entry_userid1 = Entry(framelogin1, textvariable=fname_var, width=40)
        entry_userid1.place(x=250,y=28)
        validate_name= top.register(firstname)
        entry_userid1.config(validate= 'key', validatecommand=(validate_name, '%P'))
        user_entry_register.append(fname_var.get())

    for x in range(1):
        global lname_var
        lname_var = StringVar()
        entry_userid2 = Entry(framelogin2, textvariable=lname_var, width=40)
        entry_userid2.place(x=250,y=30)
        validate_name1= top.register(lastname)
        entry_userid2.config(validate= 'key', validatecommand=(validate_name1, '%P'))
        user_entry_register.append(lname_var.get())

    for x in range(1):
        global phone_var
        phone_var = StringVar()
        phone_var.set("")
        entry_userid3 = Entry(framelogin3, textvariable=phone_var, width=40)
        entry_userid3.place(x=250,y=32)
        validate_num= top.register(contactnum)
        entry_userid3.config(validate= 'key', validatecommand=(validate_num, '%P'))
        user_entry_register.append(phone_var.get())

    for x in range(1):
        global mail_var
        mail_var = StringVar()
        mail_var.set("")
        entry_userid4 = Entry(framelogin4, textvariable=mail_var, width=40)
        entry_userid4.place(x=250,y=34)
        validate_whatnum= top.register(checkemail)
        entry_userid4.config(validate= 'key', validatecommand=(validate_whatnum, '%P'))
        user_entry_register.append(mail_var.get())

    for x in range(1):
        global add_var
        add_var = StringVar()
        entry_userid5 = Entry(framelogin5, textvariable=add_var, width=80)
        entry_userid5.place(x=250,y=36)
        user_entry_register.append(add_var.get())

    


    btnlogin = Button(framelogin6, border=0, text="REGISTER", bg="#262525", fg="gold", compound=TOP,
                   font=("gill sans ultra bold condensed", 20), borderwidth=5,command= validation)
    btnlogin.pack(side=TOP, anchor="sw", padx=200, pady=0)

#Function to send mail 
def bill_mail():
    try:
        x = str(u_name)
        sendermail = "rainbowfilm007@gmail.com"
        receivermail = mail_var.get()
        senderpass = "sharukhsharukh"
        subject =  "Titan cafe bill" 
        bodyofmail = "Hello "+ x + "\nThank You for ordering the meal from Titan Cafe!! \nThis is your order bill"
        filename = u_name
        location = "D:\Food-Ordering-and-Bill-Management-System/"

        send = sendpdf(sendermail,receivermail,senderpass,subject,bodyofmail,filename,location)
        send.email_send()
    except Error as b_err:
        messagebox.showerror("Error", b_err, parent=TOP)


#Inserting data of bill in database 
def fooditems():
    try:
        mycursor.execute("INSERT INTO fooditems (Aloo_tikki_burger, veggie_burger, chicken_burger, fries, chicken_popcorn, cold_mojito, cold_drink, ice_cream_float, mojito, icecream, Total) VALUES ('"+entry_atburger.get()+"','"+entry_vegburger.get()+"','"+entry_chickenburger.get()+"','"+entry_fries.get()+"','"+entry_chickenpopcorn.get()+"','"+entry_coldcoffee.get()+"','"+entry_colddrink.get()+"','"+entry_float.get()+"','"+entry_mojito.get()+"','"+entry_icecream.get()+"','"+str(total)+"')")
        mydb.commit()
        mycursor.execute("select * from fooditems")       #To print data of selected fooditems in terminal
        for j in mycursor:
            print(j)
    except Error as e:                          #Throw error if any
        print("error", e)

#updating orders 
def update_order():
            mycursor.execute("update fooditems set Aloo_tikki_burger="+entry_atburger.get()+", veggie_burger="+entry_vegburger.get()+", chicken_burger="+entry_chickenburger.get()+", fries="+entry_fries.get()+", chicken_popcorn="+entry_chickenpopcorn.get()+", cold_mojito="+entry_coldcoffee.get()+", cold_drink="+entry_colddrink.get()+", ice_cream_float="+entry_float.get()+", mojito="+entry_mojito.get()+", icecream="+entry_icecream.get()+", Total="+str(total)+" where cust_id = (select max(custid) from user)")
            mydb.commit()

#Function to create bill in new window and show the bill in Text widget which is read-only mode
def view_cart():
    confirm = messagebox.askyesno("Place order", "Are you sure you want to place this order??")
    if confirm == True:
        def generate_bill():
        
            bill_number=random.randint(100,1000)
            bill_number_tk=StringVar()
            bill_number_tk.set(bill_number)
            txtReceipt.insert(END, "\t\tTITAN CAFE")
            txtReceipt.insert(END, "\n*************************************************")
            x = datetime.date.today()
            txtReceipt.insert(END, "\nORDER NUMBER :"+ bill_number_tk.get() + "\nCUSTOMER NAME : "+ fname_var.get().capitalize() + " " + lname_var.get().capitalize() + "\nORDER DATE: "+ str(x))
            txtReceipt.insert(END, "\n*************************************************")
            txtReceipt.insert(END, '\n ITEMS        \t\t' +"PRICE\t\t" + "QUANTITY")
            txtReceipt.insert(END, "\n*************************************************")
            aloo_tikki_burger = entry_atburger.get()
            if int(aloo_tikki_burger)!=0:
                txtReceipt.insert(END, '\nAloo Tikki Burger\t\t' "30/-\t\t" + entry_atburger.get())
            veggie_burger = entry_vegburger.get()
            if int(veggie_burger)!=0:
                txtReceipt.insert(END, '\nVeggie Burger\t\t' "50/-\t\t" + entry_vegburger.get())
            chicken_burger = entry_chickenburger.get()
            if int(chicken_burger)!=0:
                txtReceipt.insert(END, '\nChicken Burger\t\t' "70/-\t\t" + entry_chickenburger.get())
            fries = entry_fries.get()
            if int(fries)!=0:
                txtReceipt.insert(END, '\nFries        \t\t' "40/-\t\t" + entry_fries.get())
            chicken_popcorn = entry_chickenpopcorn.get()
            if int(chicken_popcorn)!=0:
                txtReceipt.insert(END, '\nChicken Popcorn\t\t' "70/-\t\t" + entry_chickenpopcorn.get())
            cold_mojito = entry_coldcoffee.get()
            if int(cold_mojito)!=0:
                txtReceipt.insert(END, '\nCold mojito  \t\t' "50/-\t\t" + entry_coldcoffee.get())
            cold_drink = entry_colddrink.get()
            if int(cold_drink)!=0:
                txtReceipt.insert(END, '\nCold Drink   \t\t' "40/-\t\t"+ entry_colddrink.get())
            icecream_float = entry_float.get()
            if int(icecream_float)!=0:
                txtReceipt.insert(END, '\nIce Cream Float\t\t' "50/-\t\t" + entry_float.get())
            mojito = entry_mojito.get()
            if int(mojito)!=0:
                txtReceipt.insert(END, '\nMojito       \t\t' "40/-\t\t" + entry_mojito.get())
            icecream = entry_icecream.get()
            if int(icecream)!=0:
                txtReceipt.insert(END, '\nIce Cream    \t\t' "40/-\t\t" + entry_icecream.get())
            global total
            total = ((int(aloo_tikki_burger) * 30) + (int(veggie_burger) * 50) + (int(chicken_burger) * 70) + (
                        int(fries) * 40) + (int(chicken_popcorn) * 70) + (int(cold_mojito) * 50) + (
                                int(cold_drink) * 40) + (int(icecream_float) * 50) + (int(mojito) * 40) + (
                                int(icecream) * 40))
            txtReceipt.insert(END, "\n*************************************************")
            if str(total)!=0:
                txtReceipt.insert(END, '\nTotal Amount To Be Paid\t\t\t\t' + str(total) + "/-")
            txtReceipt.insert(END, "\n*************************************************")
            txtReceipt.insert(END, '\n\t\tTHANK YOU\t\t')
            txtReceipt.insert(END, '\n\tHOPE TO SEE U BACK SOON!!')
            txtReceipt.insert(END, "\n*************************************************")
            txtReceipt.insert(END, "\n*************************************************")
            
            #Button for update the the food items
            update_button = Button(top, text= "Update", font=("rockwell",15,"bold"), relief= SOLID, bg= "green",cursor= "hand2", command= update_order)
            update_button.place(x=1000, y=520)
            #created button for whatsapp automation 
            what_message = Button(top,text= "Send bill on Mail", font=("rockwell",15,"bold"), relief= SOLID, bg= "green",cursor= "hand2", command= bill_mail)
            what_message.place(x=1110,y=520)

            txtReceipt.config(state=DISABLED)      #updated

                
            fooditems()          #calling the database function
             #calling the function which convert the bill in txt and then pdf

        def convert_to_pdf():
                """ This function will first convert the bill in txt and after that with the help of fpdf module it will 
                convert the txt file into pdf file """
                global u_name
                u_name = fname_var.get()+" "+lname_var.get()
                a = txtReceipt.get("1.0", END)
                # f = open("user Bill.txt",'w+')  
                cust_name = u_name + " bill.txt"    
                with open(cust_name,"w+") as f:  
                    f.writelines(a)
                    f.close()

                #This part is used to convert the txt file in pdf file 
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size= 12)
                conv = open(cust_name,"r")
                
                #read the contents of txt file
                for x in conv:
                    pdf.cell(200,10, txt= x, ln= 1, align= 'C')

                pdf.output(u_name+".pdf")              #output in pdf
                messagebox.showinfo("Printed Sucesfully", "Bill is printed successfully!!!", parent= top)

        def del_data():
            # data = """select max(custid) from user"""
            # data1 = mycursor.execute(data)
            # print(data1)
            query = """delete from user where custid = (select cust_id from fooditems order by cust_id DESC limit 1)""" 
            # mycursor.execute(query)
            # data = [(-1,),(-1,)]
            mycursor.execute(query)
            mydb.commit()

            # messagebox.showerror("Update Error", "Something went")
        def cancel_order():
            can_button = messagebox.askokcancel("Cancel Order", "Are you sure to want to cancel the order??", parent= top)
            if can_button == True:
                # sql code to delete order
                del_data()
                messagebox.showinfo("Order", "Order cancelled sucessfully", parent= top)
                # txtReceipt.insert(END, "Order cancelled sucessfully.")
            else:
                pass

        def new_order():
            messagebox.showinfo("New Order", "For new order you have register the user detail again in registeration page", parent= top)
            top.destroy()
            clear_entry()


        global photo_paytm
        global photo_otherpayment
        top=Toplevel()
        top.title("CART")
        top.geometry("1500x800")
        frame = Frame(top, bg="#262525")
        frame.pack(fill="both")
        frame2 = Frame(top, bg="#262525")
        frame2.pack(fill="both")
        frame3 = Frame(top, bg="#262525")
        frame3.pack( fill="both", expand=True)
        # frame4 = Frame(top, bg="#262525")
        # frame4.pack(expand=True,fill="both")

        
        btn12 = Button(frame, border=0, text="BACK", bg="#262525", fg="gold", compound=TOP,font=("gill sans ultra bold condensed", 20),borderwidth=5,command=top.destroy)
        btn12.pack(side=LEFT, anchor="nw", padx=115, pady=30)
        btn11 = Button(frame, border=0, text="PRINT BILL", bg="#262525", fg="gold", compound=TOP,font=("gill sans ultra bold condensed", 20),borderwidth=5, command= convert_to_pdf)
        btn11.place(x=960, y=30)
        btn13 = Button(frame, border=0, text="GENERATE BILL", bg="#262525", fg="gold", compound=TOP,font=("gill sans ultra bold condensed", 20),borderwidth=5,command=generate_bill)
        btn13.pack(side=RIGHT, anchor="nw", padx=30, pady=30)

        global txtReceipt
        txtReceipt = Text(frame2, height=25, width=43, font=("comic sans ms", 10))
        txtReceipt.pack(side=RIGHT, padx=50, pady=0)
        

        Lbl_bill = Label(frame2, text="PAYMENT MODE",bg="#262525", fg="gold", font=("eras bold itc", 20))
        Lbl_bill.pack(side=TOP, anchor="nw", pady=0)

        image_paytm = Image.open("IMG_6959.jpg")
        photo_paytm = ImageTk.PhotoImage(image_paytm)

        btn_paytm = Button(frame2, image=photo_paytm,bg="#262525",fg="gold",borderwidth=5, text='scan the code'+"\n"+ 'to pay via paytm', compound=TOP,font=("eras bold itc", 14))

        btn_paytm.pack(side=LEFT, anchor="nw", padx=20, pady=30)

        image_otherpayment = Image.open("payment options.png")
        photo_otherpayment = ImageTk.PhotoImage(image_otherpayment)

        btn_otherpayment = Button(frame2, image=photo_otherpayment, text='visit the counter'+"\n"+ 'to pay using card'+"\n" 'or cash or for any other'+"\n"'order realted queries',
                           compound=TOP, font=("eras bold itc", 14), bg="#262525", fg="gold", borderwidth=5)

        btn_otherpayment.pack(side=LEFT, anchor="nw", padx=20, pady=30)

        #new order button in generate bill section
        btn_neworder = Button(top,border=0, text="NEW ORDER", bg="#262525", fg="gold", compound=TOP,
                       font=("gill sans ultra bold condensed", 16), borderwidth=5,command=new_order)
        btn_neworder.place(x= 880,y=600)

        #Change order button in generate bill section
        btn_changeorder = Button(top, border=0, text="UPDATE ORDER", bg="#262525", fg="gold", compound=TOP,
                              font=("gill sans ultra bold condensed", 16), borderwidth=5, command= top.destroy)
        btn_changeorder.place(x=1020, y=600)


        #Cancel order button in generate bill section
        btn_cancel = Button(top, border=0, text="CANCEL ORDER", bg="#262525", fg="gold", compound=TOP,
                              font=("gill sans ultra bold condensed", 16), borderwidth=5, command= cancel_order)
        btn_cancel.place(x=1190, y=600)

    else:
        pass

root = Tk()
root.title("FOOD ORDERING SYSTEM - TITAN CAFE")
# root.iconbitmap("icon pics/order.ico")
loginrow= Frame(root, bg="#262525")
loginrow.pack(fill = "both")

title_label = Label(loginrow, text ="PLACE YOUR ORDER",bg ="#262525",fg ="gold", padx= 600, pady =10, font=("eras bold itc",14))
title_label.pack(side=BOTTOM)

title_label = Label(loginrow, text =" TITAN CAFE",bg ="gold",fg ="#262525", padx= 800, pady =10, font=("eras bold itc",30))
title_label.pack(side=BOTTOM,anchor="e")

btnlogin1 = Button(loginrow, text="REGISTER",bg ="#262530",fg ="gold", compound=RIGHT, font=("gill sans ultra bold", 12),borderwidth=5, command= register)
btnlogin1.place(x=1090,y=0)                                     #updated

btnlogin = Button(loginrow, text="ADMIN LOGIN",bg ="#262530",fg ="gold", compound=RIGHT, font=("gill sans ultra bold", 12),borderwidth=5, command=adlogin)
btnlogin.pack(side=TOP, anchor="e", padx=0, pady=0)

btnrow1 = Frame(root,bg="#262525")
btnrow1.pack(fill = "both")

btnrow2 = Frame(root,bg="#262525")
btnrow2.pack( fill = "both")

btnrow3 = Frame(root,bg="#262525")
btnrow3.pack(fill = "both")

btnrow4 = Frame(root,bg="#262525")
btnrow4.pack(fill = "both")

btnrow5 = Frame(root,bg="#262525")
btnrow5.pack(fill = "both",expand=True)

Lbl = Label(btnrow1,text="BURGERS",bg = "#262525" , fg = "gold", font=("eras bold itc",16))
Lbl.pack(side=LEFT,anchor="nw")

Lbl = Label(btnrow1,text="SIDES",bg = "#262525" , fg = "gold", font=("eras bold itc",16))
Lbl.pack(side=RIGHT,anchor="nw")

Lbl = Label(btnrow2,text="QUANTITY",bg = "#262525" , fg = "gold", font=("eras bold itc",16))
Lbl.pack(side=LEFT,anchor="nw",pady=6)

Lbl = Label(btnrow3,text="BEVRAGES",bg = "#262525" , fg = "gold", font=("eras bold itc",16))
Lbl.pack(side=LEFT,anchor="nw",pady=15)

Lbl = Label(btnrow3, text="DESSERTS", bg="#262525", fg="gold", font=("eras bold itc", 16))
Lbl.pack(side=RIGHT, anchor="nw", pady=15)

Lbl = Label(btnrow4, text="QUANTITY", bg="#262525", fg="gold", font=("eras bold itc", 16))
Lbl.pack(side=LEFT, anchor="nw", pady=0)

#callback function for burger at first entry
def burgernum(burger):
    if burger.isdigit():
        return True
    if len(str(burger))== 0:
        return True 
    else:
        messagebox.showerror("Invalid","Alphabets are not allowed")
        return False

#callback function for veg burger at 2nd entry
def veg_burgernum(vegburger):
    if vegburger.isdigit():
        return True
    if len(str(vegburger))== 0:
        return True 
    else:
        messagebox.showerror("Invalid","Alphabets are not allowed")
        return False

#callback funnction for chicken burger at 3rd entry
def chic_burgernum(chicburger):
    if chicburger.isdigit():
        return True
    if len(str(chicburger))== 0:
        return True 
    else:
        messagebox.showerror("Invalid","Alphabets are not allowed")
        return False

#callback function for fries at 4th entry
def friesnum(fries):
    if fries.isdigit():
        return True
    if len(str(fries))== 0:
        return True 
    else:
        messagebox.showerror("Invalid","Alphabets are not allowed")
        return False

#callback function for chicken popcorn at 5th entry
def popcornnum(popcorn):
    if popcorn.isdigit():
        return True
    if len(str(popcorn))== 0:
        return True 
    else:
        messagebox.showerror("Invalid","Alphabets are not allowed")
        return False

#callback function for cold mojito at 6th entry
def coffeenum(coffee):
    if coffee.isdigit():
        return True
    if len(str(coffee))== 0:
        return True 
    else:
        messagebox.showerror("Invalid","Alphabets are not allowed")
        return False

#callback function for colddrink at 7th entry
def drinknum(drink):
    if drink.isdigit():
        return True
    if len(str(drink))== 0:
        return True 
    else:
        messagebox.showerror("Invalid","Alphabets are not allowed")
        return False
 
#callback function for cold mojito at 8th entry
def floatnum(floatn):
    if floatn.isdigit():
        return True
    if len(str(floatn))== 0:
        return True 
    else:
        messagebox.showerror("Invalid","Alphabets are not allowed")
        return False

#callback function for mojito at 9th entry
def mojitonum(mojito):
    if mojito.isdigit():
        return True
    if len(str(mojito))== 0:
        return True 
    else:
        messagebox.showerror("Invalid","Alphabets are not allowed")
        return False

#callback function for cold icecream at 10th entry
def icecreamnum(icecream):
    if icecream.isdigit():
        return True
    if len(str(icecream))== 0:
        return True 
    else:
        messagebox.showerror("Invalid","Alphabets are not allowed")
        return False


for x in range(1):
    value1 = IntVar()
    entry_atburger = Entry(btnrow2, textvariable=value1,width=20)
    entry_atburger.pack(side=LEFT, anchor="nw", padx=8, pady=10)
    validate_burger= root.register(burgernum)
    entry_atburger.config(validate= 'key', validatecommand=(validate_burger, '%P'))
    food_items.append(entry_atburger)
    
for x in range(1):
    value2 = IntVar()
    entry_vegburger= Entry(btnrow2, textvariable=value2,width=20)
    entry_vegburger.pack(side=LEFT, anchor="nw", padx=95, pady=10)
    validate_vegburger= root.register(veg_burgernum)
    entry_vegburger.config(validate= 'key', validatecommand=(validate_vegburger, '%P'))
    food_items.append(entry_vegburger)

for x in range(1):
    value3 = IntVar()
    entry_chickenburger = Entry(btnrow2, textvariable=value3,width=20)
    entry_chickenburger.pack(side=LEFT, anchor="nw", padx=9, pady=10)
    validate_chicburger= root.register(chic_burgernum)
    entry_chickenburger.config(validate= 'key', validatecommand=(validate_chicburger, '%P'))
    food_items.append(entry_chickenburger)

for x in range(1):
    value4 = IntVar()
    entry_fries = Entry(btnrow2,textvariable=value4,width=20)
    entry_fries.pack(side=RIGHT, anchor="nw", padx=76, pady=10)
    validate_fries= root.register(friesnum)
    entry_fries.config(validate= 'key', validatecommand=(validate_fries, '%P'))
    food_items.append(entry_fries)

for x in range(1):
    value5 = IntVar()
    entry_chickenpopcorn = Entry(btnrow2, textvariable=value5,width=20)
    entry_chickenpopcorn.pack(side=RIGHT, anchor="nw", padx=11, pady=10)
    validate_popcorn= root.register(popcornnum)
    entry_chickenpopcorn.config(validate= 'key', validatecommand=(validate_popcorn, '%P'))
    food_items.append(entry_chickenpopcorn)

for x in range(1):
    value6 = IntVar()
    entry_coldcoffee = Entry(btnrow4, textvariable=value6,width=20)
    entry_coldcoffee.pack(side=LEFT, anchor="nw", padx=13, pady=3)
    validate_coffee= root.register(coffeenum)
    entry_coldcoffee.config(validate= 'key', validatecommand=(validate_coffee, '%P'))
    food_items.append(entry_coldcoffee)

for x in range(1):
    value7 = IntVar()
    entry_colddrink = Entry(btnrow4, textvariable=value7,width=20)
    entry_colddrink.pack(side=LEFT, anchor="nw", padx=73, pady=3)
    validate_colddrink= root.register(drinknum)
    entry_colddrink.config(validate= 'key', validatecommand=(validate_colddrink, '%P'))
    food_items.append(entry_colddrink)

for x in range(1):
    value8 = IntVar()
    entry_float = Entry(btnrow4, textvariable=value8,width=20)
    entry_float.pack(side=LEFT, anchor="nw", padx=11, pady=3)
    validate_float= root.register(floatnum)
    entry_float.config(validate= 'key', validatecommand=(validate_float, '%P'))
    food_items.append(entry_float)

for x in range(1):
    value9 = IntVar()
    entry_mojito = Entry(btnrow4, textvariable=value9,width=20)
    entry_mojito.pack(side=LEFT, anchor="nw", padx=73, pady=3)
    validate_mojito= root.register(mojitonum)
    entry_mojito.config(validate= 'key', validatecommand=(validate_mojito, '%P'))
    food_items.append(entry_mojito)

for x in range(1):
    value10 = IntVar()
    entry_icecream = Entry(btnrow4, textvariable=value10, width=20)
    entry_icecream.pack(side=RIGHT, anchor="nw", padx=123, pady=3)
    validate_icecream= root.register(icecreamnum)
    entry_icecream.config(validate= 'key', validatecommand=(validate_icecream, '%P'))
    food_items.append(entry_icecream)


def change(e):
    image = Image.open("clickme.jpg")
    photo = ImageTk.PhotoImage(image)
    btn.config(image=photo,cursor= "hand2")
    btn.image=photo

def change_back(e):
    image = Image.open("aloo tiki burger.jpg")
    photo = ImageTk.PhotoImage(image)
    btn.config(image=photo)
    btn.image = photo

image = Image.open("aloo tiki burger.jpg")
photo = ImageTk.PhotoImage(image)

btn = Button(btnrow1,image=photo,text="Aloo Tiki Burger: 30/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked)

btn.pack(side=LEFT,anchor="nw",padx=20,pady=10)

btn.bind("<Enter>", change)
btn.bind("<Leave>", change_back)

def change2(e2):
    image2 = Image.open("clickme.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    btn2.config(image=photo2,cursor= "hand2")
    btn2.image2=photo2

def change_back2(e2):
    image2 = Image.open("veggie burger.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    btn2.config(image=photo2)
    btn2.image2 = photo2

image2 = Image.open("veggie burger.jpg")
photo2 = ImageTk.PhotoImage(image2)

btn2 = Button(btnrow1,image=photo2,text="Veggie Burger: 50/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked2)

btn2.pack(side=LEFT,anchor="nw",padx=20,pady=10)

btn2.bind("<Enter>", change2)
btn2.bind("<Leave>", change_back2)

def change3(e3):
    image3 = Image.open("clickme.jpg")
    photo3 = ImageTk.PhotoImage(image3)
    btn3.config(image=photo3,cursor= "hand2")
    btn3.image3=photo3

def change_back3(e3):
    image3 = Image.open("chicken burger.jpg")
    photo3 = ImageTk.PhotoImage(image3)
    btn3.config(image=photo3)
    btn3.image3 = photo3


image3 = Image.open("chicken burger.jpg")
photo3 = ImageTk.PhotoImage(image3)

btn3 = Button(btnrow1,image=photo3,text="Chicken Burger: 70/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked3)

btn3.pack(side=LEFT,anchor="nw",padx=20,pady=10)

btn3.bind("<Enter>", change3)
btn3.bind("<Leave>", change_back3)

def change4(e4):
    image4 = Image.open("clickme.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    btn4.config(image=photo4,cursor= "hand2")
    btn4.image4=photo4

def change_back4(e4):
    image4 = Image.open("fries.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    btn4.config(image=photo4)
    btn4.image4 = photo4


image4 = Image.open("fries.jpg")
photo4 = ImageTk.PhotoImage(image4)

btn4 = Button(btnrow1,image=photo4,text="Fries: 40/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked4)

btn4.pack(side=RIGHT,anchor="nw",padx=10,pady=10)

btn4.bind("<Enter>", change4)
btn4.bind("<Leave>", change_back4)

def change5(e5):
    image5 = Image.open("clickme.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    btn5.config(image=photo5,cursor= "hand2")
    btn5.image5=photo5

def change_back5(e5):
    image5 = Image.open("chicken popcorn.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    btn5.config(image=photo5)
    btn5.image5 = photo5


image5 = Image.open("chicken popcorn.jpg")
photo5 = ImageTk.PhotoImage(image5)

btn5 = Button(btnrow1,image=photo5,text="Chicken Popcorn: 70/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked5)

btn5.pack(side=RIGHT,anchor="nw",padx=10,pady=10)

btn5.bind("<Enter>", change5)
btn5.bind("<Leave>", change_back5)

def change6(e6):
    image6 = Image.open("clickme.jpg")
    photo6 = ImageTk.PhotoImage(image6)
    btn6.config(image=photo6,cursor= "hand2")
    btn6.image6=photo6

def change_back6(e6):
    image6 = Image.open("cold coffee.jpg")
    photo6 = ImageTk.PhotoImage(image6)
    btn6.config(image=photo6)
    btn6.image6 = photo6


image6 = Image.open("cold coffee.jpg")
photo6 = ImageTk.PhotoImage(image6)

btn6 = Button(btnrow3,image=photo6,text="Cold mojito: 50/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked6)

btn6.pack(side=LEFT,anchor="nw",padx=10,pady=25)

btn6.bind("<Enter>", change6)
btn6.bind("<Leave>", change_back6)

def change7(e7):
    image7 = Image.open("clickme.jpg")
    photo7 = ImageTk.PhotoImage(image7)
    btn7.config(image=photo7,cursor= "hand2")
    btn7.image7=photo7

def change_back7(e7):
    image7 = Image.open("cold drinks.jpg")
    photo7 = ImageTk.PhotoImage(image7)
    btn7.config(image=photo7)
    btn7.image7 = photo7

image7 = Image.open("cold drinks.jpg")
photo7 = ImageTk.PhotoImage(image7)

btn7 = Button(btnrow3,image=photo7,text="Cold Drinks: 40/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked7)

btn7.pack(side=LEFT,anchor="nw",padx=10,pady=25)

btn7.bind("<Enter>", change7)
btn7.bind("<Leave>", change_back7)


def change8(e8):
    image8 = Image.open("clickme.jpg")
    photo8 = ImageTk.PhotoImage(image8)
    btn8.config(image=photo8,cursor= "hand2")
    btn8.image8=photo8

def change_back8(e8):
    image8 = Image.open("float.jpg")
    photo8 = ImageTk.PhotoImage(image8)
    btn8.config(image=photo8)
    btn8.image8 = photo8

image8 = Image.open("float.jpg")
photo8 = ImageTk.PhotoImage(image8)

btn8 = Button(btnrow3,image=photo8,text="Ice Cream Float: 50/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked8)

btn8.pack(side=LEFT,anchor="nw",padx=10,pady=25)

btn8.bind("<Enter>", change8)
btn8.bind("<Leave>", change_back8)

def change9(e9):
    image9 = Image.open("clickme.jpg")
    photo9 = ImageTk.PhotoImage(image9)
    btn9.config(image=photo9,cursor= "hand2")
    btn9.image9=photo9

def change_back9(e9):
    image9 = Image.open("mo.jpg")
    photo9 = ImageTk.PhotoImage(image9)
    btn9.config(image=photo9)
    btn9.image9 = photo9

image9 = Image.open("mo.jpg")
photo9 = ImageTk.PhotoImage(image9)

btn9 = Button(btnrow3,image=photo9,text="Mojito: 40/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked9)

btn9.pack(side=LEFT,anchor="nw",padx=10,pady=25)


btn9.bind("<Enter>", change9)
btn9.bind("<Leave>", change_back9)

def change10(e10):
    image10 = Image.open("clickme.jpg")
    photo10 = ImageTk.PhotoImage(image10)
    btn10.config(image=photo10,cursor= "hand2")
    btn10.image10=photo10

def change_back10(e10):
    image10 = Image.open("ice cream.jpg")
    photo10 = ImageTk.PhotoImage(image10)
    btn10.config(image=photo10)
    btn10.image10 = photo10

image10 = Image.open("ice cream.jpg")
photo10 = ImageTk.PhotoImage(image10)

btn10 = Button(btnrow3, image=photo10, text="Ice Cream: 40/-", compound=TOP, font=("gill sans ultra bold", 10), command=btn_is_clicked10)

btn10.pack(side=RIGHT, anchor="nw", padx=10, pady=25)

btn10.bind("<Enter>", change10)
btn10.bind("<Leave>", change_back10)

# image11 = Image.open("cort.jpg")
# photo11 = ImageTk.PhotoImage(image11)

btn11 = Button(btnrow5,border=0,text="PLACE ORDER",bg="#262525", fg="gold",compound=TOP,font=("gill sans ultra bold condensed",20),borderwidth=5,command=view_cart)

btn11.pack(side=RIGHT,anchor="nw",padx=30,pady=30)

# imageexit = Image.open("exit(1).png")
# photoexit = ImageTk.PhotoImage(imageexit)
# exitbtn = Button(btnrow5,border=0,text="EXIT",bg="#262525",fg="gold",compound=TOP,font=("gill sans ultra bold condensed",20),borderwidth=5,command=root.destroy)
#
# exitbtn.pack(side=RIGHT,anchor="nw",padx=0,pady=30)

total_btn = Button(btnrow5,border=0,width=10,height=0,text="TOTAL BILL",bg="#262525",fg="gold",compound=TOP,font=("gill sans ultra bold condensed",20),borderwidth=5,command=calculate_bill)

total_btn.pack(side=LEFT,anchor="center",padx=20,pady=30)


# imagereset = Image.open("trash(1).png")
# photoreset = ImageTk.PhotoImage(imagereset)
resetbtn = Button(btnrow5,border=0,text="CLEAR",bg="#262525",fg="gold",compound=TOP,font=("gill sans ultra bold condensed",20),borderwidth=5,command=clear_entry)

resetbtn.pack(side=RIGHT,anchor="nw",padx=10,pady=30)


root.mainloop()
