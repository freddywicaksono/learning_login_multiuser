# Tambahkan import ke FrmAdmin, FrmManager, dan FrmOperator
# Tambahkan fungsi new_window

import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox, Menu
from Users import *
from FrmAdmin1 import *
from FrmAdmin2 import *
from FrmAdmin3 import *
from FrmManager1 import *
from FrmManager2 import *
from FrmManager3 import *
from FrmOperator1 import *
from FrmOperator2 import *
from FrmOperator3 import *

class Dashboard:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("600x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.my_w_child = None
        self.aturKomponen()

    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        mainmenu = Menu(self.parent)
        self.parent.config(menu=mainmenu)
        file_menu_awal = Menu(mainmenu)
        file_menu_awal
        # Menu Awal
        file_menu_awal.add_command(
            label='Login', command=self.show_login
        )
        file_menu_awal.add_command(
            label='Exit', command=root.destroy
        )
        
        # Tampilkan menu ke layar
        mainmenu.add_cascade(
            label="File", menu=file_menu_awal
        )    
        

        
    def show_login(self):
        self.my_w_child=tk.Toplevel(root)
        self.my_w_child.geometry("250x200") 
        # pasang Label
        Label(self.my_w_child, text='Username:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)

        Label(self.my_w_child, text="Password:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtUsername = Entry(self.my_w_child) 
        self.txtUsername.grid(row=0, column=1, padx=5, pady=5)

        self.txtPassword = Entry(self.my_w_child) 
        self.txtPassword.grid(row=1, column=1, padx=5, pady=5)  
        self.txtPassword.config(show='*')
                
        # Pasang Button
        self.btnLogin = tk.Button(self.my_w_child, text='Login',
            command=self.onLogin)
        self.btnLogin.grid(row=2, column=1, padx=5, pady=5) 
        
    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = Users()
        B =[]
        A.username = u
        A.password = p
        B = A.Login()
        
        if(B[0]=='True'):           
            if(B[1]=='admin'):
                messagebox.showinfo("showinfo", "Login diterima, Anda login sebagai " + B[1])
            elif(B[1]=='manager'): 
                messagebox.showinfo("showinfo", "Login diterima, Anda login sebagai " + B[1])
            elif(B[1]=='operator'):
                messagebox.showinfo("showinfo", "Login diterima, Anda login sebagai " + B[1])
            else: 
                messagebox.showinfo("showinfo", "Maaf, User tidak dikenal")    
            
        else:
            messagebox.showinfo("showinfo", "Login Tidak Valid")  
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Dashboard(root, "Dashboard Aplikasi")
    root.mainloop() 