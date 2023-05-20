import requests

url = "https://openweathermap.org/img/wn/"
end = "@2x.png"

listCodes=[1,2,3,4,9,10,11,13,50]
listtimes=["d","n"]

for code in listCodes:
    for time in listtimes:
        name = str(format(code, '02d')) + time
        finalUrl= url + name + end
        r = requests.get(finalUrl)
        open(name+".png","wb").write(r.content)