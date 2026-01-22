
"""
TECH HOUSE - Elektron Do'kon Boshqaruv Tizimi
Asosiy dastur fayli
"""

from yadro import get_choice, cls
from admin import admin_menu
from mijoz import haridor_munyusi
from mijoz.user_auth import sign_tanlash


def main():
    cls()
    while True:
        print("\n" + "~" * 60)
        print(" TECH HOUSE - ELEKTRON DO'KON".center(60))
        print("_" * 60)
        print("\033[95m1.  Admin panel\033[0m")
        print("\033[96m2.  Xaridor \033[0m")

        print("\033[93m0.  Chiqish\033[0m")

        choice = get_choice("\nTanlov: ", ["1", "2", "0"])

        if choice == "1":
            admin_menu()
        elif choice == "2":
            sign_tanlash()
        elif choice == "0":
            print("\n" + "-" * 60)
            print("\033[91m Dasturdan chiqildi\033[0m".center(60))
            print("_" * 60)
            print("\033[32m  Tech Houseni tanlaganingiz uchun rahmat!\033[0m".center(60))

            print("-" * 60)
            break


if __name__ == "__main__":
    main()