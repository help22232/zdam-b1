"""Słownik Zdam B1: rzeczowniki (pełna odmiana l.poj. + wybrane formy l.mn.), przymiotniki, czasowniki.
Formy wpisane ręcznie i sprawdzone; generator używa tylko tych form (nic nie jest "zgadywane")."""

# Rzeczownik: (mianownik, dopełniacz, celownik, biernik, narzędnik, miejscownik, M l.mn., D l.mn., rodzaj, tagi)
# rodzaj: m (męskoosobowy / męski żywotny), mi (męski nieżywotny), f, n
N = {}


def noun(nom, gen, dat, acc, ins, loc, pl_nom=None, pl_gen=None, g="mi", tags=(), ua=None, ru=None):
    N[nom] = dict(nom=nom, gen=gen, dat=dat, acc=acc, ins=ins, loc=loc, pl_nom=pl_nom, pl_gen=pl_gen,
                  g=g, tags=set(tags))


# --- osoby (mężczyźni)
noun("brat", "brata", "bratu", "brata", "bratem", "bracie", "bracia", "braci", "m", ["person", "family"])
noun("ojciec", "ojca", "ojcu", "ojca", "ojcem", "ojcu", "ojcowie", "ojców", "m", ["person", "family"])
noun("syn", "syna", "synowi", "syna", "synem", "synu", "synowie", "synów", "m", ["person", "family"])
noun("kolega", "kolegi", "koledze", "kolegę", "kolegą", "koledze", "koledzy", "kolegów", "m", ["person"])
noun("sąsiad", "sąsiada", "sąsiadowi", "sąsiada", "sąsiadem", "sąsiedzie", "sąsiedzi", "sąsiadów", "m", ["person"])
noun("lekarz", "lekarza", "lekarzowi", "lekarza", "lekarzem", "lekarzu", "lekarze", "lekarzy", "m", ["person", "prof"])
noun("szef", "szefa", "szefowi", "szefa", "szefem", "szefie", "szefowie", "szefów", "m", ["person"])
noun("nauczyciel", "nauczyciela", "nauczycielowi", "nauczyciela", "nauczycielem", "nauczycielu", "nauczyciele", "nauczycieli", "m", ["person", "prof"])
noun("mąż", "męża", "mężowi", "męża", "mężem", "mężu", "mężowie", "mężów", "m", ["person", "family"])
noun("dziadek", "dziadka", "dziadkowi", "dziadka", "dziadkiem", "dziadku", "dziadkowie", "dziadków", "m", ["person", "family"])
noun("Tomek", "Tomka", "Tomkowi", "Tomka", "Tomkiem", "Tomku", g="m", tags=["person", "name"])
noun("Marek", "Marka", "Markowi", "Marka", "Markiem", "Marku", g="m", tags=["person", "name"])
noun("Piotr", "Piotra", "Piotrowi", "Piotra", "Piotrem", "Piotrze", g="m", tags=["person", "name"])
noun("Paweł", "Pawła", "Pawłowi", "Pawła", "Pawłem", "Pawle", g="m", tags=["person", "name"])
noun("Adam", "Adama", "Adamowi", "Adama", "Adamem", "Adamie", g="m", tags=["person", "name"])
# --- osoby (kobiety)
noun("siostra", "siostry", "siostrze", "siostrę", "siostrą", "siostrze", "siostry", "sióstr", "f", ["person", "family", "count"])
noun("matka", "matki", "matce", "matkę", "matką", "matce", "matki", "matek", "f", ["person", "family"])
noun("mama", "mamy", "mamie", "mamę", "mamą", "mamie", g="f", tags=["person", "family"])
noun("córka", "córki", "córce", "córkę", "córką", "córce", "córki", "córek", "f", ["person", "family", "count"])
noun("koleżanka", "koleżanki", "koleżance", "koleżankę", "koleżanką", "koleżance", "koleżanki", "koleżanek", "f", ["person"])
noun("sąsiadka", "sąsiadki", "sąsiadce", "sąsiadkę", "sąsiadką", "sąsiadce", "sąsiadki", "sąsiadek", "f", ["person"])
noun("żona", "żony", "żonie", "żonę", "żoną", "żonie", "żony", "żon", "f", ["person", "family"])
noun("babcia", "babci", "babci", "babcię", "babcią", "babci", "babcie", "babć", "f", ["person", "family"])
noun("Anna", "Anny", "Annie", "Annę", "Anną", "Annie", g="f", tags=["person", "name"])
noun("Kasia", "Kasi", "Kasi", "Kasię", "Kasią", "Kasi", g="f", tags=["person", "name"])
noun("Ola", "Oli", "Oli", "Olę", "Olą", "Oli", g="f", tags=["person", "name"])
noun("Ewa", "Ewy", "Ewie", "Ewę", "Ewą", "Ewie", g="f", tags=["person", "name"])
# --- zwierzęta (męskie żywotne: biernik = dopełniacz)
noun("pies", "psa", "psu", "psa", "psem", "psie", "psy", "psów", "m", ["animal", "count"])
noun("kot", "kota", "kotu", "kota", "kotem", "kocie", "koty", "kotów", "m", ["animal", "count"])
# --- rzeczy (męskie nieżywotne)
noun("samochód", "samochodu", "samochodowi", "samochód", "samochodem", "samochodzie", "samochody", "samochodów", "mi", ["thing", "count", "vehicle_obj"])
noun("telefon", "telefonu", "telefonowi", "telefon", "telefonem", "telefonie", "telefony", "telefonów", "mi", ["thing", "count"])
noun("komputer", "komputera", "komputerowi", "komputer", "komputerem", "komputerze", "komputery", "komputerów", "mi", ["thing", "count"])
noun("rower", "roweru", "rowerowi", "rower", "rowerem", "rowerze", "rowery", "rowerów", "mi", ["thing", "count"])
noun("bilet", "biletu", "biletowi", "bilet", "biletem", "bilecie", "bilety", "biletów", "mi", ["thing", "count"])
noun("klucz", "klucza", "kluczowi", "klucz", "kluczem", "kluczu", "klucze", "kluczy", "mi", ["thing", "count"])
noun("paszport", "paszportu", "paszportowi", "paszport", "paszportem", "paszporcie", "paszporty", "paszportów", "mi", ["thing", "count"])
noun("parasol", "parasola", "parasolowi", "parasol", "parasolem", "parasolu", "parasole", "parasoli", "mi", ["thing", "count"])
noun("portfel", "portfela", "portfelowi", "portfel", "portfelem", "portfelu", "portfele", "portfeli", "mi", ["thing", "count"])
noun("prezent", "prezentu", "prezentowi", "prezent", "prezentem", "prezencie", "prezenty", "prezentów", "mi", ["thing", "count"])
noun("chleb", "chleba", "chlebowi", "chleb", "chlebem", "chlebie", g="mi", tags=["food"])
noun("ser", "sera", "serowi", "ser", "serem", "serze", g="mi", tags=["food"])
noun("cukier", "cukru", "cukrowi", "cukier", "cukrem", "cukrze", g="mi", tags=["food", "addon"])
noun("sok", "soku", "sokowi", "sok", "sokiem", "soku", g="mi", tags=["food", "drink"])
noun("czas", "czasu", "czasowi", "czas", "czasem", "czasie", g="mi", tags=["abstract"])
noun("problem", "problemu", "problemowi", "problem", "problemem", "problemie", "problemy", "problemów", "mi", ["abstract", "count"])
noun("film", "filmu", "filmowi", "film", "filmem", "filmie", "filmy", "filmów", "mi", ["thing", "count", "topic"])
# --- rzeczy (żeńskie)
noun("książka", "książki", "książce", "książkę", "książką", "książce", "książki", "książek", "f", ["thing", "count", "topic"])
noun("kawa", "kawy", "kawie", "kawę", "kawą", "kawie", g="f", tags=["food", "drink"])
noun("herbata", "herbaty", "herbacie", "herbatę", "herbatą", "herbacie", g="f", tags=["food", "drink"])
noun("woda", "wody", "wodzie", "wodę", "wodą", "wodzie", g="f", tags=["food", "drink"])
noun("zupa", "zupy", "zupie", "zupę", "zupą", "zupie", g="f", tags=["food"])
noun("praca", "pracy", "pracy", "pracę", "pracą", "pracy", g="f", tags=["abstract", "topic"])
noun("torba", "torby", "torbie", "torbę", "torbą", "torbie", "torby", "toreb", "f", ["thing", "count", "container"])
noun("gazeta", "gazety", "gazecie", "gazetę", "gazetą", "gazecie", "gazety", "gazet", "f", ["thing", "count"])
noun("kurtka", "kurtki", "kurtce", "kurtkę", "kurtką", "kurtce", "kurtki", "kurtek", "f", ["thing", "count", "container"])
noun("lekcja", "lekcji", "lekcji", "lekcję", "lekcją", "lekcji", "lekcje", "lekcji", "f", ["abstract", "count"])
noun("wizyta", "wizyty", "wizycie", "wizytę", "wizytą", "wizycie", "wizyty", "wizyt", "f", ["abstract", "count"])
noun("szafa", "szafy", "szafie", "szafę", "szafą", "szafie", "szafy", "szaf", "f", ["thing", "count", "container"])
# --- rzeczy (nijakie)
noun("mieszkanie", "mieszkania", "mieszkaniu", "mieszkanie", "mieszkaniem", "mieszkaniu", "mieszkania", "mieszkań", "n", ["thing", "count", "container"])
noun("mleko", "mleka", "mleku", "mleko", "mlekiem", "mleku", g="n", tags=["food", "drink", "addon"])
noun("auto", "auta", "autu", "auto", "autem", "aucie", "auta", "aut", "n", ["thing", "count", "container"])
noun("okno", "okna", "oknu", "okno", "oknem", "oknie", "okna", "okien", "n", ["thing", "count"])
noun("jabłko", "jabłka", "jabłku", "jabłko", "jabłkiem", "jabłku", "jabłka", "jabłek", "n", ["food", "count"])
noun("krzesło", "krzesła", "krzesłu", "krzesło", "krzesłem", "krześle", "krzesła", "krzeseł", "n", ["thing", "count"])
noun("dziecko", "dziecka", "dziecku", "dziecko", "dzieckiem", "dziecku", "dzieci", "dzieci", "n", ["person", "family"])
noun("zdjęcie", "zdjęcia", "zdjęciu", "zdjęcie", "zdjęciem", "zdjęciu", "zdjęcia", "zdjęć", "n", ["thing", "count"])
noun("biurko", "biurka", "biurku", "biurko", "biurkiem", "biurku", "biurka", "biurek", "n", ["thing", "count", "container"])

