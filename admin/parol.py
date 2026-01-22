

import time
from yadro import ADMIN_PASSWORD, cls


def admin_login():



    cls()
    attempts = 3
    while attempts > 0:
        password = input("🔐 Admin parol: ")
        cls()
        if password == ADMIN_PASSWORD:
            return True
        attempts -= 1
        if attempts > 0:
            print(f"❌ Noto'g'ri parol. Qolgan urinishlar: {attempts}")
    print("🚫 Kirish rad etildi")
    return False


def parolni_almashtirish():
    """Bu yerda admin ni kirishparolini ozgartiriladi mobodoessimdan chiqib qolsa """
    global ADMIN_PASSWORD #buni global ozgaruvchi deb aytmasak bu tanimedi buni local ozgaruvchu deb biladi
    from yadro import sozlamalar

    urinish = 0
    while True:
        eski_parol = input("Eski parolni kiriting: ")
        cls()

        if eski_parol == ADMIN_PASSWORD:
            yangi_parol = input("Yangi parolni kiriting: ")
            cls()
            ADMIN_PASSWORD = yangi_parol
            sozlamalar.ADMIN_PASSWORD = yangi_parol
            print("✅ Parol muvaffaqiyatli o'rnatildi")
            return

        else:
            urinish += 1
            print(f"✖️ Admin paroli noto'g'ri kiritildi qaytadan urinib ko'ring {urinish}/3")
            if urinish == 3:
                print("Sizda shubhali harakat aniqlandi, bloklangiz")
                print("1 daqiqa kuting")
                time.sleep(60)
                print("\nBlok yechildi. Admin panelga qaytdingiz")
                return




