# admin/maxsulot_boshqarish.py
"""Mahsulotlarni boshqarish"""

from datetime import datetime
from yadro import PRODUCTS_FILE, read_json, write_json, get_int_input, get_choice, cls

# Ma'lumotlarni yuklash
products_data = read_json(PRODUCTS_FILE)
products = products_data.get("products", [])


def mahsulot_qoshish():
    """bu yerda yangi mahsulot qoshiladiva togridan togri jsonga yozilib boradi """
    cls()
    print("\n~~~ YANGI MAHSULOT ~~~".center(50, "-"))
    name = input(" Nomi: ").strip()
    if not name:
        print("\033[101m Nom bo'sh bo'lishi mumkin emas\033[0m")
        return

    category = input(" Kategoriya: ").strip()
    price = get_int_input(" Narxi (so'm): ", min_val=1)
    quantity = get_int_input(" Miqdori: ", min_val=1)

    new_id = max([p["id"] for p in products], default=0) + 1

    products.append({
        "id": new_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    write_json(PRODUCTS_FILE, {"products": products})
    print("\033[102m Mahsulot muvaffaqiyatli qo'shildi\033[0m")


def omborni_korish():
    """Omborni ko'rish"""
    cls()
    print("\n=== OMBOR HOLATI ===".center(50, "-"))
    if not products:
        print("Ombor bo'sh")
        return

    print(f"{'ID':<5} {'Nomi':<25} {'Kategoriya':<15} {'Narxi':<12} {'Miqdori':<8}")
    print("-" * 70)

    total_items = 0
    total_value = 0

    for p in products:
        status = "" if p["quantity"] > 5 else "⚠️" if p["quantity"] > 0 else "❌"
        print(f'{status} {p["id"]:<3} {p["name"]:<25} {p["category"]:<15} '
              f'{p["price"]:>10} so\'m {p["quantity"]:>5} ta')
        total_items += p["quantity"]
        total_value += p["price"] * p["quantity"]

    print("-" * 70)
    print(f"📊 Jami mahsulotlar: {total_items} ta")
    print(f"💰 Umumiy qiymat: {total_value:,} so'm")


def miqdorni_yangilash():
    """Mahsulot miqdorini o'zgartirish"""
    cls()
    if not products:
        print("❌ Mahsulotlar mavjud emas")
        return

    omborni_korish()

    pid = get_int_input("\n🔢 Mahsulot ID: ")
    product = next((p for p in products if p["id"] == pid), None)

    if not product:
        print("❌ Mahsulot topilmadi")
        return

    print(f"\n📦 {product['name']}")
    print(f"💰 Narx: {product['price']:,} so'm")
    print(f"📊 Hozirgi miqdor: {product['quantity']} ta")
    print("\n1. Miqdorni ko'paytirish")
    print("2. Miqdorni kamaytirish")
    print("3. Mahsulotni o'chirish")
    print("0. Bekor qilish")

    choice = get_choice("Tanlov: ", ["1", "2", "3", "0"])

    if choice == "0":
        return

    if choice == "1":
        amount = get_int_input("Qo'shiladigan miqdor: ", min_val=1)
        product["quantity"] += amount
        print(f"✅ Miqdor yangilandi: {product['quantity']} ta")

    elif choice == "2":
        amount = get_int_input("Kamaytirilgan miqdor: ", min_val=1)
        if amount >= product["quantity"]:
            confirm = get_choice(f"⚠️ Bu mahsulotni butunlay o'chirmoqchimisiz? (ha/yoq): ",
                                 ["ha", "yoq"])
            if confirm == "ha" or confirm == "Ha":
                products.remove(product)
                print("✅ Mahsulot o'chirildi")
                write_json(PRODUCTS_FILE, {"products": products})
                return
            else:
                print("❌ Bekor qilindi")
                return
        else:
            product["quantity"] -= amount
            print(f"✅ Miqdor yangilandi: {product['quantity']} ta")

    elif choice == "3":
        confirm = get_choice(f"⚠️ '{product['name']}' o'chirilsinmi? (ha/yoq): ",
                             ["ha", "yoq"])
        if confirm == "ha":
            products.remove(product)
            print("✅ Mahsulot o'chirildi")

    write_json(PRODUCTS_FILE, {"products": products})