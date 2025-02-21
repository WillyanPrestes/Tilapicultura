from tkinter import *
from tkinter.ttk import *


'''
window = Tk()
window.geometry('350x200')

window.title("Welcome to LikeGeeks app")


lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

#txt = Entry(window, width=30, state='disabled')
#txt.grid(column=1, row=0)
#txt.focus()

#combo = Combobox(window)
#combo['values'] = (1,2,3,4,"text")
#combo.current(1) #set the selected item
#combo.grid(column=0, row=0)

#btn = Button(window, text="Click Me", bg="orange", fg="red",command=clicked)
#btn.grid(column=2, row=0)


#chk_state = BooleanVar()
#chk_state.set(False) #set check state
#chk = Checkbutton(window, text='check box', var=chk_state)
#chk.grid(column=1, row=0)
#chk_state = IntVar()
#chk_state.set(0) #uncheck
#chk_state.set(1) #check

selected = IntVar()


def clicked():
    lbl.configure(text="Bem vindo-"+str(selected.get()))


rad1 = Radiobutton(window,text='First', name="radio1", value=1, variable=selected)
rad1.grid(column=0,row=1)

rad2 = Radiobutton(window,text='Second', name="radio2", value=0, variable=selected)
rad2.grid(column=1, row=1)

btn=Button(window,text="botao",command=clicked)
btn.grid(column=1,row=2)

spin =Spinbox(window, from_=0, to=100, width=5)
spin1 = Spinbox(window, values=(3, 8, 11), width=5)
var =IntVar()

var.set(36)
spin2 = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin2.grid(column=2, row=2)



window.mainloop()
'''
"""
import tkinter as tk

def validate_input(*args):
    value = entry_var.get()

    # Remove todos os caracteres que não são números ou um ponto decimal
    value = ''.join(char for char in value if char.isdigit() or char == '.')

    # Garante que haja apenas um ponto decimal
    if value.count('.') > 1:
        value = value[:value.rfind('.')]

    # Garante que o valor seja exibido no formato "0.00"
    if not value:
        value = "0.00"
    elif value.count('.') == 0:
        value += ".00"
    elif value.index('.') == 0:
        value = "0" + value

    entry_var.set(value)

root = tk.Tk()

entry_var = tk.StringVar()
entry_var.trace("w", validate_input)  # Chama a função validate_input quando o valor muda

entry = tk.Entry(root, textvariable=entry_var)
entry.pack()

root.mainloop()
"""


import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Treeview demo')
        self.geometry('620x200')

        self.tree = self.create_tree_widget()

    def create_tree_widget(self):
        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # adding an item
        tree.insert('', tk.END, values=('John', 'Doe', 'john.doe@email.com'))

        # insert a the end
        tree.insert('', tk.END, values=('Jane', 'Miller', 'jane.miller@email.com'))

        # insert at the beginning
        tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))

        tree.bind('<<TreeviewSelect>>', self.item_selected)

        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            self.tree.delete(selected_item)


if __name__ == '__main__':
    app = App()
    app.mainloop()