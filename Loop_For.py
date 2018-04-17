#  //DONGULER - LOOPS
# Bir baslangic degeri olan, belirli bir kosul gerceklesene dek suren ve bu surec icerisinde bir takim islemleri tekrarli olarak gerceklestiren nesnelere "dongu" adini vermekteyiz.

# 0-4 arasındaki sayıları yazacaktır.
# Eğer başlangıç değeri belirtmezsek x => 0 sayısından başlayacaktır.
for x in range(5):
    print(x)
#
# Eğer başlangıç değerini değiştirmek istiyorsak iki parametre kullanabiliriz.
for x in range(3, 5):
    print(x)
# Ekranda 3-4 sayılarını görebiliriz.

# Örnek 1=> 1-100 aralığındaki sayıları ekrana getirilmesi

for sayi in range(1, 101):
    print("sayi objesinin şu anki değeri => {}".format(sayi))

# Örnek 2=> 100-1 aralığındaki sayıların ekrana getirilmesi
# Eğer artış-azalış yöntemi belirtmezsek kendiliğinden her turda +1 yapar. Belirtmek istersek üçüncü parametrede bunu gösterebiliriz.

for deger in range(100, 0, -1):
    print("deger isimli objenin şu anki değeri => {}".format(deger))
    # -1 parametre değeri sayesinde her turda deger isimli objenin bir azalmasını sağlıyoruz.

# Örnek 3=> 0-1000 aralığındaki tek sayıları ekrana getiriniz =>

# 1.Yöntem
for x in range(1, 1001, 2):
    print(x)

# 2.Yöntem
for sayi in range(0, 1000):
    if sayi%2 != 0:
        print(sayi)

# Örnek 4=> 1-100 Aralığındaki sayıların toplamını ekrana yazdırınız

toplam = 0
for x in range(1, 100):
    toplam += x

print(toplam)

# Örnek 5=> 1-100 arasındaki çift sayıalrın toplamı ile tek sayıların toplamı arasındaki farkın karesi kaçtır?

ciftToplam = 0
tekToplam = 0

for x in range(0, 100):
    if x%2 == 0:
        ciftToplam += x
    else:
        tekToplam += x

import math  # Math kütüphanesi gibi import işlemleri genelde en tepeye eklenir.

sonuc = math.pow((ciftToplam-tekToplam), 2)
# veya
# sonuc = (ciftToplam-tekToplam) * (ciftToplam-tekToplam)

print(sonuc)

# Örnek 6=> 1945 - günümüz yılı arasındaki yıllar Listbox'a eklensin ancak 1990 ve 1992 yılları eklenmeyecek...

import datetime  # bu kütüphane sayesinde datetime.datetime.now() işlemini yapabiliriz.

for tarih in range(1945, datetime.datetime.now().year):  # Bu fonksiyon sayesinde günün tarihini alabiliriz.
    if tarih != 1990 and tarih != 1992:
        print(tarih)

# Continue anahtar kelimesi ile yapılışı.

for tarih in range(1945, datetime.datetime.now().year):
    if tarih == 1990 or tarih == 1992:
        continue
    else:
        print(tarih)

# Continue anahtar kelimesi döngü içerisinde döngüdeki geri kalan adımların o tur için çalışmasını engeller ve döngü , bir sonraki aşamadan devam eder.


# Örnek

# Döngü kullanarak Console üzerinde bir kare oluşturunuz
kare = ""
for x in range(0,5):
    for y in range(0,5):
        kare += "X"
    print(kare)
    kare = ""

# İçi Boş  Kare

kare = ""
for x in range(0, 5):
    for y in range(0, 5):
        if x == 0 or x == 4 or y == 0 or y == 4:
            kare += "X"
        else:
            kare += " "
    print(kare)
    kare = ""

# Üçgen Çizimi
kare = ""
for x in range(0,5):
    for y in range(0,5):
        if x >= y:
            kare += "X"
        else:
            kare += " "
    print(kare)
    kare = ""

# Diğer Yöntem

kare = ""
for x in range(0, 5):
    for y in range(0, x+1):  # +1 koymazsak bir boy küçük üçgen olur eşitlik durumunda da koyması için +1 ekledik
        kare += "X"
    print(kare)
    kare = ""