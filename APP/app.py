from PySimpleGUI import PySimpleGUI as sg
#modo = input('Digite qual modo deseja, "c" para Criptar e "d" para descriptar:')
Modo =["Criptografar","Descriptografar"]

def Menu():
    layout =[
    [sg.Text('Texto:    '),sg.Input('',key='texto_input',size=(40,5),background_color='white')],
    [sg.Text('Selecione o Modo:'),sg.Combo(Modo,key='modo'),sg.Button('Feito')],
    [sg.Text('Resultado:'),sg.Input('',key='resultado',size=(40,5),background_color='white',text_color='black')],
]
    return sg.Window("Cripto",layout=layout,finalize=True)
janela1 = Menu()

ok=''
while True:
    window, eventos, values = sg.read_all_windows()
    minusculo = ('abcdefghijklmnopqrstuvwxyzçáàãâêéèíìóòõôúùû1234567890!@#$%¨&*()_+=?/\"')
    maiuscula = ('abcdefghijklmnopqrstuvwxyzçáàãâêéèíìóòõôúùû1234567890!@#$%¨&*()_+=?/\"')
    alfabeto = (minusculo) + maiuscula.upper()
    cripto = ''
    descripto = ''
    if eventos == 'Feito':
        if values['modo'] == "Criptografar":
            string = values['texto_input']
            o = len(string)
            oo = int(o)-1
            for letra in string:
                co = alfabeto.find(letra)
                codigo = int(co) + 13
                if letra == ' ':
                    cripto = cripto +' '
                elif codigo > 70:
                    codigo = codigo - 26
                    cripto = cripto + alfabeto[codigo]
                else:
                    cripto = cripto + alfabeto[codigo]
            window['resultado'].update(str(cripto))
        elif values['modo'] == "Descriptografar":
            string = values['texto_input']
            o = len(string)
            for letra in string:
                co = alfabeto.find(letra)
                codigo = int(co) - 13
                if letra == ' ':
                    descripto = descripto + ' '
                elif codigo > 70:
                    codigo = codigo +26
                    descripto = descripto + alfabeto[codigo]
                else:
                    descripto = descripto + alfabeto[codigo]
            window['resultado'].update(descripto)
    elif eventos == 'Fechar' or eventos == sg.WIN_CLOSED:
        break
