# mijoz/azolik.py
"""A'zolik boshqaruvi"""

from yadro import MEMBERSHIPS_FILE, read_json, get_choice, cls
from .tolov import tolov_jarayoni

# Ma'lumotlarni yuklash
memberships_data = read_json(MEMBERSHIPS_FILE)
memberships = memberships_data.get("memberships", {})


def azolikni_boshqarish(customer):
    """A'zolikni boshqarish"""
    cls()
    print("\n" + "=" * 50)
    print("💎 A'ZOLIK".center(50))
    print("=" * 50)

    if customer["membership"]:
        discount = memberships[customer["membership"]]["discount"]
        print(f"\n✅ Sizda a'zolik mavjud: {customer['membership']}")
        print(f"💰 Chegirma: {discount}%")
        print("\n1. A'zolikni bekor qilish")
        print("0. Orqaga")

        choice = get_choice("Tanlov: ", ["1", "0"])
        if choice == "1":
            confirm = get_choice("⚠️ A'zolikni bekor qilmoqchimisiz? (ha/yoq): ", ["ha", "yoq"])
            if confirm == "ha":
                customer["membership"] = None
                print("✅ A'zolik bekor qilindi")
        return

    # A'zolik sotib olish
    print("\n💎 A'ZOLIK PAKETLARI:")
    print("-" * 50)
    paketlar = [k for k in memberships.keys() if k != "None"]

    for i, paket in enumerate(paketlar, start=1):
        discount = memberships[paket]['discount']
        print(f"{i}. {paket:<20} - {discount}% chegirma")
    print("0. Orqaga")
    print("-" * 50)

    choice = input("Tanlov: ").strip()
    if choice == "0":
        return

    try:
        paket = paketlar[int(choice) - 1]
    except (ValueError, IndexError):
        print("❌ Noto'g'ri tanlov")
        return

    print(f"\n💎 Siz {paket} paketini tanladingiz")
    print(f"💰 Chegirma: {memberships[paket]['discount']}%")

    if tolov_jarayoni():
        customer["membership"] = paket
        print(f"\n✅ {paket} a'zoligi faollashtirildi!")
        print("🎉 Endi siz barcha xaridlaringizda chegirma olasiz!")