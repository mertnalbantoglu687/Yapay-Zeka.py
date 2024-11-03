import random

ad = input("Lütfen adınızı giriniz : ")

while True:

    print(" ")

    cevap = input("Sorunuzu yazınız : ")

    if cevap == "Nasılsın" or cevap == "nasılsın":
        print(" ")
        print("İyiyim sen nasılsın",ad)
        print(" ")

    elif cevap == "Merhaba" or cevap == "merhaba":
        print(" ")
        print("Sanada merhaba",ad)
        print(" ")

    elif cevap == "Adın Ne" or cevap == "adın ne" or cevap == "Adın ne" or cevap == "adın Ne" or cevap == "ADIN NE":
        print(" ")
        print("Benim Adım Yapay Zeka.")
        print(" ")

    elif cevap == "İsmin Ne" or cevap == "ismin ne" or cevap == "İsmin ne" or cevap == "ismin Ne" or cevap == "İSMİN NE":
        print(" ")
        print("Benim İsmim Yapay Zeka.")
        print(" ")

    elif cevap == "Oyun Aç" or cevap == "oyun aç" or cevap == "Oyun aç" or cevap == "oyun Aç":
        print(" ")
        secim = random.randint(1,3)
        if secim == 1:
            print("Bu oyuna girebilirsin",ad,": https://hub.kodland.org/en/project/308651")
        elif secim == 2:
            print("Bu oyuna girebilirsin",ad,": https://hub.kodland.org/en/project/296170")
        elif secim == 3:
            print("Bu oyuna girebilirsin",ad,": https://hub.kodland.org/en/project/289819")
        print(" ")

    elif cevap == "Sorum Yok" or cevap == "sorum yok" or cevap == "Sorum yok" or cevap == "sorum Yok":
        print(" ")
        print("Tamam. Sorun olduğunda sormaktan çekinme",ad)
        print(" ")

    elif cevap == "Sıkıldım" or cevap == "sıkıldım":
        print(" ")
        print("Belki Desen Makinesi sıkıntını giderebilir",ad,": https://hub.kodland.org/en/project/284214")
        print(" ")

    else:
        print(" ")
        print("Sorunuz anlaşılamadı",ad)
        print(" ")
