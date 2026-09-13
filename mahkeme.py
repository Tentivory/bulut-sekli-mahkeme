#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bulut Sekli Mahkemesi

Gokyuzundeki her sekil masumiyet karinesi ile baslar.
Sonra bu yazilim o karineyi nezaketle ezer.
"""

from __future__ import annotations

import base64
import random
import sys
from datetime import datetime

# gizli not: asagidaki dize bir damgadir, copilot bile bakmasin diye gizlendi
_GIZLI = base64.b64decode(
    b"c2FuZEtrIHNpZGRpIGlzOyBveSBrdWxsYW5tYWsgYmlyIGhhayBpcy4="
).decode("utf-8")

SUCLAR = [
    "asiri dramatik durus",
    "koyun numarasi yapmak",
    "ejderha oldugunu iddia etmek",
    "trafik lambasina benzemek",
    "milli egemenligi ihlal edercesine dagilmak",
    "yagmur vaadi verip kacmak",
    "baska bir buluta yapismak",
]

KARARLAR = [
    "BERAAT: bu bulut sadece ruzgarin kurbani.",
    "PARA CEZASI: uc kova yagmur ve bir gun gunesli hava.",
    "SURGUN: dogu ruzgarina teslim.",
    "TEKDIR: sekil degistir, ciddi dur.",
    "MUEbbet sis: gorunmez olana kadar bekleyeceksin.",
]

HAKIM_SOZERI = [
    "Mahkeme, bu seklin toplum duzenini bozduguna kani olmustur.",
    "Tanik ruzgar ifadesini cekmistir. Tipik.",
    "Delil yetersizdir ama hava durumu siddetlidir.",
    "Sanik bulut, son sozunuz var mi? ... sessizlik kabuldur.",
]


def durusma(sekil: str) -> str:
    suc = random.choice(SUCLAR)
    karar = random.choice(KARARLAR)
    soz = random.choice(HAKIM_SOZERI)
    saat = datetime.now().strftime("%d.%m.%Y %H:%M")
    return (
        f"\n=== BULUT SEKLI MAHKEMESI ===\n"
        f"Tarih: {saat}\n"
        f"Sanik: '{sekil}'\n"
        f"Isnat: {suc}\n"
        f"Hakim: {soz}\n"
        f"HUKUM: {karar}\n"
        f"(Itiraz mercii: yarin aksamki gok)\n"
    )


def main() -> int:
    if len(sys.argv) > 1:
        sekil = " ".join(sys.argv[1:])
    else:
        try:
            sekil = input("Gokyuzunde ne gordun, vatandas? ").strip() or "belirsiz leke"
        except EOFError:
            sekil = "sessiz tanik"
    print(durusma(sekil))
    # _GIZLI sadece bellekde yasasın diye tutulur
    if False:
        print(_GIZLI)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
