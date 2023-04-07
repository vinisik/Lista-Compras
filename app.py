import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Lista de Compras")

        #Area para adicionar novos itens a lista
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Botao para adicionar item a lista
        self.add_button = tk.Button(master, text="Adicionar", command=self.add_item)
        self.add_button.pack()

        #Botao para remover um item da lista

        self.remove_button = tk.Button(master, text="Remover", command=self.remove_item)
        self.remove_button.pack()

        # Botao para salvar a lista em um arquivo de texto
        self.save_button = tk.Button(master, text="Salvar", command=self.save_list)
        self.save_button.pack()

        # Area para exibir a lista de compras
        self.listbox = tk.Listbox(master)
        self.listbox.pack()

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
