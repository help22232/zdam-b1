"""Wspólne narzędzia generatora Zdam B1: liczby słownie, godziny, daty, złotówki."""
import random

ONES = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć",
        "dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście",
        "siedemnaście", "osiemnaście", "dziewiętnaście"]
TENS = ["", "", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt",
        "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
HUNDREDS = ["", "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset",
            "osiemset", "dziewięćset"]


def plural_form(n, one, few, many):
    """Polska forma liczebnika: 1 rok, 2 lata, 5 lat; 22 lata; 12 lat."""
    if n == 1:
        return one
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return few
    return many


def words(n):
    """Liczebnik główny słownie (0–999 999)."""
    if n < 20:
        return ONES[n]
    if n < 100:
        t, o = divmod(n, 10)
        return TENS[t] + ("" if o == 0 else " " + ONES[o])
    if n < 1000:
        h, r = divmod(n, 100)
        return HUNDREDS[h] + ("" if r == 0 else " " + words(r))
    th, r = divmod(n, 1000)
    if th == 1:
        head = "tysiąc"
    else:
        head = words(th) + " " + plural_form(th, "tysiąc", "tysiące", "tysięcy")
    return head + ("" if r == 0 else " " + words(r))


def zl_words(n):
    return words(n) + " " + plural_form(n, "złoty", "złote", "złotych")


def zl(n):
    return f"{n} zł"


HOUR_ORD_LOC = ["", "pierwszej", "drugiej", "trzeciej", "czwartej", "piątej", "szóstej", "siódmej", "ósmej",
                "dziewiątej", "dziesiątej", "jedenastej", "dwunastej", "trzynastej", "czternastej",
                "piętnastej", "szesnastej", "siedemnastej", "osiemnastej", "dziewiętnastej", "dwudziestej",
                "dwudziestej pierwszej", "dwudziestej drugiej", "dwudziestej trzeciej"]
HOUR_ORD_NOM = ["", "pierwsza", "druga", "trzecia", "czwarta", "piąta", "szósta", "siódma", "ósma",
                "dziewiąta", "dziesiąta", "jedenasta", "dwunasta", "trzynasta", "czternasta", "piętnasta",
                "szesnasta", "siedemnasta", "osiemnasta", "dziewiętnasta", "dwudziesta",
                "dwudziesta pierwsza", "dwudziesta druga", "dwudziesta trzecia"]
HOUR_ORD_GEN = HOUR_ORD_LOC  # "do czternastej", "od ósmej" — dopełniacz = miejscownik w l.poj. żeńskiej


def hm(h, m=0):
    return f"{h}:{m:02d}"


def hour_words(h, m=0, form="loc"):
    """'o czternastej dwadzieścia' (form loc), 'czternasta' (nom)."""
    base = {"loc": HOUR_ORD_LOC, "nom": HOUR_ORD_NOM, "gen": HOUR_ORD_GEN}[form][h]
    if m == 0:
        return base
    if m < 10:
        return base + " zero " + words(m)
    return base + " " + words(m)


DAY_ORD_GEN = ["", "pierwszego", "drugiego", "trzeciego", "czwartego", "piątego", "szóstego", "siódmego",
               "ósmego", "dziewiątego", "dziesiątego", "jedenastego", "dwunastego", "trzynastego",
               "czternastego", "piętnastego", "szesnastego", "siedemnastego", "osiemnastego",
               "dziewiętnastego", "dwudziestego", "dwudziestego pierwszego", "dwudziestego drugiego",
               "dwudziestego trzeciego", "dwudziestego czwartego", "dwudziestego piątego",
               "dwudziestego szóstego", "dwudziestego siódmego", "dwudziestego ósmego",
               "dwudziestego dziewiątego", "trzydziestego", "trzydziestego pierwszego"]
MONTH_GEN = ["", "stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia",
             "września", "października", "listopada", "grudnia"]
MONTH_LEN = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def date_txt(d, m):
    return f"{d} {MONTH_GEN[m]}"


def date_words(d, m):
    return f"{DAY_ORD_GEN[d]} {MONTH_GEN[m]}"


DAYS_NOM = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
DAYS_ACC_PREP = ["w poniedziałek", "we wtorek", "w środę", "w czwartek", "w piątek", "w sobotę", "w niedzielę"]
DAYS_PL_ACC = ["w poniedziałki", "we wtorki", "w środy", "w czwartki", "w piątki", "w soboty", "w niedziele"]


def pick_distinct(rng, pool, k, exclude=()):
    cand = [x for x in dict.fromkeys(pool) if x not in exclude]
    rng.shuffle(cand)
    return cand[:k]


def abc(rng, correct, pool, k=2):
    """Pytanie wyboru: [poprawna, k błędnych] z puli (bez duplikatów)."""
    wrong = pick_distinct(rng, pool, k, exclude=(correct,))
    if len(wrong) < k:
        raise ValueError(f"za mało dystraktorów dla {correct!r}: {pool}")
    return [correct] + wrong


def make_rng(seed):
    return random.Random(seed)
