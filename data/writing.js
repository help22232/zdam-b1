/* Zdam B1 — pisanie. Szablony, zadania, wzory odpowiedzi i bank zwrotów — treści autorskie.
   Objętość (words) to orientacyjny cel w trenażerze, nie oficjalny limit. */
window.B1 = window.B1 || {};

B1.writingTypes = {
  ogloszenie: {
    name: "Ogłoszenie", size: "short", words: [40, 70], minutes: 15,
    about: {
      ua: "Коротке оголошення: продам, шукаю, загубив, пропоную. Головне — виконати ВСІ пункти завдання і дати контакт.",
      ru: "Короткое объявление: продам, ищу, потерял, предлагаю. Главное — выполнить ВСЕ пункты задания и дать контакт."
    },
    parts: [
      { pl: "Nagłówek", ua: "Заголовок великими літерами: що ви робите.", ru: "Заголовок крупно: что вы делаете.", ex: "SPRZEDAM ROWER / SZUKAM WSPÓŁLOKATORA / ZGUBIONO KLUCZE" },
      { pl: "Opis", ua: "Що саме: вигляд, стан, де, коли. 2–3 речення.", ru: "Что именно: вид, состояние, где, когда. 2–3 предложения.", ex: "Sprzedam rower górski w bardzo dobrym stanie. Ma dwa lata…" },
      { pl: "Warunki", ua: "Ціна, термін, вимоги, винагорода.", ru: "Цена, срок, требования, вознаграждение.", ex: "Cena: 600 zł (do negocjacji)." },
      { pl: "Kontakt", ua: "Як і коли зв'язатися + ім'я.", ru: "Как и когда связаться + имя.", ex: "Kontakt: tel. 500 000 000, najlepiej po 17:00. Paweł" }
    ],
    skeleton: "SPRZEDAM / SZUKAM / ZGUBIONO …\n\n… w bardzo dobrym stanie. …\n\nCena: … zł (do negocjacji).\nKontakt: …, najlepiej po godzinie …\n…",
    checks: [
      { ua: "Є заголовок (SPRZEDAM / SZUKAM / ZGUBIONO…)", ru: "Есть заголовок (SPRZEDAM / SZUKAM / ZGUBIONO…)" },
      { ua: "Є контакт і коли дзвонити / писати", ru: "Есть контакт и когда звонить / писать" }
    ]
  },
  email: {
    name: "E-mail / list prywatny", size: "short", words: [50, 80], minutes: 15,
    about: {
      ua: "Неформальний лист другу: запрошення, вибачення, подяка, новини. Звертання на «ty».",
      ru: "Неформальное письмо другу: приглашение, извинение, благодарность, новости. Обращение на «ty»."
    },
    parts: [
      { pl: "Powitanie", ua: "Звертання з комою, далі текст з маленької літери.", ru: "Обращение с запятой, дальше текст с маленькой буквы.", ex: "Cześć Kasiu, / Drogi Marku," },
      { pl: "Cel listu", ua: "Одразу: навіщо пишете.", ru: "Сразу: зачем пишете.", ex: "piszę, bo chcę Cię zaprosić na…" },
      { pl: "Szczegóły", ua: "Усі пункти завдання: коли, де, чому, що взяти.", ru: "Все пункты задания: когда, где, почему, что взять.", ex: "Impreza będzie w sobotę o 18:00 u mnie w domu…" },
      { pl: "Zakończenie i podpis", ua: "Прохання відповісти + прощання + ім'я.", ru: "Просьба ответить + прощание + имя.", ex: "Daj znać, czy przyjdziesz! Pozdrawiam, Ola" }
    ],
    skeleton: "Cześć …,\n\npiszę, bo …\n\n…\n\nDaj znać, czy …!\nPozdrawiam serdecznie,\n…",
    checks: [
      { ua: "Неформальне звертання (Cześć / Drogi…) і прощання (Pozdrawiam / Ściskam)", ru: "Неформальное обращение (Cześć / Drogi…) и прощание (Pozdrawiam / Ściskam)" },
      { ua: "Ty / Cię / Ci — у листі можна з великої літери з ввічливості", ru: "Ty / Cię / Ci — в письме можно с большой буквы из вежливости" }
    ]
  },
  formalny: {
    name: "List formalny", size: "long", words: [100, 150], minutes: 30,
    about: {
      ua: "Офіційний лист: скарга (reklamacja), запит інформації, прохання. Тільки Pan / Pani / Państwo + дієслово у 3-й особі.",
      ru: "Официальное письмо: жалоба (reklamacja), запрос информации, просьба. Только Pan / Pani / Państwo + глагол в 3-м лице."
    },
    parts: [
      { pl: "Miejscowość, data", ua: "Праворуч угорі.", ru: "Справа вверху.", ex: "Sokołów Podlaski, 5 grudnia 2026 r." },
      { pl: "Zwrot grzecznościowy", ua: "Ніколи не «Cześć»!", ru: "Никогда не «Cześć»!", ex: "Szanowni Państwo, / Szanowna Pani," },
      { pl: "Cel", ua: "У якій справі пишете.", ru: "По какому делу пишете.", ex: "piszę w sprawie… / zwracam się z prośbą o…" },
      { pl: "Rozwinięcie", ua: "Факти: що, коли, де сталося, чого ви хочете. Кожен пункт завдання — окремий абзац.", ru: "Факты: что, когда, где случилось, чего вы хотите. Каждый пункт задания — отдельный абзац.", ex: "Dnia 10 listopada kupiłem w Państwa sklepie… Niestety już po tygodniu…" },
      { pl: "Oczekiwanie", ua: "Чітко: що ви просите.", ru: "Чётко: что вы просите.", ex: "Proszę o wymianę towaru na nowy lub zwrot pieniędzy." },
      { pl: "Zakończenie", ua: "Подяка + Z poważaniem + ім'я і прізвище.", ru: "Благодарность + Z poważaniem + имя и фамилия.", ex: "Z góry dziękuję za odpowiedź. Z poważaniem, Jan Kowalski" }
    ],
    skeleton: "…, … 2026 r.\n\nSzanowni Państwo,\n\npiszę w sprawie …\n\n…\n\nW związku z tym proszę o …\n\nZ góry dziękuję za odpowiedź.\nZ poważaniem\n…",
    checks: [
      { ua: "Szanowni Państwo / Szanowna Pani… і Z poważaniem — без «Cześć» і «Pozdrawiam»", ru: "Szanowni Państwo / Szanowna Pani… и Z poważaniem — без «Cześć» и «Pozdrawiam»" },
      { ua: "Pan / Pani / Państwo з великої літери, дієслово у 3-й особі (Czy mogliby Państwo…)", ru: "Pan / Pani / Państwo с большой буквы, глагол в 3-м лице (Czy mogliby Państwo…)" },
      { ua: "Чітко написано, чого я хочу (proszę o…)", ru: "Чётко написано, чего я хочу (proszę o…)" }
    ]
  },
  wypowiedz: {
    name: "Wypowiedź (opinia / opis)", size: "long", words: [100, 150], minutes: 30,
    about: {
      ua: "Висловлення на тему: думка з аргументами, опис події чи досвіду. Структура: вступ → 2 аргументи з прикладами → підсумок.",
      ru: "Высказывание на тему: мнение с аргументами, описание события или опыта. Структура: вступление → 2 аргумента с примерами → итог."
    },
    parts: [
      { pl: "Wstęp i teza", ua: "1–2 речення: тема + ваша думка.", ru: "1–2 предложения: тема + ваше мнение.", ex: "Wiele osób uważa, że… Moim zdaniem…" },
      { pl: "Argument 1 + przykład", ua: "Przede wszystkim… Na przykład…", ru: "Przede wszystkim… Na przykład…", ex: "Przede wszystkim w małym mieście jest taniej. Na przykład…" },
      { pl: "Argument 2 + przykład", ua: "Poza tym… / Z drugiej strony…", ru: "Poza tym… / Z drugiej strony…", ex: "Poza tym ludzie się znają i chętnie sobie pomagają…" },
      { pl: "Podsumowanie", ua: "Повторіть думку іншими словами.", ru: "Повторите мнение другими словами.", ex: "Podsumowując, uważam, że…" }
    ],
    skeleton: "Wiele osób uważa, że … Moim zdaniem …\n\nPrzede wszystkim … Na przykład …\n\nPoza tym … Dlatego …\n\nPodsumowując, uważam, że …",
    checks: [
      { ua: "Є вступ з моєю думкою (Moim zdaniem / Uważam, że…)", ru: "Есть вступление с моим мнением (Moim zdaniem / Uważam, że…)" },
      { ua: "Два аргументи, кожен з прикладом (Na przykład…)", ru: "Два аргумента, каждый с примером (Na przykład…)" },
      { ua: "Є підсумок (Podsumowując…)", ru: "Есть итог (Podsumowując…)" }
    ]
  }
};

