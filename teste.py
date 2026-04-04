import tkinter as tk
from tkinter import ttk
from clienteFrame import ClienteFrame
from adminFrame import AdminFrame
class Tela():
   def __init__(self):

      self.tela = tk.Tk()
      self.tela.title('Vendas bot')
      self.tela.geometry('400x700')
      self.tela.configure(background='lightgreen')

      self.btn = tk.Button(self.tela, text='ativar', state=tk.NORMAL, command=self.ativar)
      self.btn.grid(row=0)
      
      
      
      self.btnd = tk.Button(self.tela, text='desativar', state=tk.NORMAL, command=self.ativar)
      self.btnd.grid(row= 0, column=1)
      
      
      self.tela.mainloop()


   def ativar (self):
      print(self.btn['state'])
      if str(self.btn['state']) == 'normal' and not self.btn.winfo_viewable():
         # self.btn['state'] = tk.NORMAL
         # self.btnd['state'] = tk.DISABLED
         self.btn.grid(row= 0, column=1)          # Mostra o Ativar
         self.btnd.grid_remove()  # Esconde o Desativar
        
      else:
         # self.btn['state'] = tk.DISABLED
         # self.btn['state'] = tk.NORMAL
         self.btn.grid_remove()   # Esconde o Ativar
         self.btnd.grid(row=0)         # Mostra o Desativar
             
    
Tela()
