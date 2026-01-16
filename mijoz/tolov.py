# mijoz/tolov.py
"""To'lov jarayonlari"""

from datetime import datetime
from yadro import (PRODUCTS_FILE, ORDERS_FILE, MEMBERSHIPS_FILE, FILIALLAR,
                   read_json, write_json, get_int_input, get_choice, cls)

# Ma'lumotlarni yuklash
products_data = read_json(PRODUCTS_FILE)
products = products_data.get("products", [])

orders_data = read_json(ORDERS_FILE)
orders = orders_data.get("orders", [])

memberships_data = read_json(MEMBERSHIPS_FILE)
memberships = memberships_data.get("memberships", {})


def tolov_jarayoni():
    """Karta orqali to'lov"""
    cls()
    print("\n" + "=" * 50)
    print("💳 TO'LOV".center(50))
    print("=" * 50)

    karta = input("💳 16 xonali karta raqami: ").strip().replace(" ", "")

    if len(karta) != 16 or not karta.isdigit():
        print("❌ Noto'g'ri karta raqami (16 ta raqam bo'lishi kerak)")
        return False

    muddat = input("📅 Amal qilish muddati (MM/YY): ").strip()

    if len(muddat) != 5 or muddat[2] != "/":
        print("❌ Noto'g'ri format (MM/YY formatida kiriting)")
        return False

    # Visa (4) yoki MasterCard (5)
    if karta.startswith("4") or karta.startswith("5"):
        cvv = input("🔒 CVV kod (3 raqam): ").strip()
        if len(cvv) != 3 or not cvv.isdigit():
            print("❌ Noto'g'ri CVV (3 ta raqam bo'lishi kerak)")
            return False

    print("\n📱 Telefoningizga SMS kod yuborildi...")
    sms = input("🔐 SMS kodni kiriting (4 raqam): ").strip()

    if len(sms) != 4 or not sms.isdigit():
        print("❌ Noto'g'ri SMS kod")
        return False

    print("\n✅ To'lov muvaffaqiyatli amalga oshirildi!")
    return True


def checkout(customer, cart):
    """Buyurtma berish"""
    cls()
    if cart.is_empty():
        print("🛒 Savatcha bo'sh")
        return

    total = cart.get_total()

    # A'zolik chegirmasi
    discount = 0
    discount_amount = 0
    if customer["membership"]:
        discount = memberships[customer["membership"]]["discount"]
        discount_amount = total * discount // 100

    final_price = total - discount_amount

    # Hisob
    print("\n" + "=" * 60)
    print("💰 HISOB".center(60))
    print("=" * 60)

    # Mahsulotlar ro'yxati
    for idx, item in enumerate(cart.items, 1):
        item_total = item["price"] * item["count"]
        print(f'{idx}. {item["name"]:<30} {item["price"]:>10,} so\'m x {item["count"]} = '
              f'{item_total:>10,} so\'m')

    print("-" * 60)
    print(f"{'Asl narx:':<48} {total:>10,} so'm")

    if discount > 0:
        print(f"{'Azolik (' + str(discount) + '%):':<48} {-discount_amount:>10,} so'm")

    print("=" * 60)
    print(f"{'JAMI TOLOV:':<48} {final_price:>10,} so'm")
    print("=" * 60)

    # Tasdiqlash
    confirm = get_choice("\n✅ Buyurtmani tasdiqlaysizmi? (ha/yoq): ", ["ha", "yoq"])
    if confirm == "yoq":
        print("❌ Buyurtma bekor qilindi")
        return

    # Yetkazib berish
    print("\n" + "=" * 60)
    print("🚚 YETKAZIB BERISH".center(60))
    print("=" * 60)
    print("1. 🏪 Do'kondan olib ketish (Bepul)")
    print("2. 🚛 Kuryer orqali yetkazib berish")

    delivery_choice = get_choice("Tanlov: ", ["1", "2"])

    delivery_info = {}

    if delivery_choice == "1":
        print("\n🏪 FILIALLARIMIZ:")
        print("-" * 60)
        for i, f in enumerate(FILIALLAR, start=1):
            print(f"{i}. {f}")
        print("-" * 60)

        f_choice = get_int_input("Filial tanlang: ", min_val=1)
        if f_choice < 1 or f_choice > len(FILIALLAR):
            print("❌ Noto'g'ri filial")
            return

        delivery_info = {
            "type": "pickup",
            "branch": FILIALLAR[f_choice - 1]
        }

        print(f"\n✅ {FILIALLAR[f_choice - 1]} tanlandi")
        print("⏰ Buyurtma 2-3 soatda tayyor bo'ladi")

    else:
        print("\n📍 YETKAZIB BERISH MA'LUMOTLARI:")
        print("-" * 60)
        address = input("📍 To'liq manzil: ").strip()
        phone = input("📞 Telefon (+998XXXXXXXXX): ").strip()

        if not address or not phone:
            print("❌ Ma'lumotlar to'liq emas")
            return

        phone_digits = ''.join(filter(str.isdigit, phone))
        if len(phone_digits) != 12:
            print("❌ Noto'g'ri telefon raqami")
            return

        delivery_info = {
            "type": "courier",
            "address": address,
            "phone": phone,
            "delivery_time": "2-3 kun ichida"
        }

        print(f"\n✅ Manzil qabul qilindi: {address}")
        print("⏰ Yetkazib berish: 2-3 kun ichida")

    # To'lov
    print("\n" + "=" * 60)
    if not tolov_jarayoni():
        print("\n❌ To'lov amalga oshmadi. Buyurtma bekor qilindi.")
        return

    # Mahsulotlar miqdorini kamaytirish
    for item in cart.items:
        for p in products:
            if p["id"] == item["id"]:
                p["quantity"] -= item["count"]
                break

    write_json(PRODUCTS_FILE, {"products": products})

    # Buyurtmani saqlash
    order = {
        "id": len(orders) + 1,
        "customer_membership": customer["membership"],
        "items": cart.items.copy(),
        "delivery": delivery_info,
        "price": final_price,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    orders.append(order)
    write_json(ORDERS_FILE, {"orders": orders})

    # Muvaffaqiyatli xabar
    print("\n" + "=" * 60)
    print("✅ BUYURTMA QABUL QILINDI!".center(60))
    print("=" * 60)
    print(f"\n🆔 Buyurtma raqami: #{order['id']}")
    print(f"📅 Sana: {order['date']}")

    if delivery_info["type"] == "pickup":
        print(f"\n🏪 Olib ketish joyi: {delivery_info['branch']}")
        print("⏰ Tayyor bo'lish vaqti: 2-3 soat")
    else:
        print(f"\n🚚 Yetkazib berish: {delivery_info['address']}")
        print(f"📞 Telefon: {delivery_info['phone']}")
        print(f"⏰ Yetkazish vaqti: {delivery_info['delivery_time']}")

    print(f"\n💰 To'langan summa: {final_price:,} so'm")

    if discount > 0:
        print(f"💎 A'zolik orqali tejaldi: {discount_amount:,} so'm")

    print("\n🙏 Xaridingiz uchun rahmat!")
    print("⭐ Bizni tanlaganingiz uchun tashakkur!")
    print("=" * 60)

    cart.clear()