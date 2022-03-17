from PySimpleGUI import PySimpleGUI as sg


def interface(valor_final, v1, v2, v3):
    soma = int()
    sg.theme('Reddit')
    layout = [
        [sg.T('Valor aleatório: ' + str(valor_final)), sg.Sizer(120, 50)],
        [sg.T('Valor somado até agora: ' + str(soma))],
        [sg.T('Valores Disponíveis: '),
         sg.T('[' + str(v1) + ']'),
         sg.T('[' + str(v2) + ']'),
         sg.T('[' + str(v3) + ']')],
        [sg.T('Entrada de valores:  '), sg.I(key='valor_digitado', size=(10, 1))],
        [sg.B('Enviar'), sg.B('Sair')]
    ]

    janela = sg.Window('Jogo da soma', layout)
    eventos, valores = janela.read()

    if eventos in [sg.WINDOW_CLOSED, 'Sair']:
        sg.popup('[Obrigado por jogar!]', no_titlebar=True)
        exit()

    if eventos == 'Enviar':
        if int(valores['valor_digitado']) in [v1, v2, v3]:
            soma += int(valores['valor_digitado'])
            print(soma)

        else:
            sg.popup('[ERRO] Valor não disponivel!', no_titlebar=True)
            soma = 0
            exit()