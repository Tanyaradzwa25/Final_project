from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from admission import admission_Win
from medical import medical_history
from surgical import surgical_history
from hospitals import hospitals


class iadmitapp:
    def __init__(self,root):
        self.root=root
        self.root.title("iadmit-app")
        self.root.geometry("1550x800+0+0")

        # ============1st image=================

        img1=Image.open(r"C:\Users\amand\Desktop\iadmit-app\top.jpg")
        img1=img1.resize((1550, 150), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        Iblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        Iblimg.place(x=0,y=0,width=1550,height=140)

        # ==============logo===================

        img2=Image.open(r"C:\Users\amand\Desktop\iadmit-app\logo final.png")
        img2=img2.resize((220, 130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        Iblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        Iblimg.place(x=0,y=0,width=230,height=140)

        # ==========Title=============
        IbI_title=Label(self.root,text="ONLINE HOSPITAL ADMSSION",font=("times new roman",40,"bold"),bg="orange",fg="black",bd=4,relief=RIDGE)
        IbI_title.place(x=0,y=140,width=1550,height=50)

        #=============Main Frame===========
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #==============Menu===========
        IbI_menu=Label(main_frame,text="MENU",font=("times new roman",30,"bold"),bg="orange",fg="black",bd=4,relief=RIDGE)
        IbI_menu.place(x=0,y=0,width=230)

        #=============Btn Frame===========
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=70,width=228,height=200)

        admission_btn=Button(btn_frame,text="PERSONAL DETAILS",command=self.admission_details,width=18,font=("times new roman",15,"bold"),bg="orange",fg="black",bd=0,cursor="hand1")
        admission_btn.grid(row=0,column=0,padx=0,pady=1)

        medical_btn=Button(btn_frame,text="MEDICAL HISTORY",command=self.medical_history,width=18,font=("times new roman",15,"bold"),bg="orange",fg="black",bd=0,cursor="hand1")
        medical_btn.grid(row=1,column=0,padx=0,pady=1)

        surgical_history_btn=Button(btn_frame,text="SURGICAL HISTORY",command=self.surgical_history,width=18,font=("times new roman",15,"bold"),bg="orange",fg="black",bd=0,cursor="hand1")
        surgical_history_btn.grid(row=2,column=0,padx=0,pady=1)

        hospitals_btn=Button(btn_frame,text="HOSPITALS",command=self.hospitals,width=18,font=("times new roman",15,"bold"),bg="orange",fg="black",bd=0,cursor="hand1")
        hospitals_btn.grid(row=3,column=0,padx=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=18,font=("times new roman",15,"bold"),bg="orange",fg="black",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,padx=0,pady=0)

        #===========right side image==========

        img3=Image.open(r"C:\Users\amand\Desktop\iadmit-app\hospital.jpg")
        img3=img3.resize((1310, 590), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        Iblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        Iblimg1.place(x=225,y=0,width=1310,height=590)

        #=========down images============
 
        img4=Image.open(r"C:\Users\amand\Desktop\iadmit-app\surg.jpg")
        img4=img4.resize((230, 210), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        Iblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        Iblimg1.place(x=0,y=255,width=230,height=190)

        img5=Image.open(r"C:\Users\amand\Desktop\iadmit-app\xray.jpg")
        img5=img5.resize((230, 190), Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        Iblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        Iblimg1.place(x=0,y=420,width=230,height=190)

    def admission_details(self):
        self.new_window=Toplevel(self.root)
        self.app=admission_Win(self.new_window)   

 
    def medical_history(self):
        self.new_window=Toplevel(self.root)
        self.app=medical_history(self.new_window)
        
 
    def surgical_history(self):
        self.new_window=Toplevel(self.root)
        self.app=surgical_history(self.new_window)


    def hospitals(self):
         self.new_window=Toplevel(self.root)
         self.app=hospitals(self.new_window)

   
    def logout(self):
        self.root.destroy()
          

 


if __name__=="__main__": 
    root=Tk()
    obj=iadmitapp(root)
    root.mainloop()   
    

