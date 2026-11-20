"""Generuje teksty do czytania (data/reading.json) i nagrania do słuchania (data/listening.json + skrypty TTS).
Każdy szablon ma parametry; pytania są wyprowadzane z parametrów, więc odpowiedź jest zawsze zgodna z tekstem."""
import json, sys
from common import (make_rng, abc, words, zl_words, hour_words, hm, date_txt, date_words, plural_form,
                    DAYS_NOM, DAYS_ACC_PREP, DAYS_PL_ACC, MONTH_GEN, MONTH_LEN)

NAMES_M = ["Tomek", "Marek", "Piotr", "Paweł", "Adam", "Andrij", "Kamil", "Michał", "Ołeh", "Jakub"]
NAMES_F = ["Anna", "Kasia", "Ola", "Ewa", "Iryna", "Olena", "Natalia", "Marta", "Julia", "Oksana"]
CITIES = [("Warszawa", "Warszawy", "w Warszawie"), ("Kraków", "Krakowa", "w Krakowie"), ("Lublin", "Lublina", "w Lublinie"),
          ("Siedlce", "Siedlec", "w Siedlcach"), ("Sokołów Podlaski", "Sokołowa Podlaskiego", "w Sokołowie Podlaskim"),
          ("Białystok", "Białegostoku", "w Białymstoku"), ("Łódź", "Łodzi", "w Łodzi"), ("Poznań", "Poznania", "w Poznaniu"),
          ("Gdańsk", "Gdańska", "w Gdańsku"), ("Wrocław", "Wrocławia", "we Wrocławiu"), ("Radom", "Radomia", "w Radomiu"),
          ("Rzeszów", "Rzeszowa", "w Rzeszowie")]
UA_CITIES = [("Lwów", "Lwowa", "we Lwowie"), ("Kijów", "Kijowa", "w Kijowie"), ("Charków", "Charkowa", "w Charkowie"),
             ("Odessa", "Odessy", "w Odessie"), ("Winnica", "Winnicy", "w Winnicy"), ("Łuck", "Łucka", "w Łucku"),
             ("Równe", "Równego", "w Równem"), ("Dniepr", "Dniepru", "w Dnieprze"), ("Tarnopol", "Tarnopola", "w Tarnopolu")]
STREETS = ["Lipowa", "Długa", "Ogrodowa", "Kościuszki", "Mickiewicza", "Polna", "Szkolna", "Słoneczna", "Kwiatowa",
           "Leśna", "Sienkiewicza", "Kolejowa", "Parkowa", "Krótka", "Zielona"]


STREET_GEN = {"Lipowa": "Lipowej", "Długa": "Długiej", "Ogrodowa": "Ogrodowej", "Kościuszki": "Kościuszki",
              "Mickiewicza": "Mickiewicza", "Polna": "Polnej", "Szkolna": "Szkolnej", "Słoneczna": "Słonecznej",
              "Kwiatowa": "Kwiatowej", "Leśna": "Leśnej", "Sienkiewicza": "Sienkiewicza", "Kolejowa": "Kolejowej",
              "Parkowa": "Parkowej", "Krótka": "Krótkiej", "Zielona": "Zielonej"}
VOC = {"Tomek": "Tomku", "Marek": "Marku", "Piotr": "Piotrze", "Paweł": "Pawle", "Adam": "Adamie", "Andrij": "Andriju",
       "Kamil": "Kamilu", "Michał": "Michale", "Ołeh": "Ołehu", "Jakub": "Jakubie", "Anna": "Anno", "Kasia": "Kasiu",
       "Ola": "Olu", "Ewa": "Ewo", "Iryna": "Iryno", "Olena": "Oleno", "Natalia": "Natalio", "Marta": "Marto",
       "Julia": "Julio", "Oksana": "Oksano"}


def street(rng):
    return f"ul. {rng.choice(STREETS)} {rng.randint(1, 48)}"


def g(gender, m, f):
    return m if gender == "m" else f


def a_date(rng, months=(1, 2, 3, 4, 5, 6, 9, 10, 11, 12)):
    m = rng.choice(months)
    return rng.randint(1, MONTH_LEN[m]), m


def tf(q, val, hint):
    return dict(q=q, tf=val, hint=hint)


def ch(rng, q, correct, pool, hint):
    return dict(q=q, o=abc(rng, correct, pool), hint=hint)


def tf_pair(rng, true_s, false_s, hint):
    """Zdanie prawdziwe albo fałszywe (losowo) — test P/F."""
    return tf(true_s, True, hint) if rng.random() < 0.5 else tf(false_s, False, hint)


PRICES = lambda lo, hi, step: list(range(lo, hi + 1, step))


# ============================================================ CZYTANIE
def r_wynajem(rng):
    kind = rng.choice([("pokój", "pokój"), ("kawalerkę", "kawalerka"), ("mieszkanie dwupokojowe", "mieszkanie dwupokojowe"),
                       ("mieszkanie trzypokojowe", "mieszkanie trzypokojowe")])
    city = rng.choice(CITIES)
    m2 = rng.choice([12, 14, 16, 25, 28, 32, 38, 45, 52, 60])
    near = rng.choice(["dworca PKP", "centrum", "przystanku autobusowego", "uniwersytetu", "szpitala", "parku"])
    mins = rng.choice([3, 5, 7, 10, 15])
    price = rng.choice(PRICES(700, 2600, 50))
    media = rng.choice([100, 150, 200, 250, 300])
    kaucja_n = rng.choice([1, 2])
    pets = rng.random() < 0.4
    furn = rng.random() < 0.6
    d, mo = a_date(rng)
    contact = rng.choice([("SMS-em", "napisać SMS"), ("telefonicznie po 17:00", "zadzwonić po 17:00"),
                          ("mailowo", "napisać e-mail"), ("telefonicznie w weekendy", "zadzwonić w weekend")])
    name = rng.choice(NAMES_F + NAMES_M)
    text = (f"WYNAJMĘ {kind[0].upper()}\n\n"
            f"Mam do wynajęcia {kind[0]} ({m2} m²) {city[2]}, {mins} minut pieszo od {near}. "
            f"{'Mieszkanie jest umeblowane i ma pralkę.' if furn else 'Mieszkanie jest nieumeblowane, w kuchni jest tylko lodówka i kuchenka.'}\n\n"
            f"Cena: {price} zł miesięcznie + media (ok. {media} zł).\n"
            f"Kaucja: {'jeden czynsz' if kaucja_n == 1 else 'dwa czynsze'}.\n"
            f"{'Zwierzęta są mile widziane.' if pets else 'Niestety nie akceptujemy zwierząt.'} W mieszkaniu nie wolno palić.\n"
            f"Wolne od {date_txt(d, mo)}.\n\nKontakt: {contact[0]}. {name}")
    qs = [
        ch(rng, "Ile wynosi czynsz bez mediów?", f"{price} zł", [f"{p} zł" for p in (price + 100, price - 100, price + media, media)], f"Cena: {price} zł miesięcznie + media"),
        ch(rng, "Ile wynosi kaucja?", f"{price * kaucja_n} zł", [f"{price * (3 - kaucja_n)} zł", f"{media} zł", f"{price + media} zł"], f"Kaucja: {'jeden czynsz' if kaucja_n == 1 else 'dwa czynsze'}"),
        tf("W mieszkaniu można mieszkać z psem.", pets, "Zwierzęta są mile widziane." if pets else "nie akceptujemy zwierząt"),
        ch(rng, "Od kiedy mieszkanie jest wolne?", f"od {date_txt(d, mo)}", [f"od {date_txt(*a_date(rng))}" for _ in range(4)], f"Wolne od {date_txt(d, mo)}"),
        ch(rng, "Jak najlepiej skontaktować się z właścicielem?", contact[1], ["napisać SMS", "zadzwonić po 17:00", "napisać e-mail", "zadzwonić w weekend", "przyjść osobiście"], f"Kontakt: {contact[0]}"),
        tf_pair(rng, f"Mieszkanie jest {'umeblowane' if furn else 'nieumeblowane'}.", f"Mieszkanie jest {'nieumeblowane' if furn else 'umeblowane'}.",
                "Mieszkanie jest umeblowane" if furn else "Mieszkanie jest nieumeblowane"),
    ]
    return dict(kind="ogłoszenie", title=f"Ogłoszenie: {kind[1]} do wynajęcia", text=text, qs=qs)


SALE = [("rower górski", "m"), ("wózek dziecięcy", "m"), ("lodówkę", "f"), ("pralkę", "f"), ("laptop", "m"),
        ("telewizor", "m"), ("kanapę", "f"), ("biurko", "n"), ("szafę", "f"), ("ekspres do kawy", "m"),
        ("hulajnogę elektryczną", "f"), ("fotelik samochodowy", "m"), ("zmywarkę", "f"), ("gitarę", "f"), ("stół z krzesłami", "m")]
SALE_NOM = {"lodówkę": "lodówka", "pralkę": "pralka", "kanapę": "kanapa", "szafę": "szafa", "hulajnogę elektryczną": "hulajnoga elektryczna",
            "zmywarkę": "zmywarka", "gitarę": "gitara"}
REASONS = ["przeprowadzka do innego miasta", "zakup nowego modelu", "brak miejsca w mieszkaniu", "wyjazd za granicę",
           "remont mieszkania", "zmiana pracy"]