B1.writingTasks = [
  /* ---------- OGŁOSZENIA ---------- */
  {
    id: "w01", type: "ogloszenie", title: "Sprzedaż roweru",
    prompt: "Wyjeżdżasz na rok za granicę i chcesz sprzedać swój rower. Napisz ogłoszenie, które powiesisz w sklepie na osiedlu.",
    points: ["jaki to rower i w jakim jest stanie", "dlaczego go sprzedajesz", "ile kosztuje", "jak można się z Tobą skontaktować"],
    model: "SPRZEDAM ROWER\n\nSprzedam rower miejski marki Kross, kolor niebieski. Rower ma dwa lata i jest w bardzo dobrym stanie – w zeszłym miesiącu wymieniłem opony. Sprzedaję go, ponieważ za tydzień wyjeżdżam na rok do Niemiec.\n\nCena: 700 zł (do negocjacji).\nKontakt: tel. 500 000 000, najlepiej po godzinie 17:00.\nPaweł"
  },
  {
    id: "w02", type: "ogloszenie", title: "Szukam współlokatora",
    prompt: "Wynajmujesz mieszkanie i szukasz osoby, która zamieszka z Tobą. Napisz ogłoszenie do internetowej grupy Twojego miasta.",
    points: ["gdzie jest mieszkanie i jaki pokój oferujesz", "jakiej osoby szukasz", "ile kosztuje pokój", "od kiedy pokój jest wolny i jak się skontaktować"],
    model: "SZUKAM WSPÓŁLOKATORA / WSPÓŁLOKATORKI\n\nMam do wynajęcia pokój w dwupokojowym mieszkaniu blisko centrum, 5 minut od przystanku autobusowego. Pokój jest umeblowany i ma balkon. Szukam spokojnej, niepalącej osoby, która pracuje lub studiuje.\n\nCena: 800 zł + media.\nPokój jest wolny od 1 stycznia.\nZainteresowanych proszę o wiadomość prywatną.\nMarta"
  },
  {
    id: "w03", type: "ogloszenie", title: "Zgubione klucze",
    prompt: "Wczoraj zgubiłeś / zgubiłaś klucze. Napisz ogłoszenie, które powiesisz na tablicy przy wejściu do parku.",
    points: ["co i gdzie zgubiłeś / zgubiłaś", "kiedy to się stało", "jak wyglądają klucze", "nagroda i kontakt"],
    model: "ZGUBIONO KLUCZE!\n\nWczoraj, w sobotę, około godziny 15:00 zgubiłam klucze w parku miejskim, prawdopodobnie przy placu zabaw albo na ławce przy fontannie. Są to trzy klucze na czerwonym breloczku w kształcie serca.\n\nDla znalazcy nagroda!\nBardzo proszę o kontakt: tel. 500 000 000 (o każdej porze).\nAnna"
  },
  {
    id: "w04", type: "ogloszenie", title: "Lekcje języka ukraińskiego",
    prompt: "Chcesz dorobić, ucząc języka ukraińskiego. Napisz ogłoszenie do lokalnej gazety.",
    points: ["co oferujesz i dla kogo", "jakie masz doświadczenie", "gdzie i kiedy mogą odbywać się lekcje", "cena i kontakt"],
    model: "LEKCJE JĘZYKA UKRAIŃSKIEGO\n\nJestem rodowitą Ukrainką. Oferuję lekcje języka ukraińskiego dla dzieci i dorosłych, na każdym poziomie. Od trzech lat uczę online, a wcześniej pracowałam w szkole językowej w Kijowie. Lekcje mogą odbywać się u mnie, u ucznia albo przez internet, od poniedziałku do soboty.\n\nCena: 60 zł za 60 minut. Pierwsza lekcja gratis!\nKontakt: e-mail ukrainski.lekcje@przyklad.pl\nOksana"
  },
  /* ---------- E-MAILE PRYWATNE ---------- */
  {
    id: "w05", type: "email", title: "Zaproszenie na urodziny",
    prompt: "W przyszłą sobotę masz urodziny. Napisz e-mail do kolegi / koleżanki z kursu polskiego i zaproś go / ją na przyjęcie.",
    points: ["z jakiej okazji jest przyjęcie", "kiedy i gdzie się odbędzie", "kto jeszcze przyjdzie", "co kolega / koleżanka może przynieść"],
    model: "Cześć Marto,\n\nw przyszłą sobotę kończę trzydzieści lat i z tej okazji organizuję małe przyjęcie. Zapraszam Cię serdecznie! Spotykamy się o 18:00 u mnie w domu, na ulicy Lipowej 5. Przyjdą też Ola i Tomek z naszego kursu oraz kilku moich kolegów z pracy. Jeśli chcesz, możesz przynieść jakąś sałatkę albo ciasto, ale to nie jest konieczne.\n\nDaj znać, czy przyjdziesz!\nPozdrawiam serdecznie,\nAndrij"
  },
  {
    id: "w06", type: "email", title: "Przeprosiny — nie przyjdę",
    prompt: "Obiecałeś / obiecałaś koledze, że pomożesz mu w przeprowadzce w sobotę, ale nie możesz. Napisz do niego e-mail.",
    points: ["przeproś i napisz, że nie możesz przyjść", "wyjaśnij dlaczego", "zaproponuj inną pomoc lub inny termin"],
    model: "Cześć Tomku,\n\nbardzo Cię przepraszam, ale niestety nie mogę pomóc Ci w sobotę w przeprowadzce. Wczoraj szef poprosił mnie, żebym w ten weekend przyszedł do pracy, bo dwóch kolegów jest chorych. Nie mogłem odmówić. Mogę za to przyjść w niedzielę po południu i pomóc Ci złożyć meble albo rozpakować kartony. Mam też samochód, więc mogę przewieźć mniejsze rzeczy.\n\nJeszcze raz przepraszam!\nŚciskam,\nMaksym"
  },
  {
    id: "w07", type: "email", title: "Podziękowanie za pomoc",
    prompt: "Sąsiadka opiekowała się Twoim psem, kiedy byłeś / byłaś w szpitalu. Napisz do niej krótki list z podziękowaniem.",
    points: ["podziękuj za pomoc", "napisz, jak się teraz czujesz", "zaproponuj, jak możesz się odwdzięczyć"],
    model: "Droga Pani Krystyno,\n\nbardzo dziękuję za opiekę nad Burkiem, kiedy byłam w szpitalu. Wiem, że to był dla Pani dodatkowy obowiązek, i jestem naprawdę wdzięczna. Czuję się już dużo lepiej, a lekarz pozwolił mi wrócić do pracy od poniedziałku. Chciałabym zaprosić Panią w niedzielę na obiad i domowe ciasto. Jeśli kiedyś będzie Pani potrzebowała pomocy, na przykład przy zakupach, proszę dać mi znać.\n\nSerdecznie pozdrawiam,\nIryna"
  },
  /* ---------- LISTY FORMALNE ---------- */
  {
    id: "w08", type: "formalny", title: "Reklamacja butów",
    prompt: "Dwa tygodnie temu kupiłeś / kupiłaś buty w sklepie internetowym. Okazało się, że mają wadę. Napisz reklamację do sklepu.",
    points: ["kiedy i co kupiłeś / kupiłaś", "na czym polega wada", "jak to wpłynęło na Ciebie", "czego oczekujesz od sklepu"],
    model: "Sokołów Podlaski, 20 listopada 2026 r.\n\nSzanowni Państwo,\n\npiszę w sprawie reklamacji butów zimowych, które kupiłem w Państwa sklepie internetowym 5 listopada (numer zamówienia 12345). Buty kosztowały 289 zł.\n\nNiestety już po tygodniu noszenia lewy but zaczął przemakać, a podeszwa odkleiła się z przodu. Używałem butów zgodnie z przeznaczeniem, tylko w drodze do pracy. Z tego powodu przez kilka dni musiałem chodzić w mokrych butach i przeziębiłem się.\n\nW związku z tym proszę o zwrot pieniędzy na moje konto bankowe. Jeśli nie jest to możliwe, zgadzam się na wymianę butów na nową parę. Do listu dołączam zdjęcia uszkodzonego buta oraz dowód zakupu.\n\nZ góry dziękuję za szybką odpowiedź.\n\nZ poważaniem\nJan Kowalczuk"
  },
  {
    id: "w09", type: "formalny", title: "Pytanie o kurs językowy",
    prompt: "Przeczytałeś / przeczytałaś ogłoszenie szkoły językowej o kursie przygotowującym do egzaminu B1. Napisz list do szkoły z prośbą o informacje.",
    points: ["gdzie przeczytałeś / przeczytałaś ogłoszenie i dlaczego piszesz", "zapytaj o terminy i cenę kursu", "zapytaj o liczbę osób w grupie", "napisz, w jakich godzinach możesz się uczyć"],
    model: "Siedlce, 3 października 2026 r.\n\nSzanowni Państwo,\n\nprzeczytałam na Państwa stronie internetowej ogłoszenie o kursie przygotowującym do egzaminu certyfikatowego z języka polskiego na poziomie B1. Jestem zainteresowana tym kursem, ponieważ w grudniu chcę zdawać egzamin.\n\nChciałabym zapytać, kiedy zaczyna się kurs, ile trwa i ile kosztuje. Czy można płacić w ratach? Interesuje mnie również, ile osób jest w grupie, ponieważ najbardziej zależy mi na ćwiczeniu mówienia i pisania. Chciałabym również wiedzieć, czy pod koniec kursu jest egzamin próbny.\n\nPracuję od poniedziałku do piątku do godziny 16:00, dlatego mogę uczyć się tylko wieczorem albo w soboty.\n\nByłabym wdzięczna za odpowiedź.\n\nZ poważaniem\nOlena Kowalenko"
  },
  /* ---------- WYPOWIEDZI ---------- */
  {
    id: "w10", type: "wypowiedz", title: "Małe miasto czy duże miasto?",
    prompt: "Napisz wypowiedź na temat: „Czy lepiej mieszkać w małym mieście, czy w dużym?”",
    points: ["przedstaw swoje zdanie", "podaj co najmniej dwa argumenty", "podaj przykłady z własnego życia", "podsumuj"],
    model: "Wiele osób uważa, że w dużym mieście żyje się lepiej, bo jest tam więcej pracy i rozrywki. Moim zdaniem jednak małe miasto ma więcej zalet.\n\nPrzede wszystkim życie w małym mieście jest tańsze i spokojniejsze. Na przykład w Sokołowie płacę za mieszkanie dużo mniej niż mój kolega w Warszawie, a do pracy chodzę pieszo, więc nie tracę czasu w korkach.\n\nPoza tym w małym mieście ludzie lepiej się znają i chętnie sobie pomagają. Kiedy przyjechałem do Polski, sąsiedzi pomogli mi znaleźć lekarza i pokazali, gdzie są najlepsze sklepy. Z drugiej strony, jeśli ktoś chce chodzić do teatru albo na koncerty, musi czasem pojechać do większego miasta.\n\nPodsumowując, uważam, że dla rodziny i dla osób, które cenią spokój, małe miasto jest lepszym wyborem."
  },
  {
    id: "w11", type: "wypowiedz", title: "Nauka języka przez internet",
    prompt: "Napisz wypowiedź na temat: „Czy można nauczyć się języka obcego tylko przez internet?”",
    points: ["przedstaw swoje zdanie", "napisz o zaletach nauki przez internet", "napisz o wadach", "podsumuj i podaj własny przykład"],
    model: "Dzisiaj coraz więcej osób uczy się języków przez internet. Uważam, że to bardzo dobra metoda, ale nie wystarczy, żeby dobrze mówić.\n\nPrzede wszystkim internet daje dużo możliwości. Można oglądać filmy, słuchać podcastów i robić ćwiczenia w aplikacjach, kiedy ma się wolną chwilę, na przykład w autobusie. Poza tym wiele materiałów jest bezpłatnych.\n\nZ drugiej strony w internecie trudno ćwiczyć prawdziwą rozmowę. Aplikacja nie poprawi błędów w mówieniu tak dobrze jak nauczyciel albo kolega. Ja na przykład dużo czytałem po polsku w internecie, ale zacząłem swobodnie mówić dopiero wtedy, gdy codziennie rozmawiałem z kolegami w pracy.\n\nPodsumowując, internet bardzo pomaga w nauce, ale najlepiej łączyć go z rozmowami z ludźmi."
  },
  {
    id: "w12", type: "wypowiedz", title: "Mój najlepszy dzień w Polsce",
    prompt: "Opisz dzień w Polsce, który szczególnie zapamiętałeś / zapamiętałaś.",
    points: ["kiedy to było i gdzie", "co się wydarzyło", "kto był z Tobą", "dlaczego ten dzień był dla Ciebie ważny"],
    model: "Najlepszy dzień w Polsce przeżyłam w czerwcu ubiegłego roku, kiedy pierwszy raz pojechałam nad Bałtyk.\n\nRazem z mężem i córką wyjechaliśmy wcześnie rano pociągiem z Warszawy do Gdańska. Najpierw spacerowaliśmy po Starym Mieście i jedliśmy lody na Długim Targu. Potem pojechaliśmy tramwajem na plażę w Brzeźnie. Woda była zimna, ale córka i tak weszła do morza i była bardzo szczęśliwa. Wieczorem zjedliśmy rybę w małej restauracji niedaleko plaży.\n\nTen dzień był dla mnie ważny, ponieważ po raz pierwszy od przyjazdu do Polski poczułam się jak na prawdziwych wakacjach, a nie tylko jak w pracy. Poza tym sama kupiłam bilety i rozmawiałam z kelnerem po polsku. Wtedy zrozumiałam, że naprawdę robię postępy."
  }
];

