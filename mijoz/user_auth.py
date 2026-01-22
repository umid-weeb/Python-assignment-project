from yadro import read_json, write_json, cls
from mijoz import haridor_munyusi

USER_PATH = "baza/users.json"


def load_users():
    data = read_json(path=USER_PATH)
    if not data or "users" not in data:
        return {"users": []}
    return data


def sign_tanlash():
    print("1) Royhatdan otish")
    print("2) Xisobga kirish")
    print("0) Orqaga qaytish")

    tanlash = input("Tanlash: ").strip()

    if tanlash == "1":
        user_signup()
    elif tanlash == "2":
        user_login()
    elif tanlash == "0":
        return
    else:
        print("Xato tanlash")
        sign_tanlash()


def user_signup():
    cls()
    data = load_users()

    print("Royhatdan otish".center(50))

    ism = input("Ismingizni kiriting: ").strip()
    telefon = input("Telefon raqamingizni kiriting (+998...): ").strip()
    parol = input("Parolingizni kiriting: ").strip()

    if (not ism) or (not parol) or (not telefon.startswith("+998")):
        print("Xato malumot! Ism/parol bosh bolmasin va telefon +998 bilan boshlansin.")
        return user_signup()

    # Agar oldin ro'yxatdan o'tgan bo'lsa (ism+parol mos kelsa) => login oynasiga o'tkazamiz
    for u in data["users"]:
        if u["ism"].strip().lower() == ism.lower() and u["parol"] == parol:
            print("Siz avval ro'yxatdan o'tgansiz. Iltimos, hisobingizga kiring.")
            return user_login(default_name=ism)

    # Agar oldin ro'yxatdan o'tgan bo'lsa (ism+parol mos kelsa) => login oynasiga o'tkazamiz
    for u in data["users"]:
        if u["ism"].strip().lower() == ism.lower() and u["parol"] == parol:
            print("Siz avval ro'yxatdan o'tgansiz. Iltimos, hisobingizga kiring.")
            return user_login(default_name=ism)

    # aks holda yangi user qo'shamiz (ism bir xil bo'lishi mumkin)
    data["users"].append({
        "ism": ism,
        "telefon": telefon,
        "parol": parol
    })
    write_json(path=USER_PATH, data=data)
    print("Ro'yxatdan muvaffaqiyatli o'tdingiz!")
    return haridor_munyusi()


def user_login(default_name: str | None = None):
    cls()
    data = load_users()

    if len(data["users"]) == 0:
        print("Hali foydalanuvchi yo'q. Avval ro'yxatdan o'ting.")
        return user_signup()

    urinish = 2
    while urinish > 0:
        if default_name:
            user_ism = default_name.strip()
            print(f"Ism: {user_ism}")
        else:
            user_ism = input("Ismingizni kiriting: ").strip()

        user_parol = input("Parolingizni kiriting: ").strip()


        for user in data["users"]:
            if user["ism"].strip().lower() == user_ism.lower() and user["parol"] == user_parol:
                print("Muvaffaqiyatli kirdingiz!")
                return haridor_munyusi()

        urinish -= 1
        default_name = None  # keyingi urinishda ismni qayta so'raymiz
        if urinish > 0:
            print(f"Xato ism yoki parol. Qayta urinib ko'ring ({urinish}/2).")

    print("Hisob topilmadi. Ro'yxatdan o'tishingiz kerak!")
    return user_signup()
