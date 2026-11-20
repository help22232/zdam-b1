"use strict";
/* Zdam B1 — aplikacja (bloki testów, odtwarzacz MP3, pisanie z LanguageTool). */
const VER = "3";
const T = {
  ua: {
    nav_home: "Головна", nav_g: "Граматика", nav_r: "Читання", nav_l: "Аудіювання", nav_w: "Письмо",
    hero_t: "Підготовка до іспиту з польської B1", hero_p: "Понад 4000 завдань: граматика, читання, аудіювання з живими голосами і письмо з перевіркою помилок. Вчися блоками по 15–20 питань.",
    days: "днів до іспиту", exam_date: "Письмова частина: 5 грудня 2026", today: "Порада на сьогодні",
    sec_g: "Граматика", sec_r: "Читання", sec_l: "Аудіювання", sec_w: "Письмо",
    sec_g_d: "Відмінки, вид дієслова, числівники, прийменники, займенники. Пояснення до кожної відповіді.",
    sec_r_d: "Оголошення, листи, комунікати, правила, історії. Вибір відповіді та «правда / неправда».",
    sec_l_d: "Записи з живими польськими голосами. Як на іспиті — максимум 2 прослуховування.",
    sec_w_d: "Шаблони, банк фраз, таймер і справжня перевірка орфографії, граматики та структури.",
    questions: "питань", blocks: "блоків", block: "Блок", done_blocks: "пройдено", start: "Почати", next_block: "Наступний блок →",
    continue_: "Продовжити", all_blocks: "Усі блоки", mistakes: "Мої помилки", mistakes_n: "помилок у банку", mistakes_empty: "Помилок поки немає — так тримати!",
    finish: "Перевірити відповіді", time_up: "Час вийшов — перевіряємо!", answered: "відповідей", score: "Результат",
    again: "Пройти ще раз", back: "До блоків", correct: "Правильно", wrong: "Помилка", right_is: "Правильна відповідь:", no_answer: "Без відповіді.",
    tf_true: "Prawda", tf_false: "Fałsz", in_text: "У тексті:", in_rec: "У записі:",
    play: "▶ Слухати", playing: "Звучить…", plays_left: "Залишилось прослуховувань", no_plays: "Прослуховування вичерпано", replay: "▶ Слухати ще раз",
    transcript: "Текст запису", loading: "Завантаження…", load_err: "Не вдалося завантажити дані. Перевір інтернет і онови сторінку.",
    pass: "Зараховано (≥ 60%)", fail: "Нижче 60% — повтори цей блок пізніше", best: "найкраще",
    w_title: "Письмо", w_p: "Обери завдання. Подивись шаблон, пиши з таймером, а потім натисни «Перевірити текст» — отримаєш список помилок і орієнтовну оцінку.",
    short: "коротке", long: "довге", words: "слів", target: "ціль", min: "хв",
    tab_tpl: "Шаблон", tab_phr: "Банк фраз", tab_model: "Зразок", tab_check: "Пункти завдання",
    insert_skel: "Вставити каркас у текст", model_warn: "Спершу спробуй написати сам(а) — так запам'ятовується краще.", show_model: "Показати зразок",
    timer_start: "Старт", timer_pause: "Пауза", timer_reset: "Скинути",
    check_text: "Перевірити текст", checking: "Перевіряю…", save: "Зберегти спробу", saved: "Спробу збережено", draft: "Чернетка зберігається автоматично",
    lt_note: "Мовну перевірку робить LanguageTool: текст відправляється на languagetool.org.", lt_err: "Сервіс перевірки зараз недоступний — показую лише перевірку структури.",
    lt_none: "LanguageTool не знайшов помилок 👍", lt_found: "Знайдено мовних помилок", apply: "Виправити",
    est: "Орієнтовна оцінка", est_note: "Це не офіційна оцінка, а підказка: завдання, обсяг, форма і мовна правильність.",
    est_no_lt: "без мовної перевірки", points_hint: "Відміть пункти завдання, які ти виконав(ла) — це найважливіша частина оцінки.",
    k_task: "Завдання", k_vol: "Обсяг", k_form: "Форма", k_lang: "Мова",
    cat_TYPOS: "Орфографія", cat_PUNCTUATION: "Пунктуація", cat_GRAMMAR: "Граматика", cat_CASING: "Великі літери", cat_STYLE: "Стиль", cat_other: "Інше",
    struct: "Структура і стиль", history: "Твої спроби",
    h_words_low: "Замало слів", h_words_ok: "Обсяг у нормі", h_words_high: "Забагато слів — скороти",
    h_greet_ok: "Є звертання на початку", h_greet_no: "Немає звертання на початку (Cześć… / Szanowni Państwo…)",
    h_bye_ok: "Є прощання і підпис", h_bye_no: "Немає прощання / підпису в кінці",
    h_formal_bad: "Офіційний лист: «Cześć / Pozdrawiam / ty / ciebie» — помилка стилю, пиши Pan / Pani / Państwo",
    h_formal_ok: "Офіційний стиль витримано", h_pan_case: "У листі пиши з великої: Pan, Pani, Państwo",
    h_inf_bad: "Лист другу: «Szanowny / Z poważaniem» звучить занадто офіційно",
    h_par_ok: "Текст поділено на абзаци", h_par_no: "Поділи текст на абзаци (вступ — основна частина — закінчення)",
    h_conn_ok: "Сполучників достатньо", h_conn_no: "Додай сполучники: ponieważ, ale, więc, poza tym, dlatego",
    h_head_ok: "Є заголовок", h_head_no: "Додай заголовок великими літерами (SPRZEDAM… / SZUKAM…)",
    h_contact_ok: "Є контакт", h_contact_no: "Додай контакт: телефон, e-mail або «proszę dzwonić…»",
    h_op_ok: "Є твоя думка", h_op_no: "Немає думки: Moim zdaniem… / Uważam, że…",
    h_sum_ok: "Є підсумок", h_sum_no: "Додай підсумок: Podsumowując… / Dlatego uważam, że…",
    h_diac: "Немає польських літер (ą, ę, ł, ó, ś, ż…) — на іспиті це помилки", h_cyr: "У тексті є кирилиця",
    h_cap: "Речення після крапки починай з великої літери", h_comma: "Перед «że, żeby, który, ponieważ, kiedy, jeśli, bo» став кому",
    h_long: "Дуже довге речення — розбий на два", h_rep: "Слово повторюється забагато разів:",
    disclaimer: "Неофіційний тренажер. Усі завдання авторські, це не копії офіційних тестів. Офіційні зразки і правила іспиту: ",
    progress_note: "Прогрес зберігається лише в цьому браузері.", reset: "Скинути прогрес", reset_q: "Видалити весь прогрес і чернетки?",
    tips: ["Сьогодні: одне оголошення за 15 хвилин. Обов'язково всі пункти завдання + контакт.", "Сьогодні: 2 блоки граматики. Читай пояснення до кожної помилки.",
      "Сьогодні: висловлення (wypowiedź). Вступ → 2 аргументи з прикладом → Podsumowując.", "Сьогодні: аудіювання. Спершу прочитай питання, потім вмикай запис.",
      "Сьогодні: офіційний лист. Szanowni Państwo… Z poważaniem — і жодного «Cześć».", "Сьогодні: блок читання. Шукай у тексті слова з питання."],
    tip_m: "У тебе є помилки в банку граматики — 10 хвилин на повторення."
  },
  ru: {
    nav_home: "Главная", nav_g: "Грамматика", nav_r: "Чтение", nav_l: "Аудирование", nav_w: "Письмо",
    hero_t: "Подготовка к экзамену по польскому B1", hero_p: "Более 4000 заданий: грамматика, чтение, аудирование с живыми голосами и письмо с проверкой ошибок. Учись блоками по 15–20 вопросов.",
    days: "дней до экзамена", exam_date: "Письменная часть: 5 декабря 2026", today: "Совет на сегодня",
    sec_g: "Грамматика", sec_r: "Чтение", sec_l: "Аудирование", sec_w: "Письмо",
    sec_g_d: "Падежи, вид глагола, числительные, предлоги, местоимения. Объяснение к каждому ответу.",
    sec_r_d: "Объявления, письма, сообщения, правила, истории. Выбор ответа и «правда / ложь».",
    sec_l_d: "Записи с живыми польскими голосами. Как на экзамене — максимум 2 прослушивания.",
    sec_w_d: "Шаблоны, банк фраз, таймер и настоящая проверка орфографии, грамматики и структуры.",
    questions: "вопросов", blocks: "блоков", block: "Блок", done_blocks: "пройдено", start: "Начать", next_block: "Следующий блок →",
    continue_: "Продолжить", all_blocks: "Все блоки", mistakes: "Мои ошибки", mistakes_n: "ошибок в банке", mistakes_empty: "Ошибок пока нет — так держать!",
    finish: "Проверить ответы", time_up: "Время вышло — проверяем!", answered: "ответов", score: "Результат",
    again: "Пройти ещё раз", back: "К блокам", correct: "Верно", wrong: "Ошибка", right_is: "Правильный ответ:", no_answer: "Без ответа.",
    tf_true: "Prawda", tf_false: "Fałsz", in_text: "В тексте:", in_rec: "В записи:",
    play: "▶ Слушать", playing: "Звучит…", plays_left: "Осталось прослушиваний", no_plays: "Прослушивания закончились", replay: "▶ Слушать ещё раз",
    transcript: "Текст записи", loading: "Загрузка…", load_err: "Не удалось загрузить данные. Проверь интернет и обнови страницу.",
    pass: "Зачёт (≥ 60%)", fail: "Ниже 60% — повтори этот блок позже", best: "лучший",
    w_title: "Письмо", w_p: "Выбери задание. Посмотри шаблон, пиши с таймером, а потом нажми «Проверить текст» — получишь список ошибок и примерную оценку.",
    short: "короткий", long: "длинный", words: "слов", target: "цель", min: "мин",
    tab_tpl: "Шаблон", tab_phr: "Банк фраз", tab_model: "Образец", tab_check: "Пункты задания",
    insert_skel: "Вставить каркас в текст", model_warn: "Сначала попробуй написать сам(а) — так запоминается лучше.", show_model: "Показать образец",
    timer_start: "Старт", timer_pause: "Пауза", timer_reset: "Сброс",
    check_text: "Проверить текст", checking: "Проверяю…", save: "Сохранить попытку", saved: "Попытка сохранена", draft: "Черновик сохраняется автоматически",
    lt_note: "Языковую проверку делает LanguageTool: текст отправляется на languagetool.org.", lt_err: "Сервис проверки сейчас недоступен — показываю только проверку структуры.",
    lt_none: "LanguageTool не нашёл ошибок 👍", lt_found: "Найдено языковых ошибок", apply: "Исправить",
    est: "Примерная оценка", est_note: "Это не официальная оценка, а подсказка: задание, объём, форма и языковая правильность.",
    est_no_lt: "без языковой проверки", points_hint: "Отметь пункты задания, которые ты выполнил(а) — это самая важная часть оценки.",
    k_task: "Задание", k_vol: "Объём", k_form: "Форма", k_lang: "Язык",
    cat_TYPOS: "Орфография", cat_PUNCTUATION: "Пунктуация", cat_GRAMMAR: "Грамматика", cat_CASING: "Заглавные буквы", cat_STYLE: "Стиль", cat_other: "Другое",
    struct: "Структура и стиль", history: "Твои попытки",
    h_words_low: "Мало слов", h_words_ok: "Объём в норме", h_words_high: "Слишком много слов — сократи",
    h_greet_ok: "Есть обращение в начале", h_greet_no: "Нет обращения в начале (Cześć… / Szanowni Państwo…)",
    h_bye_ok: "Есть прощание и подпись", h_bye_no: "Нет прощания / подписи в конце",
    h_formal_bad: "Официальное письмо: «Cześć / Pozdrawiam / ty / ciebie» — ошибка стиля, пиши Pan / Pani / Państwo",
    h_formal_ok: "Официальный стиль выдержан", h_pan_case: "В письме пиши с большой буквы: Pan, Pani, Państwo",
    h_inf_bad: "Письмо другу: «Szanowny / Z poważaniem» звучит слишком официально",
    h_par_ok: "Текст разбит на абзацы", h_par_no: "Раздели текст на абзацы (вступление — основная часть — завершение)",
    h_conn_ok: "Связок достаточно", h_conn_no: "Добавь связки: ponieważ, ale, więc, poza tym, dlatego",
    h_head_ok: "Есть заголовок", h_head_no: "Добавь заголовок крупными буквами (SPRZEDAM… / SZUKAM…)",
    h_contact_ok: "Есть контакт", h_contact_no: "Добавь контакт: телефон, e-mail или «proszę dzwonić…»",
    h_op_ok: "Есть твоё мнение", h_op_no: "Нет мнения: Moim zdaniem… / Uważam, że…",
    h_sum_ok: "Есть итог", h_sum_no: "Добавь итог: Podsumowując… / Dlatego uważam, że…",
    h_diac: "Нет польских букв (ą, ę, ł, ó, ś, ż…) — на экзамене это ошибки", h_cyr: "В тексте есть кириллица",
    h_cap: "Предложение после точки начинай с заглавной буквы", h_comma: "Перед «że, żeby, który, ponieważ, kiedy, jeśli, bo» ставь запятую",
    h_long: "Очень длинное предложение — раздели на два", h_rep: "Слово повторяется слишком часто:",
    disclaimer: "Неофициальный тренажёр. Все задания авторские, это не копии официальных тестов. Официальные образцы и правила экзамена: ",
    progress_note: "Прогресс хранится только в этом браузере.", reset: "Сбросить прогресс", reset_q: "Удалить весь прогресс и черновики?",
    tips: ["Сегодня: одно объявление за 15 минут. Обязательно все пункты задания + контакт.", "Сегодня: 2 блока грамматики. Читай объяснение к каждой ошибке.",
      "Сегодня: высказывание (wypowiedź). Вступление → 2 аргумента с примером → Podsumowując.", "Сегодня: аудирование. Сначала прочитай вопросы, потом включай запись.",
      "Сегодня: официальное письмо. Szanowni Państwo… Z poważaniem — и никакого «Cześć».", "Сегодня: блок чтения. Ищи в тексте слова из вопроса."],
    tip_m: "У тебя есть ошибки в банке грамматики — 10 минут на повторение."
  }
};

