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
a = input()
b = input()
c = input()
s = input()
f = input()
g = input()
t = input()
d["modelbook"] = a
d["prosesor"] = b
d["operativnayapamat"] = c
d["video"] = s
d["jostkiydisk"] = f
d["materinskayaplata"] = g
d["razmerekrana"] = t
print(d)
