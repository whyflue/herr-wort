"""Тема 5. Modalverben: können, müssen, wollen."""

TOPIC = {
    "id": "modalverben",
    "nr": 5,
    "title": "Модальные глаголы: können, müssen, wollen",
    "short": "Модальные глаголы",
    "title_de": "Modalverben: können, müssen, wollen",
    "location": "Нюрнберг, замок мастера",
    "location_de": "Nürnberg, Burg des Meisters",
    "intro": (
        "Из Кёльна дорога поднимается в горы, и перед бардом вырастает "
        "нюрнбергский замок. У ворот стоит стража: без разрешения мастера "
        "внутрь нельзя. «Was willst du hier?», — спрашивает стражник. Бард "
        "хочет увидеть мастера, должен объяснить своё дело и не может найти "
        "нужных слов — а без них не скажешь ни «хочу», ни «должен»."
    ),
    "listen": (
        "Бард прижимается к каменной стене и слышит, как перекликаются в "
        "замке: «Ich muss noch arbeiten», «Kannst du mir helfen?», «Wir wollen "
        "heute nicht warten». В каждом предложении два глагола: один говорит, "
        "как относится к делу говорящий, а второй, в самом конце, — что именно "
        "делают."
    ),
    "theory": [
        {
            "title": "Два глагола: модальный и инфинитив",
            "body": (
                "Модальные глаголы говорят не о действии, а об отношении к нему: "
                "могу, должен, хочу.\n\n"
                "können — мочь, уметь;\n"
                "müssen — быть должным, нужно;\n"
                "wollen — хотеть.\n\n"
                "Сказуемое состоит из двух частей, они образуют рамку: модальный "
                "глагол стоит на втором месте, а инфинитив — в самом конце.\n\n"
                "Ich will den Meister sehen. Wir müssen heute arbeiten.\n\n"
                "В вопросе модальный глагол выходит на первое место: Kannst du "
                "mir helfen?\n\n"
                "Отрицание nicht стоит перед инфинитивом: Ich will nicht warten."
            ),
        },
        {
            "title": "Спряжение: у ich и er одна форма",
            "body": (
                "ich kann / muss / will\n"
                "du kannst / musst / willst\n"
                "er, sie, es kann / muss / will\n"
                "wir können / müssen / wollen\n"
                "ihr könnt / müsst / wollt\n"
                "sie, Sie können / müssen / wollen\n\n"
                "Главное: у ich и er/sie/es форма одинаковая, без окончания -t. "
                "Ich kann, er kann — нельзя сказать «er kannt». Так же: ich muss, "
                "er muss; ich will, er will.\n\n"
                "В единственном числе меняется корневой гласный: können → kann, "
                "müssen → muss, а у wollen меняется только форма du: du willst. "
                "Во множественном числе формы обычные: wir können, ihr könnt."
            ),
        },
        {
            "title": "Что значит какой глагол",
            "body": (
                "können — уметь или иметь возможность: Ich kann singen. Kann ich "
                "hier bleiben?\n\n"
                "müssen — быть должным, нужно: Ich muss arbeiten. Du musst leise "
                "sein.\n\n"
                "wollen — хотеть: Ich will schlafen. Wir wollen nach Wien fahren.\n\n"
                "Отрицания меняют смысл по-разному. Ich muss nicht arbeiten — "
                "«мне не нужно работать», это не обязательно. Ich will nicht "
                "arbeiten — «я не хочу работать». А запрет передают словами "
                "nicht dürfen: Du darfst nicht laut singen.\n\n"
                "Вопрос о разрешении обычно с können: Kann ich hier bleiben?"
            ),
        },
    ],
    "song_line": (
        "In Nürnberg auf der Burg, da kann ich viel,\n"
        "ich muss nur üben, und ich will mein Ziel."
    ),
    "exercises": [
        {
            "id": "modalverben_1",
            "kind": "gap",
            "prompt": (
                "Бард объясняет стражнику, зачем пришёл: «Ich ___ den Meister "
                "sehen.» (wollen)"
            ),
            "options": ["willst", "will", "wollen", "wollt"],
            "answer": 1,
            "explain": (
                "С ich модальный глагол wollen даёт форму will, и у er тоже will. "
                "Форма willst — только для du, wollt — для ihr, wollen — для wir "
                "и sie."
            ),
            "retry": {
                "prompt": (
                    "Стражник проверяет документы: «Der Wächter ___ den Namen "
                    "wissen.» (müssen)"
                ),
                "options": ["musst", "müsst", "muss", "müssen"],
                "answer": 2,
                "explain": (
                    "der Wächter — это er, поэтому muss. Форма musst подходит "
                    "только для du, müsst — для ihr, müssen — для wir и sie."
                ),
            },
        },
        {
            "id": "modalverben_2",
            "kind": "gap",
            "prompt": "Бард просит о помощи: «___ du mir helfen?» (können)",
            "options": ["Kann", "Könnt", "Kannst", "Können"],
            "answer": 2,
            "explain": (
                "С du у können появляется окончание -st и умлаут пропадает: du "
                "kannst. Форма kann — для ich и er, könnt — для ihr, können — "
                "для wir и sie."
            ),
            "retry": {
                "prompt": (
                    "Мастер спрашивает о раннем подъёме: «___ du morgen früh "
                    "aufstehen?» (müssen)"
                ),
                "options": ["Muss", "Musst", "Müsst", "Müssen"],
                "answer": 1,
                "explain": (
                    "С du форма musst. Muss стоит при ich и er, müsst — при ihr, "
                    "müssen — при wir и sie."
                ),
            },
        },
        {
            "id": "modalverben_3",
            "kind": "gap",
            "prompt": (
                "Бард и мастер работают вдвоём: «Wir ___ heute viel tun.» "
                "(müssen)"
            ),
            "options": ["müsst", "musst", "muss", "müssen"],
            "answer": 3,
            "explain": (
                "С wir форма совпадает с инфинитивом: wir müssen. Формы musst и "
                "muss стоят в единственном числе, müsst — при ihr."
            ),
            "retry": {
                "prompt": (
                    "Мастер обращается к работникам: «Ihr ___ das Tor schließen.» "
                    "(können)"
                ),
                "options": ["kann", "können", "könnt", "kannst"],
                "answer": 2,
                "explain": (
                    "У ihr форма könnt. Können подходит для wir и sie, kann — для "
                    "ich и er, kannst — только для du."
                ),
            },
        },
        {
            "id": "modalverben_4",
            "kind": "order",
            "prompt": "Собери предложение: бард хочет увидеть мастера.",
            "words": ["Der", "Barde", "will", "den", "Meister", "sehen"],
            "answer": "Der Barde will den Meister sehen",
            "explain": (
                "Модальный глагол will стоит на втором месте, а инфинитив sehen — "
                "в конце: Der Barde will den Meister sehen."
            ),
            "retry": {
                "prompt": "Собери предложение: стражник должен открыть ворота.",
                "words": ["Der", "Wächter", "muss", "das", "Tor", "öffnen"],
                "answer": "Der Wächter muss das Tor öffnen",
                "explain": (
                    "Модальный глагол — на втором месте, инфинитив — в самом "
                    "конце: Der Wächter muss das Tor öffnen."
                ),
            },
        },
        {
            "id": "modalverben_5",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «Я могу петь громко.»",
            "options": [
                "Ich kann laut singt.",
                "Ich kann singen laut.",
                "Ich kann laut singen.",
                "Ich laut kann singen.",
            ],
            "answer": 2,
            "explain": (
                "Модальный глагол на втором месте, инфинитив в конце: Ich kann "
                "laut singen. Форма singt здесь невозможна, а «singen laut» "
                "нарушает порядок слов."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «Мы хотим здесь остаться.»",
                "options": [
                    "Wir wollt hier bleiben.",
                    "Wir wollen hier bleiben.",
                    "Wir wollen hier bleibt.",
                    "Wir wollen bleiben hier.",
                ],
                "answer": 1,
                "explain": (
                    "С wir форма wollen, инфинитив bleiben — в конце: Wir wollen "
                    "hier bleiben. Форма wollt стоит при ihr, а bleibt — при er."
                ),
            },
        },
        {
            "id": "modalverben_6",
            "kind": "mc",
            "prompt": (
                "Бард просит у мастера помощи. Какое предложение верно?"
            ),
            "options": [
                "Kannst du mir helfe?",
                "Kannst du mir helfen?",
                "Kannst du helfen mir?",
                "Kann du mir helfen?",
            ],
            "answer": 1,
            "explain": (
                "В вопросе модальный глагол стоит первым: Kannst du mir helfen? "
                "Инфинитив — в конце. Форма kann подходит для ich и er, а не "
                "для du."
            ),
            "retry": {
                "prompt": (
                    "Бард говорит мастеру о ночлеге. Какое предложение верно?"
                ),
                "options": [
                    "Ich will hier schlafe.",
                    "Ich will schlafen hier.",
                    "Ich will hier schlafen.",
                    "Ich wolle hier schlafen.",
                ],
                "answer": 2,
                "explain": (
                    "Ich will hier schlafen: модальный глагол на втором месте, "
                    "инфинитив в конце. У ich форма will, а не wolle."
                ),
            },
        },
        {
            "id": "modalverben_7",
            "kind": "error",
            "prompt": (
                "В песне барда одна ошибка — в форме глагола после модального. "
                "Найди её."
            ),
            "sentence": "Der Barde muss den Meister sehe.",
            "wrong": "sehe",
            "fix": {
                "options": ["sieht", "sehen", "sehe", "sah"],
                "answer": 1,
                "explain": (
                    "После модального глагола стоит инфинитив: muss ... sehen. "
                    "Форма sieht — для er без модального глагола."
                ),
            },
            "explain": (
                "После модального глагола всегда инфинитив в конце: Der Barde "
                "muss den Meister sehen."
            ),
            "retry": {
                "prompt": (
                    "В песне барда одна ошибка — в форме глагола после "
                    "модального. Найди её."
                ),
                "sentence": "Der Wächter will das Tor schließt.",
                "wrong": "schließt",
                "fix": {
                    "options": ["schließt", "schließe", "schließen", "schloss"],
                    "answer": 2,
                    "explain": (
                        "После will нужен инфинитив: will das Tor schließen. "
                        "Форма schließt подходит для er без модального глагола."
                    ),
                },
                "explain": (
                    "Модальный глагол требует инфинитива в конце: Der Wächter "
                    "will das Tor schließen."
                ),
            },
        },
        {
            "id": "modalverben_8",
            "kind": "gap",
            "prompt": (
                "Мастер видит, что бард устал: «Du ___ nicht arbeiten, du "
                "kannst schlafen.» (müssen)"
            ),
            "options": ["willst", "musst", "kannst", "müssen"],
            "answer": 1,
            "explain": (
                "Du musst nicht arbeiten — «тебе не нужно работать». При du у "
                "müssen форма musst; wollen и können не подходят по смыслу."
            ),
            "retry": {
                "prompt": (
                    "Мастер разрешает остаться: «Du ___ heute hier bleiben.» "
                    "(können)"
                ),
                "options": ["willst", "musst", "kannst", "können"],
                "answer": 2,
                "explain": (
                    "Разрешение передаёт können: du kannst hier bleiben. "
                    "Musst означало бы «должен», а wollen — «хочешь»."
                ),
            },
        },
    ],
}