/* ================= stan ================= */
const KEY = "zdamb1:v3";
const S = Object.assign({ lang: "ua", blocks: { g: {}, r: {}, l: {} }, miss: [], drafts: {}, essays: [], totals: {} },
  JSON.parse(localStorage.getItem(KEY) || "null") || (() => { // migracja z v1: język, szkice, eseje
    const o = JSON.parse(localStorage.getItem("zdamb1:v1") || "{}");
    return { lang: o.lang || "ua", drafts: o.drafts || {}, essays: o.essays || [] };
  })());
const save = () => localStorage.setItem(KEY, JSON.stringify(S));
const t = k => (T[S.lang] && T[S.lang][k] !== undefined) ? T[S.lang][k] : (T.ua[k] !== undefined ? T.ua[k] : k);
const L = o => (o && (o[S.lang] || o.ua)) || "";
const $ = (s, el = document) => el.querySelector(s);
const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const pct = (a, b) => b ? Math.round(a / b * 100) : 0;
const fmt = s => `${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`;
const app = $("#app");
let cleanup = [];
const onLeave = fn => cleanup.push(fn);
function toast(msg) { const el = $("#toast"); el.textContent = msg; el.classList.add("show"); clearTimeout(toast.t); toast.t = setTimeout(() => el.classList.remove("show"), 2400); }
const EXAM = new Date(2026, 11, 5);
const daysLeft = () => Math.max(0, Math.ceil((EXAM - new Date(new Date().toDateString())) / 864e5));

