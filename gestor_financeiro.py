import json
import os
from datetime import datetime

class Transacao:
    """Representa uma única transação financeira."""
    def __init__(self, descricao, valor, categoria):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def para_dicionario(self):
        return {
            "descricao": self.descricao,
            "valor": self.valor,
            "categoria": self.categoria,
            "data": self.data
        }

class GerenciadorFinanceiro:
    """Gerencia as transações e o salvamento de dados."""
    def __init__(self, arquivo='dados_financeiros.json'):
        self.arquivo = arquivo
        self.transacoes = self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as f:
                return json.load(f)
        return []

    def salvar_dados(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.transacoes, f, indent=4)

    def adicionar_transacao(self, descricao, valor, categoria):
        nova_transacao = Transacao(descricao, valor, categoria)
        self.transacoes.append(nova_transacao.para_dicionario())
        self.salvar_dados()
        print(f"✅ Transação '{descricao}' registrada com sucesso!")

    def resumo_por_categoria(self):
        resumo = {}
        for t in self.transacoes:
            cat = t['categoria']
            resumo[cat] = resumo.get(cat, 0) + t['valor']
        return resumo

if __name__ == "__main__":
    print("-" * 40)
    print("Controle Financeiro Pessoal")
    print("-" * 40)
    
    app = GerenciadorFinanceiro()
    
    # Descomente as linhas abaixo para adicionar dados de exemplo na primeira execução:
    # app.adicionar_transacao("Compra de Livros", -150.00, "Educação")
    # app.adicionar_transacao("Bolsa Auxílio", 1200.00, "Renda")
    # app.adicionar_transacao("Mensalidade Academia", -120.00, "Saúde")
    
    print("\nResumo do seu Saldo por Categoria:")
    resumo = app.resumo_por_categoria()
    
    if not resumo:
        print("Nenhuma transação registrada ainda.")
    else:
        for categoria, total in resumo.items():
            print(f"> {categoria}: R$ {total:.2f}")
