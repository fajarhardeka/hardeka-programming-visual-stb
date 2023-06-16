import tkinter 
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

# Init
window = tkinter.Tk()
icon_img=PhotoImage(file='C:\\Users\\fajar\\Documents\\python_pv_ti\\asset\\mukbang.png')
window.iconphoto(False, icon_img)
window.configure(bg="teal")
window.geometry("400x350")
window.resizable(False,False)
window.title("Pendaftaran Mukbang")

# Header
header_label = ttk.Label(window, text="Pengisian Formulir", font=(16), background="teal", foreground="white")
header_label.pack(pady=20)

# Variabel and Function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT_RUMAH = tkinter.StringVar()
MAKANAN_FAVORIT = tkinter.StringVar()
MINUMAN_FAVORIT = tkinter.StringVar()
OLAHRAGA_FAVORIT = tkinter.StringVar()

def tombol_click(): 
    if not NAMA_LENGKAP.get() or not ALAMAT_RUMAH.get() or not MAKANAN_FAVORIT.get() or not MINUMAN_FAVORIT.get() or not MAKANAN_FAVORIT.get():
        showinfo(title="Error!", message="Mohon lengkapi semua form!")
    else:
        pesan = f"Hallo {NAMA_LENGKAP.get()}, Kamu sudah terdaftar!"
        showinfo(title="Selamat!",message=pesan)

# frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

# Komponen nama lengkap
nama_depan_label = ttk.Label(input_frame,text="Nama Lengkap :")
nama_depan_label.grid(row=0, column=0, padx=10, pady=5)
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_LENGKAP)
nama_depan_entry.grid(row=0, column=1, padx=10, pady=5)

# Komponen alamat
nama_alamat_label = ttk.Label(input_frame,text="Alamat :")
nama_alamat_label.grid(row=1, column=0, padx=10, pady=5)
nama_alamat_entry = ttk.Entry(input_frame,textvariable=ALAMAT_RUMAH)
nama_alamat_entry.grid(row=1, column=1, padx=10, pady=5)

# Komponen makanan favorit
makanan_fav_label = ttk.Label(input_frame, text="Makanan Favorit :")
makanan_fav_label.grid(row=2, column=0, padx=10, pady=5)
makanan_fav_entry = ttk.Entry(input_frame, textvariable=MAKANAN_FAVORIT)
makanan_fav_entry.grid(row=2, column=1, padx=10, pady=5)

# Komponen minuman favorit
minuman_fav_label = ttk.Label(input_frame, text="Minuman Favorit :")
minuman_fav_label.grid(row=3, column=0, padx=10, pady=5)
minuman_fav_entry = ttk.Entry(input_frame, textvariable=MINUMAN_FAVORIT)
minuman_fav_entry.grid(row=3, column=1, padx=10, pady=5)

# Komponen olahraga favorit
olahraga_fav_label = ttk.Label(input_frame, text="Olahraga Favorit :")
olahraga_fav_label.grid(row=4, column=0, padx=10, pady=5)
olahraga_fav_entry = ttk.Entry(input_frame, textvariable=OLAHRAGA_FAVORIT)
olahraga_fav_entry.grid(row=4, column=1, padx=10, pady=5)

# Button
tombol_daftar = ttk.Button(input_frame,text="Daftar",command=tombol_click)
tombol_daftar.grid(row=5, columnspan=2, padx=10, pady=10)

# Main Loop window
window.mainloop()
