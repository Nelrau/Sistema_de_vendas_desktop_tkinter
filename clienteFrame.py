import tkinter as tk

class ClienteFrame(tk.Frame):
   def __init__(self, parent):
      super().__init__(parent) # Cor para teste
     
      self.label = tk.Label(self, text="Área do Cliente")
      self.label.grid(row=2, column=2)
#Cliente clica produto
      #↓
# Tela pega produto
      #↓
# Tela mostra informações

#Cliente escolhe quantidade
     # ↓
# Tela adiciona ao carrinho
    #  ↓
# (carrinho fica na memória)

# Cliente finaliza compra
   #   ↓
# Tela chama → baixar_estoque()
  #    ↓
# Sistema atualiza dados
 #     ↓
# Sistema salva JSON
#      ↓
# Tela atualiza interface