/* Bank zwrotów: kliknięcie wstawia zwrot do tekstu */
B1.phrases = [
  { group: { ua: "Початок листа", ru: "Начало письма" }, items: [
    ["Cześć …,", "Привіт …,", "Привет …,"],
    ["Droga Kasiu, / Drogi Marku,", "Дорога Касю / Дорогий Марку", "Дорогая Кася / Дорогой Марек"],
    ["Szanowni Państwo,", "Шановні пані та панове (офіц.)", "Уважаемые дамы и господа (офиц.)"],
    ["Szanowna Pani, / Szanowny Panie,", "Шановна пані / Шановний пане (офіц.)", "Уважаемая госпожа / Уважаемый господин (офиц.)"]
  ]},
  { group: { ua: "Мета листа", ru: "Цель письма" }, items: [
    ["piszę, bo chcę Ci powiedzieć, że …", "пишу, бо хочу сказати тобі, що …", "пишу, потому что хочу сказать тебе, что …"],
    ["dziękuję za Twój list.", "дякую за твій лист.", "спасибо за твоё письмо."],
    ["przepraszam, że tak długo nie pisałem / nie pisałam.", "вибач, що так довго не писав / не писала.", "извини, что так долго не писал / не писала."],
    ["piszę w sprawie …", "пишу щодо … (офіц.)", "пишу по поводу … (офиц.)"],
    ["zwracam się z prośbą o …", "звертаюся з проханням про … (офіц.)", "обращаюсь с просьбой о … (офиц.)"],
    ["przeczytałem / przeczytałam ogłoszenie na …", "я прочитав / прочитала оголошення на …", "я прочитал / прочитала объявление на …"],
    ["chciałbym / chciałabym złożyć reklamację …", "хотів би / хотіла б подати скаргу …", "хотел бы / хотела бы подать рекламацию …"]
  ]},
  { group: { ua: "Прохання, пропозиція", ru: "Просьба, предложение" }, items: [
    ["Czy mógłbyś / mogłabyś …?", "Чи міг би ти / могла б ти …?", "Не мог бы ты / могла бы ты …?"],
    ["Czy mogliby Państwo …?", "Чи не могли б Ви … (офіц.)", "Не могли бы Вы … (офиц.)"],
    ["Uprzejmie proszę o …", "Ввічливо прошу про …", "Вежливо прошу о …"],
    ["Może spotkamy się w …?", "Може, зустрінемося в …?", "Может, встретимся в …?"],
    ["Co powiesz na …?", "Що скажеш про …?", "Как насчёт …?"],
    ["Byłbym wdzięczny / Byłabym wdzięczna za …", "Я був би вдячний / була б вдячна за …", "Я был бы благодарен / была бы благодарна за …"]
  ]},
  { group: { ua: "Вибачення, подяка, відмова", ru: "Извинение, благодарность, отказ" }, items: [
    ["Bardzo przepraszam, ale niestety nie mogę …", "Дуже перепрошую, але, на жаль, не можу …", "Очень извиняюсь, но, к сожалению, не могу …"],
    ["Bardzo Ci dziękuję za …", "Щиро дякую тобі за …", "Большое тебе спасибо за …"],
    ["To bardzo miło z Twojej strony.", "Це дуже мило з твого боку.", "Это очень мило с твоей стороны."],
    ["Niestety …", "На жаль …", "К сожалению …"],
    ["Mam nadzieję, że …", "Сподіваюся, що …", "Надеюсь, что …"]
  ]},
  { group: { ua: "Думка, аргументи", ru: "Мнение, аргументы" }, items: [
    ["Moim zdaniem …", "На мою думку …", "По-моему …"],
    ["Uważam, że …", "Я вважаю, що …", "Я считаю, что …"],
    ["Wydaje mi się, że …", "Мені здається, що …", "Мне кажется, что …"],
    ["Wiele osób uważa, że …", "Багато людей вважає, що …", "Многие считают, что …"],
    ["Nie zgadzam się z tym, że …", "Я не згоден / не згодна з тим, що …", "Я не согласен / не согласна с тем, что …"],
    ["Przede wszystkim …", "Перш за все …", "Прежде всего …"],
    ["Poza tym …", "Крім того …", "Кроме того …"],
    ["Na przykład …", "Наприклад …", "Например …"],
    ["Z jednej strony …, z drugiej strony …", "З одного боку …, з іншого боку …", "С одной стороны …, с другой стороны …"],
    ["Plusem / Minusem jest to, że …", "Плюсом / Мінусом є те, що …", "Плюсом / Минусом является то, что …"],
    ["Dlatego …", "Тому …", "Поэтому …"],
    ["Podsumowując, …", "Підсумовуючи, …", "Подводя итог, …"]
  ]},
  { group: { ua: "Сполучники і час", ru: "Связки и время" }, items: [
    ["ponieważ", "оскільки", "поскольку"],
    ["ale / jednak", "але / однак", "но / однако"],
    ["więc", "отже, тому", "так что, поэтому"],
    ["chociaż", "хоча", "хотя"],
    ["Najpierw …, potem …, na końcu …", "Спочатку …, потім …, наприкінці …", "Сначала …, потом …, в конце …"],
    ["W zeszłym tygodniu / roku …", "Минулого тижня / року …", "На прошлой неделе / В прошлом году …"],
    ["Kiedy …, to …", "Коли …, то …", "Когда …, то …"]
  ]},
  { group: { ua: "Оголошення", ru: "Объявление" }, items: [
    ["Sprzedam … w bardzo dobrym stanie.", "Продам … у дуже гарному стані.", "Продам … в очень хорошем состоянии."],
    ["Cena do negocjacji.", "Ціна договірна.", "Цена договорная."],
    ["Szukam …", "Шукаю …", "Ищу …"],
    ["Zgubiono … / Znaleziono …", "Загублено … / Знайдено …", "Потеряно … / Найдено …"],
    ["Dla znalazcy nagroda!", "Винагорода тому, хто знайде!", "Нашедшему — вознаграждение!"],
    ["Kontakt: …, najlepiej po godzinie …", "Контакт: …, найкраще після …", "Контакт: …, лучше всего после …"],
    ["Zainteresowanych proszę o kontakt.", "Зацікавлених прошу зв'язатися.", "Заинтересованных прошу связаться."]
  ]},
  { group: { ua: "Кінець листа", ru: "Конец письма" }, items: [
    ["Czekam na odpowiedź.", "Чекаю на відповідь.", "Жду ответа."],
    ["Daj znać, czy …!", "Дай знати, чи …!", "Дай знать, …ли!"],
    ["Pozdrawiam serdecznie,", "Щиро вітаю,", "С сердечным приветом,"],
    ["Ściskam,", "Обіймаю,", "Обнимаю,"],
    ["Do zobaczenia!", "До зустрічі!", "До встречи!"],
    ["Z góry dziękuję za odpowiedź.", "Заздалегідь дякую за відповідь.", "Заранее спасибо за ответ."],
    ["Z poważaniem", "З повагою (офіц.)", "С уважением (офиц.)"]
  ]}
];

