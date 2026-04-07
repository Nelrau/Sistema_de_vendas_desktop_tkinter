import tkinter as tk, json
from tkinter import ttk
from datetime import datetime

class ClienteFrame(tk.Frame):
   """ Cliente clica produto, Tela pega produto, Tela mostra informações ,Cliente escolhe quantidade,  Tela adiciona ao carrinho, (carrinho fica na memória), Cliente finaliza compra, Tela chama → baixar_estoque(), Sistema atualiza dados, Sistema salva JSON, Tela atualiza interface """
   def __init__(self, parent):
      super().__init__(parent) # Cor para teste
      
      
      self.label = tk.Label(self, text="Área do Cliente")
      self.label.grid(row=2, column=2)
      
      
      with open('produtos.json', 'r') as f:
         self.db = json.load(f)
      
      self.opcao = ttk.Combobox(self, values=list(self.db.keys()))      
      self.opcao.current(0)
      self.opcao.grid(row=2, column=1)
      self.opcao.bind("<<ComboboxSelected>>", self.pegar_produto)
      
      self.area_text = tk.Text(self, width=35, height=7, background='lightgray', font=20)
      self.area_text.grid(row=3, column=1, columnspan=2)
      
      self.carrinho = Carrinho()
      self.carrinho.mostrar(self.area_text)
      
      self.produto = ""
      
      
      self.btn_add = tk.Button(self, text="Adicionar ao Carrinho", command=self.adicionar_carrinho)
      self.btn_add.grid(row=4, column=1)
      
      self.btn_finalizar = tk.Button(self, text="Finalizar Compra", command=self.finalizar_compra)
      self.btn_finalizar.grid(row=4, column=2)
      
   def adicionar_carrinho(self):
      self.carrinho.adicionar(self.produto, f"{self.db[self.produto]['preço']}", self.db[self.produto]['estoque'])
      
      self.carrinho.mostrar(self.area_text)
      
   def finalizar_compra(self):
      if not self.carrinho.itens:
         print("Carrinho vazio")
         return
      

      # baixar estoque
      for item in self.carrinho.itens:
         self.db[item['produto']]['estoque'] -= item['qtd']

      # salvar produtos.json
      with open('produtos.json', 'w') as f:
         json.dump(self.db, f, indent=3)

      # salvar venda
      try:
         with open('vendas.json', 'r') as f:
            vendas = json.load(f)
      except:
         vendas = []

      vendas.append({
        "itens": self.carrinho.itens,
        "total": sum(i['qtd'] * i['preco'] for i in self.carrinho.itens),
        "data": datatime.now().strftime('%d/%m/%Y %H:%M')
    })

      with open('vendas.json', 'w') as f:
         json.dump(vendas, f, indent=3)

      # limpar carrinho
      self.carrinho.limpar()

      # atualizar tela
      self.carrinho.mostrar(self.area_text)

      print("Compra finalizada")
   
   def pegar_produto(self, event=None):
      self.produto = self.opcao.get()
      self.area_text.delete(1.0, tk.END)
      self.area_text.insert(tk.END, f'''{self.produto}
Preço: {self.db[self.produto]['preço']}    Estoque: {self.db[self.produto]['estoque']}
Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}      
Descrição: {self.db[self.produto]['descrição']}''')

class Carrinho:
   def __init__(self):
      self.nome = ""
      self.itens = []
      
      
   def adicionar(self, nome, preco_str, estoque):
      preco = float(preco_str.replace('R$', '').replace(',', '.'))
      for item in self.itens:
         if item['produto'] == nome:
            if item['qtd'] < estoque:               
               item['qtd'] += 1
               print(item['qtd'], estoque)
            return
         
      if estoque > 0:
         self.itens.append({
            "produto": nome,
            "qtd": 1,
            "preco": preco})
      else:
         print('não tem esse produto')


    
   def remover(self, nome):
      
        if item['produto'] == nome:
            item['qtd'] -= 1
            if item['qtd'] <= 0:
                self.itens.remove(item)
            return
   
   def limpar(self):
      self.itens = []
   
   def quantidade(self):
      pass
   
   def total(self):
      return sum(item['qtd'] * item['preço'] for item in self.itens)
   
   def mostrar(self, area_text):
      area_text.delete('1.0', 'end')

      total = self.total()   
      
      for item in self.itens:  
         area_text.insert('end', f"{item['produto']} x{item['qtd']} = {subtotal:.2f}\n")
         area_text.insert('end', f"\nTotal: R$ {total:.2f}")
      
