import yfinance as yf
from datetime import datetime, timedelta

def calcular_yoc(simbolos_acoes):
    # Dicionário para armazenar os dividendos
    yoc_acoes = {}

    # Obter os dividendos das ações
    for simbolo in simbolos_acoes:
        acao = yf.Ticker(simbolo)
        dividendo_total = 0
        for ano in range(5):
            data_inicio = (datetime.now() - timedelta(days=(ano+1)*365)).strftime('%Y-%m-%d')
            data_fim = (datetime.now() - timedelta(days=ano*365)).strftime('%Y-%m-%d')
            historico = acao.history(start=data_inicio, end=data_fim)
            if not historico.empty:
                dividendo_total += historico['Dividends'].sum()
            else:
                print(f"Não foi possível obter o histórico de dividendos para {simbolo} no ano {ano+1}")
        historico = acao.history(period="1d")
        if not historico.empty:
            preco_atual = historico['Close'].iloc[0]
            yoc = dividendo_total / 5 / preco_atual * 100  # Convertendo para porcentagem
            yoc_acoes[simbolo] = f"{yoc:.2f}%"  # Formatando como porcentagem
        else:
            print(f"Não foi possível obter o preço atual para {simbolo}")

    return yoc_acoes