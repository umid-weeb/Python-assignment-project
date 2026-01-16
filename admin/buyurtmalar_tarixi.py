# admin/buyurtmalar_tarixi.py
"""Buyurtmalar tarixini ko'rish"""

from yadro import ORDERS_FILE, read_json

# Ma'lumotlarni yuklash
orders_data = read_json(ORDERS_FILE)
orders = orders_data.get("orders", [])


def buyurtmalar_tarixi():
    """Buyurtmalar tarixini ko'rish"""
    print("\n" + "=" * 60)
    print("📊 BUYURTMALAR TARIXI".center(60))
    print("=" * 60)

    if not orders:
        print("📭 Buyurtmalar yo'q")
        return

    total_revenue = 0
    unknown_text = "Noma'lum"

    for order in orders:
        print(f"\n🆔 Buyurtma #{order['id']}")
        order_date = order.get('date', unknown_text)
        print(f"📅 Sana: {order_date}")
        print(f"💰 Summa: {order.get('price', 0):,} so'm")

        # A'zolik ma'lumoti
        membership = order.get('customer_membership')
        if membership:
            print(f"💎 A'zolik: {membership}")

        # Mahsulotlar ro'yxati
        items = order.get('items', [])
        if items:
            print("📦 Mahsulotlar:")
            for item in items:
                count = item.get('count', 1)
                name = item.get('name', unknown_text)
                price = item.get('price', 0)
                print(f"   • {name} x{count} - {price * count:,} so'm")

        # Yetkazib berish ma'lumoti
        delivery = order.get('delivery', {})
        no_info = "Ma'lumot yo'q"

        if isinstance(delivery, str):
            delivery_text = delivery if delivery else no_info
            print(f"🚚 Yetkazib berish: {delivery_text}")
        elif isinstance(delivery, dict):
            delivery_type = delivery.get('type')
            if delivery_type == 'pickup':
                branch = delivery.get('branch', unknown_text)
                print(f"🏪 Olib ketish: {branch}")
            elif delivery_type == 'courier':
                address = delivery.get('address', unknown_text)
                phone = delivery.get('phone', unknown_text)
                print(f"🚚 Yetkazib berish: {address}")
                print(f"📞 Telefon: {phone}")
            else:
                print(f"🚚 Yetkazib berish: {no_info}")
        else:
            print(f"🚚 Yetkazib berish: {no_info}")

        print("-" * 60)
        total_revenue += order.get('price', 0)

    print(f"\n💵 JAMI TUSHUM: {total_revenue:,} so'm")
    print(f"📈 Buyurtmalar soni: {len(orders)}")
    if orders:
        avg_order = total_revenue // len(orders)
        print(f"📊 O'rtacha buyurtma: {avg_order:,} so'm")
    print("=" * 60)