# --- miejsca: (forma, przyimek "gdzie?" + miejscownik, przyimek "dokąd?" + przypadek, przyimek "skąd?")
PLACES = {}


def place(nom, gen, acc, ins, loc, where, whither, whence, kind="place"):
    """where: 'w'/'we'/'na'; whither: ('do', gen) albo ('na', acc); whence: 'z'/'ze'."""
    PLACES[nom] = dict(nom=nom, gen=gen, acc=acc, ins=ins, loc=loc, where=where, whither=whither,
                       whence=whence, kind=kind)


place("Warszawa", "Warszawy", "Warszawę", "Warszawą", "Warszawie", "w", "do", "z", "city")
place("Kraków", "Krakowa", "Kraków", "Krakowem", "Krakowie", "w", "do", "z", "city")
place("Lublin", "Lublina", "Lublin", "Lublinem", "Lublinie", "w", "do", "z", "city")
place("Gdańsk", "Gdańska", "Gdańsk", "Gdańskiem", "Gdańsku", "w", "do", "z", "city")
place("Poznań", "Poznania", "Poznań", "Poznaniem", "Poznaniu", "w", "do", "z", "city")
place("Wrocław", "Wrocławia", "Wrocław", "Wrocławiem", "Wrocławiu", "we", "do", "z", "city")
place("Sokołów", "Sokołowa", "Sokołów", "Sokołowem", "Sokołowie", "w", "do", "z", "city")
place("Łódź", "Łodzi", "Łódź", "Łodzią", "Łodzi", "w", "do", "z", "city")
place("Siedlce", "Siedlec", "Siedlce", "Siedlcami", "Siedlcach", "w", "do", "z", "city")
place("sklep", "sklepu", "sklep", "sklepem", "sklepie", "w", "do", "ze")
place("szkoła", "szkoły", "szkołę", "szkołą", "szkole", "w", "do", "ze")
place("biblioteka", "biblioteki", "bibliotekę", "biblioteką", "bibliotece", "w", "do", "z")
place("apteka", "apteki", "aptekę", "apteką", "aptece", "w", "do", "z")
place("kino", "kina", "kino", "kinem", "kinie", "w", "do", "z")
place("park", "parku", "park", "parkiem", "parku", "w", "do", "z")
place("urząd", "urzędu", "urząd", "urzędem", "urzędzie", "w", "do", "z")
place("restauracja", "restauracji", "restaurację", "restauracją", "restauracji", "w", "do", "z")
place("bank", "banku", "bank", "bankiem", "banku", "w", "do", "z")
place("szpital", "szpitala", "szpital", "szpitalem", "szpitalu", "w", "do", "ze")
place("biuro", "biura", "biuro", "biurem", "biurze", "w", "do", "z")
place("poczta", "poczty", "pocztę", "pocztą", "poczcie", "na", "na", "z")
place("dworzec", "dworca", "dworzec", "dworcem", "dworcu", "na", "na", "z")
place("basen", "basenu", "basen", "basenem", "basenie", "na", "na", "z")
place("uniwersytet", "uniwersytetu", "uniwersytet", "uniwersytetem", "uniwersytecie", "na", "na", "z")
place("rynek", "rynku", "rynek", "rynkiem", "rynku", "na", "na", "z")
place("lotnisko", "lotniska", "lotnisko", "lotniskiem", "lotnisku", "na", "na", "z")
place("siłownia", "siłowni", "siłownię", "siłownią", "siłowni", "na", "na", "z")
place("stadion", "stadionu", "stadion", "stadionem", "stadionie", "na", "na", "ze")
place("przystanek", "przystanku", "przystanek", "przystankiem", "przystanku", "na", "na", "z")