def r_sprzedam(rng):
    it, gnd = rng.choice(SALE)
    nom = SALE_NOM.get(it, it)
    age = rng.choice([1, 2, 3, 4, 5, 6])
    state = rng.choice(["bardzo dobry", "dobry", "idealny"])
    price = rng.choice(PRICES(80, 2500, 10))
    reason = rng.choice(REASONS)
    neg = rng.random() < 0.5
    city = rng.choice(CITIES)
    ship = rng.random() < 0.4
    name = rng.choice(NAMES_M + NAMES_F)
    lat = plural_form(age, "rok", "lata", "lat")
    text = (f"SPRZEDAM {it.upper()}\n\n"
            f"Sprzedam {it}, {'używany' if gnd == 'm' else 'używaną' if gnd == 'f' else 'używane'} przez {age} {lat}. Stan: {state}. "
            f"Powód sprzedaży: {reason}.\n\nCena: {price} zł{' (do negocjacji)' if neg else ' – cena ostateczna'}.\n"
            f"Odbiór osobisty {city[2]}{', możliwa też wysyłka kurierem za 30 zł' if ship else ', nie wysyłam'}.\n\n"
            f"Proszę dzwonić wieczorem. {name}")
    qs = [
        ch(rng, "Co sprzedaje autor ogłoszenia?", nom, [SALE_NOM.get(x, x) for x, _ in SALE], f"Sprzedam {it}"),
        ch(rng, "Ile kosztuje ta rzecz?", f"{price} zł", [f"{p} zł" for p in (price + 50, price - 30, price * 2, 30)], f"Cena: {price} zł"),
        ch(rng, "Dlaczego autor sprzedaje tę rzecz?", reason, REASONS, f"Powód sprzedaży: {reason}"),
        tf("Cenę można negocjować.", neg, "do negocjacji" if neg else "cena ostateczna"),
        tf("Rzecz można dostać kurierem.", ship, "możliwa też wysyłka kurierem" if ship else "nie wysyłam"),
        ch(rng, f"Jak długo używano tej rzeczy?", f"{age} {lat}", [f"{a} {plural_form(a, 'rok', 'lata', 'lat')}" for a in range(1, 8)], f"przez {age} {lat}"),
    ]
    return dict(kind="ogłoszenie", title=f"Ogłoszenie: sprzedaż", text=text, qs=qs)


JOBS = [("kelnera / kelnerkę", "kelner", "restauracji w centrum miasta"), ("kierowcę kat. B", "kierowca", "firmy kurierskiej"),
        ("magazyniera", "magazynier", "hurtowni spożywczej"), ("sprzedawcę", "sprzedawca", "sklepu z odzieżą"),
        ("pomoc kuchenną", "pomoc kuchenna", "baru mlecznego"), ("opiekunkę do dziecka", "opiekunka do dziecka", "rodziny z dwójką dzieci"),
        ("pracownika do sprzątania biur", "osoba do sprzątania", "firmy sprzątającej"), ("pracownika produkcji", "pracownik produkcji", "zakładu mięsnego"),
        ("recepcjonistkę", "recepcjonistka", "hotelu przy dworcu"), ("fryzjera / fryzjerkę", "fryzjer", "salonu fryzjerskiego")]
HOURS = [("od poniedziałku do piątku, 8:00–16:00", "w dni robocze"), ("w weekendy, 10:00–18:00", "w weekendy"),
         ("na dwie zmiany: 6:00–14:00 i 14:00–22:00", "na zmiany"), ("od wtorku do soboty, 9:00–17:00", "od wtorku do soboty"),
         ("popołudniami, 15:00–20:00", "popołudniami")]
CONTRACTS = ["umowę o pracę", "umowę zlecenie"]
REQS = [("znajomość języka polskiego w stopniu komunikatywnym", "komunikatywny polski"), ("prawo jazdy kat. B", "prawo jazdy"),
        ("aktualne badania sanepidowskie", "badania sanepidowskie"), ("doświadczenie minimum rok", "rok doświadczenia"),
        ("dyspozycyjność w weekendy", "praca w weekendy")]


def r_praca(rng):
    job, short, where = rng.choice(JOBS)
    hrs = rng.choice(HOURS)
    rate = rng.choice([31, 32, 33, 34, 35, 36, 38, 40, 42, 45])
    contract = rng.choice(CONTRACTS)
    req = rng.choice(REQS)
    exp_needed = req[1] == "rok doświadczenia"
    extra = rng.choice(["darmowy posiłek", "dofinansowanie do dojazdu", "kartę sportową", "premię co kwartał"])
    d, mo = a_date(rng)
    city = rng.choice(CITIES)
    text = (f"PRACA {city[2].upper()}\n\n"
            f"Właściciel {where} zatrudni {job}.\n\n"
            f"Praca {hrs[0]}. Stawka: {rate} zł brutto za godzinę.\n"
            f"Wymagamy: {req[0]}.{'' if exp_needed else ' Doświadczenie nie jest wymagane – wszystkiego nauczymy.'}\n"
            f"Oferujemy: {contract}, {extra}, miłą atmosferę.\n\n"
            f"CV prosimy wysyłać na adres e-mail do {date_txt(d, mo)}. Zadzwonimy tylko do wybranych osób.")
    qs = [
        ch(rng, "Kogo szuka pracodawca?", short, [j[1] for j in JOBS], f"zatrudni {job}"),
        ch(rng, "Ile wynosi stawka za godzinę?", f"{rate} zł", [f"{r} zł" for r in (rate + 5, rate - 4, rate * 8, rate + 10)], f"Stawka: {rate} zł"),
        tf("Kandydat musi mieć doświadczenie.", exp_needed, "doświadczenie minimum rok" if exp_needed else "Doświadczenie nie jest wymagane"),
        ch(rng, "Jaką umowę oferuje firma?", contract.replace("umowę", "umowa"), ["umowa o pracę", "umowa zlecenie", "umowa o dzieło"], f"Oferujemy: {contract}"),
        ch(rng, "Jak trzeba zgłosić się do pracy?", "wysłać CV e-mailem", ["wysłać CV e-mailem", "przyjść osobiście", "zadzwonić do właściciela", "wysłać SMS"], "CV prosimy wysyłać na adres e-mail"),
        ch(rng, "Co jeszcze oferuje pracodawca?", extra, ["darmowy posiłek", "dofinansowanie do dojazdu", "kartę sportową", "premię co kwartał", "mieszkanie"], f"Oferujemy: … {extra}"),
    ]
    return dict(kind="ogłoszenie", title="Oferta pracy", text=text, qs=qs)


INST = [("Przychodnia", "przychodnia", "Przychodni"), ("Biblioteka miejska", "biblioteka", "Biblioteki"), ("Basen miejski", "basen", "Basenu"),
        ("Urząd Stanu Cywilnego", "urząd", "Urzędu"), ("Apteka „Pod Lipami”", "apteka", "Apteki"), ("Dom Kultury", "dom kultury", "Domu Kultury")]
CLOSE_REASONS = ["remont", "inwentaryzację", "awarię ogrzewania", "szkolenie pracowników", "wymianę instalacji elektrycznej"]
CLOSE_NOM = {"remont": "remont", "inwentaryzację": "inwentaryzacja", "awarię ogrzewania": "awaria ogrzewania",
             "szkolenie pracowników": "szkolenie pracowników", "wymianę instalacji elektrycznej": "wymiana instalacji elektrycznej"}


def r_komunikat(rng):
    inst, short, gen = rng.choice(INST)
    m = rng.choice([1, 2, 3, 4, 5, 6, 9, 10, 11])
    d1 = rng.randint(1, 20)
    days = rng.choice([2, 3, 4, 5, 7])
    d2 = d1 + days - 1
    reason = rng.choice(CLOSE_REASONS)
    alt = rng.choice(["filia na " + street(rng), "punkt w budynku urzędu miasta", "oddział na osiedlu Słonecznym"])
    after = rng.choice([("8:00", "20:00"), ("7:00", "18:00"), ("9:00", "19:00"), ("10:00", "16:00")])
    text = (f"KOMUNIKAT\n\n{inst} uprzejmie informuje, że w dniach {d1}–{d2} {MONTH_GEN[m]} będzie nieczynna/nieczynny "
            f"z powodu: {CLOSE_NOM[reason]}.\n\nW tym czasie zapraszamy do: {alt}.\n"
            f"Od {d2 + 1} {MONTH_GEN[m]} pracujemy normalnie, w godzinach {after[0]}–{after[1]}.\n"
            f"Za utrudnienia przepraszamy.\nDyrekcja {gen}").replace("nieczynna/nieczynny", "nieczynna" if inst.startswith(("Przychodnia", "Biblioteka", "Apteka")) else "nieczynny")
    qs = [
        ch(rng, "Ile dni instytucja będzie zamknięta?", f"{days} {plural_form(days, 'dzień', 'dni', 'dni')}", [f"{x} {plural_form(x, 'dzień', 'dni', 'dni')}" for x in (1, 2, 3, 4, 5, 7, 10)], f"w dniach {d1}–{d2}"),
        ch(rng, "Dlaczego instytucja będzie zamknięta?", CLOSE_NOM[reason], list(CLOSE_NOM.values()), f"z powodu: {CLOSE_NOM[reason]}"),
        ch(rng, "Gdzie można iść w tym czasie?", alt, ["filia na " + street(rng), "punkt w budynku urzędu miasta", "oddział na osiedlu Słonecznym", "nigdzie"], f"W tym czasie czynna jest {alt}"),
        ch(rng, "Od której godziny instytucja pracuje po otwarciu?", f"od {after[0]}", ["od 8:00", "od 7:00", "od 9:00", "od 10:00", "od 12:00"], f"w godzinach {after[0]}–{after[1]}"),
        tf_pair(rng, f"Instytucja otworzy się ponownie {d2 + 1} {MONTH_GEN[m]}.", f"Instytucja otworzy się ponownie {d2 + 3} {MONTH_GEN[m]}.", f"Od {d2 + 1} {MONTH_GEN[m]} pracujemy normalnie"),
    ]
    return dict(kind="komunikat", title=f"Komunikat: {short}", text=text, qs=qs)


