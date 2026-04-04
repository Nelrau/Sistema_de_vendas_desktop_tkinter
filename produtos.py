import json
class Produto:
   def __init__(self, arquivo = 'produtos.json'):
      self.arquivo = arquivo
      self.produtos = self.carregar()
      for nome, dados in self.produtos.items():
         if "estoque" not in dados:
            dados["estoque"] = 0

   def carregar(self):
      try:
         with open(self.arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
      except FileNotFoundError:
         return {}
      
   def add_produto(self, nome, preco, estoque = 0, descricao = ''):
      self.produtos[nome] = {
            "preço": preco,
            "descrição": descricao,
            "estoque": estoque
        }
      self.salvar()
       
   def salvar(self):
      with open(self.arquivo, 'w', encoding='utf-8') as f:
         json.dump(self.produtos, f, indent=4, ensure_ascii=False)
    
   def editar_estoque(self, nome, quantidade):
      
      if nome in self.produtos:
         self.produtos[nome]["estoque"] += quantidade

         if self.produtos[nome]["estoque"] < 0 :
            self.produtos[nome]["estoque"] = 0
            

         self.salvar()
         return "Estoque atualizado"
    
      return "Produto não encontrado"
        
   def get_produto(self, nome):
      return self.produtos.get(nome, None)  

if __name__ == '__main__':
   with open('produtos.json', 'r') as f:
      produtos = json.load(f)
   nome = list(produtos.keys())
   produto = Produto()
