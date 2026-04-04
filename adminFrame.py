import tkinter as tk, json
from tkinter import ttk
from produtos import Produto

class AdminFrame(tk.Frame):
   def __init__(self, parent):
      super().__init__(parent) # Cor para teste
      
        

   #Admin ativa modo admin
   #     ↓
   #Tela libera funções de admin

   #Admin escolhe produto
   #     ↓
   #Tela chama → editar_estoque()
   #     ↓
   #Sistema altera estoque
   #     ↓
   #Sistema salva JSON
   #     ↓
   #Tela atualiza interface
      with open('produtos.json', 'r') as f:
         self.db = json.load(f)
      self.opcao = ttk.Combobox(self, values=list(self.db.keys()))
      self.opcao.current(0)
      self.opcao.grid(row=2, column=1)

      self.area_text = tk.Text(self, width=35, height=7, background='lightgray', font=20)
      self.area_text.grid(row=3, column=1, columnspan=2)

      self.opcao.bind("<<ComboboxSelected>>", self.pegar_produto)
            
      btn_estoque = tk.Button(self, text='Editar Estoque', command=self.editar_estoque)
      btn_estoque.grid(row=5, column=2)
      
      self.input_qtd = tk.Entry(self)
      self.input_qtd.grid(row=5, column=1)
   
   
   
   def pegar_produto(self, event=None):
      self.atualizar_tela()
      selecionado = self.opcao.get()
      print(self.opcao.get())
      self.area_text.delete('1.0', tk.END)
      
      self.area_text.insert(tk.END, f'''{selecionado}
      Preço: {self.db[selecionado]['preço']}
      Descrição: {self.db[selecionado]['descrição']}
      Estoque: {self.db[selecionado]['estoque']}''')
      
   def editar_estoque(self):
      
      selecionado = self.opcao.get()
      
      self.qtd = self.input_qtd.get()
      if not self.qtd:
         self.qtd = 0
      self.produtos = Produto()
      resultado = self.produtos.editar_estoque(selecionado, int(self.qtd))

      self.area_text.delete('1.0', tk.END)
      self.area_text.insert(tk.END, resultado)
      self.atualizar_tela()
    
    
   def atualizar_tela(self):
      with open('produtos.json', 'r') as f:
         self.db = json.load(f)
      selecionado = self.opcao.get()

      if selecionado in self.db:
         dados = self.db[selecionado]

         self.area_text.delete('1.0', tk.END)
         self.area_text.insert(tk.END, f'''{selecionado} Preço: {dados['preço']}Descrição: {dados['descrição']}
Estoque: {dados['estoque']}''')
      
      
