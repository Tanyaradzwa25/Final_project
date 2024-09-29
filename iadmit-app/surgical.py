from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk
from dotenv import load_dotenv
import mysql.connector
import os 

import random
from tkinter import messagebox

load_dotenv()

class surgical_history:
    def __init__(self,root):
        pass
        self.root=root
        self.root.title("iadmit-app")
        self.root.geometry("1295x550+230+220")
        #==============vaariables===============

        self.var_Contact_Reference=StringVar()
       
        self.var_Do_you_have_any_allergies=StringVar()
        self.var_Name_of_the_Allergies=StringVar()
        self.var_Have_you_ever_had_a_surgery_within_the_past_5_years=StringVar()
        self.var_Please_indicate_on_which_system_of_the_body=StringVar()
        self.var_How_did_you_react_to_anaesthetic_after_surgical_procedure=StringVar()

                   # ==========Title=============
        IbI_title=Label(self.root,text="SURGICAL HISTORY DETAILS",font=("times new roman",18,"bold"),bg="black",fg="orange",bd=4,relief=RIDGE)
        IbI_title.place(x=0,y=0,width=1350,height=50)

        # ==============logo===================

        img2=Image.open(r"C:\Users\amand\Desktop\iadmit-app\logo final.png")
        img2=img2.resize((100, 50), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        Iblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        Iblimg.place(x=2,y=0,width=100,height=50)

        #============label===========
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ADD SURGICAL HISTORY",font=("times new roman",13,"bold"),bg="white",fg="black",padx=5,pady=10)
        LabelFrameleft.place(x=0,y=50,width=600,height=490)

        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Click the relevant sections",font=("times new roman",10,"bold"),bg="white",fg="black")
        LabelFrameleft.place(x=0,y=80,width=600,height=490)


         #==========label and entry============

        # personal information
        lbl_admission_ref=Label(LabelFrameleft,text="Contact Reference",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
        lbl_admission_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_Contact_Reference,font=("arial",10,"bold"),width=12)
        enty_ref.grid(row=0,column=3,sticky=W)

        #fetch data
        btnFetchData=Button(LabelFrameleft,command=self.Fetch_Contact_Reference,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="orange",width=10)
        btnFetchData.grid(row=0,column=4,padx=6)

         #========allergies==============
        lblsurg=Label(LabelFrameleft,text="Do you have any allergies",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
        lblsurg.place(x=0,y=20)
        lblsurg.grid(row=4,column=0,sticky=W)

        self.combo_allergy_status=ttk.Combobox(LabelFrameleft,textvariable=self.var_Do_you_have_any_allergies,font=("arial",10,"bold"),width=10,state="readonly")
        self.combo_allergy_status["value"]=("Select","Yes","No")
        self.combo_allergy_status.current(0)
        self.combo_allergy_status.grid(row=4,column=3)

        #===========nameof allergy==============

        lblnameallergy = Label(LabelFrameleft, text="Name of the Allergies", font=("arial", 10, "bold"), bg="white", fg="black")
        lblnameallergy.grid(row=6, column=0, sticky=W)

        self.combo_allergy_status=ttk.Combobox(LabelFrameleft,textvariable=self.var_Name_of_the_Allergies,font=("arial",10,"bold"),width=10,state="readonly")
        self.combo_allergy_status["value"]=("Select","Nil Known","Nuts","Zofran","Fish","Ipuprofen","Water","Tumeric","Penecillin","Hydrocortisone","Pethidine","Tramadol","Bees")
        self.combo_allergy_status.current(0)
        self.combo_allergy_status.grid(row=6,column=3)
        
         #surgical history
        lblsurg=Label(LabelFrameleft,text="Have you ever had a surgery within the past 5 years",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
        lblsurg.grid(row=8,column=0,sticky=W)

        self.combo_surgery_status=ttk.Combobox(LabelFrameleft,textvariable=self.var_Have_you_ever_had_a_surgery_within_the_past_5_years,font=("arial",10,"bold"),width=10,state="readonly")
        self.combo_surgery_status["value"]=("Select","Nil Known","Yes","No")
        self.combo_surgery_status.current(0)
        self.combo_surgery_status.grid(row=8,column=3)

       #========Name of surgery==============
        lblnamesurg = Label(LabelFrameleft, text="Please indicate on which system of the body", font=("arial", 10, "bold"), bg="white", fg="black")
        lblnamesurg.grid(row=10, column=0, sticky=W)

        self.combo_surgery_status=ttk.Combobox(LabelFrameleft,textvariable=self.var_Please_indicate_on_which_system_of_the_body,font=("arial",10,"bold"),width=10,state="readonly")
        self.combo_surgery_status["value"]=("Select","Nil Known","Cardiovascular System"," Respiratory System","Digestive System","Nervous System","Musculoskeletal System","Urinary System","Reproductive System","Other")
        self.combo_surgery_status.current(0)
        self.combo_surgery_status.grid(row=10,column=3)

        #===========anaesthetic========
        lblnamesurg = Label(LabelFrameleft, text="How did you react to anaesthetic after surgical procedure", font=("arial", 10, "bold"), bg="white", fg="black")
        lblnamesurg.grid(row=12, column=0, sticky=W)

        self.combo_surgery_status=ttk.Combobox(LabelFrameleft,textvariable=self.var_How_did_you_react_to_anaesthetic_after_surgical_procedure,font=("arial",10,"bold"),width=10,state="readonly")
        self.combo_surgery_status["value"]=("Select","Nil Known","No Reaction to Anaesthetic","Had a bad Reaction to Anaesthetic")
        self.combo_surgery_status.current(0)
        self.combo_surgery_status.grid(row=12,column=3)

         #===========btns===============
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=590,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="orange",width=13)
        btnAdd.grid(row=0,column=0,padx=2)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="orange",width=13)
        btnUpdate.grid(row=0,column=1,padx=2)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="orange",width=13)
        btnDelete.grid(row=0,column=2,padx=2)

        btnReset=Button(btn_frame,text="Reset",command=self.Reset,font=("arial",12,"bold"),bg="black",fg="orange",width=13)
        btnReset.grid(row=0,column=3,padx=2)

        #===========table frame saerch system==========
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",13,"bold"),bg="white",fg="black",padx=5,pady=10)
        Table_Frame.place(x=600,y=250,width=700,height=400)

        lbl_Search_By=Label(Table_Frame,text="Search By",font=("arial",10,"bold"),bg="green",fg="black")
        lbl_Search_By.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",11,"bold"),width=20,state="readonly")
        combo_Search["value"]=("Contact Reference","Do you have allergies")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        self.txtSearch_entry=Entry(Table_Frame,textvariable=self.txt_search,font=("arial",11,"bold"),width=20)
        self.txtSearch_entry.grid(row=0,column=2,padx=2)
         
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="orange",width=8)
        btnSearch.grid(row=0,column=3,padx=2)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="orange",width=8)
        btnShowAll.grid(row=0,column=4,padx=2)

