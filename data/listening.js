/* Zdam B1 — słuchanie. Nagrania czytane przez syntezator mowy (pl-PL).
   lines: [głos, tekst] — głos "A" / "B" (inna wysokość głosu). Liczby zapisane słownie dla lepszej wymowy. */
window.B1 = window.B1 || {};
B1.listening = [
  {
    id: "l1", title: "Komunikat na dworcu",
    lines: [
      ["A", "Uwaga, uwaga. Pociąg osobowy z Siedlec do Warszawy Wschodniej, planowy odjazd godzina czternasta dwadzieścia, odjedzie z toru drugiego przy peronie trzecim. Pociąg jest opóźniony o około piętnaście minut. Za utrudnienia przepraszamy."]
    ],
    qs: [
      { q: "Skąd jedzie pociąg?", o: ["z Siedlec", "z Warszawy", "z Lublina"] },
      { q: "Z którego peronu odjedzie pociąg?", o: ["z trzeciego", "z drugiego", "z piątego"] },
      { q: "Jakie jest opóźnienie?", o: ["około 15 minut", "około 5 minut", "około 20 minut"] }
    ]
  },
  {
    id: "l2", title: "Rozmowa w przychodni",
    lines: [
      ["A", "Przychodnia Zdrowie, dzień dobry. W czym mogę pomóc?"],
      ["B", "Dzień dobry. Chciałbym zapisać się do lekarza rodzinnego. Od wczoraj mam gorączkę i boli mnie gardło."],
      ["A", "Na dzisiaj niestety nie mamy już wolnych terminów. Może być jutro o dziewiątej trzydzieści?"],
      ["B", "Rano pracuję. Czy jest coś po południu?"],
      ["A", "Jutro o szesnastej, u doktor Nowak."],
      ["B", "Dobrze, to poproszę."],
      ["A", "Proszę podać numer PESEL i pamiętać o dowodzie osobistym."]
    ],
    qs: [
      { q: "Co dolega pacjentowi?", o: ["gorączka i ból gardła", "ból zęba", "ból brzucha"] },
      { q: "Kiedy pacjent pójdzie do lekarza?", o: ["jutro o 16:00", "jutro o 9:30", "dzisiaj po południu"] },
      { q: "Co pacjent musi zabrać?", o: ["dowód osobisty", "skierowanie", "wyniki badań"] }
    ]
  },
  {
    id: "l3", title: "Wiadomość na poczcie głosowej",
    lines: [
      ["B", "Cześć Marek, tu Tomek. Słuchaj, w sobotę nie możemy grać w piłkę na boisku przy szkole, bo jest remont. Spotkamy się w hali sportowej na ulicy Długiej, o tej samej godzinie, czyli o dziesiątej. Weź ze sobą buty na zmianę, bo w hali nie można grać w butach z ulicy. Wejście kosztuje dziesięć złotych. Oddzwoń, jak odsłuchasz. Na razie!"]
    ],
    qs: [
      { q: "Dlaczego koledzy nie zagrają na boisku przy szkole?", o: ["bo jest remont", "bo pada deszcz", "bo boisko jest zajęte"] },
      { q: "O której godzinie jest spotkanie?", o: ["o 10:00", "o 11:00", "o 9:00"] },
      { q: "Co Marek musi zabrać?", o: ["buty na zmianę", "piłkę", "ręcznik"] },
      { q: "Ile kosztuje wejście do hali?", o: ["10 zł", "nic, jest bezpłatne", "20 zł"] }
    ]
  },
  {
    id: "l4", title: "Prognoza pogody",
    lines: [
      ["A", "A teraz prognoza pogody na jutro. Na wschodzie kraju, na Podlasiu i Mazowszu, rano gęste mgły i temperatura około zera stopni. W ciągu dnia przejaśnienia, temperatura do pięciu stopni. Na zachodzie przez cały dzień deszcz, a w górach śnieg. Kierowców prosimy o ostrożność, szczególnie rano."]
    ],
    qs: [
      { q: "Jaka będzie pogoda rano na wschodzie kraju?", o: ["mgły", "śnieg", "burze"] },
      { q: "Jaka będzie najwyższa temperatura na wschodzie?", o: ["5 stopni", "0 stopni", "10 stopni"] },
      { q: "Gdzie będzie padać śnieg?", o: ["w górach", "na zachodzie", "na Mazowszu"] }
    ]
  },
  {
    id: "l5", title: "Rozmowa o nowym mieszkaniu",
    lines: [
      ["A", "Słyszałam, że się przeprowadzasz. Znalazłeś już coś?"],
      ["B", "Tak, mieszkanie na Bielanach. Dwa pokoje, czwarte piętro, niestety bez windy."],
      ["A", "A ile płacisz?"],
      ["B", "Dwa tysiące czterysta złotych razem z opłatami. Trochę drogo, ale mam blisko do pracy, piętnaście minut tramwajem."],
      ["A", "A kiedy się wprowadzasz?"],
      ["B", "Od piętnastego stycznia. Pomożesz mi przenieść meble?"],
      ["A", "Jasne, jeśli to będzie weekend."]
    ],
    qs: [
      { q: "Ile pokoi ma nowe mieszkanie?", o: ["dwa", "trzy", "cztery"] },
      { q: "Co jest minusem mieszkania?", o: ["nie ma windy", "jest daleko do pracy", "jest głośno"] },
      { q: "Jak będzie dojeżdżał do pracy?", o: ["tramwajem", "autobusem", "pieszo"] },
      { q: "Kiedy się wprowadza?", o: ["15 stycznia", "4 stycznia", "15 lutego"] }
    ]
  },
  {
    id: "l6", title: "W urzędzie",
    lines: [
      ["B", "Dzień dobry. Chciałabym złożyć wniosek o kartę pobytu. Czy to tutaj?"],
      ["A", "Tak, ale najpierw musi Pani pobrać numerek z automatu przy wejściu. Proszę wybrać literę C."],
      ["B", "A jakie dokumenty są potrzebne?"],
      ["A", "Wypełniony wniosek, cztery aktualne zdjęcia, paszport i potwierdzenie opłaty. Opłatę można zrobić przelewem albo w kasie na pierwszym piętrze."],
      ["B", "Dziękuję. A ile się czeka?"],
      ["A", "Dzisiaj około godziny."]
    ],
    qs: [
      { q: "Co kobieta musi zrobić najpierw?", o: ["pobrać numerek", "zapłacić w kasie", "wypełnić wniosek"] },
      { q: "Ile zdjęć jest potrzebnych?", o: ["cztery", "dwa", "trzy"] },
      { q: "Gdzie jest kasa?", o: ["na pierwszym piętrze", "przy wejściu", "na parterze"] }
    ]
  }
];
