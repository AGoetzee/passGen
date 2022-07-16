import PySimpleGUI as sg

import GenPwd

# sg.theme('DarkAmber')
layout = [[sg.Text('Python Password Generator', auto_size_text=True)],
          [sg.Text('By Arthur Goetzee, v0.1', auto_size_text=True, )],
          [sg.HorizontalSeparator()],
          [sg.Text('Character sets to include:')],
          [sg.Checkbox('Uppercase', default=True, key='-upper-'),
           sg.Checkbox('Lowercase', default=True, key='-lower-')],
          [sg.Checkbox('Special characters', default=True, key='-special-'),
           sg.Checkbox('Numbers', default=True, key='-numbers-')],
          [sg.Slider(range=(4, 32), default_value=8, orientation='horizontal', key='-length-')],
          [sg.HorizontalSeparator()],
          [sg.Button('Generate!'), sg.Button('Quit')],
          [sg.Output(size=(40, 15))]]

# Create the Window
window = sg.Window('Password Generator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':  # if user closes window or clicks cancel
        break

    pwd = GenPwd.run((values['-lower-'], values['-upper-'], values['-special-'], values['-numbers-']),
                     int(values['-length-']))
    print(pwd)

window.close()
