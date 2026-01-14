from gui import *

def add_new():
    global order
    

    try:
        summa = int(summa_entry.get())
        if summa <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Viga",
            "Summa peab olema positiivne täisarv!")
        return
    
    andmed[order] ={
        "summa": int(summa_entry.get()),
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
    with open(failinimi, "r") as file:
        reader = csv.DictReader(file)
        output_text.delete("1.0", END)
        for i, row in enumerate(reader, start=1):
            output_text.insert(END, f"list {i}\n")
            output_text.insert(END, f"  summa: {row['summa']}\n")
            output_text.insert(END, f"  Kategooria: {row['kategooria']}\n")
            output_text.insert(END, f"  Kirjeldus: {row['kirjeldus']}\n")
            output_text.insert(END, f"  Tüüp: {row['tyyp']}\n\n")

def csv_faili_salvestamine():
        failinimi = filedialog.asksaveasfilename(
        title="Salvesta CSV fail",
        defaultextension=".csv",
        filetypes=[("CSV failid", "*.csv"), ("Kõik failid", "*.*")]
    )

        fieldnames = ["summa", "kategooria", "kirjeldus", "tyyp"]
        with open(failinimi, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for entry in andmed.values():
                writer.writerow(entry)
