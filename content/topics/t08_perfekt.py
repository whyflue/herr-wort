"""Тема 8. Perfekt mit haben und sein."""

TOPIC = {
    "id": "perfekt",
    "nr": 8,
    "title": "Perfekt с haben и sein",
    "short": "Perfekt: haben/sein",
    "title_de": "Perfekt mit haben/sein",
    "location": "Ротенбург-на-Таубере, городская стена",
    "location_de": "Rothenburg ob der Tauber, Stadtmauer",
    "intro": (
        "Дорога приводит барда в Ротенбург, и он поднимается на городскую стену. "
        "Отсюда видно всю долину, а вечером здесь собираются путники: каждый "
        "рассказывает, где он был и что успел сделать. Бард тоже хочет рассказать "
        "о своей дороге, но для прошедшего времени одного глагола мало."
    ),
    "listen": (
        "Бард прижимается ухом к тёплым камням стены. Внизу скрипят телеги и "
        "звучат чужие рассказы: «Ich bin heute früh gekommen», «Er hat die ganze "
        "Nacht gesungen», «Wir sind bis zum Tor gegangen». В каждом — два глагола: "
        "haben или sein на втором месте и Partizip II в самом конце."
    ),
    "theory": [
        {
            "title": "Рамка Perfekt: два глагола",
            "body": (
                "Perfekt — прошедшее время для разговора и рассказа. Сказуемое "
                "состоит из двух частей, они образуют рамку:\n\n"
                "haben или sein — на втором месте;\n"
                "Partizip II — в самом конце.\n\n"
                "Ich habe ein Lied gesungen. Der Barde ist zur Mauer gegangen.\n\n"
                "Вспомогательный глагол спрягается: ich habe/bin, du hast/bist, "
                "er hat/ist, wir haben/sind.\n\n"
                "Все остальные слова стоят между ними: Ich habe gestern auf der "
                "Mauer gesungen."
            ),
        },
        {
            "title": "haben или sein?",
            "body": (
                "С sein идут глаголы движения и смены состояния: gehen, fahren, "
                "kommen, laufen, aufstehen, einschlafen.\n\n"
                "Der Barde ist nach Rothenburg gefahren. Ich bin früh aufgestanden. "
                "Die Stadt ist schön geworden.\n\n"
                "Остальные глаголы — с haben: machen, singen, kaufen, sehen, finden, "
                "helfen, lesen.\n\n"
                "Ich habe die Stadt gesehen. Er hat mir geholfen. Wir haben Brot "
                "gekauft.\n\n"
                "Подсказка: движение «куда-то» и смена состояния — sein, обычное "
                "действие — haben."
            ),
        },
        {
            "title": "Partizip II: как построить",
            "body": (
                "Слабые глаголы: ge- + основа + -t: machen → gemacht, kaufen → "
                "gekauft, sagen → gesagt.\n\n"
                "Сильные глаголы меняют гласную и кончаются на -en: singen → "
                "gesungen, sehen → gesehen, kommen → gekommen, gehen → gegangen, "
                "finden → gefunden.\n\n"
                "Без ge-: глаголы с неотделяемыми приставками be-, ver-, er- и "
                "глаголы на -ieren: besuchen → besucht, verlieren → verloren, "
                "studieren → studiert.\n\n"
                "Partizip II всегда стоит в конце: Wir haben lange gesungen."
            ),
        },
    ],
    "song_line": (
        "Ich bin durch Täler und Städte gegangen,\n"
        "habe am Rothenburger Tor ein Lied angefangen."
    ),
    "exercises": [
        {
            "id": "perfekt_1",
            "kind": "gap",
            "prompt": "Ich ___ gestern die Stadtmauer gesehen. (haben oder sein)",
            "options": ["habe", "bin", "ist", "hat"],
            "answer": 0,
            "explain": (
                "sehen — не движение и не смена состояния, значит вспомогательный "
                "глагол haben: ich habe gesehen. Форма bin здесь невозможна."
            ),
            "retry": {
                "prompt": "Ich ___ früh aufgestanden. (haben oder sein)",
                "options": ["bin", "habe", "ist", "hat"],
                "answer": 0,
                "explain": (
                    "aufstehen — движение и смена состояния (я встаю с постели), "
                    "поэтому sein: ich bin aufgestanden."
                ),
            },
        },
        {
            "id": "perfekt_2",
            "kind": "gap",
            "prompt": "Der Barde ___ schon nach Rothenburg gekommen. (haben oder sein)",
            "options": ["ist", "hat", "habe", "sind"],
            "answer": 0,
            "explain": (
                "kommen — движение по направлению (куда?), поэтому sein: er ist "
                "gekommen. С haben этот глагол в Perfekt не употребляется."
            ),
            "retry": {
                "prompt": "Der Torwächter ___ das Tor geschlossen. (haben oder sein)",
                "options": ["hat", "ist", "habe", "sind"],
                "answer": 0,
                "explain": (
                    "schließen — обычное действие, а не движение: der Torwächter "
                    "hat das Tor geschlossen."
                ),
            },
        },
        {
            "id": "perfekt_3",
            "kind": "transform",
            "prompt": (
                "Бард идёт по стене и говорит о настоящем: «Der Barde geht zur "
                "Stadtmauer.» Скажи то же в Perfekt."
            ),
            "options": [
                "Der Barde ist zur Stadtmauer gegangen.",
                "Der Barde hat zur Stadtmauer gegangen.",
                "Der Barde geht zur Stadtmauer gegangen.",
                "Der Barde ist gegangen zur Stadtmauer.",
            ],
            "answer": 0,
            "explain": (
                "gehen — движение, поэтому вспомогательный глагол sein: ist ... "
                "gegangen. Partizip II стоит в самом конце предложения."
            ),
            "retry": {
                "prompt": (
                    "Бард поёт песню и говорит о настоящем: «Ich singe ein Lied.» "
                    "Скажи то же в Perfekt."
                ),
                "options": [
                    "Ich habe ein Lied gesungen.",
                    "Ich bin ein Lied gesungen.",
                    "Ich habe ein Lied gesingt.",
                    "Ich habe gesungen ein Lied.",
                ],
                "answer": 0,
                "explain": (
                    "singen — не движение, поэтому haben: ich habe gesungen. "
                    "Partizip II от singen — gesungen (не gesingt), и оно стоит "
                    "в конце."
                ),
            },
        },
        {
            "id": "perfekt_4",
            "kind": "order",
            "prompt": "Собери предложение: бард пел песню у ворот (Perfekt).",
            "words": ["Der", "Barde", "hat", "am", "Tor", "ein", "Lied", "gesungen"],
            "answer": "Der Barde hat am Tor ein Lied gesungen",
            "explain": (
                "Рамка Perfekt: вспомогательный глагол hat стоит на втором месте, "
                "Partizip II gesungen — в самом конце."
            ),
            "retry": {
                "prompt": "Собери предложение: мы быстро дошли до городской стены.",
                "words": ["Wir", "sind", "schnell", "zur", "Stadtmauer", "gelaufen"],
                "answer": "Wir sind schnell zur Stadtmauer gelaufen",
                "explain": (
                    "laufen — движение, поэтому sein: wir sind gelaufen. Partizip II "
                    "закрывает предложение."
                ),
            },
        },
        {
            "id": "perfekt_5",
            "kind": "error",
            "prompt": "В предложении барда одна ошибка — в форме Partizip II. Найди её.",
            "sentence": "Der Barde hat ein Lied gesingt.",
            "wrong": "gesingt",
            "fix": {
                "options": ["gesungen", "gesingt", "singt", "singen"],
                "answer": 0,
                "explain": (
                    "singen — сильный глагол: Partizip II — gesungen. Форма gesingt "
                    "сделана по образцу слабых глаголов, это ошибка."
                ),
            },
            "explain": (
                "Partizip II от singen — gesungen (сильный глагол, окончание -en). "
                "Форма gesingt — типичная ошибка."
            ),
            "retry": {
                "prompt": "В предложении барда одна ошибка — в форме Partizip II. Найди её.",
                "sentence": "Wir haben die Stadt geseht.",
                "wrong": "geseht",
                "fix": {
                    "options": ["gesehen", "geseht", "sieht", "sehen"],
                    "answer": 0,
                    "explain": (
                        "sehen — сильный глагол: sehen → gesehen. Форма geseht "
                        "неверна."
                    ),
                },
                "explain": "sehen — сильный глагол, его Partizip II — gesehen.",
            },
        },
        {
            "id": "perfekt_6",
            "kind": "error",
            "prompt": (
                "В предложении барда одна ошибка — в выборе вспомогательного "
                "глагола. Найди её."
            ),
            "sentence": "Gestern bin ich die Stadtmauer gesehen.",
            "wrong": "bin",
            "fix": {
                "options": ["habe", "hat", "ist", "sind"],
                "answer": 0,
                "explain": (
                    "sehen — не движение, поэтому Perfekt образуется с haben: "
                    "Ich habe die Stadtmauer gesehen."
                ),
            },
            "explain": (
                "sehen требует вспомогательный глагол haben: ich habe gesehen. "
                "Вспомогательный глагол согласуется с подлежащим: ich → habe."
            ),
            "retry": {
                "prompt": (
                    "В предложении барда одна ошибка — в выборе вспомогательного "
                    "глагола. Найди её."
                ),
                "sentence": "Der Barde hat zum Tor gegangen.",
                "wrong": "hat",
                "fix": {
                    "options": ["ist", "bin", "sind", "habe"],
                    "answer": 0,
                    "explain": (
                        "gehen — движение, поэтому sein: Der Barde ist zum Tor "
                        "gegangen."
                    ),
                },
                "explain": "gehen — движение, значит sein: der Barde ist gegangen.",
            },
        },
        {
            "id": "perfekt_7",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «Я уже спел песню.»",
            "options": [
                "Ich habe schon ein Lied gesungen.",
                "Ich bin schon ein Lied gesungen.",
                "Ich habe schon ein Lied gesingt.",
                "Ich habe schon gesungen ein Lied.",
            ],
            "answer": 0,
            "explain": (
                "singen — с haben, Partizip II gesungen стоит в конце: Ich habe "
                "schon ein Lied gesungen."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «Мы уже пришли в город.»",
                "options": [
                    "Wir sind schon in die Stadt gekommen.",
                    "Wir haben schon in die Stadt gekommen.",
                    "Wir sind schon in die Stadt gekommt.",
                    "Wir sind gekommen schon in die Stadt.",
                ],
                "answer": 0,
                "explain": (
                    "kommen — движение, поэтому sein: wir sind gekommen. Partizip "
                    "II — gekommen, и оно стоит в конце."
                ),
            },
        },
        {
            "id": "perfekt_8",
            "kind": "gap",
            "prompt": "Der Barde ist nach Rothenburg ___. (kommen)",
            "options": ["gekommen", "gekommt", "gekonnt", "kommt"],
            "answer": 0,
            "explain": (
                "Partizip II от kommen — gekommen (сильный глагол). Оно стоит "
                "в конце предложения, после вспомогательного глагола ist."
            ),
            "retry": {
                "prompt": "Wir haben auf der Mauer ___. (singen)",
                "options": ["gesungen", "gesingt", "singen", "sang"],
                "answer": 0,
                "explain": (
                    "Partizip II от singen — gesungen. Форма sang — это Präteritum, "
                    "а в Perfekt нужен Partizip II."
                ),
            },
        },
    ],
}
