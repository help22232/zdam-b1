"""Generuje bank gramatyki: data/grammar.json (>= 1000 pytań, bez dwuznaczności:
w nawiasie podana forma podstawowa, a opcje to inne formy TEGO SAMEGO słowa)."""
import json, sys
from collections import defaultdict
from common import make_rng, plural_form, HOUR_ORD_LOC, HOUR_ORD_NOM, DAYS_NOM, DAYS_ACC_PREP
from lexicon import N, PLACES, VEHICLES, HOBBIES, PROFESSIONS, ADJ, adj_forms, V, COMP, COMP_SUBJ

rng = make_rng(2026)
items = []        # dict(cat, q, o[0]=correct, ex{ua,ru})
seen = set()

CASE_UA = {"gen": "родовий (dopełniacz)", "dat": "давальний (celownik)", "acc": "знахідний (biernik)",
           "ins": "орудний (narzędnik)", "loc": "місцевий (miejscownik)", "nom": "називний (mianownik)"}
CASE_RU = {"gen": "родительный (dopełniacz)", "dat": "дательный (celownik)", "acc": "винительный (biernik)",
           "ins": "творительный (narzędnik)", "loc": "предложный (miejscownik)", "nom": "именительный (mianownik)"}


def add(cat, q, correct, wrong, ua, ru):
    wrong = [w for w in dict.fromkeys(wrong) if w != correct]
    if len(wrong) < 3:
        return False
    key = q + "|" + correct
    if key in seen:
        return False
    seen.add(key)
    items.append(dict(cat=cat, q=q, o=[correct] + rng.sample(wrong, 3), ex=dict(ua=ua, ru=ru)))
    return True


VOW = set("aąeęioóuy")


def needs_ze(w):
    w = w.lower()
    if w[:2] in ("sz", "rz", "cz") and len(w) > 2:
        return w[2] not in VOW
    return w[0] in "szśźżw" and len(w) > 1 and w[1] not in VOW and w[1] not in "z"


def forms_of(n):
    return [n["nom"], n["gen"], n["dat"], n["acc"], n["ins"], n["loc"]]


def ex_case(case, why_ua, why_ru, base, form):
    return (f"{why_ua} → {CASE_UA[case]}: {base} → {form}.",
            f"{why_ru} → {CASE_RU[case]}: {base} → {form}.")


