radiusKreis = float(input('Bitte geben Sie den Radius ein: '))
durchmesserKreis = round(2*radiusKreis)
kreisFläche = round(3.14*radiusKreis**2,2)
kreisUmfang = round(2*3.14*radiusKreis)

print(f'Kreisdurchmesser: {durchmesserKreis} cm')
print(f'Kreisfläche: {kreisFläche} cm')
print(f'Kreisumfang: {kreisUmfang} cm')