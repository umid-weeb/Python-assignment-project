# yadro/input_tekshir.py
"""Foydalanuvchi kiritmalari validatsiyasi"""


def get_int_input(prompt, min_val=0):
    """Butun son kiritishni tekshirish"""
    while True:
        try:
            val = int(input(prompt))
            if val < min_val:
                print(f"❌ Qiymat {min_val} dan katta bo'lishi kerak")
                continue
            return val
        except ValueError:
            print("❌ Iltimos, raqam kiriting")


def get_choice(prompt, options):
    """Tanlov kiritishni tekshirish"""
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print(f"❌ Noto'g'ri tanlov. Faqat {', '.join(options)} kiriting")