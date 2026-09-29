umsatz = float(input("Geben Sie den Umsatz ein den der Kunde erwirtschaftet hat: "))
if umsatz >= 500:
    rabat = umsatz / 100 * 10
    umsatz -= rabat
    print("10% Rabatt")
    print(umsatz)

elif umsatz >= 100:
    rabat = umsatz / 100 * 5
    umsatz -= rabat
    print("5% Rabatt")
    print(umsatz)
else:
    print("kein Rabatt")