def r_rozklad(rng):
    line = rng.choice([2, 3, 5, 7, 8, 11, 12, 14, 17, 21, 24])
    d, mo = a_date(rng)
    freq_old, freq_new = rng.choice([(30, 20), (20, 15), (15, 10), (20, 30), (10, 15), (15, 20)])
    st = rng.choice(STREETS)
    sunday = rng.random() < 0.5
    repl = rng.choice([line + 100, line + 50, 30 + line])
    text = (f"ZMIANA ROZKŁADU JAZDY – LINIA {line}\n\n"
            f"Od {date_txt(d, mo)} z powodu remontu ulicy {STREET_GEN[st]} autobusy linii {line} pojadą objazdem. "
            f"Przystanek „{st}” będzie nieczynny – najbliższy przystanek znajduje się przy dworcu.\n\n"
            f"W dni robocze autobusy będą kursować co {freq_new} minut (do tej pory: co {freq_old} minut).\n"
            f"{'W niedziele linia ' + str(line) + ' nie będzie kursować. Zamiast niej pojedzie linia ' + str(repl) + '.' if sunday else 'W soboty i niedziele rozkład się nie zmienia.'}\n\n"
            f"Przepraszamy pasażerów za utrudnienia.")
    more = freq_new < freq_old
    qs = [
        ch(rng, "Dlaczego zmienia się rozkład?", f"remont ulicy {STREET_GEN[st]}", [f"remont ulicy {STREET_GEN[x]}" for x in STREETS] + ["nowe autobusy", "mniej pasażerów"], f"z powodu remontu ulicy {STREET_GEN[st]}"),
        ch(rng, "Jak często autobusy będą jeździć w dni robocze?", f"co {freq_new} minut", [f"co {x} minut" for x in (10, 15, 20, 30, 40)], f"co {freq_new} minut"),
        tf("Autobusy w dni robocze będą jeździć częściej niż wcześniej.", more, f"co {freq_new} minut (do tej pory: co {freq_old} minut)"),
        tf("W niedziele linia " + str(line) + " jeździ normalnie.", not sunday, "W niedziele linia nie będzie kursować" if sunday else "W soboty i niedziele rozkład się nie zmienia"),
        ch(rng, f"Gdzie jest najbliższy czynny przystanek?", "przy dworcu", ["przy dworcu", f"na ulicy {STREET_GEN[st]}", "przy szpitalu", "na rynku"], "najbliższy przystanek znajduje się przy dworcu"),
    ]
    return dict(kind="komunikat", title=f"Zmiana rozkładu – linia {line}", text=text, qs=qs)


COURSES = [("język polski dla obcokrajowców", "polski"), ("język angielski dla dorosłych", "angielski"), ("joga dla początkujących", "joga"),
           ("kurs gotowania", "gotowanie"), ("komputer dla seniorów", "komputer"), ("taniec towarzyski", "taniec"),
           ("rysunek i malarstwo", "malarstwo"), ("szachy dla dzieci", "szachy"), ("fotografia telefonem", "fotografia")]


def r_kurs(rng):
    course, short = rng.choice(COURSES)
    di = rng.randrange(7)
    h = rng.choice([16, 17, 18, 19])
    price = rng.choice([60, 80, 100, 120, 150, 180, 200])
    per = rng.choice(["za miesiąc", "za semestr", "za 10 zajęć"])
    free = rng.random() < 0.5
    place = rng.choice(["w Domu Kultury", "w bibliotece miejskiej", "w Szkole Podstawowej nr 2", "w klubie osiedlowym"])
    d, mo = a_date(rng)
    maxp = rng.choice([8, 10, 12, 15])
    text = (f"ZAPRASZAMY NA ZAJĘCIA: {course.upper()}\n\n"
            f"Zajęcia odbywają się {DAYS_PL_ACC[di]} o godzinie {h}:00 {place}. Każde spotkanie trwa 90 minut.\n"
            f"Grupa liczy maksymalnie {maxp} osób.\n\nCena: {price} zł {per}."
            f"{' Pierwsze zajęcia są bezpłatne!' if free else ''}\n"
            f"Zapisy do {date_txt(d, mo)} – osobiście w sekretariacie albo telefonicznie.\n"
            f"Liczba miejsc ograniczona – decyduje kolejność zgłoszeń.")
    qs = [
        ch(rng, "W jaki dzień są zajęcia?", DAYS_PL_ACC[di], DAYS_PL_ACC, f"Zajęcia odbywają się {DAYS_PL_ACC[di]}"),
        ch(rng, "Ile osób może być w grupie?", f"maksymalnie {maxp}", [f"maksymalnie {x}" for x in (6, 8, 10, 12, 15, 20)], f"maksymalnie {maxp} osób"),
        ch(rng, "Ile kosztują zajęcia?", f"{price} zł {per}", [f"{p} zł {per}" for p in (40, 60, 80, 100, 120, 150, 180, 200, 250)], f"Cena: {price} zł {per}"),
        tf("Pierwsze zajęcia są za darmo.", free, "Pierwsze zajęcia są bezpłatne" if free else f"Cena: {price} zł {per}"),
        ch(rng, "Jak długo trwa jedno spotkanie?", "półtorej godziny", ["godzinę", "półtorej godziny", "dwie godziny", "45 minut"], "Każde spotkanie trwa 90 minut"),
        tf("Na zajęcia można zapisać się tylko przez internet.", False, "osobiście w sekretariacie albo telefonicznie"),
    ]
    return dict(kind="ogłoszenie", title=f"Zajęcia: {short}", text=text, qs=qs)


EVENTS = [("urodziny", "na moje urodziny", "urodzinowe przyjęcie"), ("parapetówka", "na parapetówkę", "parapetówka"),
          ("grill", "na grilla", "grill"), ("imieniny", "na moje imieniny", "imieniny")]
BRING = ["sałatkę", "ciasto", "coś do picia", "gry planszowe", "kiełbaski na grilla", "dobry humor"]
BRING_NOM = {"sałatkę": "sałatka", "ciasto": "ciasto", "coś do picia": "coś do picia", "gry planszowe": "gry planszowe",
             "kiełbaski na grilla": "kiełbaski", "dobry humor": "tylko dobry humor"}


def r_zaproszenie(rng):
    gs = rng.choice("mf")
    sender = rng.choice(NAMES_M if gs == "m" else NAMES_F)
    gr = rng.choice("mf")
    rec = rng.choice(NAMES_M if gr == "m" else NAMES_F)
    ev, na, evn = rng.choice(EVENTS)
    di = rng.choice([4, 5, 6])
    h = rng.choice([15, 16, 17, 18, 19])
    where = rng.choice([("u mnie w domu", "w domu"), ("w ogrodzie moich rodziców", "w ogrodzie"), ("w pizzerii „Roma” na rynku", "w pizzerii"),
                        ("nad jeziorem", "nad jeziorem")])
    bring = rng.choice(BRING)
    d, mo = a_date(rng, (5, 6, 7, 8, 9))
    who = rng.choice(["koledzy z pracy", "moja siostra z mężem", "znajomi z kursu polskiego", "sąsiedzi"])
    text = (f"{'Cześć' if rng.random() < .5 else 'Hej'} {VOC[rec]}!\n\n"
            f"Chcę Cię zaprosić {na}! Spotykamy się {DAYS_ACC_PREP[di]}, {date_txt(d, mo)}, o {h}:00 {where[0]}. "
            f"Będą też {who}.\n"
            f"Jeśli możesz, przynieś {bring}. Resztę przygotuję sam{'a' if gs == 'f' else ''}.\n"
            f"Daj znać do czwartku, czy przyjdziesz, bo muszę zrobić zakupy.\n\nDo zobaczenia!\n{sender}")
    qs = [
        ch(rng, f"Na jaką okazję {sender} zaprasza?", ev, [e[0] for e in EVENTS], f"Chcę Cię zaprosić {na}"),
        ch(rng, "Kiedy jest spotkanie?", f"{DAYS_ACC_PREP[di]} o {h}:00", [f"{DAYS_ACC_PREP[x]} o {y}:00" for x in (3, 4, 5, 6) for y in (15, 17, 19)], f"{DAYS_ACC_PREP[di]} … o {h}:00"),
        ch(rng, "Gdzie odbędzie się spotkanie?", where[1], ["w domu", "w ogrodzie", "w pizzerii", "nad jeziorem"], where[0]),
        ch(rng, f"Co {rec} ma przynieść?", BRING_NOM[bring], list(BRING_NOM.values()), f"przynieś {bring}"),
        ch(rng, f"Do kiedy trzeba odpowiedzieć?", "do czwartku", ["do czwartku", "do piątku", "do soboty", "do środy"], "Daj znać do czwartku"),
        tf(f"{sender} sam{'a' if gs == 'f' else ''} przygotuje jedzenie.", True, f"Resztę przygotuję sam{'a' if gs == 'f' else ''}"),
    ]
    return dict(kind="e-mail", title=f"E-mail: zaproszenie", text=text, qs=qs)


PLANS = [("do kina w sobotę", "kino"), ("na wycieczkę rowerową w niedzielę", "wycieczka rowerowa"), ("na basen w piątek", "basen"),
         ("na wspólną naukę do egzaminu", "nauka"), ("na koncert na rynku", "koncert"), ("na zakupy do Warszawy", "zakupy")]
PROBLEMS = [("moje dziecko jest chore i musi zostać w domu", "choroba dziecka"), ("szef poprosił mnie o pracę w weekend", "praca w weekend"),
            ("zepsuł mi się samochód", "awaria samochodu"), ("przyjeżdża do mnie mama z Ukrainy", "przyjazd mamy"),
            ("mam ważną wizytę u lekarza", "wizyta u lekarza")]