# ---------------------------------------------------------------- przypadki: rzeczowniki
def case_items():
    persons = [n for n in N.values() if "person" in n["tags"] and n["nom"] != "dziecko"]
    things = [n for n in N.values() if "thing" in n["tags"]]
    foods = [n for n in N.values() if "food" in n["tags"]]
    animals = [n for n in N.values() if "animal" in n["tags"]]
    containers = [n for n in N.values() if "container" in n["tags"]]
    topics = [n for n in N.values() if "topic" in n["tags"]]

    T = [
        # (kategoria, lista rzeczowników, szablon, przypadek, wyjaśnienie ua, ru)
        ("gen", things + foods, "Nie mam ___ ({b}).", "gen", "Після заперечення «nie mam»", "После отрицания «nie mam»"),
        ("gen", persons + animals, "Dzisiaj nie widziałem ___ ({b}).", "gen", "Після заперечення «nie widziałem»", "После отрицания «nie widziałem»"),
        ("gen", things, "Od rana szukam ___ ({b}).", "gen", "szukać czego? (дієслово вимагає родового)", "szukać чего? (глагол требует родительного)"),
        ("gen", things + foods, "Potrzebuję ___ ({b}).", "gen", "potrzebować czego?", "potrzebować чего?"),
        ("gen", persons, "To jest prezent dla ___ ({b}).", "gen", "Прийменник «dla»", "Предлог «dla»"),
        ("gen", persons, "W weekend jadę do ___ ({b}).", "gen", "Прийменник «do» (до кого?)", "Предлог «do» (к кому?)"),
        ("gen", persons, "Mieszkam teraz u ___ ({b}).", "gen", "Прийменник «u» (у кого?)", "Предлог «u» (у кого?)"),
        ("gen", persons, "Dostałem SMS-a od ___ ({b}).", "gen", "Прийменник «od» (від кого?)", "Предлог «od» (от кого?)"),
        ("gen", persons + animals, "Nie ma ___ ({b}) w domu.", "gen", "Конструкція «nie ma» (немає кого?)", "Конструкция «nie ma» (нет кого?)"),
        ("gen", animals, "Moja córka boi się ___ ({b}).", "gen", "bać się kogo? czego?", "bać się кого? чего?"),
        ("dat", persons, "Codziennie pomagam ___ ({b}).", "dat", "pomagać komu?", "pomagać кому?"),
        ("dat", persons, "Kupiłem kwiaty ___ ({b}).", "dat", "kupić coś komu?", "kupić что-то кому?"),
        ("dat", persons, "Dziękuję ___ ({b}) za pomoc.", "dat", "dziękować komu?", "dziękować кому?"),
        ("dat", persons, "Wysłałem zdjęcia ___ ({b}).", "dat", "wysłać coś komu?", "wysłać что-то кому?"),
        ("dat", persons, "Opowiedziałem wszystko ___ ({b}).", "dat", "opowiedzieć komu?", "opowiedzieć кому?"),
        ("dat", animals, "Daję jeść ___ ({b}) dwa razy dziennie.", "dat", "dawać komu?", "давать кому?"),
        ("acc", things + foods, "Wczoraj kupiłem ___ ({b}).", "acc", "kupić co? (прямий додаток)", "kupić что? (прямое дополнение)"),
        ("acc", persons + animals, "Bardzo dobrze znam ___ ({b}).", "acc", "znać kogo?", "znać кого?"),
        ("acc", persons, "W sobotę odwiedzam ___ ({b}).", "acc", "odwiedzać kogo?", "odwiedzać кого?"),
        ("acc", persons + things, "Czekam na ___ ({b}) już pół godziny.", "acc", "czekać na kogo? na co?", "czekać на кого? на что?"),
        ("acc", foods, "Rano zawsze piję lub jem ___ ({b}).", "acc", "pić / jeść co?", "pić / jeść что?"),
        ("acc", things, "Zgubiłem ___ ({b}) w autobusie.", "acc", "zgubić co?", "zgubić что?"),
        ("ins", persons, "Wczoraj rozmawiałem z ___ ({b}).", "ins", "z (разом з ким?)", "z (вместе с кем?)"),
        ("ins", persons, "Idę do kina z ___ ({b}).", "ins", "z (з ким?)", "z (с кем?)"),
        ("ins", persons + animals, "Opiekuję się ___ ({b}).", "ins", "opiekować się kim?", "opiekować się кем?"),
        ("ins", [N["cukier"], N["mleko"], N["sok"]], "Piję herbatę z ___ ({b}).", "ins", "z (з чим?)", "z (с чем?)"),
        ("ins", [N["ser"], N["chleb"], N["jabłko"]], "Na kolację jem sałatkę z ___ ({b}).", "ins", "z (з чим?)", "z (с чем?)"),
        ("loc", persons + topics, "Często myślę o ___ ({b}).", "loc", "myśleć o kim? o czym?", "myśleć о ком? о чём?"),
        ("loc", persons + topics, "Długo rozmawialiśmy o ___ ({b}).", "loc", "rozmawiać o kim? o czym?", "rozmawiać о ком? о чём?"),
        ("loc", containers, "Zostawiłem klucze w ___ ({b}).", "loc", "w (де?)", "w (где?)"),
    ]
    for cat, nouns, tpl, case, wu, wr in T:
        for n in nouns:
            corr = n[case]
            # prepozycja z → ze przed trudnymi grupami spółgłosek
            q = tpl.format(b=n["nom"])
            if "z ___" in q and needs_ze(n[case]):
                q = q.replace("z ___", "ze ___")
            ua, ru = ex_case(case, wu, wr, n["nom"], corr)
            add("przypadki", q, corr, forms_of(n), ua, ru)


