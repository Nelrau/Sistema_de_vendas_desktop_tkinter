
from clienteFrame import ClienteFrame
from adminFrame import AdminFrame
import tkinter as tk, json
from tkinter import ttk


class Tela():
   def __init__(self):
      # criação da tela
      self.tela = tk.Tk()
      self.tela.columnconfigure(0, weight=1)
      self.tela.columnconfigure(1, weight=1)
      
      # botão “Adicionar ao carrinho”
      # botão “Finalizar compra”
      
      
      # titulo do app
      self.tela.title('Vendas bot')
      
      # tamanho em pixel
      self.tela.geometry('400x700')
      
      # cor do app
      self.tela.configure(background='lightgreen')

      #titulo label
      self.titulo = tk.Label(self.tela, text='Selecione o produto', background='green', fg='white')
      self.titulo.grid(row=0, column=0, columnspan=2, padx=0)
      
      # frame desligado
      self.container = tk.Frame(self.tela, bd=2, relief=tk.SUNKEN)
      self.container.grid(row=2, column=1, columnspan=2, sticky="nsew")
                
      
      # select de modo(cliente, admin)
      self.modoSelect = ttk.Combobox(self.tela, value=['admin', 'cliente'])
      self.modoSelect.current(0)
      self.modoSelect.grid(row=1, column = 0, columnspan=2, pady=10)
      self.modoSelect.bind("<<ComboboxSelected>>", self.alterar_modo)
      
      
      self.tela.update()
      self.tela.mainloop()
   
   def alterar_modo(self, event=None):
      modo = self.modoSelect.get()
      if modo == 'admin':
         self.mostrar_admin()
         
      elif modo == 'cliente':
         self.mostrar_cliente()
   
   
   def limpar_frame(self):
      # O winfo_children() só funciona se o AdminFrame/ClienteFrame 
      # forem criados passando o 'self.container' como pai.
      for widget in self.container.winfo_children():
         widget.destroy() # Apenas destroy é necessário
         


   def mostrar_cliente(self):
      self.limpar_frame()
      self.frame_atual = ClienteFrame(self.container)
      print(self.frame_atual)
      self.frame_atual.pack(fill="both", expand=True)
      

   def mostrar_admin(self):
      self.limpar_frame()
      self.frame_atual = AdminFrame(self.container)
      print(self.frame_atual)
      self.frame_atual.pack(fill="both", expand=True)
      

if __name__ == '__main__':
   app = Tela()

