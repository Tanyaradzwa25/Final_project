from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk
import mysql.connector
from dotenv import load_dotenv
import os 
load_dotenv() 
import random
from tkinter import messagebox



class medical_history:
        def __init__(self,root):
                pass
                self.root=root
                self.root.title("iadmit-app")
                self.root.geometry("1295x550+230+220")


                #==============vaariables===============

                self.var_Contact_Reference=StringVar()
                
                self.var_Are_you_Diabetic=StringVar()
                self.var_Are_you_Epileptic=StringVar()
                self.var_Are_you_Asthmatic=StringVar()
                self.var_Are_you_Hypertensive=StringVar()
                self.var_Are_you_Pregnant=StringVar()
                self.var_Do_you_have_Tuberculosis=StringVar()
                self.var_Do_you_have_Cholesterol=StringVar()
                self.var_Do_you_have_a_Heart_Problem=StringVar()
                self.var_Recent_Cough_or_Cold=StringVar()
                self.var_Do_you_Smoke=StringVar()
                self.var_Did_you_take_Medication=StringVar()
                self.var_Name_of_Medication=StringVar()
                



            # ==========Title=============
                IbI_title=Label(self.root,text="MEDICAL HISTORY DETAILS",font=("times new roman",18,"bold"),bg="black",fg="orange",bd=4,relief=RIDGE)
                IbI_title.place(x=0,y=0,width=1350,height=50)

                # ==============logo===================

                img2=Image.open(r"C:\Users\amand\Desktop\iadmit-app\logo final.png")
                img2=img2.resize((100, 50), Image.Resampling.LANCZOS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                Iblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
                Iblimg.place(x=2,y=0,width=100,height=50)

                #============label===========
                LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ADD MEDICAL HISTORY",font=("times new roman",13,"bold"),bg="white",fg="black",padx=5,pady=10)
                LabelFrameleft.place(x=0,y=50,width=400,height=490)

                LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Click the relevant sections",font=("times new roman",10,"bold"),bg="white",fg="black")
                LabelFrameleft.place(x=0,y=80,width=400,height=490)


                #==========label and entry============

                # personal information
                lbl_admission_ref=Label(LabelFrameleft,text="Contact Reference",font=("arial",12,"bold"),bg="white",fg="black",padx=2,pady=4)
                lbl_admission_ref.grid(row=0,column=0,sticky=W)

                enty_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_Contact_Reference,font=("arial",10,"bold"),width=10)
                enty_ref.grid(row=0,column=1,sticky=W)

                #fetch data

                btnFetchData=Button(LabelFrameleft,command=self.Fetch_Contact_Reference,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="orange",width=10)
                btnFetchData.place(x=420,y=6)
                btnFetchData.grid(row=0,column=2,padx=1)

                # diabetes
                lbldiabetes=Label(LabelFrameleft,text="Are you Diabetic",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lbldiabetes.grid(row=2,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Are_you_Diabetic,font=("arial",10,"bold"),width=8,state="readonly")
                combo_ID["value"]=("Yes","No")
                combo_ID.current(0)
                combo_ID.grid(row=2,column=1)

                # epilepsy
                lblepi=Label(LabelFrameleft,text="Are you Epileptic",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lblepi.grid(row=3,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Are_you_Epileptic,font=("arial",10,"bold"),width=8,state="readonly")
                combo_ID["value"]=("Yes","No")
                combo_ID.current(0)
                combo_ID.grid(row=3,column=1)

                # Asthma
                lblasthma=Label(LabelFrameleft,text="Are you Asthmatic",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lblasthma.grid(row=4,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Are_you_Asthmatic,font=("arial",10,"bold"),width=8,state="readonly")
                combo_ID["value"]=("Yes","No")
                combo_ID.current(0)
                combo_ID.grid(row=4,column=1)

                # Hypertension
                lblhyper=Label(LabelFrameleft,text="Are you Hypertensive",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lblhyper.grid(row=5,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Are_you_Hypertensive,font=("arial",10,"bold"),width=8,state="readonly")
                combo_ID["value"]=("Yes","No")
                combo_ID.current(0)
                combo_ID.grid(row=5,column=1)

                # Pregnant
                lblpreg=Label(LabelFrameleft,text="Are you Pregnant",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lblpreg.grid(row=6,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Are_you_Pregnant,font=("arial",10,"bold"),width=8,state="readonly")
                combo_ID["value"]=("Yes","No")
                combo_ID.current(0)
                combo_ID.grid(row=6,column=1)

                # tb
                lbltb=Label(LabelFrameleft,text="Do you have Tuberculosis",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lbltb.grid(row=7,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Do_you_have_Tuberculosis,font=("arial",10,"bold"),width=8,state="readonly")
                combo_ID["value"]=("Yes","No")
                combo_ID.current(0)
                combo_ID.grid(row=7,column=1)

                # cholesterol
                lblidentificationnumber=Label(LabelFrameleft,text="Do you have Cholesterol",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lblidentificationnumber.grid(row=8,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Do_you_have_Cholesterol,font=("arial",10,"bold"),width=8,state="readonly")
                combo_ID["value"]=("Yes","No")
                combo_ID.current(0)
                combo_ID.grid(row=8,column=1)

                # Heart Problem
                lblheartr=Label(LabelFrameleft,text="Do you have a Heart Problem",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lblheartr.grid(row=9,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Do_you_have_a_Heart_Problem,font=("arial",10,"bold"),width=8,state="readonly")
                combo_ID["value"]=("Yes","No")
                combo_ID.current(0)
                combo_ID.grid(row=9,column=1)

                # cough
                lblcold=Label(LabelFrameleft,text="Recent Cough or Cold",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lblcold.grid(row=10,column=0,sticky=W)

                combo_cold=ttk.Combobox(LabelFrameleft,textvariable=self.var_Recent_Cough_or_Cold,font=("arial",10,"bold"),width=8,state="readonly")
                combo_cold["value"]=("Yes","No")
                combo_cold.current(0)
                combo_cold.grid(row=10,column=1)

                # diabetes
                lblsmoke=Label(LabelFrameleft,text="Do you Smoke",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lblsmoke.grid(row=11,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Do_you_Smoke,font=("arial",10,"bold"),width=8,state="readonly")
                combo_ID["value"]=("Yes","No")
                combo_ID.current(0)
                combo_ID.grid(row=11,column=1)

                #M
                lblsmoke=Label(LabelFrameleft,text="Did you take Medication",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lblsmoke.grid(row=12,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Did_you_take_Medication,font=("arial",10,"bold"),width=8,state="readonly")
                combo_ID["value"]=("Yes","No")
                combo_ID.current(0)
                combo_ID.grid(row=12,column=1)


                lblsmoke=Label(LabelFrameleft,text="Name of Medication",font=("arial",10,"bold"),bg="white",fg="black",padx=2,pady=4)
                lblsmoke.grid(row=13,column=0,sticky=W)

                combo_ID=ttk.Combobox(LabelFrameleft,textvariable=self.var_Name_of_Medication,font=("arial",10,"bold"),width=8)
                combo_ID["value"]=("Ibuprofen","Aspirin","Tramadol" ,"Antidepressants","Paracetamol","African herbs")
                combo_ID.grid(row=13,column=1)


                #===========btns===============
                btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
                btn_frame.place(x=0,y=400,width=390,height=40)

                btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="orange",width=8)
                btnAdd.grid(row=0,column=0,padx=3)

                btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="orange",width=8)
                btnUpdate.grid(row=0,column=1,padx=3)

                btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="orange",width=8)
                btnDelete.grid(row=0,column=2,padx=3)

                btnReset=Button(btn_frame,text="Reset",command=self.Reset,font=("arial",12,"bold"),bg="black",fg="orange",width=8)
                btnReset.grid(row=0,column=3,padx=3)

                #======================top image===============
                
                img3=Image.open(r"C:\Users\amand\Desktop\iadmit-app\admit.jpg")
                img3=img3.resize((800, 200), Image.Resampling.LANCZOS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                Iblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
                Iblimg.place(x=400,y=60,width=890,height=200)

                #===========table frame saerch system==========
                Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",13,"bold"),bg="white",fg="black",padx=5,pady=10)
                Table_Frame.place(x=400,y=250,width=890,height=350)

                lbl_Search_By=Label(Table_Frame,text="Search By",font=("arial",12,"bold"),bg="green",fg="black")
                lbl_Search_By.grid(row=0,column=0,sticky=W,padx=2)

                self.search_var=StringVar()
                combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=27,state="readonly")
                combo_Search["value"]=("Are you Asthmatic","Are you hypertensive","Are you Diabetic","Do you smoke")
                combo_Search.current(0)
                combo_Search.grid(row=0,column=1,padx=2)

                self.txt_search=StringVar()
                self.txtSearch_entry=Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=29)
                self.txtSearch_entry.grid(row=0,column=2,padx=2)
                
                
                btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="orange",width=8)
                btnSearch.grid(row=0,column=3,padx=1)

                btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="orange",width=8)
                btnShowAll.grid(row=0,column=4,padx=1)


                #============show date table=========
                details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
                details_table.place(x=0,y=50,width=880,height=180)

                scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

                self.Medical_Details_Table=ttk.Treeview(details_table,column=("Contact Reference","Are you Diabetic","Are you Epileptic","Are you Asthmatic","Are you Hypertensive","Are you Pregnant","Do you have Tuberculosis","Do you have Cholesterol","Do you have a Heart Problem","Recent Cough or Cold","Do you Smoke","Did you take Medication","Name of Medication"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)       
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.Medical_Details_Table.xview)
                scroll_y.config(command=self.Medical_Details_Table.yview)

                self.Medical_Details_Table.heading("Contact Reference",text="Contact Reference")
                self.Medical_Details_Table.heading("Are you Diabetic",text="Are you Diabetic")
                self.Medical_Details_Table.heading("Are you Epileptic",text="Are you Epileptic")      
                self.Medical_Details_Table.heading("Are you Asthmatic",text="Are you Asthmatic")       
                self.Medical_Details_Table.heading("Are you Hypertensive",text="Are you Hypertensive")       
                self.Medical_Details_Table.heading("Are you Pregnant",text="Are you Pregnant")       
                self.Medical_Details_Table.heading("Do you have Tuberculosis",text="Do you have Tuberculosis")       
                self.Medical_Details_Table.heading("Do you have Cholesterol",text="Do you have Cholesterol")
                self.Medical_Details_Table.heading("Do you have a Heart Problem",text="Do you have a Heart Problem")
                self.Medical_Details_Table.heading("Recent Cough or Cold",text="Recent Cough or Cold")
                self.Medical_Details_Table.heading("Do you Smoke",text="Do you Smoke")
                self.Medical_Details_Table.heading("Did you take Medication",text="Did you take Medication")       
                self.Medical_Details_Table.heading("Name of Medication",text="Name of Medication")
                

                self.Medical_Details_Table["show"]="headings"

                self.Medical_Details_Table.column("Contact Reference",width=100)
                self.Medical_Details_Table.column("Are you Diabetic",width=100)
                self.Medical_Details_Table.column("Are you Epileptic",width=100)
                self.Medical_Details_Table.column("Are you Asthmatic",width=100)
                self.Medical_Details_Table.column("Are you Hypertensive",width=100)
                self.Medical_Details_Table.column("Are you Pregnant",width=100)
                self.Medical_Details_Table.column("Do you have Tuberculosis",width=100)
                self.Medical_Details_Table.column("Do you have Cholesterol",width=100)
                self.Medical_Details_Table.column("Do you have a Heart Problem",width=100)
                self.Medical_Details_Table.column("Recent Cough or Cold",width=100)
                self.Medical_Details_Table.column("Do you Smoke",width=100)
                self.Medical_Details_Table.column("Did you take Medication",width=100)
                self.Medical_Details_Table.column("Name of Medication",width=100)

                self.Medical_Details_Table.pack(fill=BOTH,expand=1)
                self.Medical_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
                self.fetch_data()
    
#==============add==============
        def add_data(self):
            if self.var_Are_you_Pregnant.get()=="" or self.var_Are_you_Diabetic.get()=="" :
                   messagebox.showerror("Error","All Fields are required",parent=self.root) 
            else:                                  
                try:
                    conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into iadmit.medical values (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)", (
                                                                                        self.var_Contact_Reference.get(),
                                                                                        self.var_Are_you_Diabetic.get(),
                                                                                        self.var_Are_you_Epileptic.get(),
                                                                                        self.var_Are_you_Asthmatic.get(),
                                                                                        self.var_Are_you_Hypertensive.get(),
                                                                                        self.var_Are_you_Pregnant.get(),
                                                                                        self.var_Do_you_have_Tuberculosis.get(),
                                                                                        self.var_Do_you_have_Cholesterol.get(),
                                                                                        self.var_Do_you_have_a_Heart_Problem.get(),
                                                                                        self.var_Recent_Cough_or_Cold.get(),
                                                                                        self.var_Do_you_Smoke.get(),
                                                                                        self.var_Did_you_take_Medication.get(),
                                                                                        self.var_Name_of_Medication.get()))
                
                               
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Medical Information has been added",parent=self.root)
                except Exception as es:
                     messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


        #fetch data
        def fetch_data(self):
             conn=mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
             my_cursor=conn.cursor()
             my_cursor.execute("select * from medical")
             rows=my_cursor.fetchall()
             if len(rows)!=0:
                 self.Medical_Details_Table.delete(*self.Medical_Details_Table.get_children())
                 for i in rows:
                    self.Medical_Details_Table.insert("",END,values=i)
                 conn.commit()
             conn.close()


        #get cursor
        def get_cuersor(self,event=""):
          cusrsor_row=self.Medical_Details_Table.focus()
          content=self.Medical_Details_Table.item(cusrsor_row)
          row=content["values"]

          #self.var_Contact_Reference.set(row[0]),
          self.var_Are_you_Diabetic.set(row[1]),
          self.var_Are_you_Epileptic.set(row[2]),
          self.var_Are_you_Asthmatic.set(row[3]),
          self.var_Are_you_Hypertensive.set(row[4]),
          self.var_Are_you_Pregnant.set(row[5]),
          self.var_Do_you_have_Tuberculosis.set(row[6]),
          self.var_Do_you_have_Cholesterol.set(row[7]),
          self.var_Do_you_have_a_Heart_Problem.set(row[8]),
          self.var_Recent_Cough_or_Cold.set(row[9]),
          self.var_Do_you_Smoke.set(row[10]),
          self.var_Did_you_take_Medication.set(row[11]),
          self.var_Name_of_Medication.set(row[12])

        #update
        def update(self):
            if self.var_Name_of_Medication.get() == "":
               messagebox.showwarning("Error", "Please enter the name ofM", parent=self.root)
            else:
                try:
                  conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                  my_cursor = conn.cursor()
                  my_cursor.execute("""
                      UPDATE medical 
                      SET `Are you Diabetic`=%s , `Are you Epileptic`=%s , `Are you Asthmatic` =%s , `Are you Hypertensive`=%s,  `Are you Pregnant`=%s,`Do you have Tuberculosis`=%s ,`Do you have Cholesterol`=%s,`Do you have a Heart Problem`=%s, `Recent Cough or Cold`=%s, `Do you Smoke`=%s, `Did you take Medication`=%s, `Name of Medication`=%s WHERE `Contact Reference`=%s""", (                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                        self.var_Are_you_Diabetic.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Are_you_Epileptic.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Are_you_Asthmatic.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Are_you_Hypertensive.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Are_you_Pregnant.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Do_you_have_Tuberculosis.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Do_you_have_Cholesterol.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Do_you_have_a_Heart_Problem.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Recent_Cough_or_Cold.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Do_you_Smoke.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Did_you_take_Medication.get(),
                                                                                                                                                                                                                                                                                                                                                        self.var_Name_of_Medication.get(),
                                                                                                                                                                                                                                                                                                                                                         self.var_Contact_Reference.get()))
                  conn.commit()
                  self.fetch_data()  
                  conn.close()

                  messagebox.showinfo("Update", "Medical details have been updated successfully", parent=self.root)
                except Exception as es:
                 messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

        def mDelete(self):
            mDelete = messagebox.askyesno("iAdmit", "Do you want to delete this medical details", parent=self.root)
            if mDelete > 0:
                conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
                my_cursor = conn.cursor()
                query = "DELETE FROM medical WHERE `Contact Reference` = %s"  
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
                self.var_Are_you_Diabetic.set(""),
                self.var_Are_you_Epileptic.set(""),
                self.var_Are_you_Asthmatic.set(""),
                self.var_Are_you_Hypertensive.set(""),
                self.var_Are_you_Pregnant.set(""),
                self.var_Do_you_have_Tuberculosis.set(""),
                self.var_Do_you_have_Cholesterol.set(""),
                self.var_Do_you_have_a_Heart_Problem.set(""),
                self.var_Recent_Cough_or_Cold.set(""),
                self.var_Do_you_Smoke.set(""),
                self.var_Did_you_take_Medication.set(""),
                self.var_Name_of_Medication.set("")


                x=random.randint(1000,9999)
                self.var_Contact_Reference.set(str(x))

        def search(self):
            conn = mysql.connector.connect(host=os.getenv('DB_HOST'),username=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))
            my_cursor = conn.cursor()

            query = "select * from medical where `"+ str(self.search_var.get()) +"` LIKE '%" + str(self.txt_search.get()) +"%'"
            my_cursor.execute(query)
            rows=my_cursor.fetchall()
            if len (rows)!=0:
                    self.Medical_Details_Table.delete(*self.Medical_Details_Table.get_children())
                    for i in rows:
                        self.Medical_Details_Table.insert("",END,values=i)
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


                        showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2,bg="black")
                        showDataFrame.place(x=400,y=55,width=300,height=196)

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

                      lblGender=Label(showDataFrame,text="Date of Birth:",font=("arial",12,"bold"),bg="black",fg="white")
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
     obj=medical_history(root)
     root.mainloop()