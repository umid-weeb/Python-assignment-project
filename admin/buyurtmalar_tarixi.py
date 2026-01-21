

from yadro import ORDERS_FILE, read_json

# Ma'lumotlarni yuklash
orders_data = read_json(ORDERS_FILE)
orders = orders_data.get("orders", []) #bu yerda orders_data dan orders ni oladi yani buyurtmalar royxatini oladi va agar orders_data da orders bolmasa bo'sh royxat qaytaradi


def buyurtmalar_tarixi(): # bu buyurtmalar tarixini korish funksiyasi va bu funksiyani admin menyusida chaqiradi yani admin buyurtmalar tarixini korishi mumkin
    print("\n" + "_" * 60)
    print("📊 BUYURTMALAR TARIXI".center(60))
    print("~" * 60)

    if not orders: # agar orders bo'sh bolsa yani buyurtmalar royxati bo'sh bolsa  print Buyurtmalar yo'q deb chiqaradi va return qiladi blarni shunchaki eslab qolish uchun yozyapman
        print("📭 Buyurtmalar yo'q")
        return # return qiladi yani funksiyani toxtatadi

    total_revenue = 0 # jami tushum uchun o'zgaruvchi
    unknown_text = "Noma'lum" # noma'lum ma'lumotlar uchun matn

    for order in orders: # har bir buyurtma uchun buyurtma ma'lumotlarini chiqaradi yani buyurtma id, sana, summa, mahsulotlar ro'yxati va yetkazib berish ma'lumotlarini chiqaradi
        print(f"\n🆔 Buyurtma #{order['id']}") 
        order_date = order.get('date', unknown_text) # buyurtma sanasini oladi agar bo'lmasa noma'lum deb beradi
        print(f"📅 Sana: {order_date}") # bu olingan sanani qishib priont qilasidi
        print(f"💰 Summa: {order.get('price', 0):,} so'm")
        membership = order.get('customer_membership')
        if membership: # agar membership mavjud bo'lsa print qiladi
            print(f"💎 A'zolik: {membership}")

        # Mahsulotlar ro'yxati
        items = order.get('items', []) # buyurtma ichidagi mahsulotlar ro'yxatini oladi agar bo'lmasa bo'sh royxat qaytaradi
        if items: # agar items bo'sh bo'lmasa print qiladi
            print("📦 Mahsulotlar:") 
            for item in items: # har bir mahsulot uchun mahsulot nomi, soni va narxini chiqaradi
                count = item.get('count', 1)
                name = item.get('name', unknown_text)
                price = item.get('price', 0)
                print(f"   • {name} x{count} - {price * count:,} so'm")# mahsulot nomi, soni va narxini chiqaradi

        # Yetkazib berish ma'lumoti bu yerda haridor qanday yetkazib berish turini tanlagan bolsa shunga qarab chiqaradi
        delivery = order.get('delivery', {}) # buyurtma ichidagi yetkazib berish ma'lumotlarini oladi agar bo'lmasa bo'sh lug'at qaytaradi
        no_info = "Ma'lumot yo'q"

        if isinstance(delivery, str): # agar delivery string bo'lsa print qiladi
            delivery_text = delivery if delivery else no_info # agar delivery bo'sh bo'lmasa delivery ni beradi aks holda no_info ni beradi
            print(f"🚚 Yetkazib berish: {delivery_text}") 
        elif isinstance(delivery, dict): # agar delivery lug'at bo'lsa
            delivery_type = delivery.get('type') # yetkazib berish turini oladi
            if delivery_type == 'pickup': # agar yetkazib berish turi pickup bo'lsa print qiladi
                branch = delivery.get('branch', unknown_text) # filial nomini oladi agar bo'lmasa noma'lum deb beradi
                print(f"🏪 Olib ketish: {branch}")
            elif delivery_type == 'courier': # agar yetkazib berish turi courier bo'lsa print qiladi
                address = delivery.get('address', unknown_text) # manzilni oladi agar bo'lmasa noma'lum deb beradi
                phone = delivery.get('phone', unknown_text) # telefon raqamini oladi agar bo'lmasa noma'lum deb beradi
                print(f"🚚 Yetkazib berish: {address}")  
                print(f"📞 Telefon: {phone}")
            else:
                print(f"🚚 Yetkazib berish: {no_info}")
        else:
            print(f"🚚 Yetkazib berish: {no_info}")

        print("-" * 60)
        total_revenue += order.get('price', 0) # jami tushumni hisoblaydi

    print(f"\n💵 JAMI TUSHUM: {total_revenue:,} so'm")
    print(f"📈 Buyurtmalar soni: {len(orders)}")
    if orders:
        avg_order = total_revenue // len(orders)
        print(f"📊 O'rtacha buyurtma: {avg_order:,} so'm")
    print("=" * 60)