# --- środki transportu (narzędnik bez przyimka)
VEHICLES = {  # nom: (gen, acc, ins, loc)
    "autobus": ("autobusu", "autobus", "autobusem", "autobusie"),
    "tramwaj": ("tramwaju", "tramwaj", "tramwajem", "tramwaju"),
    "pociąg": ("pociągu", "pociąg", "pociągiem", "pociągu"),
    "samochód": ("samochodu", "samochód", "samochodem", "samochodzie"),
    "taksówka": ("taksówki", "taksówkę", "taksówką", "taksówce"),
    "metro": ("metra", "metro", "metrem", "metrze"),
}

# --- zainteresowania (interesować się + narzędnik)
HOBBIES = {  # nom: (gen, acc, ins, loc)
    "historia": ("historii", "historię", "historią", "historii"),
    "sport": ("sportu", "sport", "sportem", "sporcie"),
    "muzyka": ("muzyki", "muzykę", "muzyką", "muzyce"),
    "polityka": ("polityki", "politykę", "polityką", "polityce"),
    "sztuka": ("sztuki", "sztukę", "sztuką", "sztuce"),
    "fotografia": ("fotografii", "fotografię", "fotografią", "fotografii"),
    "kuchnia włoska": ("kuchni włoskiej", "kuchnię włoską", "kuchnią włoską", "kuchni włoskiej"),
    "piłka nożna": ("piłki nożnej", "piłkę nożną", "piłką nożną", "piłce nożnej"),
    "literatura": ("literatury", "literaturę", "literaturą", "literaturze"),
    "motoryzacja": ("motoryzacji", "motoryzację", "motoryzacją", "motoryzacji"),
    "informatyka": ("informatyki", "informatykę", "informatyką", "informatyce"),
    "przyroda": ("przyrody", "przyrodę", "przyrodą", "przyrodzie"),
}

