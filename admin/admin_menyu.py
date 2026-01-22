# admin/admin_menyu.py
from yadro.input_tekshir import get_choice
from yadro.util import cls  #bu yadrodan cls yani tozalash funksiyasini va get_choice ni chaqirib olyapmiz
from .parol import admin_login, parolni_almashtirish #bu parol.py dan admin_login va parolni_almashtirish funksiyalarini chaqirib olyapmiz
from .maxsulot_boshqarish import mahsulot_qoshish, omborni_korish, miqdorni_yangilash #bu maxsulot_boshqarish.py dan mahsulot_qoshish, omborni_korish, miqdorni_yangilash funksiyalarini chaqirib olyapmiz
from .buyurtmalar_tarixi import buyurtmalar_tarixi #bu buyurtmalar_tarixi.py dan buyurtmalar_tarixi funksiyasini chaqirib olyapmiz
from .statistika import view_statistics #bu statistika.py dan view_statistics funksiyasini chaqirib olyapmiz


def admin_menu(): #bu admin menyusi funksiyasi
    """Bu admin  menyusi adminga tegishli funksiyalar manashu yerda chaqirilgan  """
    cls() #ekranni tozalash
     #admin login funksiyasini chaqirib uni tekshiradi agar false bolsa return qiladi
    if not admin_login(): # agar admin_login funksiyasi false bolsa
        return  #return qiladi yani funksiyani toxtatadi

    while True:
        print("\033[94mXush kelibsiz\033[0m".center(50)) #bu yerda xush kelibsiz degan yozuvni markazlashtirib chiqaradi
        print("🔧 ADMIN PANEL".center(40)) 
        print("-" * 40)
        print("1. ➕ Mahsulot qo'shish")
        print("2. 📦 Omborni ko'rish")
        print("3. ✏️ Mahsulotni tahrirlash")
        print("4. 📊 Buyurtmalar tarixi")
        print("5. 📈 Statistika")
        print("6. Parolni almashtirish")
        print("\033[51m0. Chiqish\033[0m")

        choice = get_choice("Tanlov: ", ["1", "2", "3", "4", "5", "6", "0"]) #bu yerda get_choice funksiyasini chaqirib tanlovni oladi va faqat berilgan variantlardan birini qabul qiladi

        if choice == "1":
            mahsulot_qoshish()
        elif choice == "2":
            omborni_korish()
        elif choice == "3":
            miqdorni_yangilash()
        elif choice == "4":
            buyurtmalar_tarixi()
        elif choice == "5":
            view_statistics()
        elif choice == "6":
            parolni_almashtirish()
        elif choice == "0":
            print("Admin paneldan chiqildi")
            break
