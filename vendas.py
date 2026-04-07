from datetime import datetime
class Vendas:
    def __init__(self, caminho="vendas.json"):
        self.caminho = caminho

    def salvar_venda(self, carrinho):
        try:
            with open(self.caminho, "r") as f:
                dados = json.load(f)
        except:
            dados = []

        venda = {
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "itens": carrinho.itens,
            "total": carrinho.total()
        }

        dados.append(venda)

        with open(self.caminho, "w") as f:
            json.dump(dados, f, indent=4)
