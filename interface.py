import PySimpleGUI as sg

intro = [[sg.Text("Bem-vindo ao Calculador de Margem! Pressione o botão para prosseguir. Dúvidas? Leia o informativo clickando no botão 'Info'")], [sg.Button('Iniciar Cálculo')], [sg.Button('Info')]]
info = [[sg.Text('Esse é um programa feito para calcular a margem bruta de um negócio baseado nos parâmetros x, y e z.')],
        [sg.Text('Programação Back-End e Front-End feita por Gabriel Maester, única e exclusivamente em Python.')]]
calc = [[sg.Text('Insira o valor de x')], [sg.Input()],
        [sg.Text('Insira o valor de y')], [sg.Input()],
        [sg.Text('Insira o valor de z')], [sg.Input()]]

windowintro = sg.Window('Calculador de Margem', intro, margins=(100,100))
windowcalc = sg.Window('Calculadora', calc, margins=(100,100))
windowinfo = sg.Window('Informações Gerais', info, margins=(100,100))

while True:
    event_intro, values_intro = windowintro.read()
    if event_intro == 'Iniciar Cálculo':
        windowintro.close()
        windowcalc.read()
        if event_intro == sg.WIN_CLOSED:
            break
    if event_intro == 'Info':
        windowintro.close()
        windowinfo.read()
        if event_intro == sg.WIN_CLOSED:
            break
    else:
        break