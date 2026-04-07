import json

class Estoque:
    def __init__(self, caminho="produtos.json"):
        self.caminho = caminho

    def carregar(self):
        with open(self.caminho, "r") as f:
            return json.load(f)

    def salvar(self, dados):
        with open(self.caminho, "w") as f:
            json.dump(dados, f, indent=4)

    def baixar_estoque(self, carrinho):
        dados = self.carregar()

        for item in carrinho.itens:
            for produto in dados["produtos"]:
                if produto["nome"] == item["nome"]:
                    produto["estoque"] -= item["quantidade"]

        self.salvar(dados)
