from email import message
from logging import root
from tkinter import*
from tkinter import messagebox
from turtle import title
from PIL import ImageTk


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Library login page")
        self.root.geometry("1440x900+100+50")
        self.bg=ImageTk.PhotoImage(file="images/book5.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        frame_login=Frame(self.root,bg="white")
        frame_login.place(x=80,y=100,height=400,width=500) 
          
        title=Label(frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)  
        desc=Label(frame_login,text="Teachers Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)


        user_login=Label(frame_login,text="Username",font=("Goudy old style",20,"bold"),fg="#d25d17",bg="white").place(x=90,y=140)
        self.txt_user=Entry(frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)


        passw=Label(frame_login,text="Password",font=("Goudy old style",20,"bold"),fg="#d25d17",bg="white").place(x=90,y=210)
        self.passw=Entry(frame_login,font=("times new roman",15),bg="lightgray")
        self.passw.place(x=90,y=240,width=350,height=35)

        forget=Button(frame_login,text="Forget password",bd=0,bg="white",fg="#d77337",font=("times in roman",12)).place(x=90,y=280)


        Login=Button(self.root,text="Log In",command=self.login_func,bd=0,bg="#d77337",fg="white",font=("times in roman",20)).place(x=250,y=420,width=140,height=40)
 

    def login_func(self):
            if self.passw.get()==""or self.txt_user.get()=="":
                 messagebox.showerror("Error","All fields are required",parent=self.root)
            elif self.passw.get()!="kanchu" or self.txt_user.get()!="kanchu":
                messagebox.showerror("Error","Invalid username/password",parent=self.root)
            else:
                 messagebox.showinfo("welcome",f"Welcome {self.txt_user.get()}\n your pssword {self.passw.get()}",parent=self.root)                      




root=Tk()
obj=Login(root)

root.mainloop()