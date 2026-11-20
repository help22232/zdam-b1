/* Zdam B1 — pisanie, zestaw 2 (w13–w44). Treści autorskie: zadania i wzory napisane od zera. */
window.B1 = window.B1 || {};
B1.writingTasks = (B1.writingTasks || []).concat([
  /* ---------- OGŁOSZENIA ---------- */
  {
    id: "w13", type: "ogloszenie", title: "Znaleziony telefon",
    prompt: "W autobusie znalazłeś / znalazłaś telefon komórkowy. Napisz ogłoszenie na osiedlową grupę w internecie.",
    points: ["co i gdzie znalazłeś / znalazłaś", "kiedy to było", "jak właściciel może udowodnić, że to jego telefon", "jak się z Tobą skontaktować"],
    model: "ZNALEZIONO TELEFON\n\nWczoraj, we wtorek, około godziny 8:00 znalazłem telefon komórkowy w autobusie linii 3, na siedzeniu z tyłu. Telefon jest w czarnym etui z naklejką kota.\n\nWłaściciel musi podać kolor tapety ekranu albo kod do telefonu.\nKontakt: wiadomość prywatna lub tel. 500 000 000, codziennie po 16:00.\nOleh"
  },
  {
    id: "w14", type: "ogloszenie", title: "Oddam meble za darmo",
    prompt: "Przeprowadzasz się i chcesz oddać za darmo kilka mebli. Napisz ogłoszenie do lokalnej gazety.",
    points: ["co chcesz oddać i w jakim jest stanie", "dlaczego oddajesz", "do kiedy i skąd trzeba odebrać meble", "kontakt"],
    model: "ODDAM ZA DARMO\n\nOddam szafę, stół i cztery krzesła. Meble są używane, ale w dobrym stanie, bez uszkodzeń. Oddaję je, ponieważ przeprowadzam się do mniejszego mieszkania i nie mam na nie miejsca.\n\nOdbiór własny z ulicy Polnej 12 (trzecie piętro, bez windy) do końca miesiąca.\nKontakt: tel. 500 000 000, po godzinie 18:00.\nNatalia"
  },
  {
    id: "w15", type: "ogloszenie", title: "Szukam opiekunki do dziecka",
    prompt: "Szukasz osoby, która zaopiekuje się Twoim dzieckiem po południu. Napisz ogłoszenie na tablicę w przedszkolu.",
    points: ["kogo szukasz i do jakiego dziecka", "w jakich dniach i godzinach", "jakie są wymagania", "ile płacisz i jak się skontaktować"],
    model: "SZUKAM OPIEKUNKI\n\nSzukam opiekunki do pięcioletniego syna. Praca od poniedziałku do piątku w godzinach 15:00–18:00: odbiór z przedszkola, spacer, zabawa i kolacja. Szukam osoby odpowiedzialnej, cierpliwej i niepalącej. Doświadczenie z dziećmi będzie dużym plusem.\n\nStawka: 30 zł za godzinę.\nKontakt: tel. 500 000 000 lub e-mail opieka@przyklad.pl.\nIryna"
  },
  {
    id: "w16", type: "ogloszenie", title: "Zaginął kot",
    prompt: "Twój kot nie wrócił do domu. Napisz ogłoszenie, które powiesisz na klatkach schodowych w okolicy.",
    points: ["kiedy i gdzie zaginął kot", "jak wygląda", "jak się zachowuje", "nagroda i kontakt"],
    model: "ZAGINĄŁ KOT!\n\nW niedzielę wieczorem z ogrodu przy ulicy Kwiatowej 8 uciekł nasz kot Rudy. Jest duży, rudy, ma białe łapy i zieloną obrożę. Jest przyjazny, ale boi się psów i głośnych dźwięków, dlatego może chować się w piwnicach lub garażach.\n\nProsimy sprawdzić swoje piwnice!\nDla znalazcy nagroda: 200 zł.\nKontakt: tel. 500 000 000 (o każdej porze).\nRodzina Melnyków"
  },
  {
    id: "w17", type: "ogloszenie", title: "Wymiana językowa",
    prompt: "Chcesz ćwiczyć mówienie po polsku. Napisz ogłoszenie na stronę internetową biblioteki miejskiej.",
    points: ["kim jesteś i czego szukasz", "co możesz zaproponować w zamian", "gdzie i jak często chcesz się spotykać", "kontakt"],
    model: "SZUKAM PARTNERA DO WYMIANY JĘZYKOWEJ\n\nMam 25 lat, jestem z Ukrainy i od roku mieszkam w Polsce. Szukam osoby, z którą mogę rozmawiać po polsku. W zamian chętnie pomogę w nauce języka ukraińskiego lub rosyjskiego. Proponuję spotkania raz w tygodniu, na przykład w kawiarni albo w bibliotece, na godzinę: pół godziny po polsku i pół po ukraińsku.\n\nKontakt: e-mail wymiana@przyklad.pl.\nDmytro"
  },
  {
    id: "w18", type: "ogloszenie", title: "Usługi: pomoc w ogrodzie",
    prompt: "Chcesz dorobić w weekendy. Napisz ogłoszenie, w którym proponujesz pomoc w ogrodzie i przy domu.",
    points: ["jakie usługi oferujesz", "jakie masz doświadczenie lub narzędzia", "kiedy jesteś dostępny / dostępna", "cena i kontakt"],
    model: "POMOC W OGRODZIE I PRZY DOMU\n\nOferuję koszenie trawy, przycinanie krzewów, grabienie liści oraz drobne naprawy. Mam własną kosiarkę i narzędzia. Przez trzy lata pracowałem w firmie ogrodniczej, więc wiem, jak dbać o rośliny.\n\nJestem dostępny w soboty i niedziele, a latem także wieczorami.\nCena: od 40 zł za godzinę, zależy od rodzaju pracy.\nKontakt: tel. 500 000 000.\nWasyl"
  },
  {
    id: "w19", type: "ogloszenie", title: "Szukam pracy w sklepie",
    prompt: "Szukasz pracy jako sprzedawca / sprzedawczyni. Napisz krótkie ogłoszenie do internetowego serwisu z ogłoszeniami.",
    points: ["jakiej pracy szukasz", "jakie masz doświadczenie i umiejętności", "od kiedy i w jakich godzinach możesz pracować", "kontakt"],
    model: "SZUKAM PRACY – SPRZEDAWCZYNI\n\nSzukam pracy w sklepie spożywczym lub odzieżowym w Sokołowie Podlaskim. Mam dwa lata doświadczenia jako kasjerka. Jestem miła, punktualna i szybko się uczę. Mówię po polsku, ukraińsku i trochę po angielsku.\n\nMogę zacząć od zaraz. Pracuję na pełny etat lub w systemie zmianowym, także w soboty.\nKontakt: tel. 500 000 000, e-mail praca.anna@przyklad.pl.\nAnna"
  },
  {
    id: "w20", type: "ogloszenie", title: "Wspólny dojazd do pracy",
    prompt: "Codziennie jeździsz samochodem do pracy w innym mieście. Napisz ogłoszenie, że szukasz osób do wspólnych dojazdów.",
    points: ["skąd i dokąd jeździsz", "o której godzinie wyjeżdżasz i wracasz", "ile kosztuje przejazd", "kontakt"],
    model: "WSPÓLNE DOJAZDY DO SIEDLEC\n\nCodziennie od poniedziałku do piątku jeżdżę samochodem z Sokołowa Podlaskiego do Siedlec. Wyjeżdżam o 6:30 spod dworca PKS, a wracam około 16:30. Mam trzy wolne miejsca. Szukam osób, które chcą jeździć regularnie.\n\nKoszt: 10 zł w jedną stronę (dzielimy się kosztami paliwa).\nKontakt: SMS 500 000 000.\nPiotr"
  },
  /* ---------- E-MAILE PRYWATNE ---------- */
  {
    id: "w21", type: "email", title: "Zaproszenie na weekend",
    prompt: "Napisz e-mail do koleżanki / kolegi z innego miasta i zaproś ją / go do siebie na weekend.",
    points: ["zaproś i podaj termin", "napisz, co będziecie robić", "wyjaśnij, jak dojechać", "poproś o odpowiedź"],
    model: "Cześć Kasiu,\n\ndawno się nie widziałyśmy! Może przyjedziesz do mnie w przyszły weekend, 14–15 listopada? Mam dla Ciebie wolny pokój, więc nie musisz szukać hotelu. W sobotę możemy pójść na spacer do parku i na pizzę, a w niedzielę pojechać na targ w Siedlcach. Najłatwiej dojechać pociągiem z Warszawy Wschodniej do Sokołowa, ponieważ autobusy jeżdżą rzadko. Odbiorę Cię z dworca samochodem.\n\nNapisz, czy dasz radę przyjechać!\nŚciskam mocno,\nOla"
  },
  {
    id: "w22", type: "email", title: "Rada dla kolegi",
    prompt: "Kolega z Ukrainy chce przyjechać do Polski do pracy i prosi Cię o radę. Napisz do niego e-mail.",
    points: ["napisz, czy uważasz, że to dobry pomysł", "doradź, jak szukać pracy", "napisz, co jest najtrudniejsze na początku", "zaproponuj pomoc"],
    model: "Cześć Andriju,\n\ndzięki za wiadomość! Uważam, że to dobry pomysł, bo w Polsce łatwo znaleźć pracę, szczególnie w budownictwie i w magazynach. Najlepiej szukać ofert w internecie, ale nie płać nikomu za znalezienie pracy. Na początku najtrudniejszy jest język i urzędy, dlatego zacznij uczyć się polskiego już teraz. Jeśli chcesz, możesz zamieszkać u mnie przez pierwsze dwa tygodnie.\n\nDaj znać, kiedy planujesz przyjechać.\nPozdrawiam,\nSerhij"
  },
  {
    id: "w23", type: "email", title: "Zmiana planów",
    prompt: "Umówiłeś / umówiłaś się z przyjaciółką do kina w piątek, ale musisz zmienić plany. Napisz do niej e-mail.",
    points: ["przeproś i wyjaśnij, co się stało", "zaproponuj nowy termin", "zaproponuj coś dodatkowego, żeby było jej miło"],
    model: "Cześć Marysiu,\n\nprzepraszam, ale w piątek nie mogę iść z Tobą do kina. Mój syn jest chory i ma wysoką gorączkę, więc muszę zostać z nim w domu. Czy możemy pójść w przyszłą środę? Ten film będzie jeszcze grany przez dwa tygodnie. Tym razem ja kupię bilety, a po filmie zapraszam Cię na kawę i ciastko do naszej ulubionej kawiarni.\n\nNapisz, czy środa Ci pasuje.\nBuziaki,\nNatalia"
  },
  {
    id: "w24", type: "email", title: "Nowa praca",
    prompt: "Od miesiąca pracujesz w nowym miejscu. Napisz e-mail do przyjaciela / przyjaciółki i opowiedz o nowej pracy.",
    points: ["gdzie pracujesz i co robisz", "jak wyglądają Twoi koledzy i szef", "co Ci się podoba, a co nie", "zapytaj, co u niego / niej"],
    model: "Cześć Tomku,\n\nod miesiąca pracuję w nowej firmie! To duży magazyn w Siedlcach, gdzie przygotowuję zamówienia dla sklepów. Koledzy są bardzo mili i często pomagają mi, kiedy czegoś nie rozumiem. Szef jest wymagający, ale sprawiedliwy. Podoba mi się, że płacą na czas i mam umowę o pracę. Niestety muszę wstawać o piątej rano, bo zaczynam o szóstej.\n\nA co u Ciebie? Jak tam studia?\nPozdrawiam,\nMaksym"
  },
  {
    id: "w25", type: "email", title: "Gratulacje",
    prompt: "Twoja koleżanka zdała egzamin na prawo jazdy. Napisz do niej e-mail z gratulacjami.",
    points: ["pogratuluj", "napisz, co sam / sama myślisz o egzaminie na prawo jazdy", "zaproponuj, jak to uczcić"],
    model: "Droga Olu,\n\nserdecznie gratuluję zdanego egzaminu na prawo jazdy! Wiem, ile pracy Cię to kosztowało, i jestem z Ciebie bardzo dumna. Ja zdawałam dopiero za trzecim razem, bo zawsze bardzo się stresowałam przy parkowaniu. Dlatego wiem, jaki to sukces. Musimy to uczcić! Może w sobotę pojedziemy razem Twoim samochodem nad jezioro? Ja przygotuję kanapki i ciasto.\n\nJeszcze raz gratuluję i ściskam,\nIrena"
  },
  {
    id: "w26", type: "email", title: "Prośba o pożyczenie",
    prompt: "Chcesz pożyczyć od kolegi namiot na wyjazd. Napisz do niego e-mail.",
    points: ["napisz, po co Ci namiot i na jak długo", "zapytaj, czy może Ci go pożyczyć", "obiecaj, kiedy i w jakim stanie go oddasz", "zaproponuj coś w zamian"],
    model: "Cześć Pawle,\n\nmam do Ciebie prośbę. W przyszłym tygodniu jadę z rodziną na cztery dni nad jezioro i chcemy spać pod namiotem, ale nie mamy własnego. Czy mógłbyś pożyczyć mi swój duży namiot? Oddam go w niedzielę wieczorem, czysty i suchy. Obiecuję, że będę o niego dbać, więc nie musisz się martwić. W zamian mogę pomóc Ci w sobotę przy malowaniu garażu, o którym mówiłeś.\n\nDaj znać, czy to możliwe.\nDzięki z góry i pozdrawiam,\nWiktor"
  },
  {
    id: "w27", type: "email", title: "Relacja z wycieczki",
    prompt: "Wróciłeś / wróciłaś z wycieczki do Krakowa. Napisz e-mail do koleżanki z kursu polskiego.",
    points: ["z kim i jak długo byłeś / byłaś w Krakowie", "co zwiedziłeś / zwiedziłaś", "co Ci się najbardziej podobało", "poleć koleżance to miejsce"],
    model: "Cześć Basiu,\n\nwłaśnie wróciłam z Krakowa! Byłam tam z mężem przez trzy dni. Zwiedziliśmy Wawel, Rynek Główny i Kazimierz, a w niedzielę pojechaliśmy do kopalni soli w Wieliczce. Najbardziej podobała mi się kopalnia, bo pod ziemią są kaplice i rzeźby z soli. Poza tym w Krakowie wszędzie są ładne kawiarnie i jedzenie jest smaczne. Koniecznie musisz tam pojechać, najlepiej wiosną!\n\nPozdrawiam serdecznie,\nOksana"
  },
  {
    id: "w28", type: "email", title: "Odpowiedź na zaproszenie",
    prompt: "Kolega z pracy zaprosił Cię na swój ślub. Napisz do niego e-mail z odpowiedzią.",
    points: ["podziękuj za zaproszenie", "napisz, czy przyjdziesz (i z kim)", "zapytaj o szczegóły (np. prezent, strój)", "złóż życzenia"],
    model: "Cześć Michale,\n\nbardzo dziękuję za zaproszenie na Twój ślub! Oczywiście przyjdę, razem z żoną. Bardzo się cieszymy. Mam jednak kilka pytań: czy macie listę prezentów, czy wolicie pieniądze? I czy na weselu obowiązuje jakiś specjalny strój? Pytam, ponieważ nie wiem, czy muszę mieć garnitur. Już teraz życzę Wam dużo miłości i szczęścia na nowej drodze życia.\n\nDo zobaczenia w czerwcu!\nOleksandr"
  },
  /* ---------- LISTY FORMALNE ---------- */
  {
    id: "w29", type: "formalny", title: "Skarga na hałas",
    prompt: "Od kilku tygodni sąsiedzi z góry robią głośne imprezy w nocy. Napisz list do administracji budynku.",
    points: ["przedstaw się i napisz, w jakiej sprawie piszesz", "opisz problem: kiedy i jak często", "napisz, jakie ma to dla Ciebie skutki", "napisz, czego oczekujesz"],
    model: "Sokołów Podlaski, 12 listopada 2026 r.\n\nSzanowni Państwo,\n\nnazywam się Taras Bondar i mieszkam w lokalu nr 14 przy ulicy Długiej 5. Piszę w sprawie hałasu w budynku.\n\nOd około trzech tygodni sąsiedzi z lokalu nr 18 prawie w każdy piątek i sobotę organizują głośne imprezy. Muzyka gra do drugiej albo trzeciej w nocy. Kilka razy prosiłem sąsiadów o ciszę, ale to nie pomogło.\n\nPracuję na zmiany, dlatego często zaczynam pracę o szóstej rano. Z tego powodu brak snu jest dla mnie dużym problemem. Moje dzieci również nie mogą spać.\n\nBardzo proszę o rozmowę z mieszkańcami lokalu nr 18 i przypomnienie im o ciszy nocnej, która obowiązuje od 22:00 do 6:00.\n\nZ poważaniem\nTaras Bondar"
  },
  {
    id: "w30", type: "formalny", title: "Zgłoszenie na wolontariat",
    prompt: "Przeczytałeś / przeczytałaś, że fundacja szuka wolontariuszy do pomocy przy festynie dla dzieci. Napisz list do fundacji.",
    points: ["gdzie przeczytałeś / przeczytałaś informację", "napisz, dlaczego chcesz pomóc", "napisz o swoim doświadczeniu i umiejętnościach", "napisz, kiedy jesteś dostępny / dostępna i zapytaj o szczegóły"],
    model: "Sokołów Podlaski, 2 maja 2026 r.\n\nSzanowni Państwo,\n\nna stronie internetowej Państwa fundacji przeczytałam, że szukają Państwo wolontariuszy do pomocy przy festynie rodzinnym w czerwcu. Chciałabym zgłosić swoją kandydaturę.\n\nOd dwóch lat mieszkam w Polsce, dlatego chcę zrobić coś dobrego dla lokalnej społeczności. Mam doświadczenie w pracy z dziećmi, ponieważ w Ukrainie pracowałam jako nauczycielka w przedszkolu. Poza tym potrafię malować twarze i prowadzić gry dla dzieci. Jestem cierpliwa i lubię pracę w zespole.\n\nMogę pomagać w weekendy, a także w dni robocze po godzinie 16:00. Chciałabym zapytać, czy przed festynem odbędzie się spotkanie organizacyjne i jakie będą moje obowiązki.\n\nZ góry dziękuję za odpowiedź.\n\nZ poważaniem\nHalyna Petrenko"
  },
  {
    id: "w31", type: "formalny", title: "Rezygnacja z siłowni",
    prompt: "Chcesz zrezygnować z karnetu na siłownię. Napisz list do klubu fitness.",
    points: ["podaj swoje dane i numer umowy", "napisz, że chcesz zrezygnować i od kiedy", "wyjaśnij powód", "zapytaj o zwrot pieniędzy lub warunki rezygnacji"],
    model: "Siedlce, 25 października 2026 r.\n\nSzanowni Państwo,\n\nnazywam się Marek Hrycenko. Od marca jestem klientem Państwa klubu fitness przy ulicy Sportowej 3 (numer umowy 2026/0451). Piszę, ponieważ chciałbym zrezygnować z karnetu z dniem 30 listopada 2026 roku.\n\nPowodem rezygnacji jest zmiana pracy. Od grudnia będę pracował w innym mieście i nie będę mógł regularnie przychodzić na siłownię. Byłem bardzo zadowolony z zajęć i trenerów.\n\nZapłaciłem jednak z góry za cały rok, dlatego chciałbym zapytać, czy mogę otrzymać zwrot pieniędzy za grudzień, styczeń i luty. Proszę również o informację, czy muszę przyjść osobiście, aby podpisać dokumenty.\n\nZ góry dziękuję za odpowiedź.\n\nZ poważaniem\nMarek Hrycenko"
  },
  {
    id: "w32", type: "formalny", title: "Prośba o urlop",
    prompt: "Chcesz wziąć urlop w terminie, który nie był wcześniej planowany. Napisz list do swojego kierownika.",
    points: ["napisz, w jakim terminie chcesz wziąć urlop", "wyjaśnij powód", "napisz, kto Cię zastąpi lub jak zorganizujesz pracę", "poproś o zgodę"],
    model: "Sokołów Podlaski, 3 lutego 2026 r.\n\nSzanowny Panie Kierowniku,\n\nzwracam się z prośbą o udzielenie mi urlopu wypoczynkowego w dniach od 16 do 20 lutego 2026 roku.\n\nWiem, że ten termin nie był wcześniej zaplanowany. Niestety moja mama, która mieszka w Ukrainie, będzie miała operację. Chciałabym być przy niej, ponieważ będzie potrzebowała pomocy po wyjściu ze szpitala.\n\nW związku z tym rozmawiałam już z koleżanką, panią Agnieszką Nowak. Zgodziła się mnie zastąpić w tych dniach. Wszystkie pilne zadania skończę jeszcze w tym tygodniu. Poza tym przed wyjazdem przygotuję dla niej wszystkie potrzebne informacje, a w razie pilnej sprawy będę dostępna pod telefonem.\n\nBardzo proszę o pozytywne rozpatrzenie mojej prośby.\n\nZ poważaniem\nSwitłana Kowal"
  },
  {
    id: "w33", type: "formalny", title: "Reklamacja usługi w hotelu",
    prompt: "Byłeś / byłaś w hotelu, ale pobyt był bardzo nieudany. Napisz list do dyrekcji hotelu.",
    points: ["kiedy i na jak długo przyjechałeś / przyjechałaś", "opisz co najmniej dwa problemy", "napisz, jak zareagował personel", "napisz, czego oczekujesz"],
    model: "Lublin, 18 sierpnia 2026 r.\n\nSzanowni Państwo,\n\nw dniach od 10 do 14 sierpnia przebywałam z rodziną w Państwa hotelu (pokój nr 205, rezerwacja nr 7781). Niestety jestem bardzo niezadowolona z pobytu.\n\nPo pierwsze, w pokoju nie działała klimatyzacja, chociaż w ofercie była informacja, że pokoje są klimatyzowane. Temperatura w nocy przekraczała 28 stopni. Po drugie, pokój nie był sprzątany codziennie, a ręczniki wymieniono tylko raz.\n\nZgłaszałam te problemy w recepcji dwa razy. Pracownicy obiecali pomoc, ale nikt nie przyszedł naprawić klimatyzacji.\n\nW związku z tym proszę o zwrot części kosztów pobytu, czyli 30% ceny. Liczę na szybką odpowiedź.\n\nZ poważaniem\nTetiana Moroz"
  },
  {
    id: "w34", type: "formalny", title: "Zapytanie o mieszkanie",
    prompt: "Znalazłeś / znalazłaś w internecie ogłoszenie o mieszkaniu do wynajęcia. Napisz list do właściciela.",
    points: ["gdzie znalazłeś / znalazłaś ogłoszenie i przedstaw się", "zapytaj o koszty (czynsz, media, kaucja)", "zapytaj o co najmniej dwie inne rzeczy (np. zwierzęta, parking)", "zaproponuj termin obejrzenia mieszkania"],
    model: "Sokołów Podlaski, 7 września 2026 r.\n\nSzanowny Panie,\n\nna portalu z ogłoszeniami znalazłem Pana ofertę wynajmu mieszkania dwupokojowego przy ulicy Wolności. Nazywam się Roman Łysenko, pracuję w Sokołowie jako elektryk, a teraz szukam mieszkania dla siebie i żony.\n\nChciałbym zapytać, ile wynosi czynsz razem z opłatami za media i czy trzeba wpłacić kaucję. Interesuje mnie także, czy mieszkanie jest dostępne od października.\n\nMamy jednak małego, spokojnego psa, dlatego proszę o informację, czy zwierzęta są akceptowane. Chciałbym też wiedzieć, czy przy budynku jest miejsce parkingowe i czy w mieszkaniu jest pralka.\n\nJeśli to możliwe, chętnie obejrzymy mieszkanie w sobotę przed południem.\n\nZ poważaniem\nRoman Łysenko"
  },
  {
    id: "w35", type: "formalny", title: "Zapisanie dziecka na zajęcia",
    prompt: "Chcesz zapisać dziecko na zajęcia pozalekcyjne w domu kultury. Napisz list do dyrektora domu kultury.",
    points: ["napisz, na jakie zajęcia chcesz zapisać dziecko i ile ma lat", "przedstaw krótko dziecko i jego zainteresowania", "zapytaj o terminy i koszty", "zapytaj, jakie dokumenty są potrzebne"],
    model: "Sokołów Podlaski, 1 września 2026 r.\n\nSzanowna Pani Dyrektor,\n\nchciałabym zapisać moją córkę Sofię na zajęcia taneczne, które odbywają się w Państwa domu kultury. Sofia ma dziewięć lat i chodzi do trzeciej klasy szkoły podstawowej.\n\nCórka od dawna interesuje się tańcem, ponieważ w Ukrainie przez dwa lata chodziła na zajęcia z tańca ludowego. Poza tym jest bardzo aktywna i lubi występować przed publicznością.\n\nChciałabym zapytać, w jakie dni i o której godzinie odbywają się zajęcia dla dzieci w jej wieku oraz ile kosztuje miesięczny karnet. Proszę także o informację, jakie dokumenty muszę przygotować i czy potrzebny jest specjalny strój.\n\nZ góry dziękuję za odpowiedź.\n\nZ poważaniem\nKateryna Szewczuk"
  },
  {
    id: "w36", type: "formalny", title: "Opóźniona przesyłka",
    prompt: "Zamówiłeś / zamówiłaś produkt w sklepie internetowym, ale przesyłka nie przyszła na czas. Napisz list do sklepu.",
    points: ["co, kiedy i za ile zamówiłeś / zamówiłaś", "jaki był termin dostawy i co się stało", "jakie problemy to dla Ciebie spowodowało", "czego oczekujesz"],
    model: "Sokołów Podlaski, 28 listopada 2026 r.\n\nSzanowni Państwo,\n\n10 listopada zamówiłem w Państwa sklepie internetowym ekspres do kawy za 899 zł (zamówienie nr 55120). Zapłaciłem od razu przelewem.\n\nNa stronie była informacja, że czas dostawy wynosi trzy dni robocze. Niestety minęło już ponad dwa tygodnie, a przesyłka nadal do mnie nie dotarła. Dwa razy dzwoniłem na infolinię, ale za każdym razem słyszałem, że paczka jest „w drodze”.\n\nNiestety ekspres miał być prezentem urodzinowym dla mojej żony, a jej urodziny były w zeszłą sobotę.\n\nW związku z tym proszę o pilne wysłanie towaru lub zwrot pieniędzy w ciągu siedmiu dni. W przeciwnym razie zwrócę się o pomoc do rzecznika praw konsumentów.\n\nZ poważaniem\nIhor Tkachenko"
  },
  /* ---------- WYPOWIEDZI ---------- */
  {
    id: "w37", type: "wypowiedz", opinion: true, title: "Samochód czy komunikacja miejska?",
    prompt: "Napisz wypowiedź na temat: „Czym lepiej jeździć na co dzień: samochodem czy komunikacją miejską?”",
    points: ["przedstaw swoje zdanie", "podaj co najmniej dwa argumenty", "napisz o argumentach drugiej strony", "podsumuj"],
    model: "Coraz więcej osób w Polsce ma własny samochód. Moim zdaniem jednak w mieście lepiej na co dzień korzystać z komunikacji miejskiej.\n\nPrzede wszystkim autobus lub tramwaj jest tańszy. Miesięczny bilet kosztuje dużo mniej niż paliwo, ubezpieczenie i naprawy samochodu. Poza tym w autobusie można czytać, uczyć się słówek albo odpocząć, a kierowca musi cały czas uważać na drogę. Komunikacja miejska jest też lepsza dla środowiska.\n\nZ drugiej strony samochód daje wolność. Można pojechać, dokąd się chce i kiedy się chce, a z małymi dziećmi albo z dużymi zakupami jest dużo wygodniej. Na wsi bez samochodu jest naprawdę trudno.\n\nPodsumowując, uważam, że w mieście najlepiej jeździć komunikacją miejską, a samochodu używać tylko wtedy, kiedy jest naprawdę potrzebny."
  },
  {
    id: "w38", type: "wypowiedz", title: "Moje miasto",
    prompt: "Opisz miasto lub wieś, w której teraz mieszkasz.",
    points: ["gdzie leży i jak duże jest to miejsce", "co można tam robić i zobaczyć", "co Ci się podoba, a co nie", "czy chcesz tam zostać na dłużej i dlaczego"],
    model: "Od dwóch lat mieszkam w Sokołowie Podlaskim. To małe miasto na Mazowszu, które ma około siedemnastu tysięcy mieszkańców. Leży około stu kilometrów od Warszawy.\n\nW Sokołowie nie ma wielu atrakcji, ale jest tu ładny park, basen, dom kultury i kilka dobrych restauracji. W weekendy lubię spacerować nad rzeką z rodziną. Latem w mieście odbywają się festyny i koncerty.\n\nPodoba mi się, że wszędzie jest blisko, a ludzie są życzliwi. W sklepie albo w przychodni zawsze ktoś pomoże, jeśli czegoś nie rozumiem. Nie podoba mi się natomiast, że autobusy do innych miast jeżdżą rzadko, a wieczorem jest tu trochę nudno.\n\nMimo to chcę zostać tu na dłużej, ponieważ mam stabilną pracę, a moje dzieci lubią swoją szkołę i mają tu przyjaciół."
  },
  {
    id: "w39", type: "wypowiedz", opinion: true, title: "Telefon w życiu dziecka",
    prompt: "Napisz wypowiedź na temat: „Od jakiego wieku dziecko powinno mieć własny smartfon?”",
    points: ["przedstaw swoje zdanie", "podaj zalety posiadania telefonu przez dziecko", "podaj zagrożenia", "podsumuj i podaj przykład z życia"],
    model: "Dzisiaj nawet małe dzieci mają smartfony. Moim zdaniem dziecko powinno dostać własny smartfon dopiero w wieku około dwunastu lat.\n\nOczywiście telefon ma zalety. Rodzice mogą zadzwonić do syna lub córki i wiedzą, gdzie ono jest. Poza tym w telefonie są aplikacje do nauki języków i matematyki.\n\nZ drugiej strony smartfon niesie wiele zagrożeń. Dzieci spędzają przed ekranem kilka godzin dziennie, zamiast bawić się na podwórku i rozmawiać z kolegami. W internecie mogą też trafić na niebezpieczne treści albo osoby. Wielu uczniów źle śpi, bo grają w gry do późna.\n\nMój syn ma dziesięć lat i ma zwykły telefon tylko do dzwonienia. Smartfon dostanie, kiedy pójdzie do siódmej klasy. Podsumowując, uważam, że młodsze dzieci potrzebują przede wszystkim ruchu i rozmowy, a nie ekranu."
  },
  {
    id: "w40", type: "wypowiedz", title: "Święta w moim kraju",
    prompt: "Opisz ważne święto w Twoim kraju i porównaj je z tym, jak obchodzi się je w Polsce.",
    points: ["jakie to święto i kiedy się je obchodzi", "jak je obchodzisz z rodziną", "czym różni się od polskiego zwyczaju", "co lubisz w tym święcie najbardziej"],
    model: "Najważniejszym świętem w mojej rodzinie jest Boże Narodzenie. W Ukrainie wiele osób obchodziło je kiedyś 7 stycznia, ale od niedawna coraz więcej rodzin świętuje 25 grudnia tak jak w Polsce.\n\nW Wigilię cała rodzina spotyka się przy stole. Przygotowujemy dwanaście potraw bez mięsa. Najważniejsza jest kutia, czyli słodka potrawa z pszenicy, maku i miodu. Potem dzieci i młodzież chodzą od domu do domu i śpiewają kolędy.\n\nW Polsce zwyczaje są bardzo podobne, na przykład też jest dwanaście potraw i kolędy. Różnica polega na tym, że Polacy przed kolacją dzielą się opłatkiem i składają sobie życzenia. Bardzo mi się ten zwyczaj podoba.\n\nNajbardziej lubię w tym święcie to, że cała rodzina jest razem, a w domu pachnie piernikami i choinką."
  },
  {
    id: "w41", type: "wypowiedz", opinion: true, title: "Praca zdalna",
    prompt: "Napisz wypowiedź na temat: „Czy praca z domu jest lepsza niż praca w biurze?”",
    points: ["przedstaw swoje zdanie", "napisz o zaletach pracy z domu", "napisz o wadach", "podsumuj"],
    model: "Po pandemii wiele firm pozwala pracownikom pracować zdalnie. Uważam, że to dobre rozwiązanie, ale nie dla każdego.\n\nPrzede wszystkim praca z domu oszczędza czas i pieniądze. Nie trzeba codziennie dojeżdżać do biura, więc rano można dłużej pospać albo zjeść spokojnie śniadanie z dziećmi. Poza tym w mieszkaniu często jest ciszej niż w dużym biurze i łatwiej się skoncentrować.\n\nZ drugiej strony praca zdalna ma też wady. Niektórzy ludzie czują się samotni, bo brakuje im rozmów z kolegami. Trudno też oddzielić pracę od życia prywatnego. Moja siostra pracuje z domu i często odpisuje na e-maile nawet o dziesiątej wieczorem.\n\nPodsumowując, moim zdaniem najlepszy jest system mieszany: dwa lub trzy dni w biurze, a pozostałe w domu."
  },
  {
    id: "w42", type: "wypowiedz", title: "Zdrowy styl życia",
    prompt: "Napisz wypowiedź na temat: „Co robisz, żeby dbać o zdrowie?”",
    points: ["napisz, dlaczego zdrowie jest dla Ciebie ważne", "opisz, jak się odżywiasz", "napisz o aktywności fizycznej i odpoczynku", "napisz, co chcesz zmienić w przyszłości"],
    model: "Zdrowie jest dla mnie bardzo ważne, ponieważ pracuję fizycznie i mam dwoje małych dzieci. Kiedy jestem chory, cała rodzina ma problem.\n\nStaram się jeść zdrowo. Prawie codziennie gotuję w domu, jem dużo warzyw i owoców, a słodycze kupuję tylko w weekendy. Piję dużo wody i rzadko piję kawę. Niestety w pracy czasem nie mam czasu na obiad i jem coś szybko w sklepie.\n\nPoza tym trzy razy w tygodniu chodzę na basen albo jeżdżę na rowerze. Wieczorem staram się nie siedzieć długo przed telefonem i chodzić spać przed jedenastą.\n\nW przyszłości chciałbym rzucić palenie, bo wiem, że to bardzo szkodzi. Chcę też regularnie robić badania, na przykład raz w roku iść do lekarza na kontrolę."
  },
  {
    id: "w43", type: "wypowiedz", opinion: true, title: "Uczyć się w szkole czy samemu?",
    prompt: "Napisz wypowiedź na temat: „Czy lepiej uczyć się języka na kursie, czy samodzielnie?”",
    points: ["przedstaw swoje zdanie", "podaj argumenty za kursem", "podaj argumenty za nauką samodzielną", "podsumuj i opisz, jak Ty się uczysz"],
    model: "Każdy, kto przyjeżdża do Polski, musi zdecydować, jak uczyć się języka. Moim zdaniem najlepsze efekty daje kurs, ale samodzielna nauka też jest bardzo potrzebna.\n\nNa kursie nauczyciel tłumaczy gramatykę i od razu poprawia błędy. Poza tym w grupie można ćwiczyć rozmowę, a regularne zajęcia motywują do nauki. Kiedy płacę za kurs, nie chcę opuszczać lekcji.\n\nZ drugiej strony nauka w szkole językowej jest droga i nie każdy ma czas, żeby chodzić na zajęcia dwa razy w tygodniu. Samodzielnie można uczyć się w dowolnym miejscu i tempie, na przykład z aplikacji, książek albo filmów.\n\nJa łączę obie metody. W soboty chodzę na zajęcia, a w tygodniu codziennie przez piętnaście minut robię ćwiczenia w internecie i czytam polskie wiadomości. Podsumowując, uważam, że kurs daje kierunek, ale sukces zależy od codziennej pracy."
  },
  {
    id: "w44", type: "wypowiedz", title: "Ważna decyzja w moim życiu",
    prompt: "Opisz ważną decyzję, którą podjąłeś / podjęłaś w swoim życiu.",
    points: ["jaka to była decyzja i kiedy ją podjąłeś / podjęłaś", "dlaczego była trudna", "kto Ci pomógł lub doradził", "czy dziś uważasz, że to była dobra decyzja"],
    model: "Najważniejszą decyzją w moim życiu był wyjazd do Polski trzy lata temu.\n\nTa decyzja była dla mnie bardzo trudna, ponieważ w Ukrainie zostawiłam rodziców, przyjaciół i dobrą pracę w banku. Nie znałam języka polskiego i bałam się, że nie znajdę pracy. Dlatego przez pierwsze miesiące bardzo tęskniłam za domem i często płakałam.\n\nNajbardziej pomógł mi mój brat, który mieszkał już w Polsce. Doradził mi, żebym od razu zapisała się na kurs językowy, i pomógł mi znaleźć mieszkanie. Także sąsiadka, pani Halina, często ze mną rozmawiała i poprawiała moje błędy.\n\nDzisiaj uważam, że to była dobra decyzja. Mam stałą pracę w biurze, mówię po polsku coraz lepiej i w grudniu chcę zdać egzamin B1. Nadal tęsknię za rodziną, ale odwiedzam ich dwa razy w roku."
  }
]);