# ---------------------------------------------------------------- przymiotnik + rzeczownik
def adj_noun_items():
    OK = {  # sensowne połączenia przymiotnik + rzeczownik
        "samochód": "nowy stary duży mały tani drogi czerwony czarny wygodny dobry",
        "telefon": "nowy stary tani drogi czarny dobry mały duży",
        "komputer": "nowy stary tani drogi dobry czarny",
        "rower": "nowy stary tani drogi czerwony czarny wygodny dobry",
        "bilet": "tani drogi",
        "klucz": "nowy stary duży mały czarny",
        "paszport": "nowy stary polski",
        "parasol": "nowy stary duży mały czerwony czarny ładny tani",
        "portfel": "nowy stary czarny czerwony ładny drogi tani mały",
        "prezent": "ładny drogi tani duży mały dobry",
        "chleb": "dobry tani polski",
        "ser": "dobry tani drogi polski",
        "sok": "dobry tani zimny",
        "film": "nowy stary dobry polski",
        "książka": "nowy stary dobry ciekawy polski tani drogi",
        "kawa": "dobry ciepły tani drogi",
        "herbata": "dobry ciepły",
        "zupa": "dobry ciepły polski",
        "torba": "nowy stary duży mały czerwony czarny ładny wygodny tani drogi",
        "gazeta": "nowy stary polski",
        "kurtka": "nowy stary ciepły czerwony czarny ładny wygodny tani drogi",
        "szafa": "nowy stary duży mały ładny",
        "mieszkanie": "nowy stary duży mały ciepły ładny wygodny tani drogi",
        "auto": "nowy stary duży mały czerwony czarny wygodny tani drogi",
        "okno": "nowy stary duży mały",
        "jabłko": "duży mały czerwony dobry polski",
        "krzesło": "nowy stary wygodny czarny czerwony",
        "zdjęcie": "nowy stary ładny",
        "biurko": "nowy stary duży mały czarny wygodny",
    }
    pairs = []
    for m, f, nn in ADJ:
        af = adj_forms(m, f, nn)
        for nom, allowed in OK.items():
            if m in allowed.split():
                pairs.append((af, (m, f, nn), N[nom]))
    rng.shuffle(pairs)
    TPL = [("Szukam ___ ({b}).", "gen", "szukać czego?"), ("Nie mam ___ ({b}).", "gen", "після заперечення"),
           ("Kupiłem ___ ({b}).", "acc", "kupić co?"), ("Mówimy o ___ ({b}).", "loc", "mówić o czym?"),
           ("Jestem bardzo zadowolony z ___ ({b}).", "gen", "zadowolony z czego?")]
    TPL_RU = {"szukać czego?": "szukać чего?", "після заперечення": "после отрицания", "kupić co?": "kupić что?",
              "mówić o czym?": "mówić о чём?", "zadowolony z czego?": "zadowolony z чего?"}
    count = 0
    for af, (m, f, nn), n in pairs:
        g = "m" if n["g"] in ("m", "mi") else n["g"]
        base_adj = {"m": m, "f": f, "n": nn}[g]
        base = f"{base_adj} {n['nom']}"
        tpl, case, why = TPL[count % len(TPL)]
        acase = "acc" if case == "acc" else case
        corr = f"{af[(g, acase)]} {n[case]}"
        wrong = [f"{af[(g, c)]} {n[c2]}" for c, c2 in (("nom", "nom"), ("gen", "gen"), ("ins", "ins"), ("loc", "loc"), ("dat", "dat"), ("acc", "acc"))]
        ua = f"{why} → {CASE_UA[case]}; прикметник узгоджується з іменником: {base} → {corr}."
        ru = f"{TPL_RU[why]} → {CASE_RU[case]}; прилагательное согласуется с существительным: {base} → {corr}."
        if add("przymiotnik", tpl.format(b=base), corr, wrong, ua, ru):
            count += 1
        if count >= 190:
            break