def r_przeprosiny(rng):
    gs = rng.choice("mf")
    sender = rng.choice(NAMES_M if gs == "m" else NAMES_F)
    rec = rng.choice(NAMES_M + NAMES_F)
    plan, plan_s = rng.choice(PLANS)
    prob, prob_s = rng.choice(PROBLEMS)
    new_day = rng.randrange(7)
    text = (f"Cześć {rec},\n\n"
            f"bardzo Cię przepraszam, ale niestety nie mogę pójść z Tobą {plan}. Wczoraj okazało się, że {prob}. "
            f"Było mi bardzo przykro, bo naprawdę się cieszył{'am' if gs == 'f' else 'em'}.\n"
            f"Czy możemy przełożyć nasze spotkanie na {DAYS_NOM[new_day] if new_day not in (2, 5, 6) else ['środę','sobotę','niedzielę'][[2,5,6].index(new_day)]}? "
            f"Jeśli ten dzień Ci nie pasuje, zadzwoń – na pewno coś wymyślimy.\n\nJeszcze raz przepraszam!\n{sender}")
    new_acc = DAYS_ACC_PREP[new_day].split(" ", 1)[1]
    qs = [
        ch(rng, f"Dlaczego {sender} pisze?", "żeby odwołać spotkanie", ["żeby odwołać spotkanie", "żeby zaprosić na urodziny", "żeby podziękować za pomoc", "żeby zapytać o pracę"], "nie mogę pójść z Tobą"),
        ch(rng, "Jaki był plan?", plan_s, [p[1] for p in PLANS], f"pójść z Tobą {plan}"),
        ch(rng, f"Jaki problem ma {sender}?", prob_s, [p[1] for p in PROBLEMS], f"okazało się, że {prob}"),
        ch(rng, f"Na kiedy {sender} proponuje nowe spotkanie?", f"na {new_acc}", [f"na {DAYS_ACC_PREP[x].split(' ', 1)[1]}" for x in range(7)], f"przełożyć nasze spotkanie na {new_acc}"),
        tf(f"{sender} nie chce spotkać się z {rec if False else 'przyjacielem'} w ogóle.", False, "Czy możemy przełożyć nasze spotkanie"),
    ]
    qs[-1]["q"] = f"{sender} nie chce już się spotkać."
    return dict(kind="e-mail", title="E-mail: zmiana planów", text=text, qs=qs)


FESTS = [("Dni Miasta", "festyn"), ("Jarmark Bożonarodzeniowy", "jarmark"), ("Festiwal Smaków", "festiwal kulinarny"),
         ("Noc Muzeów", "noc muzeów"), ("Piknik Rodzinny", "piknik")]
ATTR = ["koncert zespołu rockowego", "warsztaty dla dzieci", "pokaz tańca ludowego", "stoiska z regionalnym jedzeniem",
        "turniej piłki nożnej", "pokaz sztucznych ogni", "malowanie twarzy", "kino plenerowe"]


def r_festyn(rng):
    name, short = rng.choice(FESTS)
    d, mo = a_date(rng, (5, 6, 7, 8, 12))
    h1, h2 = rng.choice([(10, 22), (12, 23), (14, 22), (11, 20)])
    at = rng.sample(ATTR, 3)
    paid = rng.random() < 0.4
    price = rng.choice([10, 15, 20, 25])
    kids = rng.choice([6, 7, 10, 12])
    place = rng.choice(["na rynku", "w parku miejskim", "na stadionie", "nad zalewem"])
    final = at[-1]
    text = (f"{name.upper()} – ZAPRASZAMY!\n\n"
            f"{date_txt(d, mo).capitalize()}, w godzinach {h1}:00–{h2}:00, {place}.\n\n"
            f"W programie: {at[0]}, {at[1]}, a na zakończenie – {final}.\n"
            f"{'Bilety: ' + str(price) + ' zł, dzieci do lat ' + str(kids) + ' wchodzą za darmo.' if paid else 'Wstęp wolny!'}\n"
            f"Parking przy imprezie będzie zamknięty – prosimy przyjechać autobusem lub rowerem.")
    qs = [
        ch(rng, "Gdzie odbędzie się impreza?", place, ["na rynku", "w parku miejskim", "na stadionie", "nad zalewem"], place),
        ch(rng, "Co będzie na zakończenie imprezy?", final, ATTR, f"na zakończenie – {final}"),
        tf("Wejście na imprezę jest bezpłatne dla wszystkich.", not paid, "Wstęp wolny" if not paid else f"Bilety: {price} zł"),
        ch(rng, "Do której godziny trwa impreza?", f"do {h2}:00", [f"do {x}:00" for x in (18, 20, 21, 22, 23)], f"{h1}:00–{h2}:00"),
        tf("Organizatorzy proszą, żeby przyjechać samochodem.", False, "Parking … będzie zamknięty – prosimy przyjechać autobusem lub rowerem"),
    ]
    return dict(kind="ogłoszenie", title=f"Wydarzenie: {short}", text=text, qs=qs)


def r_regulamin(rng):
    kind = rng.choice(["biblioteka", "basen", "siłownia"])
    if kind == "biblioteka":
        n = rng.choice([3, 4, 5, 6]); w = rng.choice([2, 3, 4]); fine = rng.choice([0.5, 1, 2])
        fine_s = f"{fine:.2f}".replace(".", ",") + " zł"
        text = (f"REGULAMIN WYPOŻYCZALNI – NAJWAŻNIEJSZE ZASADY\n\n1. Jednorazowo można wypożyczyć maksymalnie {n} książki.\n"
                f"2. Książki wypożyczamy na {w} tygodnie. Termin można przedłużyć jeden raz – przez internet lub telefonicznie.\n"
                f"3. Za każdy dzień spóźnienia płacimy karę: {fine_s}.\n4. Zgubioną lub zniszczoną książkę trzeba odkupić.\n"
                f"5. Do wypożyczenia potrzebna jest karta biblioteczna. Kartę wyrabiamy bezpłatnie na podstawie dowodu osobistego lub paszportu.")
        qs = [ch(rng, "Ile książek można wypożyczyć naraz?", str(n), ["2", "3", "4", "5", "6", "10"], f"maksymalnie {n} książki"),
              ch(rng, "Na jak długo wypożycza się książki?", f"na {w} tygodnie", ["na tydzień", "na 2 tygodnie", "na 3 tygodnie", "na 4 tygodnie", "na miesiąc"], f"na {w} tygodnie"),
              ch(rng, "Ile kosztuje dzień spóźnienia?", fine_s, ["0,50 zł", "1,00 zł", "2,00 zł", "5,00 zł"], f"karę: {fine_s}"),
              tf("Za kartę biblioteczną trzeba zapłacić.", False, "Kartę wyrabiamy bezpłatnie"),
              tf("Termin oddania książki można przedłużyć przez telefon.", True, "przez internet lub telefonicznie")]
    elif kind == "basen":
        age = rng.choice([7, 10, 12]); price = rng.choice([14, 16, 18, 20]); h = rng.choice([6, 7])
        text = (f"REGULAMIN PŁYWALNI\n\n1. Pływalnia jest czynna codziennie od {h}:00 do 22:00.\n"
                f"2. Czepek kąpielowy jest obowiązkowy.\n3. Dzieci do lat {age} mogą przebywać na pływalni tylko z opiekunem.\n"
                f"4. Przed wejściem do wody trzeba wziąć prysznic.\n5. Bilet normalny na godzinę kosztuje {price} zł, ulgowy – {price - 5} zł.\n"
                f"6. Na terenie pływalni nie wolno jeść ani biegać.")
        qs = [ch(rng, "Od której godziny jest czynny basen?", f"od {h}:00", ["od 6:00", "od 7:00", "od 8:00", "od 9:00"], f"od {h}:00"),
              ch(rng, "Ile kosztuje bilet ulgowy?", f"{price - 5} zł", [f"{x} zł" for x in range(8, 21)], f"ulgowy – {price - 5} zł"),
              tf(f"Dziecko w wieku {age - 2} lat może pływać samo.", False, f"Dzieci do lat {age} … tylko z opiekunem"),
              tf("Na basenie trzeba mieć czepek.", True, "Czepek kąpielowy jest obowiązkowy"),
              ch(rng, "Czego nie wolno robić na pływalni?", "jeść", ["jeść", "brać prysznica", "kupować biletów", "pływać w czepku"], "nie wolno jeść ani biegać")]
    else:
        price = rng.choice([99, 119, 129, 149]); stud = rng.choice([69, 79, 89]); h2 = rng.choice([22, 23])
        text = (f"SIŁOWNIA „FORMA” – INFORMACJE DLA KLIENTÓW\n\n• Otwarte od poniedziałku do soboty, 6:00–{h2}:00. W niedziele nieczynne.\n"
                f"• Karnet miesięczny: {price} zł, dla studentów i uczniów: {stud} zł.\n• Pierwszy trening z trenerem jest gratis.\n"
                f"• Obowiązkowe są czyste buty sportowe i ręcznik.\n• Szafki zamykamy własną kłódką.")
        qs = [ch(rng, "Ile kosztuje karnet dla studenta?", f"{stud} zł", [f"{x} zł" for x in (69, 79, 89, 99, 119)], f"dla studentów i uczniów: {stud} zł"),
              tf("Siłownia jest czynna w niedzielę.", False, "W niedziele nieczynne"),
              ch(rng, "Co trzeba mieć ze sobą?", "ręcznik i czyste buty", ["ręcznik i czyste buty", "własne hantle", "zdjęcie do karnetu", "czepek"], "czyste buty sportowe i ręcznik"),
              tf("Pierwszy trening z trenerem jest bezpłatny.", True, "Pierwszy trening z trenerem jest gratis"),
              ch(rng, "Do której godziny jest otwarta siłownia?", f"do {h2}:00", ["do 20:00", "do 21:00", "do 22:00", "do 23:00"], f"6:00–{h2}:00")]
    return dict(kind="regulamin", title=f"Regulamin: {kind}", text=text, qs=qs)


JOBS_STORY = [("w magazynie", "magazyn"), ("w sklepie", "sklep"), ("w hotelu", "hotel"), ("w szpitalu", "szpital"),
              ("w firmie budowlanej", "budowa"), ("w restauracji", "restauracja"), ("w szkole", "szkoła")]
HOBBY_STORY = [("gra w piłkę", "piłka nożna"), ("piecze ciasta", "pieczenie"), ("biega w parku", "bieganie"),
               ("chodzi do biblioteki", "czytanie"), ("jeździ na rowerze", "rower"), ("śpiewa w chórze", "śpiew")]


