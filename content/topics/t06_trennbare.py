"""Тема 6. Trennbare und nicht trennbare Verben."""

TOPIC = {
    "id": "trennbare",
    "nr": 6,
    "title": "Отделяемые и неотделяемые приставки",
    "short": "Отделяемые приставки",
    "title_de": "Trennbare und nicht trennbare Verben",
    "location": "Веймар, мельница у реки",
    "location_de": "Weimar, Mühle am Fluss",
    "intro": (
        "Из Нюрнберга бард идёт вниз, к Веймару, и выходит к реке, где шумит "
        "старая мельница. Мельник рад помощнику: надо открыть воду, принести "
        "мешки, продать муку. Бард слушает хозяина и замечает странность: "
        "короткие словечки вроде auf, mit, zu стоят не рядом с глаголом, а в "
        "самом конце фразы."
    ),
    "listen": (
        "Бард садится у мельничного колеса и слушает: «Ich stehe um vier Uhr "
        "auf», «Der Müller macht die Mühle auf», «Kommst du morgen mit?». "
        "Глагол понятен, а его приставка убежала в конец предложения — так "
        "немецкий отделяет то, что должно отделяться."
    ),
    "theory": [
        {
            "title": "Отделяемая приставка уходит в конец",
            "body": (
                "Многие немецкие глаголы носят приставку: aufstehen, aufmachen, "
                "mitkommen, anfangen, einkaufen.\n\n"
                "Если приставка отделяемая, в предложении она уходит в самый "
                "конец, а глагол остаётся на втором месте:\n\n"
                "Ich stehe um sechs Uhr auf. Der Müller macht das Tor auf.\n\n"
                "Приставки auf-, an-, aus-, ein-, mit-, zu-, los-, vor- почти "
                "всегда отделяются.\n\n"
                "Вопрос: Stehst du früh auf? Приказ: Steh auf!\n\n"
                "Смысл глагола при этом не теряется: aufstehen — «вставать», "
                "stehen — просто «стоять»."
            ),
        },
        {
            "title": "Неотделяемые приставки",
            "body": (
                "Приставки be-, ge-, er-, ver-, zer-, ent-, emp-, miss- не "
                "отделяются никогда, они остаются с глаголом:\n\n"
                "Ich verstehe den Müller. Der Barde erzählt eine Geschichte. "
                "Wir besuchen die Mühle.\n\n"
                "Сравни: aufstehen — отделяется (Ich stehe auf), verstehen — "
                "нет: «Ich stehe ver» сказать нельзя.\n\n"
                "Проверить помогает ударение: отделяемая приставка ударная "
                "(ÁUFstehen, MÍTkommen), неотделяемая — безударная "
                "(verSTÉHen, erzÄHlen)."
            ),
        },
        {
            "title": "Что делать с модальным глаголом",
            "body": (
                "Если рядом модальный глагол, он занимает второе место, а "
                "основной глагол встаёт в конец инфинитивом — и приставка "
                "остаётся на месте:\n\n"
                "Ich muss früh aufstehen. Der Müller will das Tor zumachen.\n\n"
                "Нельзя сказать «Ich muss früh stehen auf»: с модальным "
                "глаголом приставка не отделяется.\n\n"
                "Сравни два предложения:\n"
                "Ich stehe früh auf. — приставка в конце;\n"
                "Ich muss früh aufstehen. — глагол целиком в конце.\n\n"
                "Так же с частицей zu: aufzustehen, mitzukommen — приставка "
                "стоит перед zu."
            ),
        },
    ],
    "song_line": (
        "Die Mühle in Weimar dreht sich im Wind,\n"
        "ich steh früh auf und lerne geschwind."
    ),
    "exercises": [
        {
            "id": "trennbare_1",
            "kind": "order",
            "prompt": "Собери предложение: бард встаёт в шесть часов.",
            "words": ["Der", "Barde", "steht", "um", "sechs", "Uhr", "auf"],
            "answer": "Der Barde steht um sechs Uhr auf",
            "explain": (
                "Отделяемая приставка уходит в конец предложения: Der Barde "
                "steht um sechs Uhr auf. Глагол стоит на втором месте."
            ),
            "retry": {
                "prompt": "Собери предложение: мельник открывает ворота.",
                "words": ["Der", "Müller", "macht", "das", "Tor", "auf"],
                "answer": "Der Müller macht das Tor auf",
                "explain": (
                    "aufmachen: глагол macht — на втором месте, приставка auf — "
                    "в конце: Der Müller macht das Tor auf."
                ),
            },
        },
        {
            "id": "trennbare_2",
            "kind": "gap",
            "prompt": "Бард встаёт рано: «Ich stehe jeden Morgen um fünf Uhr ___.» (aufstehen)",
            "options": ["an", "auf", "mit", "aus"],
            "answer": 1,
            "explain": (
                "Глагол aufstehen отделяет приставку auf: Ich stehe um fünf Uhr "
                "auf. Приставки an, mit, aus относятся к другим глаголам."
            ),
            "retry": {
                "prompt": "Мельник открывает ворота: «Der Müller macht das Tor ___.» (aufmachen)",
                "options": ["zu", "an", "auf", "ein"],
                "answer": 2,
                "explain": (
                    "aufmachen — «открывать», приставка auf уходит в конец: "
                    "macht das Tor auf. С приставкой zu получилось бы «закрывать»."
                ),
            },
        },
        {
            "id": "trennbare_3",
            "kind": "gap",
            "prompt": "Бард не понимает мельника: «Ich ___ den Müller nicht.» (verstehen)",
            "options": ["verstehst", "verstehen", "versteht", "verstehe"],
            "answer": 3,
            "explain": (
                "verstehen — глагол с неотделяемой приставкой ver-: ich verstehe. "
                "Формы verstehst, verstehen, versteht подходят для du, wir/sie и er."
            ),
            "retry": {
                "prompt": "Бард рассказывает историю: «Der Barde ___ eine Geschichte.» (erzählen)",
                "options": ["zählt", "erzählst", "erzählt", "erzählen"],
                "answer": 2,
                "explain": (
                    "Приставка er- не отделяется: der Barde erzählt. Форма zählt "
                    "значила бы «считает», а erzählst подходит для du."
                ),
            },
        },
        {
            "id": "trennbare_4",
            "kind": "error",
            "prompt": (
                "В песне барда одна ошибка — в глаголе после модального. Найди её."
            ),
            "sentence": "Der Barde muss früh stehen auf.",
            "wrong": "stehen",
            "fix": {
                "options": ["stehen", "aufstehen", "aufstehe", "stehe auf"],
                "answer": 1,
                "explain": (
                    "С модальным глаголом основной глагол стоит в конце "
                    "инфинитивом целиком: muss früh aufstehen. Приставка не "
                    "отделяется."
                ),
            },
            "explain": (
                "После модального глагола приставка остаётся на месте: Der Barde "
                "muss früh aufstehen."
            ),
            "retry": {
                "prompt": (
                    "В песне барда одна ошибка — в глаголе после модального. "
                    "Найди её."
                ),
                "sentence": "Der Müller will das Tor machen zu.",
                "wrong": "machen",
                "fix": {
                    "options": ["machen", "macht zu", "zumachen", "zu machen"],
                    "answer": 2,
                    "explain": (
                        "После модального глагола инфинитив не отделяется: will "
                        "das Tor zumachen."
                    ),
                },
                "explain": (
                    "С модальным глаголом глагол стоит в конце целиком: Der "
                    "Müller will das Tor zumachen."
                ),
            },
        },
        {
            "id": "trennbare_5",
            "kind": "transform",
            "prompt": (
                "Скажи то же с модальным глаголом: «Ich stehe früh auf.» → "
                "с «müssen»"
            ),
            "options": [
                "Ich muss früh stehen auf.",
                "Ich muss früh auf stehen.",
                "Ich muss früh aufstehe.",
                "Ich muss früh aufstehen.",
            ],
            "answer": 3,
            "explain": (
                "С модальным глаголом основной глагол стоит в конце инфинитивом "
                "и не отделяется: Ich muss früh aufstehen."
            ),
            "retry": {
                "prompt": (
                    "Скажи то же с модальным глаголом: «Der Barde kommt mit.» → "
                    "с «wollen»"
                ),
                "options": [
                    "Der Barde will mit kommen.",
                    "Der Barde will mitkommen.",
                    "Der Barde will kommen mit.",
                    "Der Barde will mitkommt.",
                ],
                "answer": 1,
                "explain": (
                    "После wollen инфинитив mitkommen стоит целиком в конце: Der "
                    "Barde will mitkommen."
                ),
            },
        },
        {
            "id": "trennbare_6",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «Я встаю в шесть часов.»",
            "options": [
                "Ich stehe auf um sechs Uhr.",
                "Ich aufstehe um sechs Uhr.",
                "Ich stehe um sechs Uhr auf.",
                "Ich stehe um sechs Uhr aufstehen.",
            ],
            "answer": 2,
            "explain": (
                "Без модального глагола приставка отделяется и уходит в конец: "
                "Ich stehe um sechs Uhr auf."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «Мельник открывает ворота.»",
                "options": [
                    "Der Müller aufmacht das Tor.",
                    "Der Müller macht auf das Tor.",
                    "Der Müller macht das Tor aufmachen.",
                    "Der Müller macht das Tor auf.",
                ],
                "answer": 3,
                "explain": (
                    "aufmachen: глагол macht — на втором месте, приставка auf — "
                    "в конце предложения."
                ),
            },
        },
        {
            "id": "trennbare_7",
            "kind": "gap",
            "prompt": "Работа начинается рано: «Der Tag ___ früh an.» (anfangen)",
            "options": ["fangt", "fangen", "fängt", "fängst"],
            "answer": 2,
            "explain": (
                "der Tag — это er, сильный глагол anfangen даёт форму fängt, а "
                "приставка an уже стоит в конце. Fängst подходит только для du."
            ),
            "retry": {
                "prompt": "Мальчик идёт вместе со всеми: «Das Kind ___ zum Fluss mit.» (mitkommen)",
                "options": ["kommst", "kommt", "kommen", "kommt an"],
                "answer": 1,
                "explain": (
                    "das Kind — это er, поэтому kommt, а приставка mit стоит в "
                    "конце. Kommt an относилось бы к глаголу ankommen."
                ),
            },
        },
        {
            "id": "trennbare_8",
            "kind": "mc",
            "prompt": "Мельник закрывает мельницу. Какое предложение верно?",
            "options": [
                "Der Müller zu macht die Mühle.",
                "Der Müller macht zu die Mühle.",
                "Der Müller zumacht die Mühle.",
                "Der Müller macht die Mühle zu.",
            ],
            "answer": 3,
            "explain": (
                "Отделяемая приставка zu уходит в конец: Der Müller macht die "
                "Mühle zu. Рядом с глаголом она стоять не может."
            ),
            "retry": {
                "prompt": "Бард приходит на мельницу. Какое предложение верно?",
                "options": [
                    "Der Barde an kommt um sieben Uhr.",
                    "Der Barde kommt um sieben Uhr an.",
                    "Der Barde kommt an um sieben Uhr.",
                    "Der Barde ankommt um sieben Uhr.",
                ],
                "answer": 1,
                "explain": (
                    "ankommen: глагол kommt — на втором месте, приставка an — в "
                    "конце предложения: Der Barde kommt um sieben Uhr an."
                ),
            },
        },
    ],
}