/* Lista kontrolna dla każdego tekstu */
B1.commonChecks = [
  { ua: "Виконано ВСІ пункти завдання (за кожен пункт — бали!)", ru: "Выполнены ВСЕ пункты задания (за каждый пункт — баллы!)" },
  { ua: "Стиль один: або «ty» (друг), або «Pan / Pani» (офіційно) — не змішувати", ru: "Стиль один: либо «ty» (друг), либо «Pan / Pani» (официально) — не смешивать" },
  { ua: "Закінчення після прийменників: w + miejscownik, do / bez / od + dopełniacz, z + narzędnik", ru: "Окончания после предлогов: w + miejscownik, do / bez / od + dopełniacz, z + narzędnik" },
  { ua: "Минулий час — правильний рід: byłem / byłam, pisałem / pisałam", ru: "Прошедшее время — правильный род: byłem / byłam, pisałem / pisałam" },
  { ua: "Є сполучники: ponieważ, ale, więc, poza tym, dlatego", ru: "Есть связки: ponieważ, ale, więc, poza tym, dlatego" },
  { ua: "Перевірено ą / ę / ó / ż / rz / ch і великі літери на початку речень", ru: "Проверены ą / ę / ó / ż / rz / ch и заглавные буквы в начале предложений" },
  { ua: "Немає калек з української / російської (напр. «*na protiv*», «*ja dumam*»)", ru: "Нет калек с русского / украинского (напр. «*na protiv*», «*ja dumam*»)" }
];
