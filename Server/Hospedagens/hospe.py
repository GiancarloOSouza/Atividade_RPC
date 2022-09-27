class Hospe:
    def __init__(self, cidade, hotel, valor):
        self.cidade = cidade
        self.hotel = hotel
        self.valor = valor
hospe = []

hospe1 = Hospe("Marceio", "Ibis", 500)
hospe2 = Hospe("Sao Paulo", "Cabana o seu zé", 600)
hospe3 = Hospe("Fernando de noronha", "", 700)
hospe4 = Hospe("Belo Monte", "M", 800)

hospe.append(hospe1) 
hospe.append(hospe2)
hospe.append(hospe3)
hospe.append(hospe4)

valor = 800
for i in hospe:
    if(i.valor < valor):
        print(i.valor)