def r_historia(rng):
    gs = rng.choice("mf")
    name = rng.choice(NAMES_M if gs == "m" else NAMES_F)
    src = rng.choice(UA_CITIES)
    city = rng.choice(CITIES)
    yrs = rng.choice([2, 3, 4, 5, 6])
    job1, job1s = rng.choice(JOBS_STORY)
    job2, job2s = rng.choice([j for j in JOBS_STORY if j != (job1, job1s)])
    hob, hobs = rng.choice(HOBBY_STORY)
    exam = rng.random() < 0.5
    G = lambda m, f: g(gs, m, f)
    text = (f"{name} przyjechał{G('', 'a')} do Polski {yrs} {plural_form(yrs, 'rok', 'lata', 'lat')} temu z miasta {src[0]}. "
            f"Na początku mieszkał{G('', 'a')} u znajomych i pracował{G('', 'a')} {job1}. Nie znał{G('', 'a')} wtedy prawie żadnego słowa po polsku, "
            f"więc wieczorami chodził{G('', 'a')} na bezpłatny kurs językowy.\n\n"
            f"Po roku przeprowadził{G('', 'a')} się do miasta {city[0]} i znalazł{G('', 'a')} pracę {job2}. "
            f"Mówi, że najtrudniejsze były dla {G('niego', 'niej')} urzędy i rozmowy przez telefon, ale teraz radzi sobie bez problemu.\n\n"
            f"W wolnym czasie {name} {hob}. "
            f"{'W grudniu chce zdawać egzamin z języka polskiego na poziomie B1, bo potrzebuje certyfikatu do karty stałego pobytu.' if exam else 'Marzy o tym, żeby za kilka lat otworzyć własną małą firmę.'}")
    qs = [
        ch(rng, f"Skąd pochodzi {name}?", f"z miasta {src[0]}", [f"z miasta {c[0]}" for c in UA_CITIES], f"z miasta {src[0]}"),
        ch(rng, f"Ile lat {name} mieszka w Polsce?", f"{yrs} {plural_form(yrs, 'rok', 'lata', 'lat')}", [f"{x} {plural_form(x, 'rok', 'lata', 'lat')}" for x in range(1, 9)], f"{yrs} {plural_form(yrs, 'rok', 'lata', 'lat')} temu"),
        ch(rng, f"Gdzie {name} pracował{G('', 'a')} na początku?", job1, [j[0] for j in JOBS_STORY], f"pracował{G('', 'a')} {job1}"),
        tf(f"Na początku {name} dobrze mówił{G('', 'a')} po polsku.", False, "Nie znał wtedy prawie żadnego słowa po polsku"),
        ch(rng, f"Co {name} lubi robić w wolnym czasie?", hobs, [h[1] for h in HOBBY_STORY], f"W wolnym czasie {name} {hob}"),
        tf_pair(rng, f"{name} chce zdawać egzamin B1." if exam else f"{name} chce mieć własną firmę.",
                f"{name} chce mieć własną firmę." if exam else f"{name} chce zdawać egzamin B1.",
                "chce zdawać egzamin" if exam else "Marzy o tym, żeby … otworzyć własną małą firmę"),
    ]
    return dict(kind="tekst narracyjny", title=f"Historia: {name}", text=text, qs=qs)


def r_sms(rng):
    gs = rng.choice("mf")
    name = rng.choice(NAMES_M if gs == "m" else NAMES_F)
    late = rng.choice([10, 15, 20, 30])
    why = rng.choice([("autobus się spóźnił", "spóźniony autobus"), ("stoję w korku", "korek"), ("szef zatrzymał mnie w pracy", "praca"),
                      ("musiałem/musiałam odebrać dziecko z przedszkola", "dziecko")])
    buy = rng.choice([("chleb i masło", "chleb i masło"), ("mleko dla dzieci", "mleko"), ("baterie do pilota", "baterie"), ("leki z apteki", "leki")])
    place = rng.choice(["przy fontannie", "przed kinem", "przy wejściu do galerii", "na przystanku przy dworcu"])
    whytxt = why[0].replace("musiałem/musiałam", "musiał" + g(gs, "em", "am"))
    text = (f"WIADOMOŚĆ OD: {name}\n\n"
            f"Hej! Spóźnię się ok. {late} minut, bo {whytxt}. Przepraszam! "
            f"Czekaj na mnie {place}, nie w środku. Aha, i jeśli możesz, kup po drodze {buy[0]} – oddam Ci pieniądze. "
            f"Wieczorem musimy jeszcze zadzwonić do babci, bo ma dziś urodziny!")
    qs = [
        ch(rng, f"O ile minut spóźni się {name}?", f"ok. {late} minut", [f"ok. {x} minut" for x in (5, 10, 15, 20, 30, 45)], f"Spóźnię się ok. {late} minut"),
        ch(rng, "Dlaczego się spóźni?", why[1], ["spóźniony autobus", "korek", "praca", "dziecko", "choroba"], f"bo {whytxt}"),
        ch(rng, "Gdzie mają się spotkać?", place, ["przy fontannie", "przed kinem", "przy wejściu do galerii", "na przystanku przy dworcu"], f"Czekaj na mnie {place}"),
        ch(rng, "Co trzeba kupić?", buy[1], ["chleb i masło", "mleko", "baterie", "leki", "kwiaty"], f"kup po drodze {buy[0]}"),
        tf("Babcia ma dzisiaj imieniny.", False, "bo ma dziś urodziny"),
    ]
    return dict(kind="wiadomość", title="Wiadomość SMS", text=text, qs=qs)


READING_T = [r_wynajem, r_sprzedam, r_praca, r_komunikat, r_rozklad, r_kurs, r_zaproszenie, r_przeprosiny, r_festyn, r_regulamin, r_historia, r_sms]


# ============================================================ SŁUCHANIE (skrypty dla TTS: A = kobieta, B = mężczyzna)
def l_dworzec(rng):
    fr, to = rng.sample(CITIES, 2)
    h, m = rng.choice(range(6, 22)), rng.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
    peron, tor = rng.randint(1, 5), rng.randint(1, 8)
    late = rng.choice([0, 10, 15, 20, 30, 40])
    kind = rng.choice(["osobowy", "pospieszny", "regionalny"])
    s = (f"Uwaga, uwaga. Pociąg {kind} z {fr[1]} do {to[1]}, planowy odjazd godzina {hour_words(h, m, 'nom')}, "
         f"odjedzie z toru {words(tor) if tor > 2 else ['', 'pierwszego', 'drugiego'][tor]} przy peronie {['', 'pierwszym', 'drugim', 'trzecim', 'czwartym', 'piątym'][peron]}. ")
    s = s.replace(f"toru {words(tor)}", "toru " + ['', 'pierwszego', 'drugiego', 'trzeciego', 'czwartego', 'piątego', 'szóstego', 'siódmego', 'ósmego'][tor])
    if late:
        s += f"Pociąg jest opóźniony o około {words(late)} minut. Opóźnienie może ulec zmianie. Za utrudnienia przepraszamy."
    else:
        s += "Pociąg odjedzie zgodnie z rozkładem. Prosimy zachować ostrożność przy krawędzi peronu."
    qs = [
        ch(rng, "Dokąd jedzie pociąg?", f"do {to[1]}", [f"do {c[1]}" for c in CITIES], f"do {to[1]}"),
        ch(rng, "Z którego peronu odjedzie pociąg?", f"z peronu {peron}", [f"z peronu {x}" for x in range(1, 6)], f"przy peronie {peron}"),
        ch(rng, "O której jest planowy odjazd?", hm(h, m), [hm(h + 1, m), hm(h, (m + 15) % 60), hm(h - 1, m), hm(h, (m + 30) % 60)], f"godzina {hm(h, m)}"),
        ch(rng, "Jakie jest opóźnienie?", f"ok. {late} minut" if late else "nie ma opóźnienia",
           ["nie ma opóźnienia"] + [f"ok. {x} minut" for x in (10, 15, 20, 30, 40)], "opóźniony o około …" if late else "zgodnie z rozkładem"),
    ]
    return dict(title="Komunikat na dworcu", lines=[("A", s)], qs=qs)


SYMPT = [("gorączkę i kaszel", "gorączka i kaszel"), ("ból gardła", "ból gardła"), ("silny ból głowy", "ból głowy"),
         ("ból brzucha", "ból brzucha"), ("katar i kaszel", "katar"), ("ból pleców", "ból pleców")]
DOCS = ["doktora Nowaka", "doktor Kowalskiej", "doktora Wiśniewskiego", "doktor Zielińskiej", "doktora Lewandowskiego", "doktor Mazur"]
BRINGS = [("dowód osobisty", "dowód osobisty"), ("skierowanie", "skierowanie"), ("wyniki badań krwi", "wyniki badań"), ("kartę szczepień", "kartę szczepień")]


def l_przychodnia(rng):
    gp = rng.choice("mf")
    sym, syms = rng.choice(SYMPT)
    h1, h2 = rng.choice([(8, 15), (9, 16), (10, 17), (8, 16), (11, 18)])
    m1 = rng.choice([0, 30]); m2 = rng.choice([0, 15, 30, 45])
    doc = rng.choice(DOCS)
    bring = rng.choice(BRINGS)
    day = rng.choice(["jutro", "w piątek", "w poniedziałek", "w środę"])
    P = "B" if gp == "m" else "A"
    R = "A" if gp == "m" else "B"
    lines = [(R, "Przychodnia Zdrowie, dzień dobry. W czym mogę pomóc?"),
             (P, f"Dzień dobry. Chciał{g(gp, 'bym', 'abym')} zapisać się do lekarza rodzinnego. Od wczoraj mam {sym}."),
             (R, f"Na dzisiaj nie mamy już wolnych terminów. Może być {day} o {hour_words(h1, m1)}?"),
             (P, "Rano pracuję. Czy jest coś po południu?"),
             (R, f"{day.capitalize()} o {hour_words(h2, m2)}, u {doc}."),
             (P, "Dobrze, to poproszę."),
             (R, f"Proszę podać numer PESEL i pamiętać o tym, żeby zabrać {bring[0]}.")]
    qs = [
        ch(rng, f"Co dolega {g(gp, 'pacjentowi', 'pacjentce')}?", syms, [s[1] for s in SYMPT], f"Od wczoraj mam {sym}"),
        ch(rng, "O której godzinie będzie wizyta?", hm(h2, m2), [hm(h1, m1), hm(h2 + 1, m2), hm(h2, (m2 + 30) % 60), hm(h1 + 1, 0)], f"o {hm(h2, m2)}"),
        ch(rng, f"Dlaczego {g(gp, 'pacjent', 'pacjentka')} nie chce przyjść rano?", "bo rano pracuje", ["bo rano pracuje", "bo rano śpi", "bo rano ma lekcje", "bo rano jest w szkole z dzieckiem"], "Rano pracuję"),
        ch(rng, f"Co {g(gp, 'pacjent', 'pacjentka')} musi zabrać?", bring[1], [b[1] for b in BRINGS], f"zabrać {bring[0]}"),
        ch(rng, "Kiedy jest wizyta?", day, ["jutro", "w piątek", "w poniedziałek", "w środę", "dzisiaj"], f"{day} o …"),
    ]
    return dict(title="Rozmowa w przychodni", lines=lines, qs=qs)


