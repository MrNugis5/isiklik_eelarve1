from tkinter import *
from tkinter import filedialog
import csv
from tkinter import messagebox
windows = Tk()
windows.geometry("600x600")
windows.title("lihtsalt on")

andmed = {}
order = 1
        
output_text = Text(windows, width=50, height=15)
output_text.grid(row=5, column=0, columnspan=6, pady=10)

kulu_tulu_var = StringVar(value="kulu")

kulu_tulu_menu = OptionMenu(
    windows,
    kulu_tulu_var,
    "kulu",
    "tulu"
)
kulu_tulu_menu.grid(row=3, column=1)


#tekst
summa_label = Label(windows, text = "Summa", font=("Calibri", 10, "bold"))
kategooria_label = Label(windows, text = "Kategooria", font=("Calibri", 10, "bold"))
kirjeldus_label = Label(windows, text = "Kirjeldus", font=("Calibri", 10, "bold"))
tyyp_label = Label(windows, text="Tyyp", font=("Calibri", 10, "bold"))

#entry
summa_entry = Entry(windows, font=("Calibri", 10, "bold"))
kategooria_entry = Entry(windows, font=("Calibri", 10, "bold"))
kirjeldus_entry = Entry(windows, font=("Calibri", 10, "bold"))

#buttons
add_new_button = Button(windows, text="add new", command = add_new)
show_all_button = Button(windows, text="show all", command = show_all)
add_summa_button = Button(windows, text="add summa", command = summa)
open_button = Button(windows, text="open", command = csv_faili_avamine)
save_button = Button(windows, text="save", command = csv_faili_salvestamine)

#positsioon
summa_label.grid(row=0, column=0)
kategooria_label.grid(row=1, column=0)
kirjeldus_label.grid(row=2, column=0)
tyyp_label.grid(row=3, column=0)

summa_entry.grid(row=0, column=1)
kategooria_entry.grid(row=1, column=1)
kirjeldus_entry.grid(row=2, column=1)

add_new_button.grid(row=1, column=5)
show_all_button.grid(row=2, column=5)
add_summa_button.grid(row=3, column=5)
open_button.grid(row=1, column=8)
save_button.grid(row=2, column=8)

windows.mainloop()
