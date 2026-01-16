# yadro/json_baza.py
"""JSON fayllar bilan ishlash"""

import json
import os


def read_json(path):
    """JSON faylni o'qish"""
    try:
        if not os.path.exists(path):
            return {"products": []} if "maxsulot" in path else \
                {"memberships": {}} if "azolik" in path else \
                    {"orders": []}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Fayl o'qishda xatolik: {e}")
        return {}


def write_json(path, data):
    """JSON faylga yozish"""
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"❌ Faylga yozishda xatolik: {e}")