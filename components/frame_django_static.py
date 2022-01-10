from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import *


class FrameDjangoStatic(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(
        borderwidth = 4, 
        relief = "groove"    
        )
        self.master = master
        self.label_django_static = Label(self, 
                                         text = "Caminho da pasta static do app django:", 
                                         font = ("Arial", 13, "bold")
                                         ).pack(fill = "x", padx = 5, pady = 5)
       
      
        self.input_django_static = Entry(self, width = 70, 
                                         font = ("Arial", 15, "bold"),
                                         state = DISABLED,
                                         textvariable = master.caminho_static
                                         )
        self.input_django_static.pack()
        self.button_buscar_static = ttk.Button(self, 
                                           text = "Buscar", 
                                           command = self.buscar_pasta_static
                                           ).pack(pady = 10)
        self.pack(
            side = TOP, 
            fill = BOTH, 
            padx = 10, 
            pady = 5
        )
    
    def buscar_pasta_static(self):
        self.input_django_static.config(state = NORMAL)
        self.input_django_static.delete(0, END)
        self.input_django_static.insert(0, filedialog.askdirectory())
        self.input_django_static.config(state = DISABLED)
        self.master.caminho_static.set(self.input_django_static.get())    
