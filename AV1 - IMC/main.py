import PySimpleGUI as sg

sg.theme('GrayGrayGray')

layout = [ 
  [sg.Text('Índice de Massa Corporal')],
  [sg.Text('Massa: '),sg.Input(key='-MASS-', size=(20,1))],
  [sg.Text('Altura: '),sg.Input(key='-HEIGHT-', size=(20,1))],
  [sg.Button('Calcular')]    
]

window = sg.Window('IMC', layout=layout, font='Monaco 18', element_justification='center')

while True:
  event, value = window.read()   
  print(event, value)
  massa = float(value['-MASS-'])
  altura = float(value['-HEIGHT-'])
  imc = massa/(altura**2)
  sg.Popup(f'Seu IMC é {imc:.2f}', font='Monaco 16')
window.close()