import PySimpleGUI as sg
import WeatherInfo as wi

def windowTitleCreate(ct,cntry,temp,fllk,unts,hmd,wthr,icn):
    sg.theme('lightBlue7')
    #input layout
    layout1 = [[sg.Text("Weather Information", font=('Times New Roman', 25))]
            ,[sg.Text("City:"),
              sg.In(size=(25, 1), enable_events=True,key="-CITY-")]
            ,[sg.Text("Language:"),sg.Radio("English","lan",default=True,key='-ENG-'),sg.Radio("Spanish","lan",default=False,key='-SPN-'),sg.Radio("French","lan",default=False,key='-FRN-'),sg.Radio("Italian","lan",default=False,key='-ITL-')]
            ,[sg.Text("Units:"),sg.Radio("Celsius","units",default=True,key='-CEL-'),sg.Radio("Fahrenheit","units",default=False,key='-FRH-'),sg.Radio("Kelvin","units",default=False,key='-KEL-')]
            ,[sg.Text("API key:"),
              sg.In(size=(25, 1), enable_events=True,key="-API-")]
            ,[sg.Button("Check the weather!")] 
            ,[sg.Button("Exit")]]
    #output layout
    layout2 = [
        [sg.Text("Weather Information", font=('Times New Roman', 25))]
        ,[sg.Text("The weather in "+ ct + ", " + cntry + " is:",key='-CT-')]
        ,[sg.Text("The temperature is: " + temp + unts + ",",key='-TMP-')]
        ,[sg.Text("Feels like " + fllk + unts + ",",key='-FLK-')]
        ,[sg.Text("The humidity is:" + hmd + "%",key='-HMD-')]
        ,[sg.Text("The forcast is " + wthr + ",",key='-FRCST-'), sg.Image(icn,key='-ICN-')]
        ,[sg.Button("Back")]
    ]
    #error layout
    layout3 = [[sg.Text("API key is incorrect! Try again.")
               ,sg.Button("Back")]]
    #final layout
    layout=[
        [sg.Column(layout=layout1 ,visible=True, key='-MAIN-')]
        ,[sg.Column(layout=layout2, visible=False, key='-WETH-')]
        ,[sg.Column(layout=layout3, visible=False, key='-ERR-')]
    ]
    
    
    return sg.Window(title="Main Window", layout=layout, margins=(50, 50), location=(500,0))
    
  
if __name__ == "__main__":
    
    
    win=windowTitleCreate(ct="NULL",cntry="NULL",temp="NULL",fllk="NULL",unts="NULL",hmd="NULL",wthr="NULL",icn="./10n.png")
    
    while True:
        events, values = win.read()
        if events == "Exit" or events == sg.WIN_CLOSED:
            break
        elif events == "Check the weather!":
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
            print(str(values['-CITY-']))    
                
            wInfo = wi.weatherInformation(apiKey,loc,un,ln)
            print(wInfo["cod"])
            if str(wInfo["cod"]) != "401":
                win['-CT-'].update("The weather in "+ wInfo["name"] + ", " + wInfo["sys"]["country"] + " is:")
                win['-TMP-'].update("The temperature is: " + str(wInfo["main"]["temp"]) + str(unts) + ",")
                win['-FLK-'].update("Feels like " + str(wInfo["main"]["feels_like"]) + str(unts) + ",")
                win['-HMD-'].update("The humidity is:" + str(wInfo["main"]["humidity"]) + "%")
                win['-FRCST-'].update("The forcast is " + str(wInfo["weather"][0]["description"]) + ".")
                win['-ICN-'].update("./" + str(wInfo["weather"][0]["icon"]) +".png")
                win['-MAIN-'].update(visible=False)
                win['-WETH-'].update(visible=True)
            else:
                win['-MAIN-'].update(visible=False)
                win['-ERR-'].update(visible=True)
        elif events == "Back":
            win['-MAIN-'].update(visible=True)
            win['-WETH-'].update(visible=False)
            win['-ERR-'].update(visible=False)
            
    
    win.close