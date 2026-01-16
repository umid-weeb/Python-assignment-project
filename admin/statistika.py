# admin/statistika.py
"""Statistika ko'rish"""

from datetime import datetime
from yadro import PRODUCTS_FILE, ORDERS_FILE, read_json, cls

# Ma'lumotlarni yuklash
products_data = read_json(PRODUCTS_FILE)
products = products_data.get("products", [])

orders_data = read_json(ORDERS_FILE)
orders = orders_data.get("orders", [])


def view_statistics():
    """Statistika ko'rish"""
    cls()
    print("\n" + "=" * 60)
    print("📊 STATISTIKA".center(60))
    print("=" * 60)

    # Mahsulotlar statistikasi
    print("\n📦 MAHSULOTLAR:")
    print(f"   Jami turlar: {len(products)}")
    total_stock = sum(p['quantity'] for p in products)
    print(f"   Jami miqdor: {total_stock}")

    if products:
        total_value = sum(p['price'] * p['quantity'] for p in products)
        print(f"   Ombor qiymati: {total_value:,} so'm")

        # Eng qimmat mahsulot
        most_expensive = max(products, key=lambda p: p['price'])
        print(f"   Eng qimmat: {most_expensive['name']} - {most_expensive['price']:,} so'm")

    # Buyurtmalar statistikasi
    print("\n💰 BUYURTMALAR:")
    print(f"   Jami buyurtmalar: {len(orders)}")

    if orders:
        total_revenue = sum(o.get('price', 0) for o in orders)
        print(f"   Jami tushum: {total_revenue:,} so'm")
        print(f"   O'rtacha buyurtma: {total_revenue // len(orders):,} so'm")

        # Bugungi buyurtmalar
        today = datetime.now().strftime("%Y-%m-%d")
        today_orders = [o for o in orders if o.get('date', '').startswith(today)]
        if today_orders:
            today_revenue = sum(o.get('price', 0) for o in today_orders)
            print(f"\n📅 BUGUN:")
            print(f"   Buyurtmalar: {len(today_orders)}")
            print(f"   Tushum: {today_revenue:,} so'm")

    # Kategoriyalar bo'yicha
    print("\n📂 KATEGORIYALAR:")
    categories = {}
    for p in products:
        cat = p['category']
        if cat not in categories:
            categories[cat] = {'count': 0, 'total': 0}
        categories[cat]['count'] += p['quantity']
        categories[cat]['total'] += p['price'] * p['quantity']

    for cat, data in categories.items():
        print(f"   {cat}: {data['count']} ta - {data['total']:,} so'm")

    print("=" * 60)