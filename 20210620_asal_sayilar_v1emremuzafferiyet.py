#arkadaşlar selam ben python öğreniyorum. Udemyden kurs alarak başladım. başlangıç olarak bence çok iyi.
#yarıladığım kursu uzun bir aradan sonra başltan almam gerekti. o yüzden kursun nasıl olduğunu biliyorum.
#buraya gereksiz, basit veya zaten var demeden kodlar ve kaynakları yükleyeceğim.
#asıl amaç sahip olduğum yetkinlikleri göstermek. Bunu mezun olduktan sonra fark ettim.
#Bir hedef kolayım yolumuz kolaylaşsın. Ben şuanda bir Şantiyede çalışıyorum. şantiye yönetim programı planlıyorum
# o yüzden yarım kalmış python programından devam etmek istedim sonuçta bir temel atmıştım yarım da olsa.
#şimdi o temeli sağlamlaştırma vakti. bu da bir dil, dil öğrenmek için dil öğrenmeyip, projem için, fikrim için dil öğreniyorum
#bir yandan da zaten programın temel kodlarını yazmaya başlarım
#son olarak da program için en uygun dil bu mu değil mi diye düşünmedim, pythonla uygulayabildiğim kadarını yapacağım.
#neyin eksik olduğunu nasıl bir şeyin daha faydalı olacağını belirledikten sonra ana dile yöneleceğim.
#ve kurs Mustafa Murat Coşkun'un Sıfırdan İleri Seviye Programlama (2020) kursu.
#ilk programımımız asal sayı programı. kursta ki kod şu şekildeydi:

#kullanıcıdan alınan sayının asal olup olmadığını söyleyen program

#ben bunu biraz daha dallandırmaya bildiklerimi eklemeye çalışacağım. arayüz derslerini de almıştım ama onu ilerleyen zamanlarda eklerim
#eğer bu kod arayüzlü değilse.


#şimdi kodun mantığı şu şekilde. 1 ve 2 sayısının asal olup olmadığını kendimiz söylüyoruz. 1 ise asal değil, 2 ise asal diye
#2'den sonraki sayılarda ise for döngüsünü çalıştırıp. girilen sayının başka sayılara bölünüp bölünmediğini tek tek deniyoruz.
#bunu da girilen sayının birer birere arttırdığımız referans değerinde moduna bakarak sağlıyoruz.

#MMC hocamızın kodu github sayfasında şu şekilde
#https://github.com/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama/blob/master/Fonksiyonlar/Kodlama%20Egzersizleri/asal_mi.py

#ilk eklemek istediğim özellik, rakam dışında bir karakter girilmesi halinde tekrar sayi girilmesini istemek olacak.
#normalde input() olarak girdiğimiz tüm karakterler string olarak saklanıyor. kodda biz bunu sonradan int() içinde tam sayıya çevirmek istiyoruz.
#işte o noktada eğer girişimiz sadece rakamlardan oluşmuyorsa. Yani tam sayıya çevrilemiyorsa, int() satırında hata alırız.
#hatayı aldığımızda bizden tekrar giriş isteyecek şekilde basit bir try, except kodu ekleyeceğiz.

def asal_mi(sayi):#fonksiyonu tanımladık
    if sayi==1: #1 girişi asal değildir
        return False #asal_mi fonksiyonu eğer sayı asal değilse False, asalsa True return eder.#
    elif sayi==2: # en küçük asal sayımız da burda
        return True
    else:
        for i in range(2,sayi):     #range fonksiyonu ilk ve ikinci index arasında dizi adım adım artan dizi oluşturur.
            if sayi % i ==0:        #range(start, stop, step), birden fazla adım yapmak için step parametresi girilir
                return False        #for döngüsündeyken i sürekli artar ve 'sayı'yı bölüp bölemediğine bakılır
                break               ###eğer bu bir asal sayı ise if bloğu hiç bir zaman çalışmaz ve fır döngüsünden sonra#
        return True                 #True değeri döner. Eğer sayı asal değilse if bloğuna girilir ve False döndürülüp döngüden çıkılır
                                    #çünkü sayının asal olmadığı belirlenir bundan sonra bölme veya mod yapılmaz.


while True:                         #burda while ile uygulama havası katmaya çalışıyoruz. Sürekli olarak asal sayi testi yapılabiliyor.
    sayi=input("Sayı Girin, Çıkış q:")       #kullanıcı girişini alıyoruz
    if sayi=="q":
        print(("Çıkış Yapılıyor..."))
        break
    try:                            #bu noktada -sayi = int(sayi)- şeklinde olan eski kodumuzu değiştiriyoruz çünkü
        sayi = int(sayi)            #bahsettiğimiz errorlar burada ortaya çıkıyor. rakam dışı giriş yapılması veya giriş yapılmadan "" şeklinde
    except ValueError:              #giriş yapılması Value Error hatısı verir. #except Value errorda tekrar giriş yapılmasını istiyoruz kibarca.
        print("Lütfen Geçerli Bir ",end='') #print komutu step parametresi default olarak "\n" şeklindedir. yani satır başı yapar. ben ayrı istemediğim için
                                            #end='' yaparak, tek mesajla en başal döndürmyi sağlıyorm.
        continue                            #continue komutu çalıştığında döngü içindeki işlemleri durdurup döngüdebaşından, iterasyon hafızasını bir arttırırak
                                            #devam eder.

    if (asal_mi(sayi)):                             #burada sadece asal mı değil mi cevabını ekrana yansıtıyoruz.
        print(str(sayi) + " sayısı asaldır.")       #while ve for döngüsündeki değişkenler yerel değişkenlerden olduğu için
    else:                                           #sayi'yı tekrar stringe ceviriyoruz.
        print(str(sayi)+" sayısı asal değildir.")