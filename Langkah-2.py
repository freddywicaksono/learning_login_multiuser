
# Menambahkan Fungsi aturKomponen serta memanggil fungsi tersebut dari fungsi __init__
# Fungsi aturKomponen ini berisi menu awal login dan exit
# Tambahkan fungsi show_login walaupun masih kosong

import tkinter as tk
from tkinter import Frame, YES, BOTH, Menu

class Dashboard:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("600x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

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
        pass
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Dashboard(root, "Dashboard Aplikasi")
    root.mainloop() 