/* ================= dane i bloki ================= */
const DATA = {};
async function load(sec) {
  if (DATA[sec]) return DATA[sec];
  const name = { g: "grammar", r: "reading", l: "listening" }[sec];
  const res = await fetch(`data/${name}.json?v=${VER}`);
  if (!res.ok) throw new Error(res.status);
  const d = await res.json();
  d.blocks = makeBlocks(sec, d);
  S.totals[sec] = { q: sec === "g" ? d.items.length : d.items.reduce((s, x) => s + x.qs.length, 0), b: d.blocks.length };
  save();
  return (DATA[sec] = d);
}
function makeBlocks(sec, d) {
  if (sec === "g") {
    const out = [];
    for (let i = 0; i < d.items.length; i += 20) out.push(d.items.slice(i, i + 20));
    if (out.length > 1 && out[out.length - 1].length < 10) out[out.length - 2].push(...out.pop());
    return out;
  }
  const out = []; let cur = [], n = 0;
  for (const x of d.items) {
    cur.push(x); n += x.qs.length;
    if (n >= 15) { out.push(cur); cur = []; n = 0; }
  }
  if (cur.length) { if (out.length && n < 10) out[out.length - 1].push(...cur); else out.push(cur); }
  return out;
}
const blockQ = (sec, b) => sec === "g" ? b.length : b.reduce((s, x) => s + x.qs.length, 0);

/* ================= nagłówek i stopka ================= */
function renderChrome(route) {
  const items = [["#/", "nav_home"], ["#/g", "nav_g"], ["#/r", "nav_r"], ["#/l", "nav_l"], ["#/w", "nav_w"]];
  $("#nav").innerHTML = items.map(([h, k]) => {
    const on = h === "#/" ? route === "" : ("#/" + route + "/").startsWith(h + "/");
    return `<a href="${h}" class="${on ? "on" : ""}">${t(k)}</a>`;
  }).join("");
  document.querySelectorAll(".lang button").forEach(b => b.classList.toggle("on", b.dataset.lang === S.lang));
  document.documentElement.lang = S.lang === "ru" ? "ru" : "uk";
  $("#foot").innerHTML = `${t("disclaimer")}<a href="https://certyfikatpolski.pl" target="_blank" rel="noopener">certyfikatpolski.pl</a>. ${t("progress_note")}
    <button class="btn small" id="reset" style="margin-left:8px">${t("reset")}</button>`;
  $("#reset").onclick = () => { if (confirm(t("reset_q"))) { localStorage.removeItem(KEY); localStorage.removeItem("zdamb1:v1"); location.hash = "#/"; location.reload(); } };
}
document.querySelectorAll(".lang button").forEach(b => b.onclick = () => { S.lang = b.dataset.lang; save(); route(); });

