from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import *


class FrameReactDist(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(
        borderwidth = 4, 
        relief = "groove"    
        )
        #frame dist react
        self.label_react_dist = Label(self, 
                                      text = "Caminho da pasta dist do app react:", 
                                      font = ("Arial", 13, "bold")
                                      ).pack(fill = "x", padx = 5, pady = 5)
        self.input_react_dist = Entry(  self, 
                                        font = ("Arial", 13, "bold"),
                                        textvariable = master.caminho_react,
                                        state=DISABLED
                                      )
        self.input_react_dist.pack(fill = "x", padx = 5, pady = 5)
        self.button_buscar_dist = ttk.Button(self, 
                                             text = "Buscar", 
                                           command = self.buscar_pasta_react_dist, 
                                           ).pack(pady = 10)
        self.pack(
            side = TOP, 
            fill = BOTH, 
            padx = 10, 
            pady = 5
        )                                
        
    def buscar_pasta_react_dist(self):
        self.input_react_dist.config(state = NORMAL)
        self.input_react_dist.delete(0, END)
        self.input_react_dist.insert(0, filedialog.askdirectory())
        self.input_react_dist.config(state = DISABLED)
        self.master.caminho_react.set(self.input_react_dist.get())    