MEDS = [("tabletki przeciwbólowe", "tabletki przeciwbólowe"), ("syrop na kaszel", "syrop na kaszel"), ("krople do nosa", "krople do nosa"),
        ("tabletki do ssania na gardło", "tabletki na gardło"), ("maść na ból mięśni", "maść")]


def l_apteka(rng):
    gp = rng.choice("mf")
    med, meds = rng.choice(MEDS)
    times = rng.choice([2, 3, 4])
    price = rng.choice(range(12, 46))
    day = rng.choice([3, 5, 7])
    P = "B" if gp == "m" else "A"; R = "A" if gp == "m" else "B"
    tw = {2: "dwa razy", 3: "trzy razy", 4: "cztery razy"}[times]
    lines = [(R, "Dzień dobry, słucham?"),
             (P, f"Dzień dobry. Potrzebuję czegoś na {'kaszel' if 'kaszel' in med else 'ból' if 'ból' in med or 'mięśni' in med else 'gardło' if 'gardło' in med else 'katar'}. Czy mają Państwo {med}?"),
             (R, f"Tak, oczywiście. Na to nie potrzebuje {g(gp, 'Pan', 'Pani')} recepty. Proszę stosować {tw} dziennie, najlepiej po jedzeniu."),
             (P, "A jak długo?"),
             (R, f"Maksymalnie {words(day)} dni. Jeśli nie będzie lepiej, trzeba iść do lekarza."),
             (P, "Dobrze. Ile płacę?"),
             (R, f"{zl_words(price).capitalize()}. Płaci {g(gp, 'Pan', 'Pani')} kartą czy gotówką?"),
             (P, "Kartą, poproszę.")]
    qs = [
        ch(rng, "Co kupuje klient?", meds, [m[1] for m in MEDS], med),
        ch(rng, "Ile razy dziennie trzeba stosować lek?", f"{times} razy", ["1 raz", "2 razy", "3 razy", "4 razy"], f"{tw} dziennie"),
        tf("Na ten lek trzeba mieć receptę.", False, "nie potrzebuje … recepty"),
        ch(rng, "Ile kosztuje lek?", f"{price} zł", [f"{x} zł" for x in range(12, 46)], f"{price} zł"),
        ch(rng, "Jak długo maksymalnie można brać lek?", f"{day} dni", ["3 dni", "5 dni", "7 dni", "10 dni"], f"Maksymalnie {day} dni"),
        ch(rng, "Jak płaci klient?", "kartą", ["kartą", "gotówką", "BLIK-iem"], "Kartą, poproszę"),
    ]
    return dict(title="W aptece", lines=lines, qs=qs[:5])


def l_restauracja(rng):
    gp = rng.choice("mf")
    n = rng.choice([2, 3, 4, 5, 6, 8])
    di = rng.choice([4, 5, 6])
    h = rng.choice([13, 14, 17, 18, 19, 20])
    surname = rng.choice(["Kowalski", "Nowak", "Wójcik", "Kamiński", "Szymański", "Bondarenko", "Melnyk"])
    wish = rng.choice([("przy oknie", "stolik przy oknie"), ("krzesełko dla dziecka", "krzesełko dla dziecka"), ("na tarasie", "stolik na tarasie"),
                       ("w sali dla niepalących, z dala od kuchni", "stolik z dala od kuchni")])
    occ = rng.choice([("urodziny żony", "urodziny"), ("rocznica ślubu", "rocznica"), ("spotkanie z klientem", "spotkanie służbowe"), ("obiad z rodzicami", "obiad rodzinny")])
    P = "B" if gp == "m" else "A"; R = "A" if gp == "m" else "B"
    nw = {2: "dwie osoby", 3: "trzy osoby", 4: "cztery osoby", 5: "pięć osób", 6: "sześć osób", 8: "osiem osób"}[n]
    lines = [(R, "Restauracja „Pod Dębem”, dzień dobry."),
             (P, f"Dzień dobry. Chciał{g(gp, 'bym', 'abym')} zarezerwować stolik na {nw} {DAYS_ACC_PREP[di]} o {hour_words(h)}."),
             (R, f"Chwileczkę… Tak, mamy wolny stolik. Na jakie nazwisko?"),
             (P, f"{surname}{'a' if gp == 'f' and surname.endswith('ski') else ''}. I mam jeszcze prośbę: czy może być {wish[0]}?".replace("Kowalskia", "Kowalska").replace("Kamińskia", "Kamińska").replace("Szymańskia", "Szymańska")),
             (R, f"Oczywiście, zapisałam. Czy to jakaś specjalna okazja?"),
             (P, f"Tak, {occ[0]}."),
             (R, f"To zapraszamy! Proszę tylko pamiętać, że rezerwację trzymamy piętnaście minut.")]
    if R == "B":
        lines[4] = (R, "Oczywiście, zapisałem. Czy to jakaś specjalna okazja?")
    qs = [
        ch(rng, "Na ile osób jest rezerwacja?", str(n), ["2", "3", "4", "5", "6", "8"], nw),
        ch(rng, "Kiedy klient chce przyjść?", f"{DAYS_ACC_PREP[di]} o {h}:00", [f"{DAYS_ACC_PREP[x]} o {y}:00" for x in (3, 4, 5, 6) for y in (13, 17, 19, 20)], f"{DAYS_ACC_PREP[di]} o {h}:00"),
        ch(rng, "O co prosi klient?", wish[1], [w[1] for w in [("", "stolik przy oknie"), ("", "krzesełko dla dziecka"), ("", "stolik na tarasie"), ("", "stolik z dala od kuchni")]], wish[0]),
        ch(rng, "Z jakiej okazji jest kolacja?", occ[1], ["urodziny", "rocznica", "spotkanie służbowe", "obiad rodzinny", "imieniny"], occ[0]),
        ch(rng, "Jak długo restauracja czeka na gości z rezerwacją?", "15 minut", ["5 minut", "15 minut", "30 minut", "godzinę"], "rezerwację trzymamy piętnaście minut"),
    ]
    return dict(title="Rezerwacja stolika", lines=lines, qs=qs)


def l_poczta(rng):
    gs = rng.choice("mf"); sender = rng.choice(NAMES_M if gs == "m" else NAMES_F)
    rec = rng.choice(NAMES_M + NAMES_F)
    act = rng.choice([("grać w piłkę", "na boisku przy szkole", "w hali sportowej na ulicy Długiej", "buty na zmianę"),
                      ("grać w siatkówkę", "na plaży nad zalewem", "w sali gimnastycznej", "ręcznik"),
                      ("piec kiełbaski", "w parku", "u mnie w ogrodzie", "kiełbaski"),
                      ("uczyć się do egzaminu", "w bibliotece", "w kawiarni „Pod Zegarem”", "zeszyt z ćwiczeniami")])
    reason = rng.choice([("jest remont", "remont"), ("ma padać deszcz", "deszcz"), ("wszystko jest zajęte", "brak miejsc")])
    h = rng.choice([10, 11, 12, 16, 17, 18]); cost = rng.choice([0, 5, 10, 15, 20])
    voice = "B" if gs == "m" else "A"
    s = (f"Cześć {VOC[rec]}, tu {sender}. Słuchaj, w sobotę nie możemy {act[0]} {act[1]}, bo {reason[0]}. "
         f"Spotkamy się {act[2]}, o tej samej godzinie, czyli o {hour_words(h)}. Weź ze sobą {act[3]}. "
         + (f"Wejście kosztuje {zl_words(cost)}." if cost else "Wejście jest za darmo.") + " Oddzwoń, jak odsłuchasz. Na razie!")
    qs = [
        ch(rng, "Dlaczego zmienia się miejsce spotkania?", reason[1], ["remont", "deszcz", "brak miejsc", "choroba"], f"bo {reason[0]}"),
        ch(rng, "Gdzie będzie spotkanie?", act[2], [a[2] for a in [("", "", "w hali sportowej na ulicy Długiej"), ("", "", "w sali gimnastycznej"), ("", "", "u mnie w ogrodzie"), ("", "", "w kawiarni „Pod Zegarem”")]] + [act[1]], act[2]),
        ch(rng, "O której godzinie jest spotkanie?", f"{h}:00", [f"{x}:00" for x in (10, 11, 12, 16, 17, 18)], f"o {h}:00"),
        ch(rng, "Co trzeba zabrać?", act[3], ["buty na zmianę", "ręcznik", "kiełbaski", "zeszyt z ćwiczeniami", "piłkę"], f"Weź ze sobą {act[3]}"),
        ch(rng, "Ile kosztuje wejście?", f"{cost} zł" if cost else "nic", ["nic", "5 zł", "10 zł", "15 zł", "20 zł"], "Wejście …"),
    ]
    return dict(title="Wiadomość na poczcie głosowej", lines=[(voice, s)], qs=qs)


