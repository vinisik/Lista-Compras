import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Lista de Compras")
        master.geometry("400x400")

        # widgets ttk

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", padding=10, font=("Helvetica", 10))
        self.style.configure("TEntry", padding=10, font=("Helvetica", 12))
        self.style.configure("TLabel", padding=10, font=("Helvetica", 12))
        self.style.configure("TListbox", padding=10, font=("Helvetica", 12))

        #Area para adicionar novos itens a lista
        self.entry = ttk.Entry(master)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        # Botao para adicionar item a lista
        self.add_button = ttk.Button(master, text="Adicionar", command=self.add_item)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        #Botao para remover um item da lista

        self.remove_button = ttk.Button(master, text="Remover", command=self.remove_item)
        self.remove_button.grid(row=0, column=2, padx=10, pady=10)

        # Botao para salvar a lista em um arquivo de texto
        self.save_button = ttk.Button(master, text="Salvar", command=self.save_list)
        self.save_button.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

        # Area para exibir a lista de compras
        self.listbox = tk.Listbox(master, height=15)
        self.listbox.grid(row=2, column=0, padx=10, pady=10, columnspan=3, sticky="NSEW")

        # Tornando a grade responsiva
        master.grid_rowconfigure(2, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)

        # Carrega uma lista existente
        self.load_list()

    def load_list(self):
        try:
            with open("lista.txt", "r") as f:
                items = f.readlines()
                for item in items:
                    self.listbox.insert(tk.END, item.strip())
        except FileNotFoundError:
            pass

    def add_item(self):
        item = self.entry.get()
        self.listbox.insert(tk.END, item)
        self.entry.delete(0, tk.END)

    def remove_item(self):
        selection = self.listbox.curselection()
        if selection:
            self.listbox.delete(selection)

    def save_list(self):
        items = self.listbox.get(0, tk.END)
        with open("lista.txt", "w") as f:
            for item in items:
                f.write(item + "\n")

root = tk.Tk()
app = App(root)
root.mainloop()
