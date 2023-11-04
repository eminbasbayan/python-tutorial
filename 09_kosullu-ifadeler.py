yas = int(input("Yaşınızı giriniz: "))
if yas >= 21:
    print('Askere gitmek için biraz geç kalmış olabilirsin.')
elif yas == 20:
    print("Askere gitme zamanı gelmiş.")
elif yas == 19:
    print("Askere gitme zamanı yaklaşıyor.")
else:
    print("Daha zaman var.")