print("""Merhaba!
Bu birden fazla satır içeren
bir metin bloğudur.""")

isim = "Zeynep"
yas = 30
print(f"{isim} {yas} yaşındadır.")

bilgi = {"isim": "Mehmet", "yaş": 25}
print("Kullanıcı bilgisi:", bilgi)

meyveler = ["Elma", "Armut", "Çilek"]
print("Meyveler listesi:", meyveler)

print("Birinci satır\nİkinci satır")  # \n ile yeni satıra geçilir
print("Bu bir\tsekme içerir.")  # \t ile sekme (tab) eklenir

print("5 + 3 =", 5 + 3)
print("10 - 4 =", 10 - 4)
print("6 × 7 =", 6 * 7)
print("20 ÷ 5 =", 20 / 5)

print("Merhaba", end=" ")
print("Dünya!")

print("Elma", "Armut", "Muz", sep=", ")

