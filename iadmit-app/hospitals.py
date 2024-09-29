from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk
import mysql.connector
from dotenv import load_dotenv
import os 
load_dotenv()
import random
from tkinter import messagebox

class hospitals:
    def __init__(self,root):
        pass
        self.root=root
        self.root.title("iadmit-app")
        self.root.geometry("1295x550+230+220")


        #========vaariables===============

        self.var_Contact_Reference=StringVar()
        self.var_Have_you_been_admitted_at_any_hospital_before=StringVar()
        self.var_If_Yes_which_was_the_most_recent_hospital=StringVar()
        self.var_Please_select_the_hospital_that_is_close_to_you_location=StringVar()
        
        # ==========Title=============
        IbI_title=Label(self.root,text="ADD HOSPITALS ",font=("times new roman",18,"bold"),bg="black",fg="orange",bd=4,relief=RIDGE)
        IbI_title.place(x=0,y=0,width=1350,height=50)

        # ==============logo===================

        img2=Image.open(r"C:\Users\amand\Desktop\iadmit-app\logo final.png")
        img2=img2.resize((100, 50), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        Iblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        Iblimg.place(x=2,y=0,width=100,height=50)

        #============label===========
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="LIST OF HOSPITALS",font=("times new roman",14,"bold"),bg="white",fg="black",padx=5,pady=10)
        LabelFrameleft.place(x=0,y=50,width=680,height=220)

        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Click relevent sections",font=("times new roman",12,"bold"),bg="white",fg="black")
        LabelFrameleft.place(x=0,y=80,width=680,height=220)

         #==========label and entry============
        lbl_admission_ref=Label(LabelFrameleft,text="Contact Reference",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
        lbl_admission_ref.grid(row=2,column=0,sticky=W)

        enty_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_Contact_Reference,font=("arial",10,"bold"),width=32)
        enty_ref.grid(row=2,column=2,sticky=W)

        #Admission
        lblpreg=Label(LabelFrameleft,text="Have you been admitted at any hospital before",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
        lblpreg.grid(row=4,column=0,sticky=W)

        combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Have_you_been_admitted_at_any_hospital_before,font=("arial",10,"bold"),width=30,state="readonly")
        combo_ID["value"]=("Select","Yes","No")
        combo_ID.current(0)
        combo_ID.grid(row=4,column=2)

        #if yes
        lblpreg=Label(LabelFrameleft,text="If Yes which was the most recent hospital",font=("arial",10,"bold"),bg="white",fg="black",padx=0,pady=4)
        lblpreg.grid(row=6,column=0,sticky=W)

        combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_If_Yes_which_was_the_most_recent_hospital,font=("arial",10,"bold"),width=30,state="readonly")
        combo_ID["value"]=("Select","No","Charlotte Maxeke Johannesburg Academic Hospital (Johannesburg)","Tygerberg Hospital (Cape Town)","Steve Biko Academic Hospital (Pretoria)","Chris Hani Baragwanath Hospital (Soweto, Johannesburg)","Groote Schuur Hospital (Cape Town)","Nelson Mandela Academic Hospital (Eastern Cape)","Mamelodi Hospital (Gauteng)")
        combo_ID.current(0)
        combo_ID.grid(row=6,column=2)
       
        #Hospitals
        lblpreg=Label(LabelFrameleft,text="Please select the hospital that is close to you location",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
        lblpreg.grid(row=8,column=0,sticky=W)

        combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Please_select_the_hospital_that_is_close_to_you_location,font=("arial",10,"bold"),width=30,state="readonly")
        combo_ID["value"]=("Select","Charlotte Maxeke Johannesburg Academic Hospital (Johannesburg)","Tygerberg Hospital (Cape Town)","Steve Biko Academic Hospital (Pretoria)","Chris Hani Baragwanath Hospital (Soweto, Johannesburg)","Groote Schuur Hospital (Cape Town)","Nelson Mandela Academic Hospital (Eastern Cape)","Mamelodi Hospital (Gauteng)")
        combo_ID.current(0)
        combo_ID.grid(row=8,column=2)

  #===========btns===============
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=150,width=670,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="orange",width=15)
        btnAdd.grid(row=0,column=0,padx=4)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="orange",width=15)
        btnUpdate.grid(row=0,column=1,padx=4)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="orange",width=15)
        btnDelete.grid(row=0,column=2,padx=4)

        btnReset=Button(btn_frame,text="Reset",command=self.Reset,font=("arial",12,"bold"),bg="black",fg="orange",width=15)
        btnReset.grid(row=0,column=3,padx=4)


        #===========table frame saerch system==========
        #pic===========
        img3=Image.open(r"C:\Users\amand\Desktop\iadmit-app\hosp.jpg")
        img3=img3.resize((610, 500), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        Iblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        Iblimg.place(x=680,y=50,width=610,height=500)

        #==========table-================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show hospitals Details",font=("times new roman",13,"bold"),bg="white",fg="black",padx=5,pady=10)
        Table_Frame.place(x=0,y=300,width=680,height=250)
        
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        self.Hospital_Detail_Table=ttk.Treeview(Table_Frame,column=("Contact Reference","Have you been admitted at any hospital before","If Yes which was the most recent hospital","Please select the hospital that is close to you location"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)       
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Hospital_Detail_Table.xview)
        scroll_y.config(command=self.Hospital_Detail_Table.yview)

        self.Hospital_Detail_Table.heading("Contact Reference",text="Contact Reference")
        self.Hospital_Detail_Table.heading("Have you been admitted at any hospital before",text="Have you been admitted at any hospital before")
        self.Hospital_Detail_Table.heading("If Yes which was the most recent hospital",text="If Yes which was the most recent hospital")
        self.Hospital_Detail_Table.heading("Please select the hospital that is close to you location",text="Please select the hospital that is close to you location")      
        
        self.Hospital_Detail_Table["show"]="headings"

        self.Hospital_Detail_Table.column("Contact Reference",width=300)
        self.Hospital_Detail_Table.column("Have you been admitted at any hospital before",width=300)
        self.Hospital_Detail_Table.column("If Yes which was the most recent hospital",width=300)
        self.Hospital_Detail_Table.column("Please select the hospital that is close to you location",width=300)
       
        self.Hospital_Detail_Table.pack(fill=BOTH,expand=1)
        self.Hospital_Detail_Table.bind("<ButtonRelease-1>",self.get_cuersor)

    #==============add==============
    def add_data(self):
            if self.var_Have_you_been_admitted_at_any_hospital_before.get()=="" or self.var_If_Yes_which_was_the_most_recent_hospital.get()=="" :
                   messagebox.showerror("Error","All Fields are required",parent=self.root) 
            else:                                  
                try:
                    conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into iadmit.hospital values (%s, %s, %s,%s)", (
                                                            self.var_Contact_Reference.get(),
                                                            self.var_Have_you_been_admitted_at_any_hospital_before.get(),
                                                            self.var_If_Yes_which_was_the_most_recent_hospital.get(),
                                                            self.var_Please_select_the_hospital_that_is_close_to_you_location.get()
                                                                                       ))
                
                               
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Hospital Information has been added",parent=self.root)
                except Exception as es:
                     messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
             conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
             my_cursor=conn.cursor()
             my_cursor.execute("select * from hospital")
             rows=my_cursor.fetchall()
             if len(rows)!=0:
                 self.Hospital_Detail_Table.delete(*self.Hospital_Detail_Table.get_children())
                 for i in rows:
                    self.Hospital_Detail_Table.insert("",END,values=i)
                 conn.commit()
             conn.close()

     #get cursor
    def get_cuersor(self,event=""):
          cusrsor_row=self.Hospital_Detail_Table.focus()
          content=self.Hospital_Detail_Table.item(cusrsor_row)
          row=content["values"]

          self.var_Contact_Reference.set(row[1]),
          self.var_Have_you_been_admitted_at_any_hospital_before.set(row[2]),
          self.var_If_Yes_which_was_the_most_recent_hospital.set(row[3]),
          self.var_Please_select_the_hospital_that_is_close_to_you_location.set(row[4]),
    
     #update
    def update(self):
      if self.var_Have_you_been_admitted_at_any_hospital_before.get() == "":
          messagebox.showwarning("Error", "Please enter if you have been admitted", parent=self.root)
      else:
          try:
              # Establish database connection
              conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
              my_cursor = conn.cursor()

              # Corrected SQL Update Query
              my_cursor.execute("""
                  UPDATE hospital 
                  SET `Have you been admitted at any hospital before`=%s, 
                      `If Yes which was the most recent hospital`=%s, 
                      `Please select the hospital that is close to you location`=%s
                  WHERE `Contact Reference`=%s
              """, (
                  self.var_Have_you_been_admitted_at_any_hospital_before.get(),
                  self.var_If_Yes_which_was_the_most_recent_hospital.get(),
                  self.var_Please_select_the_hospital_that_is_close_to_you_location.get(),
                  self.var_Contact_Reference.get()
              ))

              # Commit changes and close the connection
              conn.commit()
              self.fetch_data()  
              conn.close()

              messagebox.showinfo("Update", "Hospital details have been updated successfully", parent=self.root)
          except Exception as es:
              messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def mDelete(self):
            mDelete = messagebox.askyesno("iAdmit", "Do you want to delete this hospital details", parent=self.root)
            if mDelete > 0:
                conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor = conn.cursor()
                query = "DELETE FROM hospital WHERE `Contact Reference` = %s"  
                value = (self.var_Contact_Reference.get(),)  
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
                self.var_Have_you_been_admitted_at_any_hospital_before.set(""),
                self.var_If_Yes_which_was_the_most_recent_hospital.set(""),
                self.var_Please_select_the_hospital_that_is_close_to_you_location.set(""),
                
                
if __name__== "__main__":
  root=Tk()
  obj=hospitals(root)
  root.mainloop()        