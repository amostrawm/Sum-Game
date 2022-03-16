from PySimpleGUI import PySimpleGUI as sg
from random import randint


def layout(valor_final):
    # Criação do layout
    soma = int()
    sg.theme('Reddit')
    layoutmenu = [
        [sg.Text('Valor aleatório: '), sg.Text(valor_final), sg.Sizer(120, 50)],
        [sg.Text('Valores somados até agora: ' + str(soma))],
        [sg.Text('Valores Disponíveis: ')],
        [sg.Button(str(b1())), sg.Sizer(7, 20)
            , sg.Button(str(b2())), sg.Sizer(7, 20)
            , sg.Button(str(b3())), sg.Sizer(5, 20)]
    ]
    tela = sg.Window('Jogo da Soma', layoutmenu)
    eventos, valores = tela.read()
    # Leitura de eventos
    if eventos == sg.WINDOW_CLOSED:
        exit()
    if eventos == 'Valor 1: ':
        soma += b1()
        print(b1())


def b1():
    v1 = randint(1, 5)
    return v1


def b2():
    v2 = randint(6, 10)
    return v2


def b3():
    v3 = randint(11, 15)
    return v3