# --- zawody (być + narzędnik, pracować jako + mianownik)
PROFESSIONS = {  # nom: (gen, acc, ins, dat), rodzaj
    "kierowca": (("kierowcy", "kierowcę", "kierowcą", "kierowcy"), "m"),
    "lekarz": (("lekarza", "lekarza", "lekarzem", "lekarzowi"), "m"),
    "nauczyciel": (("nauczyciela", "nauczyciela", "nauczycielem", "nauczycielowi"), "m"),
    "kelner": (("kelnera", "kelnera", "kelnerem", "kelnerowi"), "m"),
    "mechanik": (("mechanika", "mechanika", "mechanikiem", "mechanikowi"), "m"),
    "kucharz": (("kucharza", "kucharza", "kucharzem", "kucharzowi"), "m"),
    "elektryk": (("elektryka", "elektryka", "elektrykiem", "elektrykowi"), "m"),
    "programista": (("programisty", "programistę", "programistą", "programiście"), "m"),
    "sprzedawca": (("sprzedawcy", "sprzedawcę", "sprzedawcą", "sprzedawcy"), "m"),
    "fryzjerka": (("fryzjerki", "fryzjerkę", "fryzjerką", "fryzjerce"), "f"),
    "pielęgniarka": (("pielęgniarki", "pielęgniarkę", "pielęgniarką", "pielęgniarce"), "f"),
    "nauczycielka": (("nauczycielki", "nauczycielkę", "nauczycielką", "nauczycielce"), "f"),
    "kelnerka": (("kelnerki", "kelnerkę", "kelnerką", "kelnerce"), "f"),
    "sprzątaczka": (("sprzątaczki", "sprzątaczkę", "sprzątaczką", "sprzątaczce"), "f"),
    "księgowa": (("księgowej", "księgową", "księgową", "księgowej"), "f"),
}

