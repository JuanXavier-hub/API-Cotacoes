import PySimpleGUI as sg
import requests

# layout da janela
sg.theme('LightGrey') #Tema da janela

# Listagem das cotações dentro do painel
cotacoes = [
           [sg.Text('USD/BRL:', s=(10, 0), font = ('Arial', 30)), sg.Text('', s=(10, 0), font = ('Arial', 30), key = 'dolar')],
           [sg.Text('EUR/BRL:', s=(10, 0), font = ('Arial', 30)), sg.Text('', s=(10, 0), font = ('Arial', 30), key = 'euro')],
           [sg.Text('BTC/BRL:', s=(10, 0), font = ('Arial', 30)), sg.Text('', s=(10, 0), font = ('Arial', 30), key = 'bitcoin')],
           ]

# Posicionamento dos elementos dentro da janela
layout = [
         [sg.Text("Cotações de mercado\n", s=(20, 0), font = ('Arial', 30), justification = 'c')],
         [sg.Pane([sg.Column(cotacoes)], pad = 2, relief = sg.RELIEF_SUNKEN, border_width = 2, expand_x = True)],
         [sg.Text(key = 'mensagem')],
         [sg.Button('Sair', s = (10, 1))]
         ]

# Inicialização da janela
janela = sg.Window("Cotação USD/BRL",layout).Finalize()

# Manipulação de valores
while True:
    event, values = janela.Read(timeout=500)
    if event == "Sair" or event == sg.WIN_CLOSED:
        break
    moedas = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    if moedas:
        moedas = moedas.json()
        preco_USD = moedas ['USDBRL']['bid']
        preco_EUR = moedas ['EURBRL']['bid']
        preco_BTC = moedas ['BTCBRL']['bid']
        janela['dolar'].update('{}'.format(preco_USD) + ' R$')
        janela['euro'].update('{}'.format(preco_EUR) + ' R$')
        janela['bitcoin'].update('{}'.format(preco_BTC) + ' R$')
    else:
        janela['mensagem'].update("Sem comunicação com o servidor")

#Fechamento da janela após saída do loop
janela.close()
