
#Problem 1

boy = float(input("Lütfen boyunuzu cm türünden giriniz..."))
kilo = float(input("Lütfen kilonuzu kg türünden giriniz..."))

vki = (kilo)/((boy**2))

if vki < 18.5:
  print("Zayıfsınız...")
elif vki < 25:
  print("Normalsiniz...")
elif vki < 30:
  print("Fazla Kilolusunuz...")
else:
  print("Obezsiniz...")

#Problem 2

x = int(input("Birinci sayıyı giriniz: "))
y = int(input("İkinci sayıyı giriniz: "))
z = int(input("Üçüncü sayıyı giriniz: "))

if x > y and x > z:
  print(x)
elif y > x and y > z:
  print(y)
elif z > x and z > y:
  print(z)
else:
  print("Eşit olan sayılar var...")


#Problem 3

vize1 = float(input("1. vize notunuzu giriniz..."))
vize2 = float(input("2. vize notunuzu giriniz..."))
final = float(input("Final notunuzu giriniz..."))

note = vize1*0.39 + vize2*0.30 + final*0.40
if note >= 90:
  print("AA")
elif note >= 85:
  print("BA")
elif note >= 80:
  print("BB")
elif note >= 75:
  print("CB")
elif note >= 70:
  print("CC")
elif note >= 65:
  print("DC")
elif note >= 60:
  print("DD")
else:
  print("FF")

#Problem 4

print("""********************
1.Üçgen
2.Dörtgen
********************""")

kull = int(input("Seçiminiz..."))

if kull == 1:
  birinciKenar = int(input())
  ikinciKenar = int(input())
  ucuncuKenar = int(input())

  if birinciKenar==ikinciKenar==ucuncuKenar:
    print("Eşkenar Üçgen")
  elif birinciKenar == ikinciKenar or ikinciKenar==ucuncuKenar or ucuncuKenar==birinciKenar:
    print("İkizkenar Üçgen")
  else:
    print("Üçgen Belirtmiyor")

elif kull == 2:
    birinciKenar = int(input())
    ikinciKenar = int(input())

    if birinciKenar == ikinciKenar:
      print("Kare")
    else:
      pirnt("Dikdortgen")
