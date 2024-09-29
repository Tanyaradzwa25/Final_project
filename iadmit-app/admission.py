from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk
import mysql.connector
from dotenv import load_dotenv
import os 
load_dotenv()
import random
from tkinter import messagebox
from tkinter import END


class admission_Win:
    def __init__(self,root):
        pass
        self.root=root
        self.root.title("iadmit-app")
        self.root.geometry("1295x550+230+220")

        #==============vaariables===============

        self.var_Admission_Reference=StringVar()
        x=random.randint(1000,9999)
        self.var_Admission_Reference.set(str(x))

        self.var_Name=StringVar()
        self.var_Gender=StringVar()
        self.var_Contact=StringVar()
        self.var_Emergency_Number=StringVar()
        self.var_Email_Address=StringVar()
        self.var_Date_Of_Birth=StringVar()
        self.var_ID_Number=StringVar()
        self.var_Nationality=StringVar()
        self.var_Address=StringVar()
        self.var_Home_Language=StringVar()

        # ==========Title=============
        IbI_title=Label(self.root,text="ADD PERSONAL INFORMATION",font=("times new roman",18,"bold"),bg="black",fg="orange",bd=4,relief=RIDGE)
        IbI_title.place(x=0,y=0,width=1350,height=50)

        # ==============logo===================

        img2=Image.open(r"C:\Users\amand\Desktop\iadmit-app\logo final.png")
        img2=img2.resize((100, 50), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        Iblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        Iblimg.place(x=2,y=0,width=100,height=50)

        #============label===========
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="PERSONAL INFORMATION",font=("times new roman",13,"bold"),bg="white",fg="black",padx=5,pady=10)
        LabelFrameleft.place(x=0,y=50,width=400,height=490)

        #==========label and entry============
        # personal information
        lbl_admission_ref=Label(LabelFrameleft,text="Admission Reference",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        lbl_admission_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_Admission_Reference,font=("arial",13,"bold"),width=22,state="readonly")
        enty_ref.grid(row=0,column=1)

        # NAME
        lbl_admission_ref=Label(LabelFrameleft,text="Name and Surname",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        lbl_admission_ref.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(LabelFrameleft,textvariable=self.var_Name,width=22,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)

        # DATE OF BIRTH
        lbldateofbirth=Label(LabelFrameleft,text="Date Of Birth",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        lbldateofbirth.grid(row=2,column=0,sticky=W)

        txtcname=ttk.Entry(LabelFrameleft,textvariable=self.var_Date_Of_Birth,width=22,font=("arial",13,"bold"))
        txtcname.grid(row=2,column=1)

        # identification number
        lblidentificationnumber=Label(LabelFrameleft,text="ID Number",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        lblidentificationnumber.grid(row=3,column=0,sticky=W)

        combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_ID_Number,font=("arial",12,"bold"),width=20,state="readonly")
        combo_ID["value"]=("South African ID","Passport Number","Other")
        combo_ID.current(0)
        combo_ID.grid(row=3,column=1)

        # GENDER
        label_gender=Label(LabelFrameleft,text="Gender",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        label_gender.grid(row=4,column=0,sticky=W)

        combo_gender=ttk.Combobox(LabelFrameleft,textvariable=self.var_Gender,width=20,state="readonly",font=("arial",12,"bold"))
        combo_gender["value"]=("Female","Male","Other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1)

        # ADDRESS
        lbl_admission_ref=Label(LabelFrameleft,text="Address",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        lbl_admission_ref.grid(row=5,column=0,sticky=W)

        txtcname=ttk.Entry(LabelFrameleft,textvariable=self.var_Address,width=22,font=("arial",13,"bold"))
        txtcname.grid(row=5,column=1)

        # CONTACT
        lblcontact=Label(LabelFrameleft,text="Contact Number",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        lblcontact.grid(row=6,column=0,sticky=W)

        txtcontact=ttk.Entry(LabelFrameleft,textvariable=self.var_Contact,width=22,font=("arial",13,"bold"))
        txtcontact.grid(row=6,column=1)

        # EMERGENCY CONTACT
        lblEmergencyNumber=Label(LabelFrameleft,text="Emergency Number",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        lblEmergencyNumber.grid(row=7,column=0,sticky=W)

        txtcEmergency=ttk.Entry(LabelFrameleft,textvariable=self.var_Emergency_Number,width=22,font=("arial",13,"bold"))
        txtcEmergency.grid(row=7,column=1)


        # EMAIL
        lblEmail=Label(LabelFrameleft,text="Email Address",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        lblEmail.grid(row=8,column=0,sticky=W)

        txtEmail=ttk.Entry(LabelFrameleft,textvariable=self.var_Email_Address,width=22,font=("arial",13,"bold"))
        txtEmail.grid(row=8,column=1)

        # NATIONALITY
        lblNationality=Label(LabelFrameleft,text="Nationality",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        lblNationality.grid(row=9,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(LabelFrameleft,textvariable=self.var_Nationality,font=("arial",12,"bold"),width=20,state="readonly")
        combo_Nationality["value"]=("Botswana","Eswatini (Swaziland)","Kenya","Lesotho","Mozambican", "Namibian","Nigerian","South African","Zimbabwean","Other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=9,column=1)

        # Home Language
        lblHomeLanguage=Label(LabelFrameleft,text="Home Language",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
        lblHomeLanguage.grid(row=10,column=0,sticky=W)

        combo_HomeLanguage=ttk.Combobox(LabelFrameleft,textvariable=self.var_Home_Language,font=("arial",12,"bold"),width=20,state="readonly")
        combo_HomeLanguage["value"]=("Sesotho","Swati","Shona","English","Ndebele", "Xhosa","Pedi","Zulu","Afrikaans","Other")
        combo_HomeLanguage.current(0)
        combo_HomeLanguage.grid(row=10,column=1)

        #===========btns===============
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=490,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.Reset,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #===========table frame saerch system==========
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",13,"bold"),bg="white",fg="black",padx=5,pady=10)
        Table_Frame.place(x=400,y=50,width=900,height=490)

        lbl_Search_By=Label(Table_Frame,text="Search By",font=("arial",12,"bold"),bg="green",fg="black")
        lbl_Search_By.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        self.combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=27,state="readonly")
        self.combo_Search["value"]=("Contact","Admission Reference","Name","ID Number","Date of Birth","Email Address","Address","Passport Number","Home Language","Emergency Number")
        self.combo_Search.current(0)
        self.combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        self.txtSearch_entry=Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=29)
        self.txtSearch_entry.grid(row=0,column=2,padx=2)
        
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="orange",width=8)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="orange",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)

        #============show date table=========
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Admission_Details_Table=ttk.Treeview(details_table,column=("Admission Reference","Name","Gender","Contact","Emergency Number","Email Address","Date Of Birth","ID Number","Nationality","Address","Home Language"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)       
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Admission_Details_Table.xview)
        scroll_y.config(command=self.Admission_Details_Table.yview)

        self.Admission_Details_Table.heading("Admission Reference",text="Admission Reference")
        self.Admission_Details_Table.heading("Name",text="Name")
        self.Admission_Details_Table.heading("Gender",text="Gender")      
        self.Admission_Details_Table.heading("Contact",text="Contact")       
        self.Admission_Details_Table.heading("Emergency Number",text="Emergency Number")       
        self.Admission_Details_Table.heading("Email Address",text="Email Address")       
        self.Admission_Details_Table.heading("Date Of Birth",text="Date Of Birth")       
        self.Admission_Details_Table.heading("ID Number",text="ID Number")
        self.Admission_Details_Table.heading("Nationality",text="Nationality")
        self.Admission_Details_Table.heading("Address",text="Address")
        self.Admission_Details_Table.heading("Home Language",text="Home Language")
        

        self.Admission_Details_Table["show"]="headings"

        self.Admission_Details_Table.column("Admission Reference",width=100)
        self.Admission_Details_Table.column("Name",width=100)
        self.Admission_Details_Table.column("Gender",width=100)
        self.Admission_Details_Table.column("Contact",width=100)
        self.Admission_Details_Table.column("Emergency Number",width=100)
        self.Admission_Details_Table.column("Email Address",width=100)
        self.Admission_Details_Table.column("Date Of Birth",width=100)
        self.Admission_Details_Table.column("ID Number",width=100)
        self.Admission_Details_Table.column("Nationality",width=100)
        self.Admission_Details_Table.column("Address",width=100)
        self.Admission_Details_Table.column("Home Language",width=100)

        self.Admission_Details_Table.pack(fill=BOTH,expand=1)
        self.Admission_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
    
    def add_data(self):
      if self.var_Admission_Reference.get()=="" or self.var_Address.get()=="" :
         messagebox.showerror("Error","All Fields are required",parent=self.root) 
      else:                                  
            try:
                conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor=conn.cursor()
                my_cursor.execute("insert into iadmit.admission values (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)", (
                                                                                        self.var_Admission_Reference.get(),
                                                                                        self.var_Name.get(),
                                                                                        self.var_Gender.get(),
                                                                                        self.var_Contact.get(),
                                                                                        self.var_Emergency_Number.get(),
                                                                                        self.var_Email_Address.get(),
                                                                                        self.var_Date_Of_Birth.get(),
                                                                                        self.var_ID_Number.get(),
                                                                                        self.var_Nationality.get(),
                                                                                        self.var_Address.get(),
                                                                                        self.var_Home_Language.get()))
                
                               
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Patient has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
        my_cursor=conn.cursor()
        my_cursor.execute("select * from admission")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Admission_Details_Table.delete(*self.Admission_Details_Table.get_children())
            for i in rows:
                self.Admission_Details_Table.insert("",END,values=i)
                conn.commit()
            conn.close()

    
    def get_cuersor(self,event=""):
        cusrsor_row=self.Admission_Details_Table.focus()
        content=self.Admission_Details_Table.item(cusrsor_row)
        row=content["values"]

        self.var_Admission_Reference.set(row[0]),
        self.var_Name.set(row[1]),
        #self.var_Gender.set(row[2]),
        self.var_Contact.set(row[3]),
        self.var_Emergency_Number.set(row[4]),
        self.var_Email_Address.set(row[5]),
        self.var_Date_Of_Birth.set(row[6]),
        #self.var_ID_Number.set(row[7]),
        #self.var_Nationality.set(row[8]),
        self.var_Address.set(row[9]),
        #self.var_Home_Language.set(row[10])

    def update(self):
     if self.var_Address.get() == "":
        messagebox.showwarning("Error", "Please enter the correct Address", parent=self.root)
     else:
       try:
            conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
            my_cursor = conn.cursor()
            my_cursor.execute("""
                UPDATE admission 
                SET Name=%s, Gender=%s, Contact=%s, `Emergency Number`=%s,`Email Address`=%s, `Date Of Birth`=%s, `ID Number`=%s,  Nationality=%s, Address=%s ,`Home Language`=%s WHERE `Admission Reference`=%s""", (
                                                                                                                                                                      self.var_Name.get(),
                                                                                                                                                                      self.var_Gender.get(),
                                                                                                                                                                      self.var_Contact.get(),
                                                                                                                                                                      self.var_Emergency_Number.get(),
                                                                                                                                                                      self.var_Email_Address.get(),
                                                                                                                                                                      self.var_Date_Of_Birth.get(),
                                                                                                                                                                      self.var_ID_Number.get(),
                                                                                                                                                                      self.var_Nationality.get(),
                                                                                                                                                                      self.var_Address.get(),
                                                                                                                                                                      self.var_Home_Language.get(),
                                                                                                                                                                      self.var_Admission_Reference.get() ))
            conn.commit()
            self.fetch_data()  
            conn.close()

            messagebox.showinfo("Update", "Patient details have been updated successfully", parent=self.root)
       except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)


    def mDelete(self):
        mDelete = messagebox.askyesno("iAdmit", "Do you want to delete this patient details", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
            my_cursor = conn.cursor()
            query = "DELETE FROM admission WHERE `Admission Reference` = %s"  
            value = (self.var_Admission_Reference.get(),)  
            try:
                my_cursor.execute(query, value) 
                conn.commit()  
                self.fetch_data()  
            except mysql.connector.Error as err:
                print(f"Error: {err}")  
            finally:
                conn.close() 
        else:
            return

            
    def Reset(self):
        #self.var_Admission_Reference.set(""),
        self.var_Name.set(""),
        #self.var_Gender.set(""),
        self.var_Contact.set(""),
        self.var_Emergency_Number.set(""),
        self.var_Email_Address.set(""),
        self.var_Date_Of_Birth.set(""),
       # self.var_ID_Number.set(""),
        self.var_Nationality.set(""),
        self.var_Address.set(""),
        self.var_Home_Language.set("")


        x=random.randint(1000,9999)
        self.var_Admission_Reference.set(str(x))

    
    def search(self):
        conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
        my_cursor = conn.cursor()

        query = "select * from admission where `"+ str(self.search_var.get()) +"` LIKE '%" + str(self.txt_search.get()) +"%'"
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        if len (rows)!=0:
                self.Admission_Details_Table.delete(*self.Admission_Details_Table.get_children())
                for i in rows:
                    self.Admission_Details_Table.insert("",END,values=i)
                    conn.commit()
                conn.close()



if __name__== "__main__":
  root=Tk()
  obj=admission_Win(root)
  root.mainloop()