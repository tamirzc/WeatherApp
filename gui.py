import PySimpleGUI as sg
import WeatherInfo as wi


def generalError():
    layout = [
    [sg.Text("Error!", font=('Times New Roman', 25))]
    ,[sg.Text("Unknown error. Please check you chose an exisiting city, inserted the right API key or try again later.",key='-CT-')]
    ,[sg.Button("Back")]
    ]
    window = sg.Window("City Error Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Back" or event == sg.WIN_CLOSED:
            break
    window.close()

def weatherWindow(ct,cntry,temp,fllk,unts,hmd,wthr,icn):
    layout = [
        [sg.Text("Weather Information", font=('Times New Roman', 25))]
        ,[sg.Text("The weather in "+ ct + ", " + cntry + " is:",key='-CT-')]
        ,[sg.Text("The temperature is: " + temp + unts + ",",key='-TMP-')]
        ,[sg.Text("Feels like " + fllk + unts + ",",key='-FLK-')]
        ,[sg.Text("The humidity is:" + hmd + "%",key='-HMD-')]
        ,[sg.Text("The forcast is " + wthr + ",",key='-FRCST-'), sg.Image(icn,key='-ICN-')]
        ,[sg.Button("Back")]
    ]
    window = sg.Window("Weather Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Back" or event == sg.WIN_CLOSED:
            break
    window.close()
    
    
def windowTitleCreate():
    layout = [[sg.Text("Weather Information", font=('Times New Roman', 25))]
            ,[sg.Text("City:"),
              sg.In(size=(25, 1), enable_events=True,key="-CITY-")]
            ,[sg.Text("Language:"),sg.Radio("English","lan",default=True,key='-ENG-'),sg.Radio("Spanish","lan",default=False,key='-SPN-'),sg.Radio("French","lan",default=False,key='-FRN-'),sg.Radio("Italian","lan",default=False,key='-ITL-')]
            ,[sg.Text("Units:"),sg.Radio("Celsius","units",default=True,key='-CEL-'),sg.Radio("Fahrenheit","units",default=False,key='-FRH-'),sg.Radio("Kelvin","units",default=False,key='-KEL-')]
            ,[sg.Text("API key:"),
              sg.In(size=(25, 1), enable_events=True,key="-API-")]
            ,[sg.Button("Check the weather!")] 
            ,[sg.Button("Exit")]]
    window = sg.Window("Information Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Check the weather!":
            apiKey=values['-API-']

            #language
            if values['-SPN-'] == True:
                ln = "sp"
            elif values['-FRN-'] == True:
                ln = "fr"
            elif values['-ITL-'] == True:
                ln = "it"
            else:
                ln = "en"
            
            #units
            if values['-KEL-'] == True:
                un = "standard"
                unts = "K"
            elif values['-FRH-'] == True:
                un = "imperial"
                unts = "F"
            else:
                un = "metric"
                unts = "C"
            
            loc = str(values['-CITY-'])
                
            wInfo = wi.weatherInformation(apiKey,loc,un,ln)
            if (wInfo["cod"]) == 200:
                weatherWindow(ct=wInfo["name"],cntry=wInfo["sys"]["country"],temp=str(wInfo["main"]["temp"]),fllk=str(wInfo["main"]["feels_like"]),unts=str(unts),hmd=str(wInfo["main"]["humidity"]),wthr=str(wInfo["weather"][0]["description"]),icn="./" + str(wInfo["weather"][0]["icon"]) +".png")      
            else:
                generalError()
    window.close()
    
    
if __name__ == "__main__":
    windowTitleCreate()