from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import *


class FrameDjangoTemplate(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(
        borderwidth = 4, 
        relief = "groove"    
        )
        self.label_django_template = Label(self, 
                                             text = "Caminho da pasta templates do app django:", 
                                             font = ("Arial", 13, "bold")
                                             ).pack(fill = "x", padx = 5, pady = 5)
        self.input_django_template = Entry(self, width = 70, 
                                            font = ("Arial", 15, "bold"), state = DISABLED,
                                            textvariable = master.caminho_template
                                            )
        self.input_django_template.pack()
        self.button_buscar_template = ttk.Button(self, 
                                            text = "Buscar", 
                                            command = self.buscar_pasta_template
                                            ).pack(pady = 10)
        self.pack(
            side = TOP, 
            fill = BOTH, 
            padx = 10, 
            pady = 5
        )

    def buscar_pasta_template(self):
        self.input_django_template.config(state = NORMAL)
        self.input_django_template.delete(0, END)
        self.input_django_template.insert(0, filedialog.askdirectory())
        self.input_django_template.config(state = DISABLED)
        self.master.caminho_template.set(self.input_django_template.get())    
