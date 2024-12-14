# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random

ad = input("Lütfen adınızı giriniz : ")

while True:

    print(" ")

    cevap = input("Sorunuzu yazınız : ")

    if cevap == "nasılsın" or cevap == "Nasılsın" or cevap == "NASILSIN":
        print(" ")
        print("İyiyim sen nasılsın",ad)
        print(" ")

    elif cevap == "merhaba" or cevap == "Merhaba" or cevap == "MERHABA":
        print(" ")
        print("Sanada merhaba",ad)
        print(" ")

    elif cevap == "adın ne" or cevap == "Adın ne" or cevap == "adın Ne" or cevap == "Adın Ne" or cevap == "ADIN NE":
        print(" ")
        print("Benim Adım Yapay Zeka.")
        print(" ")

    elif cevap == "ismin ne" or cevap == "İsmin ne" or cevap == "ismin Ne" or cevap == "İsmin Ne" or cevap == "İSMİN NE":
        print(" ")
        print("Benim İsmim Yapay Zeka.")
        print(" ")

    elif cevap == "oyun aç" or cevap == "Oyun aç" or cevap == "oyun Aç" or cevap == "Oyun Aç" or cevap == "OYUN AÇ":
        print(" ")
        secim = random.randint(1,3)
        if secim == 1:
            print("Bu oyuna girebilirsin",ad,": https://hub.kodland.org/en/project/308651")
        elif secim == 2:
            print("Bu oyuna girebilirsin",ad,": https://hub.kodland.org/en/project/296170")
        elif secim == 3:
            print("Bu oyuna girebilirsin",ad,": https://hub.kodland.org/en/project/289819")
        print(" ")

    elif cevap == "sorum yok" or cevap == "Sorum yok" or cevap == "sorum Yok" or cevap == "Sorum Yok" or cevap == "SORUM YOK":
        print(" ")
        print("Tamam. Sorun olduğunda sormaktan çekinme",ad)
        print(" ")

    elif cevap == "sıkıldım" or cevap == "Sıkıldım" or cevap == "SIKILDIM":
        print(" ")
        print("Belki Desen Makinesi sıkıntını giderebilir",ad,": https://hub.kodland.org/en/project/284214")
        print(" ")

    else:
        print(" ")
        print("Sorunuz anlaşılamadı",ad)
        print(" ")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
