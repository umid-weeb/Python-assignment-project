# mijoz/yordam.py
"""Yordam va qo'llab-quvvatlash"""

from yadro import YORDAM_FILE, read_json, cls


def tez_yordam():
    """Yordam ma'lumotlarini ko'rsatish"""
    cls()
    data = read_json(YORDAM_FILE)
    print("☎️ YORDAM")
    print("_" * 40)

    yordam_list = data.get("yordam", [])
    if not yordam_list:
        print("❌ Yordam ma'lumotlari topilmadi")
        return

    for person in yordam_list:
        print(f"👤 Ismi: {person.get('ism', 'Nomalum')}")
        print(f"🚩 Roli: {person.get('role', 'Nomalum')}")
        print(f"📞 Telefon: {person.get('phone', 'Nomalum')}")
        print(f"📧 Email: {person.get('email', 'Nomalum')}")
        print(f"💭 Telegram: {person.get('telegram', 'Nomalum')}")
        print("_" * 40)