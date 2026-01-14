from tkinter import *
from tkinter import filedialog, messagebox
import csv


windows = Tk()
windows.geometry("600x600")
windows.title("Isiklik eelarve")


# Data storage
andmed = {}
order = 1


# Widgets
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

# tekst
summa_label = Label(windows, text="Summa", font=("Calibri", 10, "bold"))
kategooria_label = Label(windows, text="Kategooria", font=("Calibri", 10, "bold"))
kirjeldus_label = Label(windows, text="Kirjeldus", font=("Calibri", 10, "bold"))
tyyp_label = Label(windows, text="Tüüp", font=("Calibri", 10, "bold"))

# entry
summa_entry = Entry(windows, font=("Calibri", 10, "bold"))
kategooria_entry = Entry(windows, font=("Calibri", 10, "bold"))
kirjeldus_entry = Entry(windows, font=("Calibri", 10, "bold"))


def trukita_taht_haaval(text, index=0):
    if index < len(text):
        output_text.insert(END, text[index])
        windows.after(10, trukita_taht_haaval, text, index + 1)


def add_new():
    global order
    try:
        summa = int(summa_entry.get())
        if summa <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Viga", "Summa peab olema positiivne täisarv!")
        return

    andmed[order] = {
        "summa": summa,
        "kategooria": kategooria_entry.get(),
        "kirjeldus": kirjeldus_entry.get(),
        "tyyp": kulu_tulu_var.get()
    }

    order += 1

    summa_entry.delete(0, END)
    kategooria_entry.delete(0, END)
    kirjeldus_entry.delete(0, END)


def show_all():
    output_text.delete("1.0", END)
    kogu_tekst = ""
    for k, v in andmed.items():
        kogu_tekst += f"list {k}\n"
        kogu_tekst += f"  summa: {v['summa']}\n"
        kogu_tekst += f"  Kategooria: {v['kategooria']}\n"
        kogu_tekst += f"  Kirjeldus: {v['kirjeldus']}\n"
        kogu_tekst += f"  Tüüp: {v['tyyp']}\n\n"

    trukita_taht_haaval(kogu_tekst)


def summa():
    kokku = 0
    for v in andmed.values():
        amount = int(v["summa"])
        if v["tyyp"] == "tulu":
            kokku += amount
        elif v["tyyp"] == "kulu":
            kokku -= amount
    output_text.insert(END, f"Kogusumma: {kokku}\n")


def csv_faili_avamine():
    failinimi = filedialog.askopenfilename(
        title="Vali CSV fail",
        filetypes=[("CSV failid", "*.csv"), ("Kõik failid", "*.*")]
    )

    if not failinimi:
        return
    with open(failinimi, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        output_text.delete("1.0", END)
        for i, row in enumerate(reader, start=1):
            output_text.insert(END, f"list {i}\n")
            output_text.insert(END, f"  summa: {row.get('summa','')}\n")
            output_text.insert(END, f"  Kategooria: {row.get('kategooria','')}\n")
            output_text.insert(END, f"  Kirjeldus: {row.get('kirjeldus','')}\n")
            output_text.insert(END, f"  Tüüp: {row.get('tyyp','')}\n\n")


def csv_faili_salvestamine():
    failinimi = filedialog.asksaveasfilename(
        title="Salvesta CSV fail",
        defaultextension=".csv",
        filetypes=[("CSV failid", "*.csv"), ("Kõik failid", "*.*")]
    )

    if not failinimi:
        return

    fieldnames = ["summa", "kategooria", "kirjeldus", "tyyp"]
    with open(failinimi, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in andmed.values():
            writer.writerow(entry)


# buttons
add_new_button = Button(windows, text="add new", command=add_new)
show_all_button = Button(windows, text="show all", command=show_all)
add_summa_button = Button(windows, text="add summa", command=summa)
open_button = Button(windows, text="open", command=csv_faili_avamine)
save_button = Button(windows, text="save", command=csv_faili_salvestamine)

# positsioon
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
