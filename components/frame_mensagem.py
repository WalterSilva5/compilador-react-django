from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import *

class FrameMensagem(Frame):
    def __init__(self, master, danger=False, **kwargs):
        super().__init__(
        borderwidth = 4, 
        relief = "groove"    
        )
        
        cor_texto = "red" if  master.erro.get() else "green"
        self.label_mensagem = Label(self, 
                                    text = master.mensagem.get(),
                                    font = ("arial", 10, 'bold'), 
                                    width = 50, 
                                    foreground = cor_texto
                                    ).pack(
                                        side = TOP, 
                                        fill = BOTH, 
                                        padx = 10, 
                                        pady = 10
                                    )
        self.pack(
                side = TOP, 
                fill = BOTH,
                padx = 10, 
                pady = 5
            )

    
    def refresh(self):
        self.destroy()        
        self.__init__(self.master)
    