REGIONS = [("na Podlasiu i Mazowszu", "na wschodzie"), ("na Pomorzu", "na północy"), ("na Śląsku", "na południu"), ("w Wielkopolsce", "na zachodzie")]
WEATHER = [("gęste mgły", "mgły"), ("przelotny deszcz", "deszcz"), ("opady śniegu", "śnieg"), ("burze", "burze"), ("słońce", "słońce"), ("silny wiatr", "wiatr")]


def l_pogoda(rng):
    season = rng.choice(["zima", "lato", "wiosna"])
    r1, r2 = rng.sample(REGIONS, 2)
    w1, w2 = rng.sample(WEATHER if season != "lato" else [w for w in WEATHER if w[1] != "śnieg"], 2)
    if season == "zima":
        t1, t2 = rng.choice([-8, -5, -3, -2, 0]), rng.choice([1, 2, 3, 4])
    elif season == "lato":
        t1, t2 = rng.choice([14, 15, 16, 18]), rng.choice([24, 26, 28, 30, 32])
    else:
        t1, t2 = rng.choice([2, 4, 5, 6]), rng.choice([10, 12, 14, 15, 17])

    def tw(t):
        return ("minus " + words(-t) if t < 0 else words(t)) + " " + plural_form(abs(t), "stopień", "stopnie", "stopni") if t else "zero stopni"
    mount = rng.choice(["w górach przymrozek", "nad morzem silny wiatr", "w górach opady śniegu" if season != "lato" else "w górach burze"])
    cap = lambda x: x[0].upper() + x[1:]
    s = (f"A teraz prognoza pogody na jutro. {cap(r1[0])} rano {w1[0]}, a termometry pokażą {tw(t1)}. "
         f"W ciągu dnia będzie cieplej, maksymalnie {tw(t2)}. "
         f"{cap(r2[0])} przez cały dzień {w2[0]}. Dodatkowo {mount}. Kierowców prosimy o ostrożność, szczególnie rano.")
    qs = [
        ch(rng, f"Jaka będzie pogoda rano {r1[1]} kraju?", w1[1], [w[1] for w in WEATHER], f"{r1[0]} rano {w1[0]}"),
        ch(rng, f"Jaka będzie najwyższa temperatura {r1[1]}?", f"{t2}°C", [f"{x}°C" for x in {t1, t2 + 3, t2 - 2, t2 + 6, t1 + 2} - {t2}], f"maksymalnie {t2}°C"),
        ch(rng, f"Jaka pogoda będzie {r2[1]}?", w2[1], [w[1] for w in WEATHER], f"{r2[0]} … {w2[0]}"),
        tf("Prognoza mówi o pogodzie na dziś.", False, "prognoza pogody na jutro"),
    ]
    return dict(title="Prognoza pogody", lines=[("A" if rng.random() < .5 else "B", s)], qs=qs)


SHOP = [("czajnik elektryczny", "czajnik", "nie grzeje wody"), ("buty sportowe", "buty", "odkleiła się podeszwa"), ("suszarka do włosów", "suszarka", "przestała działać"),
        ("kurtka zimowa", "kurtka", "zepsuł się zamek"), ("słuchawki bezprzewodowe", "słuchawki", "jedna słuchawka nie działa"), ("blender", "blender", "bardzo głośno pracuje")]


def l_reklamacja(rng):
    gp = rng.choice("mf")
    item, short, prob = rng.choice(SHOP)
    days = rng.choice([3, 5, 7, 10, 12])
    receipt = rng.random() < 0.7
    sol = rng.choice([("wymienić produkt na nowy", "wymiana"), ("oddać pieniądze", "zwrot pieniędzy")])
    P = "B" if gp == "m" else "A"; R = "A" if gp == "m" else "B"
    lines = [(P, f"Dzień dobry. Chciał{g(gp, 'bym', 'abym')} złożyć reklamację. {words(days).capitalize()} dni temu kupił{g(gp, 'em', 'am')} tutaj {item} i {prob}."),
             (R, f"Rozumiem. Czy ma {g(gp, 'Pan', 'Pani')} paragon?"),
             (P, "Tak, proszę, tutaj jest." if receipt else "Niestety zgubił" + g(gp, "em", "am") + " paragon, ale płacił" + g(gp, "em", "am") + " kartą. Mam potwierdzenie w aplikacji banku."),
             (R, "Dobrze, to wystarczy." if not receipt else "Dziękuję."),
             (R, f"Możemy {sol[0]} od razu albo wysłać towar do serwisu. Co {g(gp, 'Pan', 'Pani')} woli?"),
             (P, f"Wolał{g(gp, 'bym', 'abym')} {sol[0].replace('wymienić produkt na nowy', 'wymianę na nowy produkt').replace('oddać pieniądze', 'zwrot pieniędzy')}, proszę."),
             (R, "W porządku. Proszę jeszcze podpisać ten formularz.")]
    qs = [
        ch(rng, "Co reklamuje klient?", short, [s[1] for s in SHOP], item),
        ch(rng, "Jaki jest problem?", prob, [s[2] for s in SHOP], prob),
        ch(rng, "Kiedy klient kupił ten produkt?", f"{days} dni temu", [f"{x} dni temu" for x in (3, 5, 7, 10, 12, 14)], f"{days} dni temu"),
        tf("Klient ma paragon.", receipt, "Tak, proszę, tutaj jest." if receipt else "zgubił paragon"),
        ch(rng, "Czego chce klient?", sol[1], ["wymiana", "zwrot pieniędzy", "naprawa w serwisie"], sol[0]),
    ]
    return dict(title="Reklamacja w sklepie", lines=lines, qs=qs)


TARGETS = [("poczty", "poczta"), ("apteki", "apteka"), ("dworca", "dworzec"), ("urzędu miasta", "urząd miasta"), ("biblioteki", "biblioteka"), ("szpitala", "szpital")]


def l_droga(rng):
    gp = rng.choice("mf")
    tg, tgs = rng.choice(TARGETS)
    turn = rng.choice(["w lewo", "w prawo"])
    land = rng.choice([("przy kościele", "kościół"), ("przy rondzie", "rondo"), ("za bankiem", "bank"), ("na światłach", "światła")])
    mins = rng.choice([3, 5, 10, 15])
    side = rng.choice(["po lewej stronie", "po prawej stronie", "naprzeciwko parku"])
    P = "B" if gp == "m" else "A"; R = "A" if gp == "m" else "B"
    lines = [(P, f"Przepraszam, jak dojść do {tg}?"),
             (R, f"Proszę iść prosto tą ulicą, a {land[0]} skręcić {turn}. Potem idzie się jeszcze {words(mins)} minut prosto i {tgs.split()[0]} będzie {side}."),
             (P, "Czy to daleko? Może lepiej pojechać autobusem?"),
             (R, "Nie, nie warto. Autobus jedzie naokoło. Pieszo będzie szybciej."),
             (P, "Dziękuję bardzo!")]
    qs = [
        ch(rng, "Dokąd chce dojść pytający?", tgs, [t[1] for t in TARGETS], f"jak dojść do {tg}"),
        ch(rng, "Gdzie trzeba skręcić?", land[1], ["kościół", "rondo", "bank", "światła"], land[0]),
        ch(rng, "W którą stronę trzeba skręcić?", turn, ["w lewo", "w prawo", "nigdzie, cały czas prosto"], f"skręcić {turn}"),
        tf("Autobusem będzie szybciej niż pieszo.", False, "Pieszo będzie szybciej"),
        ch(rng, "Ile minut trzeba jeszcze iść po skręcie?", f"ok. {mins} minut", [f"ok. {x} minut" for x in (3, 5, 10, 15, 20)], f"jeszcze {mins} minut"),
    ]
    return dict(title="Pytanie o drogę", lines=lines, qs=qs)


def l_praca(rng):
    gp = rng.choice("mf")
    job = rng.choice([("magazynie", "magazyn"), ("sklepie", "sklep"), ("restauracji", "restauracja"), ("hotelu", "hotel"), ("piekarni", "piekarnia")])
    exp = rng.choice([1, 2, 3, 5])
    start = rng.choice([("od poniedziałku", "w poniedziałek"), ("od pierwszego", "pierwszego dnia miesiąca"), ("od jutra", "jutro")])
    rate = rng.choice([31, 32, 34, 35, 36, 38, 40])
    shift = rng.choice([("rano, od szóstej do czternastej", "rano"), ("po południu, od czternastej do dwudziestej drugiej", "po południu"),
                        ("w weekendy", "w weekendy")])
    P = "B" if gp == "m" else "A"; R = "A" if gp == "m" else "B"
    lines = [(R, f"Dzień dobry, proszę usiąść. Czy pracował{g(gp, '', 'a')} {g(gp, 'Pan', 'Pani')} już w {job[0]}?"),
             (P, f"Tak, przez {words(exp) if exp > 1 else 'jeden'} {plural_form(exp, 'rok', 'lata', 'lat')}, jeszcze na Ukrainie."),
             (R, f"Bardzo dobrze. U nas praca jest {shift[0]}. Czy to {g(gp, 'Panu', 'Pani')} odpowiada?"),
             (P, "Tak, bez problemu. A ile wynosi stawka?"),
             (R, f"{words(rate).capitalize()} złote brutto za godzinę na początek, po trzech miesiącach więcej."
              .replace("złote", plural_form(rate, "złoty", "złote", "złotych"))),
             (P, "Rozumiem. Kiedy mógł" + g(gp, "bym", "abym") + " zacząć?"),
             (R, f"Najlepiej {start[0]}. Proszę jutro przynieść dokumenty i zrobić badania lekarskie.")]
    qs = [
        ch(rng, "Ile lat doświadczenia ma kandydat?", f"{exp} {plural_form(exp, 'rok', 'lata', 'lat')}", [f"{x} {plural_form(x, 'rok', 'lata', 'lat')}" for x in (1, 2, 3, 4, 5)], f"przez {exp} …"),
        ch(rng, "Kiedy jest praca?", shift[1], ["rano", "po południu", "w weekendy", "w nocy"], shift[0]),
        ch(rng, "Ile wynosi stawka na początek?", f"{rate} zł/h", [f"{x} zł/h" for x in (31, 32, 34, 35, 36, 38, 40, 45)], f"{rate} zł brutto"),
        ch(rng, "Kiedy kandydat może zacząć pracę?", start[1], ["w poniedziałek", "pierwszego dnia miesiąca", "jutro", "za miesiąc"], start[0]),
        ch(rng, "Co kandydat musi zrobić jutro?", "przynieść dokumenty i zrobić badania", ["przynieść dokumenty i zrobić badania", "podpisać umowę", "przyjść na pierwszy dzień pracy", "wysłać CV"], "Proszę jutro przynieść dokumenty"),
    ]
    return dict(title="Rozmowa o pracę", lines=lines, qs=qs)


