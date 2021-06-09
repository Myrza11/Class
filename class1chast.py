# первое задание
class Notebook:
    def __init__(self, modelbook, prosesor, operativnaapamat, video, jostkiydisk, materinskayaplata, razmerekrana):
        self.modelbook = modelbook
        self.prosesor = prosesor
        self.operativnayapamat = operativnaapamat
        self.video = video
        self.jostkiydisk = jostkiydisk
        self.materinskayaplata = materinskayaplata
        self.razmerekrana = razmerekrana



d = {"modelebook": "qwerty", "prosesor": None, "operativnayapamat": None, "video": None, "jostkiydisk": None, "materinskayaplata": None, "razmerekrana": None }
a = input("Процессор")
b = input("Оперативная Память")
c = input("Видео карта")
s = input("Жёсткий Диск")
f = input("Материнская плата")
g = input("Размер экрана")
t = input("модель ноутбука")
d["modelbook"] = a
d["prosesor"] = b
d["operativnayapamat"] = c
d["video"] = s
d["jostkiydisk"] = f
d["materinskayaplata"] = g
d["razmerekrana"] = t
print(d)



# втарое задание
Data #1:
colors = {
"black": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,255,255,1],
"hex": "#000"
}
},
"white": {
"category": "value",
"type": "primary",
"code": {
"rgba": [0,0,0,1],
"hex": "#FFF"
}
},
"red": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,0,0,1],
"hex": "#FF0"
}
},
"blue": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [0,0,255,1],
"hex": "#00F"
}
},
"yellow": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,255,0,1],
"hex": "#FF0"
}
},
"green": {
"category": "hue",
"type": "secondary",
"code": {
"rgba": [0,255,0,1],
"hex": "#0F0"
}
}
}

class Parse:

    pass

    def keytuple():
        pass

    def valuestuple():
        pass









#Data #2:
data = {
"markers": [
{
"name": "Rixos The Palm Dubai",
"position": [25.1212, 55.1535],
},
{
"name": "Shangri-La Hotel",
"location": [25.2084, 55.2719]
},
{
"name": "Grand Hyatt",
"location": [25.2285, 55.3273]
}
]
}