# --- przymiotniki: (m nom, f nom, n nom); formy zależne liczone regułą w adj_forms()
ADJ = [("nowy", "nowa", "nowe"), ("stary", "stara", "stare"), ("duży", "duża", "duże"), ("mały", "mała", "małe"),
       ("tani", "tania", "tanie"), ("drogi", "droga", "drogie"), ("ładny", "ładna", "ładne"),
       ("wygodny", "wygodna", "wygodne"), ("czerwony", "czerwona", "czerwone"), ("czarny", "czarna", "czarne"),
       ("polski", "polska", "polskie"), ("dobry", "dobra", "dobre"), ("ciepły", "ciepła", "ciepłe"),
       ("ciekawy", "ciekawa", "ciekawe"), ("zimny", "zimna", "zimne"), ("młodszy", "młodsza", "młodsze"), ("starszy", "starsza", "starsze"), ("miły", "miła", "miłe")]


def adj_forms(m, f, n):
    obl = m[:-1] if m.endswith("y") else m          # nowy -> now, drogi -> drogi, tani -> tani
    ym = "m" if obl.endswith("i") else "ym"         # drogim / nowym
    fst = f[:-1]                                     # nowa -> now, droga -> drog, tania -> tani
    return {
        ("m", "nom"): m, ("m", "gen"): obl + "ego", ("m", "dat"): obl + "emu", ("m", "acc_anim"): obl + "ego",
        ("m", "acc"): m, ("m", "ins"): obl + ym, ("m", "loc"): obl + ym,
        ("f", "nom"): f, ("f", "gen"): obl + "ej", ("f", "dat"): obl + "ej", ("f", "acc"): fst + "ą",
        ("f", "ins"): fst + "ą", ("f", "loc"): obl + "ej",
        ("n", "nom"): n, ("n", "gen"): obl + "ego", ("n", "dat"): obl + "emu", ("n", "acc"): n,
        ("n", "ins"): obl + ym, ("n", "loc"): obl + ym,
    }