def l_sklep_komunikat(rng):
    prod = rng.choice([("kawa mielona", "kawę"), ("owoce i warzywa", "owoce i warzywa"), ("pieczywo", "pieczywo"), ("chemia gospodarcza", "chemię"), ("zabawki", "zabawki")])
    pct = rng.choice([10, 15, 20, 25, 30, 40, 50])
    until = rng.choice([12, 14, 16, 18, 20])
    close = rng.choice([20, 21, 22])
    floor = rng.choice([("na parterze", "parter"), ("na pierwszym piętrze", "1. piętro"), ("przy kasach", "przy kasach")])
    s = (f"Szanowni klienci! Tylko dzisiaj do godziny {hour_words(until, 0, 'gen')} {prod[1]} kupicie {words(pct)} procent taniej. "
         f"Promocyjne produkty znajdziecie {floor[0]}. Przypominamy, że nasz sklep jest dziś otwarty do godziny {hour_words(close, 0, 'gen')}. "
         f"Zapraszamy też do naszej piekarni, gdzie co godzinę wypiekamy świeży chleb. Dziękujemy za zakupy!")
    qs = [
        ch(rng, "Co jest w promocji?", prod[0], ["kawa mielona", "owoce i warzywa", "pieczywo", "chemia gospodarcza", "zabawki"], prod[1]),
        ch(rng, "Ile wynosi rabat?", f"{pct}%", [f"{x}%" for x in (10, 15, 20, 25, 30, 40, 50)], f"{pct} procent taniej"),
        ch(rng, "Do której godziny trwa promocja?", f"do {until}:00", [f"do {x}:00" for x in (12, 14, 16, 18, 20, 22)], f"do godziny {until}:00"),
        ch(rng, "Do której jest otwarty sklep?", f"do {close}:00", [f"do {x}:00" for x in (18, 20, 21, 22, 23)], f"otwarty do godziny {close}:00"),
        ch(rng, "Gdzie są produkty w promocji?", floor[1], ["parter", "1. piętro", "przy kasach", "przy wejściu"], floor[0]),
    ]
    return dict(title="Komunikat w sklepie", lines=[("A" if rng.random() < .5 else "B", s)], qs=qs)


SERV = [("strzyżenie", "strzyżenie", 60, 45), ("farbowanie włosów", "farbowanie", 180, 120), ("wymianę oleju", "wymiana oleju", 150, 60),
        ("wymianę opon", "wymiana opon", 100, 40), ("przegląd klimatyzacji", "klimatyzacja", 200, 60)]


def l_umowienie(rng):
    gp = rng.choice("mf")
    sv = rng.choice(SERV)
    place = "salon" if sv[1] in ("strzyżenie", "farbowanie") else "warsztat"
    price = sv[2] + rng.choice([-20, -10, 0, 10, 20])
    di = rng.choice([0, 1, 2, 3, 4, 5]); h = rng.choice([9, 10, 11, 12, 14, 15, 16])
    P = "B" if gp == "m" else "A"; R = "A" if gp == "m" else "B"
    lines = [(R, ("Salon fryzjerski „Lustro”" if place == "salon" else "Warsztat samochodowy „Tłok”") + ", słucham."),
             (P, f"Dzień dobry, chciał{g(gp, 'bym', 'abym')} umówić się na {sv[0]}. Czy jest wolny termin w tym tygodniu?"),
             (R, f"Najbliższy wolny termin to {DAYS_NOM[di]}, godzina {hour_words(h, 0, 'nom')}."),
             (P, "Dobrze, pasuje mi. Ile to będzie kosztować i ile potrwa?"),
             (R, f"Około {zl_words(price)}, a potrwa mniej więcej {words(sv[3])} minut." if sv[3] < 100 else f"Około {zl_words(price)}, a potrwa około dwóch godzin."),
             (P, "Świetnie. Czy mogę zapłacić kartą?"),
             (R, "Tak, oczywiście. To zapisuję. Do zobaczenia!")]
    dur = f"{sv[3]} minut" if sv[3] < 100 else "2 godziny"
    qs = [
        ch(rng, "Na jaką usługę umawia się klient?", sv[1], [s[1] for s in SERV], sv[0]),
        ch(rng, "Kiedy jest wizyta?", f"{DAYS_NOM[di]} {h}:00", [f"{DAYS_NOM[x]} {y}:00" for x in range(6) for y in (9, 11, 14, 16)], f"{DAYS_NOM[di]} o {h}:00"),
        ch(rng, "Ile mniej więcej będzie kosztować usługa?", f"{price} zł", [f"{x} zł" for x in {price + 30, price - 25, price + 60, price + 15}], f"Około {price} zł"),
        ch(rng, "Ile potrwa usługa?", dur, ["40 minut", "45 minut", "60 minut", "2 godziny", "3 godziny"], dur),
        tf("Klient może zapłacić kartą.", True, "Tak, oczywiście"),
    ]
    return dict(title="Umawianie wizyty", lines=lines, qs=qs)


TRIPS = [("nad morze, do Gdańska", "nad morzem"), ("w góry, do Zakopanego", "w górach"), ("na Mazury", "na Mazurach"), ("do Krakowa", "w Krakowie"), ("do Torunia", "w Toruniu")]


def l_weekend(rng):
    ga = rng.choice("mf")
    trip, where = rng.choice(TRIPS)
    with_ = rng.choice([("z rodziną", "z rodziną"), ("z kolegami z pracy", "z kolegami"), ("z żoną" if ga == "m" else "z mężem", "z partnerem"), ("sam" if ga == "m" else "sama", "sam / sama")])
    weather = rng.choice([("cały czas padało", "deszczowa"), ("było pięknie, słonecznie", "słoneczna"), ("było bardzo zimno", "zimna")])
    best = rng.choice([("rejs statkiem", "rejs statkiem"), ("kolacja w restauracji z rybami", "kolacja"), ("spacer po starym mieście", "spacer"), ("wycieczka rowerowa", "rower")])
    nxt = rng.choice([("do Wrocławia", "do Wrocławia"), ("do Lublina", "do Lublina"), ("w Bieszczady", "w Bieszczady")])
    A = "A" if ga == "f" else "B"; B = "B" if ga == "f" else "A"
    lines = [(B, "Cześć! Jak minął weekend? Gdzie byłaś?" if ga == "f" else "Cześć! Jak minął weekend? Gdzie byłeś?"),
             (A, f"Pojechał{g(ga, 'em', 'am')} {trip} {with_[0]}."),
             (B, "Super! A jak pogoda?"),
             (A, f"Niestety {weather[0]}. Ale i tak było fajnie." if weather[1] != "słoneczna" else f"{weather[0].capitalize()}! Mieliśmy dużo szczęścia." if with_[1] != "sam / sama" else f"{weather[0].capitalize()}! Miał{g(ga, 'em', 'am')} dużo szczęścia."),
             (B, "A co ci się najbardziej podobało?"),
             (A, f"Chyba {best[0]}. Za miesiąc chcę pojechać {nxt[0]}. Może pojedziesz ze mną?"),
             (B, "Czemu nie! Pogadamy w tygodniu.")]
    qs = [
        ch(rng, f"Gdzie {g(ga, 'był', 'była')} w weekend?", where, [t[1] for t in TRIPS], trip),
        ch(rng, f"Z kim {g(ga, 'pojechał', 'pojechała')}?", with_[1], ["z rodziną", "z kolegami", "z partnerem", "sam / sama"], with_[0]),
        ch(rng, "Jaka była pogoda?", weather[1], ["deszczowa", "słoneczna", "zimna"], weather[0]),
        ch(rng, "Co podobało się najbardziej?", best[1], ["rejs statkiem", "kolacja", "spacer", "rower"], best[0]),
        ch(rng, "Dokąd chce pojechać za miesiąc?", nxt[1], ["do Wrocławia", "do Lublina", "w Bieszczady", "do Gdańska"], nxt[0]),
    ]
    return dict(title="Rozmowa o weekendzie", lines=lines, qs=qs)


LISTEN_T = [l_dworzec, l_przychodnia, l_apteka, l_restauracja, l_poczta, l_pogoda, l_reklamacja, l_droga, l_praca, l_sklep_komunikat, l_umowienie, l_weekend]


def build(templates, n_target_q, seed, prefix):
    rng = make_rng(seed)
    out, seen, total, i = [], set(), 0, 0
    while total < n_target_q:
        t = templates[i % len(templates)]
        i += 1
        try:
            x = t(rng)
        except ValueError:
            continue
        key = x.get("text") or json.dumps(x["lines"], ensure_ascii=False)
        if key in seen:
            continue
        seen.add(key)
        for q in x["qs"]:
            if "o" in q:
                assert len(set(q["o"])) == len(q["o"]) >= 3, (t.__name__, q)
        x["id"] = f"{prefix}{len(out) + 1:03d}"
        out.append(x)
        total += len(x["qs"])
    return out, total


if __name__ == "__main__":
    reading, nr = build(READING_T, 1000, 11, "r")
    listening, nl = build(LISTEN_T, 1000, 22, "l")
    json.dump(dict(items=reading), open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    json.dump(dict(items=listening), open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("czytanie:", len(reading), "tekstów,", nr, "pytań | słuchanie:", len(listening), "nagrań,", nl, "pytań")
