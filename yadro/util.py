# yadro/util.py
"""Yordamchi funksiyalar"""

import os


def cls():
    """Ekranni tozalash"""
    os.system('cls' if os.name == 'nt' else 'clear')