# --- czasowniki
# pres: ja, ty, on/ona, my, wy, oni ; past: (on, ona) ; past1: (ja-m, ja-f) gdy nieregularne
V = []


def verb(inf, pres, past_m, past_f, obj, perf=None, pfut=None, ppast=None, past1=None, ppast1=None,
         refl=False, ua="", ru=""):
    d = dict(inf=inf, pres=pres.split(), past_m=past_m, past_f=past_f, obj=obj, perf=perf,
             pfut=pfut.split() if pfut else None, ppast=ppast, refl=refl)
    d["past1m"], d["past1f"] = past1 if past1 else (past_m + "em", past_f + "m")
    if ppast:
        d["ppast_m"], d["ppast_f"] = ppast
        d["ppast1m"], d["ppast1f"] = ppast1 if ppast1 else (ppast[0] + "em", ppast[1] + "m")
    V.append(d)


verb("pracować", "pracuję pracujesz pracuje pracujemy pracujecie pracują", "pracował", "pracowała", "w biurze")
verb("czytać", "czytam czytasz czyta czytamy czytacie czytają", "czytał", "czytała", "gazetę",
     "przeczytać", "przeczytam przeczytasz przeczyta przeczytamy przeczytacie przeczytają", ("przeczytał", "przeczytała"))
verb("pisać", "piszę piszesz pisze piszemy piszecie piszą", "pisał", "pisała", "list do babci",
     "napisać", "napiszę napiszesz napisze napiszemy napiszecie napiszą", ("napisał", "napisała"))
verb("robić", "robię robisz robi robimy robicie robią", "robił", "robiła", "zakupy",
     "zrobić", "zrobię zrobisz zrobi zrobimy zrobicie zrobią", ("zrobił", "zrobiła"))
verb("kupować", "kupuję kupujesz kupuje kupujemy kupujecie kupują", "kupował", "kupowała", "chleb",
     "kupić", "kupię kupisz kupi kupimy kupicie kupią", ("kupił", "kupiła"))
verb("gotować", "gotuję gotujesz gotuje gotujemy gotujecie gotują", "gotował", "gotowała", "obiad",
     "ugotować", "ugotuję ugotujesz ugotuje ugotujemy ugotujecie ugotują", ("ugotował", "ugotowała"))
verb("oglądać", "oglądam oglądasz ogląda oglądamy oglądacie oglądają", "oglądał", "oglądała", "film",
     "obejrzeć", "obejrzę obejrzysz obejrzy obejrzymy obejrzycie obejrzą", ("obejrzał", "obejrzała"))
verb("pić", "piję pijesz pije pijemy pijecie piją", "pił", "piła", "kawę",
     "wypić", "wypiję wypijesz wypije wypijemy wypijecie wypiją", ("wypił", "wypiła"))
verb("jeść", "jem jesz je jemy jecie jedzą", "jadł", "jadła", "śniadanie",
     "zjeść", "zjem zjesz zje zjemy zjecie zjedzą", ("zjadł", "zjadła"))
verb("uczyć się", "uczę uczysz uczy uczymy uczycie uczą", "uczył", "uczyła", "polskiego",
     "nauczyć się", "nauczę nauczysz nauczy nauczymy nauczycie nauczą", ("nauczył", "nauczyła"), refl=True)
verb("sprzątać", "sprzątam sprzątasz sprząta sprzątamy sprzątacie sprzątają", "sprzątał", "sprzątała", "mieszkanie",
     "posprzątać", "posprzątam posprzątasz posprząta posprzątamy posprzątacie posprzątają", ("posprzątał", "posprzątała"))
