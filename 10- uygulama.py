# 1- İlk olarak, kullanıcıdan yaşını, kilosunu ve boyunu alalım:
yas = int(input("Yaşınızı giriniz: "))
kilo = float(input("Kilonuzu giriniz (kg): "))
boy = float(input("Boyunuzu giriniz (metre): "))

# 2- Şimdi kullanıcının Beden Kitle İndeksi'ni (BMI) hesaplayalım:
bmi = kilo / (boy ** 2)
print("Beden Kitle İndeksiniz: ", round(bmi, 2))

# 3- Şimdi BMI değerine göre sağlık durumunu değerlendirelim:
if bmi < 18.5:
    print("Zayıf.")
elif 18.5 <= bmi < 24.9:
    print("Normal kilolu") 
elif 25 <= bmi < 29.9:
    print("Fazla kilolu.")
else:
    print("Obez.")

# 4- Şimdi de kullanıcının askere gitme durumunu değerlendirelim. 20 yaş ve üzeri erkekler askerlik yapmak zorundadır.
if yas >= 20:
    print("Askere gitme yaşı gelmiş.")
else:
    print("Daha askere gitme yaşı gelmedi.")

# 5- Son olarak, kullanıcının ideal kilodan ne kadar uzak olduğunu söyleyelim:
ideal_kilo = 22 * (boy ** 2)
kilo_farki = kilo - ideal_kilo
if kilo_farki > 0:
    print("İdeal kilonuzun üzerindesiniz. İdeal kiloya ulaşmak için", round(abs(kilo_farki), 2), "kg vermelisiniz.")
elif kilo_farki < 0:
     print("İdeal kilonuzun altındasınız. İdeal kiloya ulaşmak için", round(abs(kilo_farki), 2), "kg almalısınız.")
else:
    print("Tebrikler! İdeal kilodasınız!")