#======================top image===============
                
        img3=Image.open(r"C:\Users\amand\Desktop\iadmit-app\admit.jpg")
        img3=img3.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        Iblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        Iblimg.place(x=600,y=50,width=700,height=200)
         #============show date table=========
    # Create the frame for the Treeview
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=60, width=700, height=180)

        # Create horizontal and vertical scrollbars
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        # Create the Treeview
        self.Surgical_Details_Table = ttk.Treeview(details_table,column=("Contact Reference","Do you have allergies","Name of the Allergies","Have you ever had a surgery within the past 5 years","Please indicate on which system of the body","How did you react to anaesthetic after surgical procedure"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set )

        # Configure scrollbars
        scroll_x.config(command=self.Surgical_Details_Table.xview)
        scroll_y.config(command=self.Surgical_Details_Table.yview)

        # Pack scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Define column headings and widths
        self.Surgical_Details_Table.heading("Contact Reference", text="Contact Reference")
        self.Surgical_Details_Table.heading("Do you have allergies", text="Do you have allergies")
        self.Surgical_Details_Table.heading("Name of the Allergies", text="Name of the Allergies")
        self.Surgical_Details_Table.heading("Have you ever had a surgery within the past 5 years", text="Have you ever had a surgery within the past 5 years")
        self.Surgical_Details_Table.heading("Please indicate on which system of the body", text="Please indicate on which system of the body")
        self.Surgical_Details_Table.heading("How did you react to anaesthetic after surgical procedure", text="How did you react to anaesthetic after surgical procedure")

        self.Surgical_Details_Table["show"]="headings"

        self.Surgical_Details_Table.column("Contact Reference", width=200)
        self.Surgical_Details_Table.column("Do you have allergies", width=200)
        self.Surgical_Details_Table.column("Name of the Allergies", width=200)
        self.Surgical_Details_Table.column("Have you ever had a surgery within the past 5 years", width=200)
        self.Surgical_Details_Table.column("Please indicate on which system of the body", width=200)
        self.Surgical_Details_Table.column("How did you react to anaesthetic after surgical procedure", width=200)

        # Pack the Treeview
        self.Surgical_Details_Table.pack(fill=BOTH,expand=1)

        # Bind event
        self.Surgical_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)

        #==========fetch=======
    def fetch_data(self):
            conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
            my_cursor=conn.cursor()
            my_cursor.execute("select * from surgical")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.Surgical_Details_Table.delete(*self.Surgical_Details_Table.get_children())
                for i in rows:
                 self.Surgical_Details_Table.insert("",END,values=i)
                conn.commit()
            conn.close()

    #===========addd 

    def add_data(self):
        if self.var_Have_you_ever_had_a_surgery_within_the_past_5_years.get()=="" or self.var_Name_of_the_Allergies.get()=="" :
                messagebox.showerror("Error","All Fields are required",parent=self.root) 
        else:                                  
            try:
                conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO iadmit.surgical VALUES (%s, %s, %s, %s, %s,%s)", (
                                                                                self.var_Contact_Reference.get(),
                                                                                self.var_Do_you_have_any_allergies.get(),
                                                                                self.var_Name_of_the_Allergies.get(),
                                                                                self.var_Have_you_ever_had_a_surgery_within_the_past_5_years.get(),
                                                                                self.var_Please_indicate_on_which_system_of_the_body.get(),
                                                                                self.var_How_did_you_react_to_anaesthetic_after_surgical_procedure.get()
                                                                                ))
                                                                                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Surgical Information has been added",parent=self.root)
            except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    
    def get_cursor(self, event=""):
            cursor_row = self.Surgical_Details_Table.focus()
            content = self.Surgical_Details_Table.item(cursor_row)
            row = content["values"] 

            #self.var_Contact_Reference.set(row [0]),
            self.var_Do_you_have_any_allergies.set(row[1]),
            self.var_Name_of_the_Allergies.set(row[2]),
            self.var_Have_you_ever_had_a_surgery_within_the_past_5_years.set(row[3]),
            self.var_Please_indicate_on_which_system_of_the_body.set(row[4]),
            self.var_How_did_you_react_to_anaesthetic_after_surgical_procedure.set(row[5]),
    

    def update(self):
            if self.var_Do_you_have_any_allergies.get() == "":
               messagebox.showwarning("Error", "Please enter allergies", parent=self.root)
            else:
                try:
                  conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                  my_cursor = conn.cursor()
                  my_cursor.execute("""
                      UPDATE surgical 
                      SET `Do you have allergies`=%s , `Name of the Allergies`=%s , `Have you ever had a surgery within the past 5 years` =%s , `How did you react to anaesthetic after surgical procedure`=%s,`Please indicate on which system of the body`=%s WHERE `Contact Reference`=%s""", (                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                        self.var_Do_you_have_any_allergies.get(),
                                                                                                                                                                                                        self.var_Name_of_the_Allergies.get(),
                                                                                                                                                                                                        self.var_Have_you_ever_had_a_surgery_within_the_past_5_years.get(),
                                                                                                                                                                                                        self.var_How_did_you_react_to_anaesthetic_after_surgical_procedure.get(),
                                                                                                                                                                                                        self.var_Please_indicate_on_which_system_of_the_body.get(),
                                                                                                                                                                                                        self.var_Contact_Reference.get()))
                  conn.commit()
                  self.fetch_data()  
                  conn.close()

                  messagebox.showinfo("Update", "Surgical details have been updated successfully", parent=self.root)
                except Exception as es:
                 messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
            

     
    def mDelete(self):
        mDelete = messagebox.askyesno("iAdmit", "Do you want to delete this surgical details", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
            my_cursor = conn.cursor()
            query = "DELETE FROM surgical WHERE `Contact Reference` = %s"  
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
                self.var_Contact_Reference.set(""),
                self.var_Do_you_have_any_allergies.set(""),
                self.var_Name_of_the_Allergies.set(""),
                self.var_Have_you_ever_had_a_surgery_within_the_past_5_years.set(""),
                self.var_Please_indicate_on_which_system_of_the_body.set(""),
                self.var_How_did_you_react_to_anaesthetic_after_surgical_procedure.set(""),
                
    
                x=random.randint(1000,9999)
                self.var_Contact_Reference.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
        my_cursor = conn.cursor()

        query = "select * from surgical where `"+ str(self.search_var.get()) +"` LIKE '%" + str(self.txt_search.get()) +"%'"
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        if len (rows)!=0:
                self.Surgical_Details_Table.delete(*self.Surgical_Details_Table.get_children())
                for i in rows:
                    self.Surgical_Details_Table.insert("",END,values=i)
                    conn.commit()
                conn.close()
   

        #=================fetch data all=================
    def Fetch_Contact_Reference(self):
        if self.var_Contact_Reference.get()=="":
                messagebox.showerror("Error","Please enter the correct Contact Reference",parent=self.root)
        else:
                conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor = conn.cursor()
                query = ("select Name from admission where Contact=%s")
                value = (self.var_Contact_Reference.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()


                if row==None:
                 messagebox.showerror("Error","This number is not found",parent=self.root)
                else:
                 conn.commit()
                 conn.close()


                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=6,pady=8,bg="black")
                showDataFrame.place(x=600,y=60,width=400,height=190)

                lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"),bg="black",fg="white")
                lblName.place(x=0, y=0)

                lbl=Label(showDataFrame, text=row, font=("arial", 12, "bold"),bg="black",fg="white")
                lbl.place(x=120, y=0)

                #===============DOB===============
                conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor = conn.cursor()
                query = ("select `Date of Birth` from admission where Contact=%s")
                value = (self.var_Contact_Reference.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Date of Birth: ",font=("arial",12,"bold"),bg="black",fg="white")
                lblGender.place(x=0, y=30)

                lbl=Label(showDataFrame, text=row, font=("arial", 12, "bold"),bg="black",fg="white")
                lbl.place(x=120, y=30)
                #================gender===============
                conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor = conn.cursor()
                query = ("select Gender from admission where Contact=%s")
                value = (self.var_Contact_Reference.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"),bg="black",fg="white")
                lblGender.place(x=0, y=60)

                lbl=Label(showDataFrame, text=row, font=("arial", 12, "bold"),bg="black",fg="white")
                lbl.place(x=120, y=60)

                #===============contact==============
                conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor = conn.cursor()
                query = ("select Contact from admission where Contact=%s")
                value = (self.var_Contact_Reference.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Contact:",font=("arial",12,"bold"),bg="black",fg="white")
                lblName.place(x=0, y=90)

                lbl=Label(showDataFrame, text=row, font=("arial", 12, "bold"),bg="black",fg="white")
                lbl.place(x=120, y=90)

                #=================nationality===========
                conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor = conn.cursor()
                query = ("select Nationality from admission where Contact=%s")
                value = (self.var_Contact_Reference.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"),bg="black",fg="white")
                lblName.place(x=0, y=120)

                lbl=Label(showDataFrame, text=row, font=("arial", 12, "bold"),bg="black",fg="white")
                lbl.place(x=120, y=120)

                ####===============Adresss==========
                conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor = conn.cursor()
                query = ("select Address from admission where Contact=%s")
                value = (self.var_Contact_Reference.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Address:",font=("arial",12,"bold"),bg="black",fg="white")
                lblName.place(x=0, y=150)

                lbl=Label(showDataFrame, text=row, font=("arial", 12, "bold"),bg="black",fg="white")
                lbl.place(x=120, y=150)




if __name__== "__main__":
     root=Tk()
     obj=surgical_history(root)
     root.mainloop()