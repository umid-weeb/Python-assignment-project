# admin/admin_menyu.py
"""Admin menyusi"""

from yadro import get_choice, cls
from .parol import admin_login, parolni_almashtirish
from .maxsulot_boshqarish import mahsulot_qoshish, omborni_korish, miqdorni_yangilash
from .buyurtmalar_tarixi import buyurtmalar_tarixi
from .statistika import view_statistics


def admin_menu():
    """Admin menyusi"""
    cls()
    if not admin_login():
        return

    while True:
        print("\033[94mXush kelibsiz\033[0m".center(50))
        print("🔧 ADMIN PANEL".center(40))
        print("-" * 40)
        print("1. ➕ Mahsulot qo'shish")
        print("2. 📦 Omborni ko'rish")
        print("3. ✏️ Mahsulotni tahrirlash")
        print("4. 📊 Buyurtmalar tarixi")
        print("5. 📈 Statistika")
        print("6. 🔑 Parolni almashtirish")
        print("0. 🚪 Chiqish")

        choice = get_choice("Tanlov: ", ["1", "2", "3", "4", "5", "6", "0"])

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
            print("👋 Admin paneldan chiqildi")
            break
            cls()