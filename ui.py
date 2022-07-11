import PySimpleGUI as sg
import GenPwd

# sg.theme('DarkAmber')
layout = [  [sg.Text('Python Password Generator')],
            [sg.Text('By Arthur Goetzee, v0.1')],
            [],
            [sg.Checkbox('Uppercase',default=True),sg.Checkbox('Lowercase',default=True)],
            [sg.Checkbox('Special characters',default=True), sg.Checkbox('Numbers',default=True)],
            [sg.Slider(range=(4,32),default_value=8,orientation='horizontal')],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Output(size=(60,15))] ]

# Create the Window
window = sg.Window('Password Generator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print(values)
    print(GenPwd.run((values[0],values[1],values[2],values[3]),int(values[4])))

window.close()