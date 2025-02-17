import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        
        self.resultado = tk.StringVar()
        self.entrada = tk.Entry(root, textvariable=self.resultado, font=('arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)
        
        self.criar_botoes()
    
    def criar_botoes(self):
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]
        
        for (texto, linha, coluna) in botoes:
            self.criar_botao(texto, linha, coluna)
    
    def criar_botao(self, texto, linha, coluna):
        botao = tk.Button(self.root, text=texto, padx=20, pady=20, font=('arial', 18), bd=4, bg='lightgrey')
        
        if texto == '=':
            botao.config(command=self.calcular, bg='lightblue', fg='black')
        elif texto == 'C':
            botao.config(command=self.limpar, bg='red', fg='white')
        else:
            botao.config(command=lambda t=texto: self.adicionar_entrada(t))
        
        botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")
        
        self.root.grid_rowconfigure(linha, weight=1)
        self.root.grid_columnconfigure(coluna, weight=1)
    
    def adicionar_entrada(self, valor):
        atual = self.resultado.get()
        if valor == '×':
            self.resultado.set(atual + '*')  
        elif valor == '÷':
            self.resultado.set(atual + '/')  
        else:
            self.resultado.set(atual + valor)
    
    def calcular(self):
        try:
            resultado = eval(self.resultado.get())
            self.resultado.set(resultado)
        except:
            self.resultado.set("Erro")
    
    def limpar(self):
        self.resultado.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x600") 
    app = Calculadora(root)
    root.mainloop()
