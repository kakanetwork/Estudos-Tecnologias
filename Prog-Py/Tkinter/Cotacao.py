import requests

def pegar_cotacoes():
    # Função que requisita a API informações sobre cotação atual 
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    # estou chamando a label com a variável "text" que será completada com a geração do texto
    texto_cotacao["text"] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''


import tkinter as tk

# inicia a janela 
janela1 = tk.Tk() 

# alterar titulo da janela
janela1.title('Cotação atual') 

# label cria o texto na janela (param1 = janela, param2 = texto)
texto_janela = tk.Label(janela1, text="Clique no botão para ver a cotação das moedas") 
# o grid define onde a Label do texto ficara (param1 = coluna, param2 = linha, param3 = espaçamento largura, param4 = espaçamento altura)
texto_janela.grid(column=1, row=0, padx=50, pady=20) 

# criando o botão (param1 = janela, param2 = texto, param3 = comando que o botão executara)
botao = tk.Button(janela1, text="Buscar Cotações", command=pegar_cotacoes)  
botao.grid(column=1, row=2)

texto_cotacao = tk.Label(janela1, text="") # deixo o texto em branco (será preenchido na função)
texto_cotacao.grid(column=1, row=3, pady=20)


janela1.mainloop() # mantém a janela aberta (última linha do código)