# ---------------------------------------------------------------- miejsca, kierunki, przyimki
def place_items():
    for p in PLACES.values():
        allf = [p["nom"], p["gen"], p["acc"], p["ins"], p["loc"]]
        b = p["nom"]
        # gdzie?
        lead = "Od roku mieszkam" if p["kind"] == "city" else "Jestem teraz"
        add("miejsca", f"{lead} {p['where']} ___ ({b}).", p["loc"], allf,
            f"«{p['where']}» у значенні «де?» → {CASE_UA['loc']}: {b} → {p['loc']}.",
            f"«{p['where']}» в значении «где?» → {CASE_RU['loc']}: {b} → {p['loc']}.")
        # dokąd?
        if p["whither"] == "do":
            add("miejsca", f"Jutro {'jadę' if p['kind'] == 'city' else 'idę'} do ___ ({b}).", p["gen"], allf,
                f"«do» (куди?) → {CASE_UA['gen']}: {b} → {p['gen']}.", f"«do» (куда?) → {CASE_RU['gen']}: {b} → {p['gen']}.")
        else:
            add("miejsca", f"Jutro idę na ___ ({b}).", p["acc"], allf,
                f"«na» (куди?) → {CASE_UA['acc']}: {b} → {p['acc']}. Де? → na + miejscownik ({p['loc']}).",
                f"«na» (куда?) → {CASE_RU['acc']}: {b} → {p['acc']}. Где? → na + miejscownik ({p['loc']}).")
        # skąd?
        add("miejsca", f"Właśnie wracam {p['whence']} ___ ({b}).", p["gen"], allf,
            f"«{p['whence']}» (звідки?) → {CASE_UA['gen']}: {b} → {p['gen']}.",
            f"«{p['whence']}» (откуда?) → {CASE_RU['gen']}: {b} → {p['gen']}.")
        # wybór przyimka
        if p["kind"] != "city":
            wh = p["where"]
            other = "na" if wh in ("w", "we") else "w"
            add("przyimki", f"Spotkajmy się ___ {p['loc']}.", wh, [other, "do", "z", "u", "o"],
                f"Місце «де?»: з цим словом кажуть «{wh} {p['loc']}». Запам'ятай: na poczcie, na dworcu, na basenie, na uniwersytecie; w sklepie, w banku, w szkole.",
                f"Место «где?»: с этим словом говорят «{wh} {p['loc']}». Запомни: na poczcie, na dworcu, na basenie, na uniwersytecie; w sklepie, w banku, w szkole.")
            if p["whither"] == "do":
                add("przyimki", f"Po pracy idę ___ {p['gen']}.", "do", ["na", "w", "o", "przy"],
                    f"Куди? → «do» + родовий: do {p['gen']}.", f"Куда? → «do» + родительный: do {p['gen']}.")
            else:
                add("przyimki", f"Po pracy idę ___ {p['acc']}.", "na", ["do", "w", "o", "przy"],
                    f"Куди? → з цим місцем «na» + знахідний: na {p['acc']}.", f"Куда? → с этим местом «na» + винительный: na {p['acc']}.")
    for v, (gen, acc, ins, loc) in VEHICLES.items():
        allf = [v, gen, acc, ins, loc]
        for tpl in ("Do pracy jeżdżę ___ ({b}).", "Do Warszawy pojedziemy ___ ({b})."):
            add("miejsca", tpl.format(b=v), ins, allf,
                f"Чим їдемо? Транспорт без прийменника → {CASE_UA['ins']}: {v} → {ins}.",
                f"На чём едем? Транспорт без предлога → {CASE_RU['ins']}: {v} → {ins}.")


# ---------------------------------------------------------------- zainteresowania i zawody
def hobby_prof_items():
    for h, (gen, acc, ins, loc) in HOBBIES.items():
        allf = [h, gen, acc, ins, loc]
        add("przypadki", f"Od dziecka interesuję się ___ ({h}).", ins, allf,
            f"interesować się czym? → {CASE_UA['ins']}: {h} → {ins}.", f"interesować się чем? → {CASE_RU['ins']}: {h} → {ins}.")
        add("przypadki", f"Mój syn nie interesuje się ___ ({h}).", ins, allf,
            f"interesować się czym? (і з запереченням теж орудний) → {ins}.", f"interesować się чем? (и с отрицанием тоже творительный) → {ins}.")
    for p, ((gen, acc, ins, dat), g) in PROFESSIONS.items():
        allf = [p, gen, acc, ins, dat]
        who = "Moja siostra" if g == "f" else "Mój brat"
        add("przypadki", f"{who} jest ___ ({p}).", ins, allf,
            f"być + ким? → {CASE_UA['ins']}: jest {ins}.", f"być + кем? → {CASE_RU['ins']}: jest {ins}.")
        add("przypadki", f"{who} pracuje jako ___ ({p}).", p, allf,
            f"Пастка! «jako» + називний відмінок: pracuje jako {p}. Але: jest {ins}.",
            f"Ловушка! «jako» + именительный падеж: pracuje jako {p}. Но: jest {ins}.")