/* ================= strona główna ================= */
function secStats(sec) {
  const done = Object.values(S.blocks[sec] || {});
  const tot = S.totals[sec];
  return { done: done.length, avg: done.length ? Math.round(done.reduce((s, x) => s + x.best, 0) / done.length) : null, tot };
}
function home() {
  const tip = S.miss.length >= 5 ? t("tip_m") : t("tips")[new Date().getDate() % t("tips").length];
  const card = (sec, ico) => {
    const st = secStats(sec), tot = st.tot;
    return `<a class="card sec" href="#/${sec}">
      <span class="ico">${ico}</span><h3>${t("sec_" + sec)}</h3>
      <p class="muted" style="margin:0;font-size:.92rem">${t("sec_" + sec + "_d")}</p><span class="spacer"></span>
      <div class="bar"><i style="width:${tot ? pct(st.done, tot.b) : 0}%"></i></div>
      <span class="label">${tot ? `${tot.q} ${t("questions")} · ${t("done_blocks")} ${st.done}/${tot.b}` : `${t("done_blocks")} ${st.done}`}${st.avg !== null ? ` · Ø ${st.avg}%` : ""}</span></a>`;
  };
  app.innerHTML = `
  <section class="hero">
    <div class="card">
      <span class="label">Egzamin certyfikatowy · B1</span>
      <h1 style="margin:8px 0 10px">${t("hero_t")}</h1>
      <p class="muted" style="margin:0 0 16px">${t("hero_p")}</p>
      <div class="row"><a class="btn primary" href="#/w">${t("sec_w")} ✍</a><a class="btn" href="#/g">${t("sec_g")}</a><a class="btn" href="#/l">${t("sec_l")} 🎧</a></div>
      <p style="margin:16px 0 0;font-size:.94rem"><b>${t("today")}:</b> ${tip}</p>
    </div>
    <div class="card count"><div class="big">${daysLeft()}</div><div style="font-weight:600;margin-top:6px">${t("days")}</div>
      <div class="muted" style="font-size:.9rem;margin-top:4px">${t("exam_date")}</div></div>
  </section>
  <section class="grid g4">
    <a class="card sec star" href="#/w"><span class="ico">✍️</span><h3>${t("sec_w")} <span class="pill red">TOP</span></h3>
      <p class="muted" style="margin:0;font-size:.92rem">${t("sec_w_d")}</p><span class="spacer"></span>
      <span class="label">${B1.writingTasks.length} ✎ · ${S.essays.length} ✓</span></a>
    ${card("g", "📘")}${card("r", "📄")}${card("l", "🎧")}
  </section>`;
  ["g", "r", "l"].forEach(s => { if (!S.totals[s]) load(s).then(() => location.hash.replace(/^#\/?/, "") === "" && home()).catch(() => { }); });
}

/* ================= lista bloków ================= */
async function section(sec) {
  app.innerHTML = `<p class="muted">${t("loading")}</p>`;
  let d; try { d = await load(sec); } catch (e) { app.innerHTML = `<p class="hint bad">${t("load_err")}</p>`; return; }
  const st = S.blocks[sec];
  const next = d.blocks.findIndex((_, i) => !st[i]);
  app.innerHTML = `
    <div class="row" style="align-items:flex-end"><div><h1>${t("sec_" + sec)}</h1>
      <p class="muted" style="margin:6px 0 0">${t("sec_" + sec + "_d")}</p></div></div>
    <div class="card row" style="margin:18px 0">
      <div><b>${S.totals[sec].q}</b> ${t("questions")} · <b>${d.blocks.length}</b> ${t("blocks")} · ${t("done_blocks")} <b>${Object.keys(st).length}</b></div>
      <span class="spacer"></span>
      ${sec === "g" ? `<a class="btn" href="#/g/m">${t("mistakes")} (${S.miss.length})</a>` : ""}
      ${next >= 0 ? `<a class="btn primary" href="#/${sec}/${next + 1}">${Object.keys(st).length ? t("continue_") : t("start")}: ${t("block")} ${next + 1}</a>` : ""}
    </div>
    <div class="blocks">${d.blocks.map((b, i) => {
      const r = st[i];
      const cls = !r ? "" : r.best >= 80 ? "good" : r.best >= 60 ? "mid" : "low";
      return `<a class="blk ${cls}" href="#/${sec}/${i + 1}"><b>${i + 1}</b><small>${r ? r.best + "%" : blockQ(sec, b) + " " + t("questions").slice(0, 3) + "."}</small></a>`;
    }).join("")}</div>`;
}

/* ================= test (blok) ================= */
async function runBlock(sec, n) {
  app.innerHTML = `<p class="muted">${t("loading")}</p>`;
  let d; try { d = await load(sec); } catch (e) { app.innerHTML = `<p class="hint bad">${t("load_err")}</p>`; return; }
  let groups, title, idx = null;
  if (n === "m") {
    const pool = d.items.filter(x => S.miss.includes(x.id));
    if (!pool.length) { app.innerHTML = `<p>${t("mistakes_empty")}</p><a class="btn" href="#/g">${t("back")}</a>`; return; }
    groups = [{ items: shuffle(pool).slice(0, 20) }]; title = t("mistakes");
  } else {
    idx = +n - 1; const b = d.blocks[idx];
    if (!b) { location.hash = `#/${sec}`; return; }
    groups = sec === "g" ? [{ items: b }] : b.map(x => ({ src: x, items: x.qs }));
    title = `${t("sec_" + sec)} · ${t("block")} ${idx + 1} / ${d.blocks.length}`;
  }
  // przygotuj pytania: każda opcja zna swoją poprawność (bez indeksów, które mogłyby się rozjechać)
  const Q = [];
  groups.forEach((g, gi) => g.items.forEach(it => {
    const view = it.o ? shuffle(it.o.map((text, i) => ({ text, ok: i === 0 })))
      : [{ text: t("tf_true"), ok: it.tf === true }, { text: t("tf_false"), ok: it.tf === false }];
    Q.push({ it, gi, view, chosen: null, id: it.id || null });
  }));
  const minutes = sec === "g" ? Math.max(10, Q.length) : sec === "r" ? groups.length * 6 : groups.length * 5;
  let left = minutes * 60, done = false;

  const qHtml = (q, k) => `<div class="q" data-k="${k}">
      <div class="qt"><span class="num">${k + 1}.</span>${esc(q.it.q).replace("___", "<b class='gap'>_____</b>")}</div>
      <div class="opts ${q.it.o ? "" : "tf"}">${q.view.map((v, i) => `
        <label class="opt"><input type="radio" name="q${k}" value="${i}"><span>${esc(v.text)}</span></label>`).join("")}</div>
      <div class="fb"></div></div>`;
  let body = "", k = 0;
  groups.forEach((g, gi) => {
    const qs = g.items.map(() => qHtml(Q[k], k++)).join("");
    if (sec === "r") body += `<div class="split" style="margin-bottom:28px"><div class="stick"><span class="label">${esc(g.src.kind)}</span>
        <h2 style="margin:4px 0 10px">${esc(g.src.title)}</h2><div class="text">${esc(g.src.text)}</div></div><div>${qs}</div></div>`;
    else if (sec === "l") body += `<section class="rec" data-g="${gi}" style="margin-bottom:28px"><h2>${gi + 1}. ${esc(g.src.title)}</h2>
        <div class="player"><button class="btn primary small play">${t("play")}</button><div class="prog"><i></i></div><span class="muted plays">${t("plays_left")}: 2</span>
        <audio preload="none" src="audio/${g.src.id}.mp3?v=${VER}"></audio></div>${qs}<div class="tr" hidden></div></section>`;
    else body += qs;
  });
  app.innerHTML = `<div class="testhead row"><a class="btn small" href="#/${sec}">←</a><b>${title}</b>
      <span class="muted" id="cnt">0 / ${Q.length} ${t("answered")}</span><span class="spacer"></span>
      <span class="timer" id="timer">${fmt(left)}</span></div>
    <div id="res"></div><div id="qs">${body}</div>
    <div class="row" style="margin-top:20px"><span class="spacer"></span><button class="btn primary" id="finish">${t("finish")}</button></div>`;

  app.querySelectorAll(".opt input").forEach(inp => inp.onchange = () => {
    if (done) return;
    const q = Q[+inp.name.slice(1)];
    q.chosen = +inp.value;
    inp.closest(".opts").querySelectorAll(".opt").forEach(o => o.classList.toggle("sel", o.contains(inp)));
    $("#cnt").textContent = `${Q.filter(x => x.chosen !== null).length} / ${Q.length} ${t("answered")}`;
  });

  // odtwarzacz: maks. 2 odsłuchania przed sprawdzeniem, potem bez limitu
  const players = [];
  if (sec === "l") app.querySelectorAll(".rec").forEach(box => {
    const au = box.querySelector("audio"), btn = box.querySelector(".play"), bar = box.querySelector(".prog i"), lbl = box.querySelector(".plays");
    const p = { plays: 2, au };
    players.push(p);
    btn.onclick = () => {
      if (!au.paused) return;
      if (!done && p.plays <= 0) return;
      players.forEach(o => { if (o !== p) { o.au.pause(); } });
      if (!done) p.plays--;
      au.currentTime = 0; btn.disabled = true; btn.textContent = t("playing");
      au.play().catch(() => { btn.disabled = false; btn.textContent = t("play"); if (!done) p.plays++; toast(t("load_err")); });
    };
    au.ontimeupdate = () => { bar.style.width = (au.duration ? au.currentTime / au.duration * 100 : 0) + "%"; };
    au.onended = au.onpause = () => {
      btn.disabled = !done && p.plays <= 0;
      btn.textContent = done ? t("replay") : p.plays > 0 ? t("play") : t("no_plays");
      lbl.textContent = done ? "" : `${t("plays_left")}: ${p.plays}`;
    };
    onLeave(() => au.pause());
  });

  const tick = setInterval(() => {
    if (done) return;
    left--; const el = $("#timer"); if (!el) return;
    el.textContent = fmt(Math.max(0, left)); el.classList.toggle("low", left <= 60);
    if (left <= 0) { toast(t("time_up")); finish(); }
  }, 1000);
  onLeave(() => clearInterval(tick));

  function finish() {
    if (done) return; done = true; clearInterval(tick);
    let s = 0;
    Q.forEach((q, k) => {
      const box = app.querySelector(`.q[data-k="${k}"]`);
      const ok = q.chosen !== null && q.view[q.chosen].ok === true;
      if (ok) s++;
      box.classList.add(ok ? "is-ok" : "is-bad");
      box.querySelectorAll("input").forEach(i => i.disabled = true);
      box.querySelectorAll(".opt").forEach((o, i) => { o.classList.remove("sel"); if (q.view[i].ok) o.classList.add("right"); else if (i === q.chosen) o.classList.add("wrong"); });
      const right = q.view.find(v => v.ok).text;
      let fb = ok ? `<b>✓ ${t("correct")}.</b> ` : `<b>✗ ${q.chosen === null ? t("no_answer") : t("wrong") + "."}</b> ${t("right_is")} <b>${esc(right)}</b>. `;
      if (q.it.ex) fb += L(q.it.ex);
      else if (q.it.hint) fb += `${sec === "l" ? t("in_rec") : t("in_text")} «${esc(q.it.hint)}»`;
      box.querySelector(".fb").innerHTML = `<div class="expl ${ok ? "" : "bad"}">${fb}</div>`;
      if (sec === "g" && q.id) {
        const i = S.miss.indexOf(q.id);
        if (!ok && i < 0) S.miss.push(q.id);
        if (ok && i >= 0) S.miss.splice(i, 1);
      }
    });
    if (sec === "l") app.querySelectorAll(".rec").forEach((box, gi) => {
      const tr = box.querySelector(".tr"); tr.hidden = false;
      tr.innerHTML = `<details open><summary class="label">${t("transcript")}</summary><div class="transcript">${groups[gi].src.lines.map(([v, x]) => `<p><b>${v === "A" ? "♀" : "♂"}</b> ${esc(x)}</p>`).join("")}</div></details>`;
      const p = players[gi]; p.au.onended();
    });
    const p = pct(s, Q.length);
    if (idx !== null) {
      const prev = S.blocks[sec][idx];
      S.blocks[sec][idx] = { best: Math.max(p, prev ? prev.best : 0), last: p, tries: (prev ? prev.tries : 0) + 1 };
    }
    save();
    const nextIdx = idx !== null && idx + 1 < d.blocks.length ? idx + 2 : null;
    $("#finish").parentElement.remove();
    $("#res").innerHTML = `<div class="card result" style="margin-bottom:18px">
      <span class="label">${t("score")}</span><div class="big">${s} / ${Q.length}</div>
      <p><span class="pill ${p >= 60 ? "ok" : "warn"}">${p}% · ${p >= 60 ? t("pass") : t("fail")}</span></p>
      <div class="row" style="justify-content:center">
        ${nextIdx ? `<a class="btn primary" href="#/${sec}/${nextIdx}">${t("next_block")}</a>` : ""}
        <button class="btn" id="again">${t("again")}</button><a class="btn" href="#/${sec}">${t("back")}</a>
        ${sec === "g" && S.miss.length ? `<a class="btn" href="#/g/m">${t("mistakes")} (${S.miss.length})</a>` : ""}</div></div>`;
    $("#again").onclick = () => route();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
  $("#finish").onclick = finish;
}

/* ================= pisanie ================= */
function wordCount(s) { return (s.match(/[\p{L}\p{N}]+(?:[-'’][\p{L}\p{N}]+)*/gu) || []).length; }

function writeList() {
  const groups = Object.entries(B1.writingTypes);
  app.innerHTML = `<h1>${t("w_title")} ✍️</h1><p class="muted" style="max-width:720px">${t("w_p")}</p>
  ${groups.map(([k, ty]) => `
    <section style="margin-top:26px">
      <div class="row"><h2>${ty.name}</h2><span class="pill ${ty.size === "short" ? "" : "red"}">${t(ty.size)} · ${ty.words[0]}–${ty.words[1]} ${t("words")}</span></div>
      <p class="muted" style="margin:6px 0 12px">${L(ty.about)}</p>
      <div class="tasks">${B1.writingTasks.filter(x => x.type === k).map(x => {
        const tries = S.essays.filter(e => e.id === x.id).length;
        const dr = (S.drafts[x.id] || "").trim();
        return `<a class="card task" href="#/w/${x.id}"><b>${esc(x.title)}</b><span class="muted" style="font-size:.9rem">${esc(x.prompt)}</span>
          <span class="row" style="margin-top:4px">${tries ? `<span class="pill ok">✓ ${tries}</span>` : ""}${dr ? `<span class="pill warn">✎ ${wordCount(dr)} ${t("words")}</span>` : ""}</span></a>`;
      }).join("")}</div></section>`).join("")}`;
}

/* Lokalna analiza tekstu (struktura, styl, typowe błędy) */
const CONN = /(?<!\p{L})(ponieważ|bo|ale|więc|dlatego|jednak|chociaż|poza tym|przede wszystkim|na przykład|z drugiej strony|z jednej strony|podsumowując|najpierw|potem|kiedy|jeśli|jeżeli|żeby|oraz|a także|również|z tego powodu|w związku z tym|niestety|natomiast|następnie)(?!\p{L})/giu;
const STOP = new Set("jest jestem będzie było mnie mój moja moje twój twoja jego jej nasz nasza który która które także bardzo tylko jeszcze można przez jako tego tej tym tych oraz albo więc kiedy jeśli żeby ponieważ chciałbym chciałabym proszę".split(" "));
function analyse(text, task, ty) {
  const H = [], add = (ok, msg) => H.push({ ok, msg });
  const w = wordCount(text), [lo, hi] = ty.words;
  const vol = w < lo ? w / lo : w > hi ? Math.max(0.6, 1 - (w - hi) / hi) : 1;
  add(w >= lo && w <= hi, (w < lo ? t("h_words_low") : w > hi ? t("h_words_high") : t("h_words_ok")) + ` (${w} / ${lo}–${hi})`);
  const trimmed = text.trim(), lines = trimmed.split(/\n/).map(x => x.trim()).filter(Boolean);
  const head = trimmed.slice(0, 120), tail = trimmed.slice(-160);
  const form = [];
  const chk = (ok, good, bad) => { form.push(ok); add(ok, ok ? good : bad); };
  const paras = trimmed.split(/\n\s*\n/).filter(p => wordCount(p) > 0).length;
  if (task.type === "ogloszenie") {
    const h0 = lines[0] || "";
    chk(h0.length > 3 && h0 === h0.toUpperCase() && /\p{L}/u.test(h0), t("h_head_ok"), t("h_head_no"));
    chk(/(\d{3}[\s-]?\d{3}[\s-]?\d{3}|@|tel\.|telefon|dzwonić|kontakt|SMS|e-mail|mail)/i.test(text), t("h_contact_ok"), t("h_contact_no"));
  } else {
    chk(lines.slice(0, 3).some(l => /^(cześć|hej|witaj|drog[aiy]|kochan[aiy]|szanown[aiy]|dzień dobry)/i.test(l)), t("h_greet_ok"), t("h_greet_no"));
    if (task.type !== "wypowiedz") chk(/(pozdrawiam|pozdrowienia|z poważaniem|z wyrazami szacunku|ściskam|do zobaczenia|całuję|trzymaj się|buziaki|do usłyszenia)/i.test(tail), t("h_bye_ok"), t("h_bye_no"));
  }
  if (task.type === "formalny" && w > 3) {
    const bad = /(?<!\p{L})(cześć|hej|pozdrawiam|ściskam|buziaki|ty|cię|ci|ciebie|tobie|tobą|twój|twoja|twoje|twojego|twoim|możesz|chcesz|wiesz|masz|napisz|odpisz|daj znać)(?!\p{L})/iu.test(text);
    chk(!bad, t("h_formal_ok"), t("h_formal_bad"));
    if (/(?<!\p{L}|[.!?]\s|^)(pan|pani|państwo|państwa|państwu|panu)(?!\p{L})/u.test(text)) { form.push(false); add(false, t("h_pan_case")); }
  }
  if (task.type === "email" && /(szanown|z poważaniem)/i.test(text)) { form.push(false); add(false, t("h_inf_bad")); }
  if (ty.size === "long" || task.type === "email") chk(paras >= (ty.size === "long" ? 3 : 2), t("h_par_ok"), t("h_par_no"));
  if (task.type === "wypowiedz") {
    chk(/(moim zdaniem|uważam, że|uważam że|wydaje mi się|według mnie|myślę, że|myślę że|jestem przekonany|jestem przekonana)/i.test(text) || task.id === "w12", t("h_op_ok"), t("h_op_no"));
    chk(/(podsumowując|reasumując|dlatego uważam|na koniec|w końcu|wsumie|ogólnie rzecz biorąc|ten dzień był)/i.test(text.slice(-Math.max(200, text.length / 3))), t("h_sum_ok"), t("h_sum_no"));
  }
  if (ty.size === "long" || task.type === "email") {
    const conn = (text.match(CONN) || []).length, need = ty.size === "long" ? 4 : 2;
    chk(conn >= need, t("h_conn_ok") + ` (${conn})`, t("h_conn_no") + ` (${conn}/${need})`);
  }
  // typowe błędy
  if (/[Ѐ-ӿ]/.test(text)) add(false, t("h_cyr"));
  if (w > 25 && !/[ąćęłńóśźż]/i.test(text)) add(false, t("h_diac"));
  const ABBR = /(?<!\p{L})(np|ok|ul|tel|godz|nr|tzn|tj|dr|itd|itp|r|in|pt|ds|wg|zł|ew|br|prof|mgr|inż)\.$/iu;
  const capBad = [...text.matchAll(/(\S*[.!?])\s+([a-ząćęłńóśźż]\S*)/gu)].filter(m => !ABBR.test(m[1]) && !/\d\.$/.test(m[1]));
  if (capBad.length) add(false, `${t("h_cap")}: «${esc(capBad[0][1] + " " + capBad[0][2])}»`);
  trimmed.split(/[.!?]+/).forEach(s => { if (wordCount(s) > 35) add(false, `${t("h_long")}: «${esc(s.trim().slice(0, 50))}…»`); });
  const freq = {};
  (text.toLowerCase().match(/\p{L}{4,}/gu) || []).forEach(x => { if (!STOP.has(x)) freq[x] = (freq[x] || 0) + 1; });
  const reps = Object.entries(freq).filter(([, n]) => n >= 4).map(([x, n]) => `${x} ×${n}`);
  if (reps.length) add(false, `${t("h_rep")} ${esc(reps.slice(0, 4).join(", "))}`);
  return { H, w, vol, form: form.length ? form.filter(Boolean).length / form.length : 1 };
}

async function languageTool(text) {
  const r = await fetch("https://api.languagetool.org/v2/check", {
    method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ text, language: "pl-PL" })
  });
  if (!r.ok) throw new Error(r.status);
  return (await r.json()).matches;
}

function writeTask(id) {
  const task = B1.writingTasks.find(x => x.id === id);
  if (!task) { location.hash = "#/w"; return; }
  const ty = B1.writingTypes[task.type];
  const allChecks = [...task.points.map(p => ({ pl: p, point: true })), ...ty.checks, ...B1.commonChecks];
  let tab = "tpl", modelShown = false, left = ty.minutes * 60, running = false, tick = null, lt = null, ltFor = "";

  app.innerHTML = `
  <div class="row" style="margin-bottom:12px"><a href="#/w" class="btn small">← ${t("w_title")}</a>
    <span class="pill ${ty.size === "short" ? "" : "red"}">${ty.name} · ${t(ty.size)}</span></div>
  <div class="wgrid">
    <div>
      <div class="prompt"><span class="label">Polecenie</span><h2 style="margin:4px 0 8px">${esc(task.title)}</h2>
        <p style="margin:0">${esc(task.prompt)}</p><p style="margin:10px 0 0"><b>Napisz:</b></p>
        <ul>${task.points.map(p => `<li>${esc(p)}</li>`).join("")}</ul>
        <p class="muted" style="margin:10px 0 0;font-size:.9rem">${t("target")}: ${ty.words[0]}–${ty.words[1]} ${t("words")} · ${ty.minutes} ${t("min")}</p></div>
      <div class="tabs" id="tabs"><button data-tab="tpl">${t("tab_tpl")}</button><button data-tab="phr">${t("tab_phr")}</button>
        <button data-tab="check">${t("tab_check")}</button><button data-tab="model">${t("tab_model")}</button></div>
      <div class="tabpane" id="pane"></div>
    </div>
    <div class="editor">
      <div class="row" style="margin-bottom:8px"><span class="timer" id="wtimer">${fmt(left)}</span>
        <button class="btn small" id="tgo">${t("timer_start")}</button><button class="btn small" id="treset">${t("timer_reset")}</button>
        <span class="spacer"></span><span class="wc" id="wc">0</span><span class="muted">/ ${ty.words[0]}–${ty.words[1]} ${t("words")}</span></div>
      <textarea class="essay" id="essay" spellcheck="true" lang="pl" placeholder="Pisz tutaj po polsku…"></textarea>
      <div class="bar" style="margin:8px 0"><i id="wbar" style="width:0"></i></div>
      <div class="row"><button class="btn primary" id="wcheck">🔍 ${t("check_text")}</button><button class="btn" id="wsave">${t("save")}</button>
        <span class="spacer"></span><span class="muted" style="font-size:.82rem">${t("draft")}</span></div>
      <div id="report" style="margin-top:14px"></div>
      <div id="hist" style="margin-top:14px"></div>
    </div>
  </div>`;
  const ta = $("#essay");
  ta.value = S.drafts[id] || "";
  const chkState = () => S.drafts[id + ":chk"] || [];

  function renderPane() {
    document.querySelectorAll("#tabs button").forEach(b => b.classList.toggle("on", b.dataset.tab === tab));
    const pane = $("#pane");
    if (tab === "tpl") {
      pane.innerHTML = ty.parts.map((p, i) => `<div class="part"><b class="n">${i + 1}</b><div><b>${p.pl}</b> — <span class="muted">${S.lang === "ru" ? p.ru : p.ua}</span><code>${esc(p.ex)}</code></div></div>`).join("")
        + `<button class="btn small" id="skel" style="margin-top:12px">${t("insert_skel")}</button>`;
      $("#skel").onclick = () => insertText((ta.value.trim() ? "\n\n" : "") + ty.skeleton);
    } else if (tab === "phr") {
      const li = S.lang === "ru" ? 2 : 1;
      pane.innerHTML = B1.phrases.map(g => `<div class="phr-group"><span class="label">${L(g.group)}</span><div class="phr">
        ${g.items.map(it => `<button data-p="${esc(it[0])}">${esc(it[0])}<small>${esc(it[li])}</small></button>`).join("")}</div></div>`).join("");
      pane.querySelectorAll("[data-p]").forEach(b => b.onclick = () => insertText(b.dataset.p.split(" / ")[0].replace(/ …$/, " ")));
    } else if (tab === "check") {
      const st = chkState();
      pane.innerHTML = `<p class="muted" style="margin:0 0 8px;font-size:.9rem">${t("points_hint")}</p><div class="checks">
        ${allChecks.map((c, i) => `${i === task.points.length ? `<span class="label" style="display:block;margin-top:12px">${t("struct")}</span>` : ""}
          <label><input type="checkbox" data-i="${i}" ${st[i] ? "checked" : ""}><span>${c.pl ? "<b>" + esc(c.pl) + "</b>" : L(c)}</span></label>`).join("")}</div>`;
      pane.querySelectorAll("input").forEach(c => c.onchange = () => { const a = chkState(); a[+c.dataset.i] = c.checked; S.drafts[id + ":chk"] = a; save(); if (lt !== null) report(); });
    } else {
      pane.innerHTML = modelShown ? `<div class="model">${esc(task.model)}</div><p class="muted" style="font-size:.85rem">${wordCount(task.model)} ${t("words")}</p>`
        : `<p class="muted">${t("model_warn")}</p><button class="btn" id="showm">${t("show_model")}</button>`;
      const b = $("#showm"); if (b) b.onclick = () => { modelShown = true; renderPane(); };
    }
  }
  document.querySelectorAll("#tabs button").forEach(b => b.onclick = () => { tab = b.dataset.tab; renderPane(); });

  function insertText(txt) {
    const s = ta.selectionStart ?? ta.value.length, e = ta.selectionEnd ?? s;
    const before = ta.value.slice(0, s), after = ta.value.slice(e);
    const pad = before && !/\s$/.test(before) && !/^\n/.test(txt) ? " " : "";
    ta.value = before + pad + txt + after;
    const pos = (before + pad + txt).length;
    ta.focus(); ta.setSelectionRange(pos, pos); update();
  }
  function update() {
    S.drafts[id] = ta.value; save();
    const w = wordCount(ta.value), [lo, hi] = ty.words;
    $("#wc").textContent = w;
    const bar = $("#wbar"); bar.style.width = Math.min(100, w / lo * 100) + "%";
    bar.style.background = w > hi ? "var(--warn)" : w >= lo ? "var(--ok)" : "var(--red)";
    if (lt !== null && ta.value !== ltFor) { $("#report").querySelector(".stale")?.removeAttribute("hidden"); }
  }
  ta.addEventListener("input", update);

  function report() {
    const text = ta.value, A = analyse(text, task, ty);
    const st = chkState(), pts = task.points.length ? task.points.filter((_, i) => st[i]).length / task.points.length : 1;
    const words = Math.max(1, A.w);
    const langScore = Array.isArray(lt) ? Math.max(0, 1 - (lt.length / words * 100) / 15) : null;
    const parts = [[t("k_task"), pts, .35], [t("k_vol"), A.vol, .15], [t("k_form"), A.form, .2]];
    if (langScore !== null) parts.push([t("k_lang"), langScore, .3]);
    const wsum = parts.reduce((s, p) => s + p[2], 0);
    const total = Math.round(parts.reduce((s, p) => s + p[1] * p[2], 0) / wsum * 100);
    const CAT = { TYPOS: "cat_TYPOS", PUNCTUATION: "cat_PUNCTUATION", GRAMMAR: "cat_GRAMMAR", CASING: "cat_CASING", STYLE: "cat_STYLE" };
    const ltHtml = lt === null ? "" : lt === "err" ? `<div class="hint bad">${t("lt_err")}</div>`
      : !lt.length ? `<div class="hint ok">✓ ${t("lt_none")}</div>`
      : `<span class="label">${t("lt_found")}: ${lt.length}</span><div class="lt">${lt.map((m, i) => {
          const frag = text.substr(m.offset, m.length);
          return `<div class="ltm"><span class="pill">${t(CAT[m.rule.category.id] || "cat_other")}</span> <b class="frag">${esc(frag)}</b>
            <div class="muted" style="font-size:.88rem;margin-top:3px">${esc(m.message)}</div>
            ${m.replacements.length ? `<div class="row" style="margin-top:6px;gap:6px">${m.replacements.slice(0, 3).map(r =>
              `<button class="btn small fix" data-i="${i}" data-r="${esc(r.value)}">${t("apply")}: ${esc(r.value) || "∅"}</button>`).join("")}</div>` : ""}</div>`;
        }).join("")}</div>`;
    const lvl = total >= 75 ? "ok" : total >= 55 ? "warn" : "red";
    $("#report").innerHTML = `
      <div class="card" style="padding:16px">
        <div class="row"><div><span class="label">${t("est")}</span><div class="score ${lvl}">≈ ${total}<small>/100</small></div></div>
          <div class="kpis">${parts.map(p => `<div><span class="label">${p[0]}</span><b>${Math.round(p[1] * 100)}%</b></div>`).join("")}</div></div>
        <p class="muted" style="font-size:.82rem;margin:6px 0 0">${t("est_note")}${langScore === null ? " (" + t("est_no_lt") + ")" : ""}</p>
        <p class="hint bad stale" hidden style="margin-top:8px">↻ ${t("check_text")}</p>
      </div>
      <div style="margin-top:12px">${ltHtml}</div>
      <span class="label" style="display:block;margin-top:12px">${t("struct")}</span>
      <div class="hints">${A.H.map(h => `<div class="hint ${h.ok ? "ok" : "bad"}">${h.ok ? "✓" : "!"} ${h.msg}</div>`).join("")}</div>
      <p class="muted" style="font-size:.8rem">${t("lt_note")}</p>`;
    $("#report").querySelectorAll(".fix").forEach(b => b.onclick = () => {
      const m = lt[+b.dataset.i];
      if (ta.value !== ltFor) { runCheck(); return; }
      ta.value = ta.value.slice(0, m.offset) + b.dataset.r + ta.value.slice(m.offset + m.length);
      update(); runCheck();
    });
  }
  async function runCheck() {
    if (!ta.value.trim()) return;
    const btn = $("#wcheck"); btn.disabled = true; btn.textContent = t("checking");
    ltFor = ta.value;
    try { lt = await languageTool(ta.value); } catch (e) { lt = "err"; }
    btn.disabled = false; btn.textContent = "🔍 " + t("check_text");
    report();
  }
  $("#wcheck").onclick = runCheck;

  function renderHist() {
    const list = S.essays.filter(e => e.id === id).slice(-5).reverse();
    $("#hist").innerHTML = list.length ? `<span class="label">${t("history")}</span>` + list.map(e =>
      `<details style="margin-top:6px"><summary>${new Date(e.d).toLocaleString(S.lang === "ru" ? "ru-RU" : "uk-UA", { dateStyle: "short", timeStyle: "short" })} · ${e.w} ${t("words")}${e.score ? " · ≈" + e.score + "/100" : ""}</summary><div class="model" style="margin-top:6px">${esc(e.text)}</div></details>`).join("") : "";
  }
  $("#wsave").onclick = () => {
    if (!ta.value.trim()) return;
    const sc = $("#report .score");
    S.essays.push({ id, d: Date.now(), w: wordCount(ta.value), text: ta.value, score: sc ? parseInt((sc.textContent.match(/\d+/) || [""])[0]) || null : null });
    save(); renderHist(); toast(t("saved"));
  };
  const tEl = $("#wtimer");
  function setRun(on) {
    running = on; $("#tgo").textContent = on ? t("timer_pause") : t("timer_start");
    clearInterval(tick);
    if (on) tick = setInterval(() => { left--; tEl.textContent = fmt(Math.max(0, left)); tEl.classList.toggle("low", left <= 60); if (left <= 0) { setRun(false); toast(t("time_up")); } }, 1000);
  }
  $("#tgo").onclick = () => setRun(!running);
  $("#treset").onclick = () => { setRun(false); left = ty.minutes * 60; tEl.textContent = fmt(left); tEl.classList.remove("low"); };
  onLeave(() => clearInterval(tick));
  renderPane(); update(); renderHist();
}

/* ================= router ================= */
function route() {
  cleanup.forEach(f => f()); cleanup = [];
  const h = location.hash.replace(/^#\/?/, "");
  let [a, b] = h.split("/");
  if (a === "test") { location.replace("#/" + (b === "m" ? "g/m" : b || "")); return; }   // stare adresy
  if (a === "write") { location.replace("#/w" + (b ? "/" + b : "")); return; }
  renderChrome(h);
  if (["g", "r", "l"].includes(a) && b) runBlock(a, b);
  else if (["g", "r", "l"].includes(a)) section(a);
  else if (a === "w" && b) writeTask(b);
  else if (a === "w") writeList();
  else home();
  window.scrollTo({ top: 0 });
}
window.addEventListener("hashchange", route);
route();
