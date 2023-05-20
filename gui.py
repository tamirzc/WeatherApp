import PySimpleGUI as sg
import WeatherInfo as wi

def windowCreate(titleWin):
    sg.theme('lightBlue7')
    layout=[[sg.Text("Weather Information", font=('Times New Roman', 25))]
            ,[sg.Text("City:"),
              sg.In(size=(25, 1), enable_events=True,key="-CITY-")]
            ,[sg.Text("Language:"),sg.Radio("English","lan",default=True),sg.Radio("Spanish","lan",default=False),sg.Radio("French","lan",default=False),sg.Radio("Italian","lan",default=False)]
            ,[sg.Text("Units:"),sg.Radio("Celsius","units",default=True),sg.Radio("Fahrenheit","units",default=False),sg.Radio("Kelvin","units",default=False)]
            ,[sg.Text("API key:"),
              sg.In(size=(25, 1), enable_events=True,key="-API-")]
            ,[sg.Button("Check the weather!")]
            ,[sg.Button("Exit")]]
    
    return sg.Window(title=titleWin, layout=layout, margins=(75, 75))
    
  
if __name__ == "__main__":
    
    
    win=windowCreate("Pitch Converter")
    
    while True:
        events, values = win.read()
        if events == "Exit" or events == sg.WIN_CLOSED:
            break

    
    win.close