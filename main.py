import math
import tkinter as tk
from tkinter import Label, Entry, Button

class CalculadoraInvestimentos:
    def __init__(self, root):
        self.root = root
        self.root.title("Cavest")

        # Definindo o tamanho fixo da janela
        self.root.geometry("700x300")

        # Variáveis globais
        self.entry_media_dividend_yield = Entry(root)
        self.entry_preco_acao = Entry(root)
        self.entry_lpa = Entry(root)
        self.entry_vpa = Entry(root)
        self.entry_porcentagem_minima_yield = Entry(root)
        self.resultado_text = Label(root, text="")
        self.resultado_text.grid(row=4, column=0, columnspan=2, pady=10)

        self.exibir_tela_principal()

    def is_float(self, value):
        try:
            float(value.replace(",", "."))
            return True
        except ValueError:
            return False

    def formatar_valor(self, valor):
        return f'{valor:,.2f}'.replace(".", ",")

    def ocultar_widgets(self):
        for widget in self.root.winfo_children():
            widget.grid_remove()

    def exibir_tela_principal(self):
        self.root.title("Calculadora de Investimentos")
        self.ocultar_widgets()

        Label(self.root, text="Escolha uma operação:").grid(row=0, column=10, pady=10)

        Button(self.root, text="Yield on Cost", command=self.exibir_tela_yoc).grid(row=1, column=10, pady=5)
        Button(self.root, text="Preço Teto", command=self.exibir_tela_preco_teto).grid(row=2, column=10, pady=5)
        Button(self.root, text="Preço Justo", command=self.exibir_tela_preco_justo).grid(row=3, column=10, pady=5)

    def centralizar_na_tela(self, widget):
        widget.update_idletasks()
        largura = widget.winfo_width()
        altura = widget.winfo_height()
        x = (widget.winfo_screenwidth() // 2) - (largura // 2)
        y = (widget.winfo_screenheight() // 2) - (altura // 2)
        widget.geometry('{}x{}+{}+{}'.format(largura, altura, x, y))

    def exibir_tela_yoc(self):
        self.root.title("Yield on Cost")
        self.ocultar_widgets()

        Label(self.root, text="Média do Dividend Yield (últimos 5 anos):").grid(row=0, column=0, pady=10)
        self.entry_media_dividend_yield.grid(row=0, column=1, pady=10, sticky="ew")

        Label(self.root, text="Preço da Ação:").grid(row=1, column=0, pady=10)
        self.entry_preco_acao.grid(row=1, column=1, pady=10, sticky="ew")

        Button(self.root, text="Calcular", command=self.calcular_e_exibir_resultados_yoc).grid(row=2, column=0, columnspan=2, pady=10)
        Button(self.root, text="Voltar", command=self.exibir_tela_principal).grid(row=3, column=0, columnspan=2, pady=5)

        # Centralizar na tela após os widgets terem sido colocados
        self.centralizar_na_tela(self.root)
       
    def calcular_e_exibir_resultados_yoc(self):
        self.resultado_text.config(text=self.calcular_yoc())
        self.resultado_text.grid(row=4, column=0, columnspan=2, pady=10)

    def exibir_tela_preco_teto(self):
        self.root.title("Preço Teto")
        self.ocultar_widgets()

        Label(self.root, text="Média dos dividendos (últimos 5 anos):").grid(row=0, column=0)
        self.entry_media_dividend_yield.grid(row=0, column=1)

        Label(self.root, text="Porcentagem mínima de Dividend Yield (recomendado 6 ou 7%):").grid(row=1, column=0)
        self.entry_porcentagem_minima_yield.grid(row=1, column=1)

        Button(self.root, text="Calcular", command=self.calcular_e_exibir_resultados_preco_teto).grid(row=2, column=0, columnspan=2, pady=10)
        Button(self.root, text="Voltar", command=self.exibir_tela_principal).grid(row=3, column=0, columnspan=2, pady=5)

    def calcular_e_exibir_resultados_preco_teto(self):
        self.resultado_text.config(text=self.calcular_preco_teto())
        self.resultado_text.grid(row=4, column=0, columnspan=2, pady=10)

    def exibir_tela_preco_justo(self):
        self.root.title("Preço Justo")
        self.ocultar_widgets()

        Label(self.root, text="Preço da Ação:").grid(row=0, column=0)
        self.entry_preco_acao.grid(row=0, column=1)

        Label(self.root, text="Lucro por Ação (LPA):").grid(row=1, column=0)
        self.entry_lpa.grid(row=1, column=1)

        Label(self.root, text="Valor Patrimonial por Ação (VPA):").grid(row=2, column=0)
        self.entry_vpa.grid(row=2, column=1)

        Button(self.root, text="Calcular", command=self.calcular_e_exibir_resultados_preco_justo).grid(row=3, column=0, columnspan=2, pady=10)
        Button(self.root, text="Voltar", command=self.exibir_tela_principal).grid(row=4, column=0, columnspan=2, pady=5)

    def calcular_e_exibir_resultados_preco_justo(self):
        self.resultado_text.config(text=self.calcular_preco_justo())
        self.resultado_text.grid(row=5, column=0, columnspan=2, pady=10)

    def calcular_yoc(self):
        if self.is_float(self.entry_media_dividend_yield.get()) and self.is_float(self.entry_preco_acao.get()):
            media_dividend_yield = float(self.entry_media_dividend_yield.get().replace(",", "."))
            preco_acao = float(self.entry_preco_acao.get().replace(",", "."))
            yoc = media_dividend_yield / preco_acao
            return f'Yield on Cost (YOC): {yoc:.2%}'
        else:
            return "Entradas inválidas"

    def calcular_preco_teto(self):
        if self.is_float(self.entry_media_dividend_yield.get()) and self.is_float(self.entry_porcentagem_minima_yield.get()):
            media_dividend_yield = float(self.entry_media_dividend_yield.get().replace(",", "."))
            porcentagem_minima_yield = float(self.entry_porcentagem_minima_yield.get().replace(",", "."))
            preco_teto = media_dividend_yield / (porcentagem_minima_yield / 100)
            return f'Preço Teto: {self.formatar_valor(preco_teto)}'
        else:
            return "Entradas inválidas"

    def calcular_preco_justo(self):
        if self.is_float(self.entry_preco_acao.get()) and self.is_float(self.entry_lpa.get()) and self.is_float(self.entry_vpa.get()):
            preco_acao = float(self.entry_preco_acao.get().replace(",", "."))
            lpa = float(self.entry_lpa.get().replace(",", "."))
            vpa = float(self.entry_vpa.get().replace(",", "."))
            preco_justo = math.sqrt(preco_acao * lpa * vpa)
            return f'Preço Justo: R${self.formatar_valor(preco_justo)}'
        else:
            return "Entradas inválidas"

# Criando a janela principal
root = tk.Tk()

# Instanciando a classe e iniciando o loop da interface gráfica
calculadora = CalculadoraInvestimentos(root)
root.mainloop()
