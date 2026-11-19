/* Zdam B1 — czytanie. Teksty autorskie.
   Pytanie: { q, o: [poprawna, ...błędne] } (kolejność losowana)
   albo    { q, tf: true|false } (prawda / fałsz). Pole "hint" — fragment tekstu z odpowiedzią. */
window.B1 = window.B1 || {};
B1.reading = [
  {
    id: "r1", title: "Ogłoszenie: pokój do wynajęcia", kind: "ogłoszenie",
    text: `WYNAJMĘ POKÓJ OD 1 GRUDNIA

Mam do wynajęcia jasny, umeblowany pokój (14 m²) w mieszkaniu trzypokojowym na osiedlu Słonecznym, 10 minut pieszo od dworca PKP. W pokoju jest łóżko, szafa i duże biurko. Kuchnię i łazienkę dzielisz z dwiema studentkami.

Cena: 900 zł miesięcznie + media (ok. 150 zł). Kaucja w wysokości jednego czynszu.
Niestety nie akceptujemy zwierząt. W mieszkaniu nie wolno palić.

Kontakt najlepiej SMS-em, po godzinie 17:00. Ewa`,
    qs: [
      { q: "Pokój jest daleko od dworca.", tf: false, hint: "10 minut pieszo od dworca PKP" },
      { q: "Za media trzeba zapłacić dodatkowo.", tf: true, hint: "900 zł miesięcznie + media" },
      { q: "W mieszkaniu można mieszkać z kotem.", tf: false, hint: "nie akceptujemy zwierząt" },
      { q: "Ile wynosi kaucja?", o: ["900 zł", "150 zł", "1050 zł"], hint: "Kaucja w wysokości jednego czynszu (= 900 zł)" },
      { q: "Jak najlepiej skontaktować się z Ewą?", o: ["napisać SMS po 17:00", "zadzwonić rano", "wysłać e-mail"], hint: "Kontakt najlepiej SMS-em, po godzinie 17:00" }
    ]
  },
  {
    id: "r2", title: "E-mail od koleżanki", kind: "list prywatny",
    text: `Cześć Olu!

Przepraszam, że tak długo nie pisałam, ale ostatnio mam mnóstwo pracy. Od września pracuję w nowej firmie – w biurze podróży w centrum Lublina. Praca jest ciekawa, ale muszę dojeżdżać autobusem prawie godzinę w jedną stronę, więc myślę o przeprowadzce. Na szczęście szef pozwala mi pracować z domu w piątki.

Pamiętasz, że planowałyśmy wspólny wyjazd w góry? Mam wolne od 27 do 30 grudnia. Może pojedziemy do Zakopanego? Mój brat zna tam tani pensjonat, mogę zapytać o wolne pokoje. Nie jeżdżę dobrze na nartach, więc wolałabym chodzić po górach albo po prostu odpocząć.

Napisz, co o tym myślisz!
Ściskam,
Kasia`,
    qs: [
      { q: "Dlaczego Kasia długo nie pisała?", o: ["bo ma dużo pracy", "bo była chora", "bo była na urlopie"], hint: "ostatnio mam mnóstwo pracy" },
      { q: "Kasia mieszka blisko pracy.", tf: false, hint: "muszę dojeżdżać autobusem prawie godzinę" },
      { q: "Kiedy Kasia pracuje z domu?", o: ["w piątki", "codziennie", "nigdy"], hint: "szef pozwala mi pracować z domu w piątki" },
      { q: "Kto zna pensjonat w Zakopanem?", o: ["brat Kasi", "Ola", "szef Kasi"], hint: "Mój brat zna tam tani pensjonat" },
      { q: "Co Kasia chce robić w górach?", o: ["chodzić po górach i odpoczywać", "dużo jeździć na nartach", "pracować zdalnie"], hint: "wolałabym chodzić po górach albo po prostu odpocząć" }
    ]
  },
  {
    id: "r3", title: "Artykuł: Biblioteka, która łączy ludzi", kind: "artykuł",
    text: `Biblioteka, która łączy ludzi

Jeszcze kilka lat temu miejska biblioteka w małym miasteczku na Mazowszu była prawie pusta. Dziś trudno znaleźć tam wolne miejsce. Wszystko zmieniło się, kiedy nowa dyrektorka, pani Anna, postanowiła, że biblioteka będzie nie tylko miejscem, gdzie wypożycza się książki.

Teraz w każdy wtorek odbywają się tu bezpłatne spotkania dla cudzoziemców, którzy chcą ćwiczyć mówienie po polsku. Prowadzą je wolontariusze – najczęściej emerytowani nauczyciele. „Na początku przychodziły trzy osoby. Teraz jest nas ponad dwadzieścia” – mówi Ołena, która od roku mieszka w miasteczku i pracuje w lokalnej piekarni.

W bibliotece można też wypożyczyć gry planszowe, skorzystać z komputera z drukarką i wziąć udział w klubie książki. Raz w miesiącu dzieci z polskich i ukraińskich rodzin razem przygotowują przedstawienie teatralne.

Pani Anna mówi, że największym sukcesem nie jest liczba czytelników, ale to, że ludzie zaczęli ze sobą rozmawiać. W przyszłym roku biblioteka planuje otworzyć kawiarenkę, w której będzie można wymieniać się książkami.`,
    qs: [
      { q: "Kilka lat temu biblioteka…", o: ["była prawie pusta", "miała bardzo wielu czytelników", "była zamknięta"], hint: "była prawie pusta" },
      { q: "Spotkania dla cudzoziemców są płatne.", tf: false, hint: "bezpłatne spotkania dla cudzoziemców" },
      { q: "Kto prowadzi spotkania?", o: ["wolontariusze", "pani Anna", "Ołena"], hint: "Prowadzą je wolontariusze" },
      { q: "Ołena pracuje w bibliotece.", tf: false, hint: "pracuje w lokalnej piekarni" },
      { q: "Według pani Anny największy sukces to…", o: ["to, że ludzie zaczęli ze sobą rozmawiać", "duża liczba czytelników", "nowa kawiarenka"], hint: "największym sukcesem nie jest liczba czytelników, ale to, że ludzie zaczęli ze sobą rozmawiać" },
      { q: "Kawiarenka w bibliotece już działa.", tf: false, hint: "W przyszłym roku biblioteka planuje otworzyć kawiarenkę" }
    ]
  },
  {
    id: "r4", title: "Krótkie komunikaty", kind: "komunikaty",
    text: `A. Uprzejmie informujemy, że w dniach 10–12 marca przychodnia będzie nieczynna z powodu remontu. W pilnych sprawach prosimy kontaktować się z nocną i świąteczną opieką zdrowotną.

B. Szanowni Mieszkańcy! Prosimy nie zostawiać rowerów i wózków na klatce schodowej. Rowery można przechowywać w piwnicy – klucz jest do odebrania u administratora budynku.

C. PROMOCJA! Przy zakupie dwóch kaw trzecią dostajesz gratis. Oferta ważna do końca miesiąca. Promocja nie łączy się z innymi rabatami.

D. Zmiana rozkładu jazdy! Od 1 lutego autobus linii 5 nie będzie kursował w niedziele. W dni robocze autobus będzie jeździł co 20 minut, a nie – jak dotychczas – co 30 minut.`,
    qs: [
      { q: "Tekst A: przychodnia…", o: ["nie będzie pracować przez trzy dni", "będzie otwarta w nocy", "zmienia adres"], hint: "w dniach 10–12 marca przychodnia będzie nieczynna" },
      { q: "Tekst B: gdzie można zostawić rower?", o: ["w piwnicy", "na klatce schodowej", "u administratora"], hint: "Rowery można przechowywać w piwnicy" },
      { q: "Tekst C: promocję można łączyć z innymi rabatami.", tf: false, hint: "Promocja nie łączy się z innymi rabatami" },
      { q: "Tekst D: od 1 lutego autobus linii 5 w dni robocze będzie jeździł…", o: ["częściej niż wcześniej", "rzadziej niż wcześniej", "tylko w niedziele"], hint: "co 20 minut, a nie – jak dotychczas – co 30 minut" }
    ]
  },
  {
    id: "r5", title: "Opowiadanie: Pierwszy dzień w pracy", kind: "tekst narracyjny",
    text: `Pierwszy dzień w pracy

Kiedy Andrij przyjechał do Polski, nie znał prawie żadnego słowa po polsku. Przez pierwsze pół roku pracował w magazynie, gdzie wszyscy rozmawiali po ukraińsku, więc nie miał okazji ćwiczyć języka. Dopiero gdy zapisał się na wieczorowy kurs, zrozumiał, ile jeszcze musi się nauczyć.

Po roku nauki znalazł pracę w warsztacie samochodowym w Siedlcach. Pierwszego dnia bardzo się denerwował. Klienci mówili szybko, a szef używał słów, których Andrij nie znał, na przykład „sprzęgło” czy „wycieraczki”. Wieczorem zapisał w zeszycie wszystkie nowe słowa i nauczył się ich na pamięć.

Teraz, po dwóch latach, Andrij sam rozmawia z klientami i tłumaczy im, co trzeba naprawić. Mówi, że najważniejsze było to, że nie bał się popełniać błędów. „Polacy są cierpliwi, kiedy widzą, że się starasz” – mówi z uśmiechem.`,
    qs: [
      { q: "W magazynie Andrij często mówił po polsku.", tf: false, hint: "wszyscy rozmawiali po ukraińsku, więc nie miał okazji ćwiczyć języka" },
      { q: "Co zrobił Andrij po pierwszym dniu w warsztacie?", o: ["nauczył się nowych słów", "zrezygnował z pracy", "zapisał się na kurs"], hint: "zapisał w zeszycie wszystkie nowe słowa i nauczył się ich na pamięć" },
      { q: "Ile czasu Andrij uczył się polskiego, zanim znalazł pracę w warsztacie?", o: ["rok", "pół roku", "dwa lata"], hint: "Po roku nauki znalazł pracę w warsztacie" },
      { q: "Według Andrija najważniejsze było…", o: ["nie bać się błędów", "dużo czytać", "pracować w magazynie"], hint: "nie bał się popełniać błędów" }
    ]
  }
];