verb("myć", "myję myjesz myje myjemy myjecie myją", "mył", "myła", "naczynia",
     "umyć", "umyję umyjesz umyje umyjemy umyjecie umyją", ("umył", "umyła"))
verb("płacić", "płacę płacisz płaci płacimy płacicie płacą", "płacił", "płaciła", "rachunki",
     "zapłacić", "zapłacę zapłacisz zapłaci zapłacimy zapłacicie zapłacą", ("zapłacił", "zapłaciła"))
verb("dzwonić", "dzwonię dzwonisz dzwoni dzwonimy dzwonicie dzwonią", "dzwonił", "dzwoniła", "do mamy",
     "zadzwonić", "zadzwonię zadzwonisz zadzwoni zadzwonimy zadzwonicie zadzwonią", ("zadzwonił", "zadzwoniła"))
verb("wracać", "wracam wracasz wraca wracamy wracacie wracają", "wracał", "wracała", "do domu",
     "wrócić", "wrócę wrócisz wróci wrócimy wrócicie wrócą", ("wrócił", "wróciła"))
verb("otwierać", "otwieram otwierasz otwiera otwieramy otwieracie otwierają", "otwierał", "otwierała", "okno",
     "otworzyć", "otworzę otworzysz otworzy otworzymy otworzycie otworzą", ("otworzył", "otworzyła"))
verb("mówić", "mówię mówisz mówi mówimy mówicie mówią", "mówił", "mówiła", "prawdę",
     "powiedzieć", "powiem powiesz powie powiemy powiecie powiedzą", ("powiedział", "powiedziała"))
verb("brać", "biorę bierzesz bierze bierzemy bierzecie biorą", "brał", "brała", "parasol",
     "wziąć", "wezmę weźmiesz weźmie weźmiemy weźmiecie wezmą", ("wziął", "wzięła"))
verb("wysyłać", "wysyłam wysyłasz wysyła wysyłamy wysyłacie wysyłają", "wysyłał", "wysyłała", "paczkę",
     "wysłać", "wyślę wyślesz wyśle wyślemy wyślecie wyślą", ("wysłał", "wysłała"))
verb("kończyć", "kończę kończysz kończy kończymy kończycie kończą", "kończył", "kończyła", "raport",
     "skończyć", "skończę skończysz skończy skończymy skończycie skończą", ("skończył", "skończyła"))
verb("pomagać", "pomagam pomagasz pomaga pomagamy pomagacie pomagają", "pomagał", "pomagała", "sąsiadce",
     "pomóc", "pomogę pomożesz pomoże pomożemy pomożecie pomogą", ("pomógł", "pomogła"), ppast1=("pomogłem", "pomogłam"))
verb("jechać", "jadę jedziesz jedzie jedziemy jedziecie jadą", "jechał", "jechała", "do Warszawy",
     "pojechać", "pojadę pojedziesz pojedzie pojedziemy pojedziecie pojadą", ("pojechał", "pojechała"))
verb("iść", "idę idziesz idzie idziemy idziecie idą", "szedł", "szła", "do sklepu",
     "pójść", "pójdę pójdziesz pójdzie pójdziemy pójdziecie pójdą", ("poszedł", "poszła"))
verb("mieszkać", "mieszkam mieszkasz mieszka mieszkamy mieszkacie mieszkają", "mieszkał", "mieszkała", "w Sokołowie")
verb("lubić", "lubię lubisz lubi lubimy lubicie lubią", "lubił", "lubiła", "kawę z mlekiem")
verb("mieć", "mam masz ma mamy macie mają", "miał", "miała", "dużo pracy")
verb("chcieć", "chcę chcesz chce chcemy chcecie chcą", "chciał", "chciała", "nową pracę")
verb("spać", "śpię śpisz śpi śpimy śpicie śpią", "spał", "spała", "do ósmej")
verb("móc", "mogę możesz może możemy możecie mogą", "mógł", "mogła", "przyjść jutro", past1=("mogłem", "mogłam"))
verb("rozmawiać", "rozmawiam rozmawiasz rozmawia rozmawiamy rozmawiacie rozmawiają", "rozmawiał", "rozmawiała", "z sąsiadem",
     "porozmawiać", "porozmawiam porozmawiasz porozmawia porozmawiamy porozmawiacie porozmawiają", ("porozmawiał", "porozmawiała"))
