from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import *
from components.frame_django_static import FrameDjangoStatic
from components.frame_react_dist import FrameReactDist
from components.frame_mensagem import FrameMensagem
from components.frame_django_template import FrameDjangoTemplate
from compilador import exec_build
import json

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Compilador React Django")
        self.geometry("800x600")
        self.resizable(False, False)
        self.estilo = Style()
        self.estilo.configure('my.TButton7', font = ('arial', 20, 'bold'))
        self.estilo.theme_use('clam')
        self.mensagem = StringVar(self)
        self.caminho_static = StringVar(self)
        self.caminho_template = StringVar(self)
        self.caminho_react = StringVar(self)
        self.erro = BooleanVar(self, False)
        try:
            with open ("config.json") as arquivo:
                json_data = json.load(arquivo)
                self.caminho_static.set(json_data['caminho_static'])
                self.caminho_template.set(json_data['caminho_template'])
                self.caminho_react.set(json_data['caminho_react'])
        except:
            pass
        #titulo
        self.label_titulo = Label(self, 
                                  text = "Compilador React Django", 
                                  font = ("arial", 25, 'bold')).pack()
        

        self.frame_django_static = FrameDjangoStatic(self)
        self.frame_django_template = FrameDjangoTemplate(self)
        self.frame_react_static = FrameReactDist(self)        
        self.botao_compilar = Button(self, 
                                    text = "Compilar", 
                                    style = "big.TButton",   
                                    command = self.compilar, 
                                    ).pack(pady = 10)
        self.frame_mensagem = FrameMensagem(self)
        self.estilo.configure('big.TButton', font=("arial", 20, "bold"), foreground="blue4")

    def compilar(self):
        if self.frame_django_static.input_django_static.get(
            ) == '' or self.frame_django_template.input_django_template.get(
            ) == '' or self.frame_react_static.input_react_dist.get() == '':
            self.mensagem.set('Preencha todos os campos')
        else:
            self.mensagem.set('Compilando...')
            exec_build(self, self.frame_django_static.input_django_static.get(),
                       self.frame_django_template.input_django_template.get(), 
                       self.frame_react_static.input_react_dist.get())
            
        self.frame_mensagem.refresh()
                           

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