# ---------------------------------------------------------------- liczebniki
def numeral_items():
    ages = list(range(2, 40)) + [41, 42, 44, 45, 52, 53, 55, 62, 64, 67, 72, 73, 81, 84, 91, 99]
    for n in ages:
        corr = plural_form(n, "rok", "lata", "lat")
        add("liczebniki", f"Mój dziadek ma {n} ___ (rok)." if n > 50 else f"Mam {n} ___ (rok).", corr,
            ["rok", "lata", "lat", "roku", "latach"],
            f"Після {n}: 2, 3, 4 (і 22, 23, 24…, крім 12–14) → lata; 5–21, 25–31… → lat; 1 → rok.",
            f"После {n}: 2, 3, 4 (и 22, 23, 24…, кроме 12–14) → lata; 5–21, 25–31… → lat; 1 → rok.")
    cnt = [n for n in N.values() if "count" in n["tags"] and n["pl_nom"] and n["g"] != "m" or n["nom"] in ("pies", "kot")]
    nums = [2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 22, 23, 24, 25, 30, 32]
    for n in cnt:
        for k in rng.sample(nums, 6):
            corr = n["pl_nom"] if (k % 10 in (2, 3, 4) and k % 100 not in (12, 13, 14)) else n["pl_gen"]
            other = n["pl_gen"] if corr == n["pl_nom"] else n["pl_nom"]
            wrong = [other, n["nom"], n["gen"], n["ins"], n["loc"]]
            rule_ua = "2, 3, 4 (22–24…) + називний відмінок множини" if corr == n["pl_nom"] else "5 і більше (а також 12–14) + родовий відмінок множини"
            rule_ru = "2, 3, 4 (22–24…) + именительный падеж мн. ч." if corr == n["pl_nom"] else "5 и больше (а также 12–14) + родительный падеж мн. ч."
            add("liczebniki", f"Mam {k} ___ ({n['nom']}).", corr, wrong,
                f"{rule_ua}: {k} {corr}.", f"{rule_ru}: {k} {corr}.")


# ---------------------------------------------------------------- czasowniki
PRON = [("Ja", 0), ("Ty", 1), ("Marek", 2), ("Anna", 2), ("My", 3), ("Wy", 4), ("Moi rodzice", 5)]
PRON_UA = ["я (ja)", "ти (ty)", "він / вона (on / ona)", "він / вона (on / ona)", "ми (my)", "ви (wy)", "вони (oni)"]
PRON_RU = ["я (ja)", "ты (ty)", "он / она (on / ona)", "он / она (on / ona)", "мы (my)", "вы (wy)", "они (oni)"]