verb("sprzedawać", "sprzedaję sprzedajesz sprzedaje sprzedajemy sprzedajecie sprzedają", "sprzedawał", "sprzedawała", "owoce na rynku",
     "sprzedać", "sprzedam sprzedasz sprzeda sprzedamy sprzedacie sprzedadzą", ("sprzedał", "sprzedała"))
verb("zamykać", "zamykam zamykasz zamyka zamykamy zamykacie zamykają", "zamykał", "zamykała", "drzwi",
     "zamknąć", "zamknę zamkniesz zamknie zamkniemy zamkniecie zamkną", ("zamknął", "zamknęła"))

# --- stopniowanie
COMP = [("tani", "tańszy", "najtańszy", "tańsza"), ("drogi", "droższy", "najdroższy", "droższa"),
        ("duży", "większy", "największy", "większa"), ("mały", "mniejszy", "najmniejszy", "mniejsza"),
        ("dobry", "lepszy", "najlepszy", "lepsza"), ("zły", "gorszy", "najgorszy", "gorsza"),
        ("szybki", "szybszy", "najszybszy", "szybsza"), ("wolny", "wolniejszy", "najwolniejszy", "wolniejsza"),
        ("ciekawy", "ciekawszy", "najciekawszy", "ciekawsza"), ("łatwy", "łatwiejszy", "najłatwiejszy", "łatwiejsza"),
        ("trudny", "trudniejszy", "najtrudniejszy", "trudniejsza"), ("wysoki", "wyższy", "najwyższy", "wyższa"),
        ("ciepły", "cieplejszy", "najcieplejszy", "cieplejsza"), ("zimny", "zimniejszy", "najzimniejszy", "zimniejsza"),
        ("długi", "dłuższy", "najdłuższy", "dłuższa"), ("krótki", "krótszy", "najkrótszy", "krótsza"),
        ("ładny", "ładniejszy", "najładniejszy", "ładniejsza"), ("nowy", "nowszy", "najnowszy", "nowsza"),
        ("stary", "starszy", "najstarszy", "starsza"), ("młody", "młodszy", "najmłodszy", "młodsza"),
        ("wygodny", "wygodniejszy", "najwygodniejszy", "wygodniejsza"), ("głośny", "głośniejszy", "najgłośniejszy", "głośniejsza"),
        ("spokojny", "spokojniejszy", "najspokojniejszy", "spokojniejsza"), ("bliski", "bliższy", "najbliższy", "bliższa")]
# rzeczowniki męskie do stopniowania z pasującymi przymiotnikami
COMP_SUBJ = {
    "telefon": ["tani", "drogi", "nowy", "stary", "dobry", "mały", "duży"],
    "film": ["ciekawy", "długi", "krótki", "dobry", "zły", "nowy"],
    "pociąg": ["szybki", "wolny", "nowy", "stary", "wygodny", "tani", "drogi"],
    "pokój": ["duży", "mały", "ciepły", "zimny", "ładny", "wygodny", "tani", "spokojny", "głośny"],
    "sklep": ["tani", "drogi", "duży", "mały", "nowy", "bliski"],
    "egzamin": ["łatwy", "trudny", "długi", "krótki"],
    "dom": ["duży", "mały", "nowy", "stary", "wysoki", "ładny", "ciepły"],
    "park": ["duży", "mały", "ładny", "spokojny", "stary", "bliski"],
    "samochód": ["szybki", "wolny", "tani", "drogi", "nowy", "stary", "wygodny"],
}
