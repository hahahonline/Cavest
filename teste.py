import yfinance as yf
from datetime import datetime, timedelta

# Símbolo da ação
simbolo = 'BBDC4.SA'

# Preço atual da ação
preco_atual = 13.67

# Obter os dividendos da ação
acao = yf.Ticker(simbolo)
dividendo_total = 0
for ano in range(5):
    data_inicio = (datetime.now() - timedelta(days=(ano+1)*365)).strftime('%Y-%m-%d')
    data_fim = (datetime.now() - timedelta(days=ano*365)).strftime('%Y-%m-%d')
    historico = acao.history(start=data_inicio, end=data_fim)
    if not historico.empty:
        dividendo_anual = historico['Dividends'].sum()
        print(f"Dividendos para {simbolo} no ano {datetime.now().year - ano}: {dividendo_anual}")
        dividendo_total += dividendo_anual

# Calcular e imprimir o Yield on Cost
yoc = (dividendo_total / 5) / preco_atual
print(f"Yield on Cost para {simbolo}: {yoc}")