def verb_items():
    for v in V:
        sie = " się" if v["refl"] else ""
        for i, (who, p) in enumerate(PRON):
            adv = rng.choice(["codziennie", "często", "zwykle", "teraz"])
            if v["inf"] in ("iść", "jechać"):
                adv = "teraz"
            elif v["inf"] in ("chcieć", "lubić"):
                adv = "naprawdę"
            elif v["inf"] == "móc":
                adv = "na pewno"
            elif v["inf"] in ("mieć", "mieszkać"):
                adv = "teraz"
            corr = v["pres"][p]
            q = f"{who} {adv} ___{sie} {v['obj']} ({v['inf']})."
            add("czasowniki", q, corr, v["pres"],
                f"Теперішній час, особа: {PRON_UA[i]} → {corr}.", f"Настоящее время, лицо: {PRON_RU[i]} → {corr}.")
        if v["inf"] in ("móc", "lubić", "mieszkać"):
            continue
        # czas przeszły – rodzaj
        add("czasowniki", f"Wczoraj Anna ___{sie} {v['obj']} ({v['inf']}).", v["past_f"],
            [v["past_m"], v["pres"][2], v["past1f"], v["past1m"]],
            f"Минулий час, жіночий рід (Anna = ona): {v['past_f']}.", f"Прошедшее время, женский род (Anna = ona): {v['past_f']}.")
        add("czasowniki", f"Wczoraj Tomek ___{sie} {v['obj']} ({v['inf']}).", v["past_m"],
            [v["past_f"], v["pres"][2], v["past1m"], v["past1f"]],
            f"Минулий час, чоловічий рід (Tomek = on): {v['past_m']}.", f"Прошедшее время, мужской род (Tomek = on): {v['past_m']}.")
        add("czasowniki", f"— Wczoraj ___{sie} {v['obj']} ({v['inf']}) — mówi Ola.", v["past1f"],
            [v["past1m"], v["past_f"], v["pres"][0], v["past_m"]],
            f"Говорить жінка про себе (ja, ż.) → закінчення -łam: {v['past1f']}.", f"Говорит женщина о себе (ja, ж.) → окончание -łam: {v['past1f']}.")
        add("czasowniki", f"— W zeszłym tygodniu ___{sie} {v['obj']} ({v['inf']}) — mówi Piotr.", v["past1m"],
            [v["past1f"], v["past_m"], v["pres"][0], v["past_f"]],
            f"Говорить чоловік про себе (ja, ч.) → закінчення -łem: {v['past1m']}.", f"Говорит мужчина о себе (ja, м.) → окончание -łem: {v['past1m']}.")
        if not v["perf"]:
            continue
        pi = v["perf"]
        # aspekt
        if v["inf"] not in ("iść", "jechać", "wracać", "otwierać", "zamykać", "kończyć"):
          add("aspekt", f"Wczoraj cały wieczór ___{sie} {v['obj']} ({v['inf']} / {pi}). — mówi Marek.", v["past1m"],
            [v["ppast1m"], v["pfut"][0], v["pres"][0]],
            "«cały wieczór» = процес, тривалість → недоконаний вид: " + v["past1m"] + ".",
            "«cały wieczór» = процесс, длительность → несовершенный вид: " + v["past1m"] + ".")
        add("aspekt", f"Wczoraj w końcu ___{sie} {v['obj']} ({v['inf']} / {pi}). — mówi Marek.", v["ppast1m"],
            [v["past1m"], v["pfut"][0], v["pres"][0]],
            "«w końcu» = результат, дію завершено → доконаний вид: " + v["ppast1m"] + ".",
            "«w końcu» = результат, действие завершено → совершенный вид: " + v["ppast1m"] + ".")
        add("aspekt", f"Kiedy byłam mała, często ___{sie} {v['obj']} ({v['inf']} / {pi}).", v["past1f"],
            [v["ppast1f"], v["pfut"][0], v["pres"][0]],
            "«często» у минулому = повторювана дія → недоконаний вид: " + v["past1f"] + ".",
            "«często» в прошлом = повторяющееся действие → несовершенный вид: " + v["past1f"] + ".")
        add("aspekt", f"Obiecuję, że jutro ___{sie} {v['obj']} ({pi}).", v["pfut"][0],
            [v["ppast1m"], v["past1m"], pi + ("" if not v["refl"] else "")],
            f"Майбутній результат, доконаний вид: форма теперішнього часу = майбутній: {v['pfut'][0]}.",
            f"Будущий результат, совершенный вид: форма настоящего времени = будущее: {v['pfut'][0]}.")
        add("aspekt", f"Ona już ___{sie} {v['obj']}, możemy iść ({v['inf']} / {pi}).", v["ppast_f"],
            [v["past_f"], v["pfut"][2], v["pres"][2]],
            "«już» + результат → доконаний вид, минулий час: " + v["ppast_f"] + ".",
            "«już» + результат → совершенный вид, прошедшее время: " + v["ppast_f"] + ".")
        # tryb przypuszczający
        add("tryb", f"Gdybym miał więcej czasu, ___{sie} {v['obj']} ({pi}).", v["ppast_m"] + "bym",
            [v["pfut"][0], v["ppast1m"], v["pres"][0]],
            f"Gdybym… → умовний спосіб: {v['ppast_m']} + bym = {v['ppast_m']}bym.",
            f"Gdybym… → условное наклонение: {v['ppast_m']} + bym = {v['ppast_m']}bym.")
        add("tryb", f"Gdybym miała wolny dzień, ___{sie} {v['obj']} ({pi}).", v["ppast_f"] + "bym",
            [v["pfut"][0], v["ppast1f"], v["ppast_m"] + "bym"],
            f"Жінка про себе: {v['ppast_f']} + bym = {v['ppast_f']}bym.",
            f"Женщина о себе: {v['ppast_f']} + bym = {v['ppast_f']}bym.")


# ---------------------------------------------------------------- stopniowanie
def comp_items():
    cmap = {c[0]: c for c in COMP}
    for subj, adjs in COMP_SUBJ.items():
        for a in adjs:
            base, comp, sup, fcomp = cmap[a]
            add("stopniowanie", f"Ten {subj} jest ___ niż tamten ({base}).", comp, [base, sup, fcomp, "bardziej " + comp],
                f"Порівняння двох речей + «niż» → вищий ступінь: {base} → {comp}.",
                f"Сравнение двух вещей + «niż» → сравнительная степень: {base} → {comp}.")
            add("stopniowanie", f"To jest ___ {subj} w całym mieście ({base}).", sup, [base, comp, sup[:-1] + "a"],
                f"«w całym mieście» = з усіх → найвищий ступінь: {sup}.",
                f"«w całym mieście» = из всех → превосходная степень: {sup}.")


