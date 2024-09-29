from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from dotenv import load_dotenv
import mysql.connector
import os 
load_dotenv()
import random
from admit import iadmitapp 


def main():
        win=Tk()
        app=Login_Window(win)
        win.mainloop()


class Login_Window:
    def __init__(self,root):
        pass
        self.root=root
        self.root.title("iadmit-app")
        self.root.geometry("1550x800+0+0")

        #variables======
        self.var_email=StringVar()
        self.var_password=StringVar() 
        self.var_Anumber=StringVar()
        self.var_newpass=StringVar()

        img1=Image.open(r"C:\Users\amand\Desktop\iadmit-app\loginpage.jpg")
        img1=img1.resize((1550, 800), Image.Resampling.LANCZOS)
        self.bg=ImageTk.PhotoImage(img1)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=400,y=170,width=340,height=450)

        #login==========

        img2=Image.open(r"C:\Users\amand\Desktop\iadmit-app\login.jpg")
        img2=img2.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=530, y=175, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=100,y=100)

    ##label=========
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,textvariable=self.var_password,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)


    #imaages=====

        img3=Image.open(r"C:\Users\amand\Desktop\iadmit-app\login.jpg")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=440, y=323, width=25, height=25)

        img4=Image.open(r"C:\Users\amand\Desktop\iadmit-app\password.jpg")
        img4=img4.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg4 = Label(image=self.photoimage4,bg="black",borderwidth=0)
        lblimg4.place(x=440, y=394, width=25, height=25)

      
         #show pass
        self.var_password_command=IntVar(value=0)
        self.Checkbtn=Checkbutton(frame,variable=self.var_password_command,command=self.password_command,text="Show Password",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.Checkbtn.place(x=40,y=290)

        #login=====
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=2,relief=RIDGE,fg="black",bg="pink",activeforeground="white",activebackground="purple")
        loginbtn.place(x=110,y=340,width=120,height=35)

        #register=====
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="purple")
        registerbtn.place(x=0,y=400,width=160)

        #forgetpass====
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="purple")
        registerbtn.place(x=15,y=380,width=120)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)



    def password_command(self):
        if self.var_password_command.get()== 1:
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required") 
        elif self.txtuser.get()=="" and self.txtpass.get()=="":
            messagebox.showinfo("Success","Welcome to iadmit app")
        else:
             conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
             my_cursor = conn.cursor()
             my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                        self.txtuser.get(),
                                                                        self.txtpass.get(),

             ))

             row=my_cursor.fetchone()
             if row==None:
                 messagebox.showerror("Error","Invalid username or password")
             else:
                open_main=messagebox.askyesno("YesNo","Are you a first time user?")
                if open_main>0:
                      self.new_window=Toplevel(self.root)
                      self.app=iadmitapp(self.new_window)
                else:
                 if not open_main:
                      self.new_window=Toplevel(self.root)
                      self.app=iadmitapp(self.new_window)

             conn.commit()
             conn.close()


      #######reset btn=====
    def reset_password(self):  
        if self.txt_Anumber.get() == "":
            messagebox.showerror("Error", "Please enter the correct alternative number", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter a new password", parent=self.root2)
        elif self.txt_newpass.get() != self.txt_confirmpass.get():  # Check if new password matches confirm password
            messagebox.showerror("Error", "New password and confirm password do not match", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor = conn.cursor()

                # Query to check if the email and alternative number match
                query = "SELECT * FROM register WHERE email=%s AND Anumber=%s"
                value = (self.txtuser.get(), self.txt_Anumber.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Please enter the correct number", parent=self.root2)
                else:
                    # Update the password and confirm password (if necessary)
                    query = "UPDATE register SET password=%s, Cpassword=%s WHERE email=%s"
                    value = (self.txt_newpass.get(), self.txt_confirmpass.get(), self.txtuser.get()) 
                    my_cursor.execute(query, value)

                    conn.commit()
                    messagebox.showinfo("Info", "Your password has been reset successfully", parent=self.root2)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}", parent=self.root2)
            finally:
                conn.close()


       
     ####forgetpass=====================
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the correct email address to reset password")
        else:
            conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter a valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="black", bg="white")
                l.place(x=0, y=10, relwidth=1)

                A_number = Label(self.root2, text="Alternative Number", font=("times new roman", 15, "bold"), fg="black", bg="white")
                A_number.place(x=50, y=80)

                # Define self.var_Anumber as a StringVar before using it
                self.var_Anumber = StringVar()
                self.txt_Anumber = ttk.Entry(self.root2, textvariable=self.var_Anumber, font=("times new roman", 15))
                self.txt_Anumber.place(x=50, y=110, width=250)

                Newpass = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
                Newpass.place(x=50, y=160)

                # Entry for new password
                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=190, width=250)

                C_Newpass = Label(self.root2, text="Confirm New Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
                C_Newpass.place(x=50, y=240)

                # Separate variable for confirm password
                self.txt_confirmpass = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_confirmpass.place(x=50, y=270, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_password, font=("times new roman", 15), fg="black", bg="white")
                btn.place(x=100, y=350, width=100)


##############REGISTRATION=======================


class Register:
    def __init__(self,root):
        pass
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #variables=========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_Anumber=StringVar()
        self.var_email=StringVar()      
        self.var_password=StringVar()       
        self.var_Cpassword=StringVar()
        
        #main pic========

        img1=Image.open(r"C:\Users\amand\Desktop\iadmit-app\register.jpg")
        img1=img1.resize((1550, 800), Image.Resampling.LANCZOS)
        self.bg=ImageTk.PhotoImage(img1)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        ##left pic====
        img2=Image.open(r"C:\Users\amand\Desktop\iadmit-app\left.jpg")
        img2=img2.resize((470, 550), Image.Resampling.LANCZOS)
        self.bg1=ImageTk.PhotoImage(img2)

        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=180, width=470, height=550) 

        #frame=========
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=180,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",28,"bold"),fg="purple",bg="white")
        register_lbl.place(x=50,y=20)

        #labels========
        #name&surname
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=378,y=130,width=250)

        #contact
        contact=Label(frame,text="Contact Number",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=180)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        contact_entry.place(x=50,y=210,width=250)

        A_number=Label(frame,text="Alternative Number",font=("times new roman",15,"bold"),fg="black",bg="white")
        A_number.place(x=370,y=180)

        self.txt_Anumber=ttk.Entry(frame,textvariable=self.var_Anumber,font=("times new roman",15))
        self.txt_Anumber.place(x=378,y=210,width=250)

        #email
        email=Label(frame,text="Email Address",font=("times new roman",15,"bold"),bg="white")
        email.place(x=50,y=260)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        email_entry.place(x=50,y=290,width=400)

        #password===
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=340)

        password_entry=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        password_entry.place(x=50,y=370,width=250)

        C_password=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        C_password.place(x=370,y=340)

        self.txt_Cpassword=ttk.Entry(frame,textvariable=self.var_Cpassword,font=("times new roman",15))
        self.txt_Cpassword.place(x=378,y=370,width=250)


        #checkbtns==============
        self.var_check=IntVar()
        self.Checkbtn=Checkbutton(frame,variable=self.var_check,text="l agree to the Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.Checkbtn.place(x=50,y=420)

        #btns============

        img=Image.open(r"C:\Users\amand\Desktop\iadmit-app\reg.jpg")
        img=img.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img)

        b1=Button(frame,image=self.photoimage1,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=480,width=300)

        img1=Image.open(r"C:\Users\amand\Desktop\iadmit-app\lo.jpg")
        img1=img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img1)

        b1=Button(frame,image=self.photoimage2,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=400,y=480,width=300)

        #functions=============
 
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.var_password.get()!=self.var_Cpassword.get():
            messagebox.showerror("Error","Password does not match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to the Terms & Conditions")
        else:
           conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
           my_cursor = conn.cursor()
           query = ("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if  row!=None:
                messagebox.showerror("Error","User already exists")
           else:
                 my_cursor.execute("insert into iadmit.register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                       self.var_fname.get(),
                                                                       self.var_lname.get(),
                                                                       self.var_contact.get(),
                                                                       self.var_Anumber.get(),
                                                                       self.var_email.get(),
                                                                       self.var_password.get(),
                                                                       self.var_Cpassword.get()
                                                                                               ))
                                                                                            

                
               
                 conn.commit()
                 conn.close()
                 messagebox.showinfo("Success","Welcome to iadmit app")

    def return_login(self): 
        self.root.destroy()  



if __name__== "__main__":
    main()
    