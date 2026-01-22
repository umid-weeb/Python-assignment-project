# mijoz/savatcha.py
"""Savatcha boshqaruvi"""

from yadro import PRODUCTS_FILE, read_json, write_json, cls

# Ma'lumotlarni yuklash
products_data = read_json(PRODUCTS_FILE)
products = products_data.get("products", [])


class ShoppingCart:
    """Savatcha klassi"""

    def __init__(self):
        self.items = []

    def add_item(self, product_id):
        """Mahsulotni qo'shish"""
        product = next((p for p in products if p["id"] == product_id), None)

        if not product:
            print("❌ Mahsulot topilmadi")
            return False

        if product["quantity"] <= 0:
            print("❌ Mahsulot tugagan")
            return False

        # Savatchada mavjudligini tekshirish
        cart_item = next((item for item in self.items if item["id"] == product_id), None)

        if cart_item:
            if cart_item["count"] >= product["quantity"]:
                print("❌ Omborda yetarli miqdor yo'q")
                return False
            cart_item["count"] += 1
            print(f"✅ '{product['name']}' miqdori oshirildi")
        else:
            self.items.append({
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "count": 1
            })
            print(f"✅ '{product['name']}' savatchaga qo'shildi")
            cls()

        return True

    def remove_item(self, product_id):
        """Mahsulotni o'chirish"""
        cls()
        item = next((item for item in self.items if item["id"] == product_id), None)
        if item:
            self.items.remove(item)
            print(f"✅ '{item['name']}' savatchadan o'chirildi")
        else:
            print("❌ Mahsulot savatchada topilmadi")

    def decrease_item(self, product_id):
        """Mahsulot miqdorini kamaytirish"""
        cls()
        item = next((item for item in self.items if item["id"] == product_id), None)
        if item:
            if item["count"] > 1:
                item["count"] -= 1
                print(f"✅ '{item['name']}' miqdori kamaytirildi")
            else:
                self.remove_item(product_id)
        else:
            print("❌ Mahsulot savatchada topilmadi")

    def view(self):
        """Savatchani ko'rish"""
        cls()
        if not self.items:
            print("\n🛒 Savatcha bo'sh")
            return 0

        print("\n" + "=" * 70)
        print("🛒 SAVATCHAM".center(70))
        print("=" * 70)
        print(f"{'#':<3} {'Nomi':<30} {'Narxi':<13} {'Soni':<8} {'Jami':<13}")
        print("-" * 70)

        total = 0
        for idx, item in enumerate(self.items, 1):
            item_total = item["price"] * item["count"]
            total += item_total
            print(f'{idx:<3} {item["name"]:<30} {item["price"]:>10} so\'m '
                  f'{item["count"]:>5} ta {item_total:>10} so\'m')

        print("-" * 70)
        print(f"{'JAMI:':<55} {total:>12} so'm")
        print("=" * 70)
        return total

    def clear(self):
        """Savatchani tozalash"""
        self.items = []

    def get_total(self):
        """Umumiy summa"""
        return sum(item["price"] * item["count"] for item in self.items)

    def is_empty(self):
        """Bo'shligini tekshirish"""
        return len(self.items) == 0


def maxsulotlarni_korish():
    """Mahsulotlarni ko'rsatish"""
    cls()
    print("\n" + "=" * 70)
    print(" MAHSULOTLAR RO'YXATI".center(70))
    print("=" * 70)

    if not products:
        print("📭 Mahsulotlar yo'q")
        return

    # Kategoriyalar bo'yicha guruhlash
    categories = {}
    for p in products:
        if p["quantity"] > 0:
            cat = p["category"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(p)

    if not categories:
        print(" Sotuvda mahsulotlar yo'q")
        return

    for cat, items in sorted(categories.items()):
        print(f"\n📂 {cat.upper()}")
        print("-" * 70)
        for p in items:
            if p["quantity"] > 10:
                stock = "✅ Ko'p miqdorda"
            elif p["quantity"] > 5:
                stock = "⚠️  Kam qoldi"
            else:
                stock = f"⚠️  Faqat {p['quantity']} ta qoldi!"

            print(f'{p["id"]:>3}. {p["name"]:<35} {p["price"]:>10,} so\'m | {stock}')

    print("=" * 70)