# ---------------------------------------------------------------- zaimki, czas, daty (ręcznie)
def manual_items():
    P = [
        ("Daj ___ (ja), proszę, ten długopis.", "mi", ["mną", "ja", "mój"], "dać komu? → коротка форма «mi»", "dać кому? → краткая форма «mi»"),
        ("Czekam na ___ (ty) przed kinem.", "ciebie", ["ty", "tobą", "tobie"], "na + знахідний; після прийменника — повна форма «ciebie»", "na + винительный; после предлога — полная форма «ciebie»"),
        ("Wczoraj rozmawiałem z ___ (on).", "nim", ["on", "jego", "niego"], "z + орудний; після прийменника — форма з «n»: nim", "z + творительный; после предлога — форма с «n»: nim"),
        ("Nie widzę ___ (ona) w klasie.", "jej", ["ona", "ją", "nią"], "заперечення → родовий: jej", "отрицание → родительный: jej"),
        ("To prezent dla ___ (ty).", "ciebie", ["ty", "ci", "tobą"], "dla + родовий: ciebie", "dla + родительный: ciebie"),
        ("Jutro pójdę do ___ (on).", "niego", ["go", "jego", "on"], "після прийменника «do» → niego", "после предлога «do» → niego"),
        ("Zadzwonię do ___ (wy) wieczorem.", "was", ["wy", "wam", "wami"], "do + родовий: was", "do + родительный: was"),
        ("Codziennie pomagam ___ (ona).", "jej", ["ją", "ona", "nią"], "pomagać komu? → давальний: jej", "pomagać кому? → дательный: jej"),
        ("Często myślę o ___ (ty).", "tobie", ["ciebie", "tobą", "ty"], "o + місцевий: tobie", "o + предложный: tobie"),
        ("Pójdziesz ze ___ (ja) do kina?", "mną", ["mnie", "mi", "ja"], "z + орудний: ze mną", "z + творительный: ze mną"),
        ("Widzę ___ (on) codziennie w autobusie.", "go", ["on", "nim", "mu"], "widzieć kogo? → коротка форма знахідного: go", "widzieć кого? → краткая форма винительного: go"),
        ("Bardzo ___ (oni) lubię.", "ich", ["oni", "im", "nimi"], "lubić kogo? → ich", "lubić кого? → ich"),
        ("Opowiem ___ (wy) wszystko jutro.", "wam", ["was", "wy", "wami"], "opowiedzieć komu? → wam", "opowiedzieć кому? → wam"),
        ("Przyjdźcie do ___ (my) w sobotę.", "nas", ["my", "nam", "nami"], "do + родовий: nas", "do + родительный: nas"),
        ("Dziękuję ___ (wy) za pomoc.", "wam", ["was", "wy", "wami"], "dziękować komu? → wam", "dziękować кому? → wam"),
        ("Kocham ___ (ty).", "cię", ["ty", "tobie", "tobą"], "kochać kogo? → коротка форма: cię", "kochać кого? → краткая форма: cię"),
        ("Powiedz ___ (on), że się spóźnię.", "mu", ["go", "on", "nim"], "powiedzieć komu? → коротка форма давального: mu", "powiedzieć кому? → краткая форма дательного: mu"),
        ("Mieszkam z ___ (ona) od roku.", "nią", ["ją", "jej", "ona"], "z + орудний: z nią", "z + творительный: z nią"),
        ("Rozmawialiśmy o ___ (oni) wczoraj.", "nich", ["ich", "oni", "nimi"], "o + місцевий: o nich", "o + предложный: o nich"),
        ("Pomóż ___ (ja), proszę.", "mi", ["mnie", "mną", "ja"], "pomóc komu? → mi", "pomóc кому? → mi"),
        ("Wyślę ___ (ty) zdjęcia jutro.", "ci", ["cię", "ty", "tobą"], "wysłać komu? → коротка форма: ci", "wysłać кому? → краткая форма: ci"),
        ("Znam ___ (ona) od dziecka.", "ją", ["jej", "nią", "ona"], "znać kogo? (ж.) → ją", "znać кого? (ж.) → ją"),
        ("Bez ___ (ty) nie pojadę.", "ciebie", ["ci", "cię", "tobą"], "bez + родовий: bez ciebie", "bez + родительный: bez ciebie"),
        ("Idę z ___ (oni) na basen.", "nimi", ["nich", "nim", "oni"], "z + орудний мн.: z nimi", "z + творительный мн.: z nimi"),
        ("Czy możesz ___ (my) pomóc?", "nam", ["nas", "nami", "my"], "pomóc komu? → nam", "pomóc кому? → nam"),
    ]
    for q, c, w, ua, ru in P:
        items.append(dict(cat="zaimki", q=q, o=[c] + w, ex=dict(ua=ua.capitalize() + ".", ru=ru.capitalize() + ".")))
    for h in range(5, 21):
        add("czas", f"Spotkajmy się o ___ ({h}:00).", HOUR_ORD_LOC[h],
            [HOUR_ORD_NOM[h], HOUR_ORD_NOM[h][:-1] + "ą", HOUR_ORD_NOM[h][:-1] + "u" if HOUR_ORD_NOM[h].endswith("a") else HOUR_ORD_NOM[h] + "u", f"{h}"],
            f"Година: «o» + місцевий відмінок порядкового числівника: o {HOUR_ORD_LOC[h]}.",
            f"Время: «o» + предложный падеж порядкового числительного: o {HOUR_ORD_LOC[h]}.")
    DAY_ALT = {0: ["w poniedziałku", "we poniedziałek", "na poniedziałek"], 1: ["w wtorek", "we wtorku", "na wtorek"],
               2: ["w środzie", "we środę", "w środa"], 3: ["w czwartku", "we czwartek", "na czwartek"],
               4: ["w piątku", "we piątek", "na piątek"], 5: ["w sobocie", "w sobota", "we sobotę"],
               6: ["w niedzieli", "w niedziela", "we niedzielę"]}
    for i, d in enumerate(DAYS_NOM):
        add("czas", f"Przyjdę do ciebie ___ ({d}).", DAYS_ACC_PREP[i], DAY_ALT[i] + ["o " + d],
            f"Коли? День тижня: w/we + знахідний: {DAYS_ACC_PREP[i]}. «we» перед «w-»: we wtorek.",
            f"Когда? День недели: w/we + винительный: {DAYS_ACC_PREP[i]}. «we» перед «w-»: we wtorek.")
        add("czas", f"Egzamin jest ___ ({d}).", DAYS_ACC_PREP[i], DAY_ALT[i] + ["o " + d],
            f"Коли? → {DAYS_ACC_PREP[i]}.", f"Когда? → {DAYS_ACC_PREP[i]}.")
    MONTHS = [("styczeń", "stycznia", "styczniu", "styczniowi"), ("luty", "lutego", "lutym", "lutemu"),
              ("marzec", "marca", "marcu", "marcowi"), ("kwiecień", "kwietnia", "kwietniu", "kwietniowi"),
              ("maj", "maja", "maju", "majowi"), ("czerwiec", "czerwca", "czerwcu", "czerwcowi"),
              ("lipiec", "lipca", "lipcu", "lipcowi"), ("sierpień", "sierpnia", "sierpniu", "sierpniowi"),
              ("wrzesień", "września", "wrześniu", "wrześniowi"), ("październik", "października", "październiku", "październikowi"),
              ("listopad", "listopada", "listopadzie", "listopadowi"), ("grudzień", "grudnia", "grudniu", "grudniowi")]
    for nom, gen, loc, dat in MONTHS:
        add("czas", f"Urodziłem się w ___ ({nom}).", loc, [nom, gen, dat],
            f"«w» + місяць → місцевий відмінок: w {loc}.", f"«w» + месяц → предложный падеж: w {loc}.")
        add("czas", f"Egzamin będzie piątego ___ ({nom}).", gen, [nom, loc, dat],
            f"Дата: порядковий числівник + місяць у родовому: piątego {gen}.",
            f"Дата: порядковое числительное + месяц в родительном: piątego {gen}.")


case_items(); adj_noun_items(); place_items(); hobby_prof_items(); numeral_items(); verb_items(); comp_items(); manual_items()

# --- kontrola jakości
bad = [it for it in items if len(set(it["o"])) != 4 or "___" not in it["q"]]
assert not bad, bad[:3]

# --- równoważenie kategorii i bloki po 20
by = defaultdict(list)
for it in items:
    by[it["cat"]].append(it)
for v in by.values():
    rng.shuffle(v)
order = []
cats = sorted(by)
while any(by[c] for c in cats):           # przeplatanie: w każdym bloku różne tematy
    for c in cats:
        if by[c]:
            order.append(by[c].pop())
for i, it in enumerate(order):
    it["id"] = f"g{i + 1:04d}"
out = dict(blockSize=20, items=order)
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
cnt = defaultdict(int)
for it in order:
    cnt[it["cat"]] += 1
print("razem:", len(order), dict(cnt))
