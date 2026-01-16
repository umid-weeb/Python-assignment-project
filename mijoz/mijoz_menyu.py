# mijoz/mijoz_menyu.py
"""Mijoz menyusi"""

from yadro import MEMBERSHIPS_FILE, read_json, get_int_input, get_choice
from .savatcha import ShoppingCart, maxsulotlarni_korish
from .tolov import checkout
from .azolik import azolikni_boshqarish
from .yordam import tez_yordam

# Ma'lumotlarni yuklash
memberships_data = read_json(MEMBERSHIPS_FILE)
memberships = memberships_data.get("memberships", {})


def haridor_munyusi():
    """Xaridor menyusi"""
    customer = {"membership": None}
    cart = ShoppingCart()

    while True:
        print("\n" + "=" * 50)
        print("🛒 TECH HOUSE - XARIDOR PANELI".center(50))
        print("=" * 50)

        # Savatcha hisobini ko'rsatish
        if not cart.is_empty():
            cart_total = cart.get_total()
            cart_items = sum(item['count'] for item in cart.items)
            print(f"🛒 Savatchada: {cart_items} ta mahsulot ({cart_total:,} so'm)")

        # A'zolik ma'lumoti
        if customer["membership"]:
            discount = memberships[customer["membership"]]["discount"]
            print(f"💎 A'zolik: {customer['membership']} ({discount}% chegirma)")

        print("-" * 50)
        print("1. 📦 Mahsulotlarni ko'rish")
        print("2. ➕ Savatchaga qo'shish")
        print("3. 🛒 Savatcha")
        print("4. 💳 Buyurtma berish")
        print("5. 💎 A'zolik")
        print("6. ☎️ Yordam")
        print("0. 🚪 Chiqish")

        tanlash = get_choice("\nTanlov: ", ["1", "2", "3", "4", "5", "6", "0"])

        if tanlash == "1":
            maxsulotlarni_korish()

        elif tanlash == "2":
            maxsulotlarni_korish()
            from yadro import PRODUCTS_FILE
            products_data = read_json(PRODUCTS_FILE)
            products = products_data.get("products", [])

            if products:
                print("\n0 - Orqaga qaytish")
                pid = get_int_input("\n📦 Mahsulot ID: ")
                if pid != 0:
                    cart.add_item(pid)

        elif tanlash == "3":
            if cart.is_empty():
                print("\n🛒 Savatcha bo'sh")
            else:
                cart.view()
                print("\n1. Mahsulot miqdorini kamaytirish")
                print("2. Mahsulotni butunlay o'chirish")
                print("3. Savatchani tozalash")
                print("0. Orqaga")

                sub_choice = get_choice("Tanlov: ", ["1", "2", "3", "0"])

                if sub_choice == "1":
                    pid = get_int_input("Mahsulot ID: ")
                    cart.decrease_item(pid)
                elif sub_choice == "2":
                    pid = get_int_input("O'chiriladigan mahsulot ID: ")
                    cart.remove_item(pid)
                elif sub_choice == "3":
                    confirm = get_choice("⚠️ Savatchani tozalamoqchimisiz? (ha/yoq): ",
                                         ["ha", "yoq"])
                    if confirm == "ha":
                        cart.clear()
                        print("✅ Savatcha tozalandi")

        elif tanlash == "4":
            checkout(customer, cart)

        elif tanlash == "5":
            azolikni_boshqarish(customer)

        elif tanlash == "6":
            tez_yordam()

        elif tanlash == "0":
            if not cart.is_empty():
                print("\n⚠️ Savatchada mahsulotlar bor!")
                confirm = get_choice("Chiqmoqchimisiz? (ha/yoq): ", ["ha", "yoq"])
                if confirm == "yoq":
                    continue
            print("👋 Xayr! Yana ko'rishguncha!")
            break