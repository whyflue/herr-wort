"""Тема 3. Personalpronomen und Verben im Präsens."""

TOPIC = {
    "id": "praesens",
    "nr": 3,
    "title": "Личные местоимения и глагол в Präsens",
    "short": "Глаголы в Präsens",
    "title_de": "Personalpronomen und Verben im Präsens",
    "location": "Бремен, трактир у ратуши",
    "location_de": "Bremen, Wirtshaus am Rathaus",
    "intro": (
        "В Бремене бард сворачивает к ратуше и заходит в трактир. Здесь тепло "
        "и шумно: служанка разносит блюда, хозяин расспрашивает гостей, "
        "а за столом кто-то хвастается дальней дорогой. Бард понимает: чтобы "
        "рассказать о себе, нужно менять глагол под каждое местоимение — "
        "ich singe, du singst, er singt. Он берёт лютню и пробует спеть о себе."
    ),
    "listen": (
        "Бард слушает трактир: хозяин спрашивает «Was trinkst du?», служанка "
        "напевает «Ich bringe Brot und Bier», а сосед за столом хвастается: "
        "«Ich fahre morgen nach Köln». Каждое лицо — своё окончание."
    ),
    "theory": [
        {
            "title": "Личные местоимения",
            "body": (
                "ich — я, du — ты, er — он, sie — она, es — оно, wir — мы, "
                "ihr — вы (друзья, не вежливая форма), sie — они, Sie — Вы "
                "(вежливо, всегда с большой буквы).\n\n"
                "er/sie/es выбираем по роду немецкого слова: der Wirt → er, "
                "die Laute → sie, das Lied → es.\n\n"
                "Важно: das Mädchen — средний род, поэтому es, хотя речь "
                "идёт о девушке.\n\n"
                "sie значит и «она», и «они»; форма глагола подскажет: "
                "sie singt — она поёт, sie singen — они поют.\n\n"
                "Вежливое Sie подходит и одному человеку, и нескольким: "
                "Wie heißen Sie?"
            ),
        },
        {
            "title": "Окончания в Präsens",
            "body": (
                "Слабые глаголы меняются по образцу machen:\n\n"
                "ich mache\n"
                "du machst\n"
                "er/sie/es macht\n"
                "wir machen\n"
                "ihr macht\n"
                "sie/Sie machen\n\n"
                "Окончания: -e, -st, -t, -en, -t, -en.\n\n"
                "Основа на -t или -d добавляет e: du arbeitest, er arbeitet.\n"
                "Основа на -s, -ß, -z во 2-м лице берёт только -t: "
                "du tanzt, du heißt, du sitzt.\n\n"
                "Глагол стоит в предложении на втором месте: Der Barde singt "
                "ein Lied. Heute singt der Barde ein Lied."
            ),
        },
        {
            "title": "Сильные глаголы меняют гласную",
            "body": (
                "Во 2-м и 3-м лице единственного числа у многих сильных "
                "глаголов меняется гласная в корне:\n\n"
                "fahren: du fährst, er fährt (a → ä)\n"
                "lesen: du liest, er liest (e → ie)\n"
                "nehmen: du nimmst, er nimmt (e → i)\n"
                "sehen: du siehst, er sieht\n"
                "essen: du isst, er isst\n\n"
                "В формах wir и ihr изменений нет: wir fahren, ihr fahrt, "
                "wir lesen, ihr lest.\n\n"
                "У du и er формы часто различаются только окончанием "
                "-st/-t: du nimmst, er nimmt."
            ),
        },
    ],
    "song_line": (
        "In Bremen sing ich, wer ich bin,\n"
        "und du, mein Wirt, hörst freundlich hin."
    ),
    "exercises": [
        {
            "id": "praesens_1",
            "kind": "gap",
            "prompt": (
                "Бард пробует голос в трактире: «Ich ___ ein Lied für den "
                "Wirt.» (singen)"
            ),
            "options": ["singe", "singst", "singt", "singen"],
            "answer": 0,
            "explain": (
                "С ich глагол получает окончание -e: ich singe. Остальные "
                "формы: du singst, er/sie/es singt, wir singen, ihr singt, "
                "sie singen."
            ),
            "retry": {
                "prompt": (
                    "Бард и трактирщик поют вместе: «Wir ___ zusammen im "
                    "Wirtshaus.» (singen)"
                ),
                "options": ["singt", "singen", "singe", "singst"],
                "answer": 1,
                "explain": (
                    "С wir глагол стоит в форме инфинитива: wir singen. "
                    "Форма singt — это er/sie/es или ihr."
                ),
            },
        },
        {
            "id": "praesens_2",
            "kind": "gap",
            "prompt": (
                "Трактирщик несёт ужин: «Der Wirt ___ Brot und Bier.» "
                "(bringen)"
            ),
            "options": ["bringen", "bringt", "bringst", "bringe"],
            "answer": 1,
            "explain": (
                "der Wirt — это er, поэтому окончание -t: er bringt. Форма "
                "bringen подходит для wir и sie, а bringst — только для du."
            ),
            "retry": {
                "prompt": (
                    "Гости в трактире шумят: «Ihr ___ heute sehr laut.» "
                    "(singen)"
                ),
                "options": ["singst", "singen", "singt", "singe"],
                "answer": 2,
                "explain": (
                    "ihr — «вы, друзья», окончание -t: ihr singt. Форма "
                    "singst бывает только у du."
                ),
            },
        },
        {
            "id": "praesens_3",
            "kind": "gap",
            "prompt": (
                "Бард расспрашивает о дороге: «Du ___ morgen nach Köln?» "
                "(fahren)"
            ),
            "options": ["fahrt", "fährt", "fährst", "fahren"],
            "answer": 2,
            "explain": (
                "fahren — сильный глагол: во 2-м лице a переходит в ä, "
                "поэтому du fährst. Форма fahrt — это ihr fahrt, "
                "а fahren — wir/sie fahren."
            ),
            "retry": {
                "prompt": (
                    "Бард листает книгу: «Der Barde ___ ein Buch über Köln.» "
                    "(lesen)"
                ),
                "options": ["lest", "liest", "lese", "lesen"],
                "answer": 1,
                "explain": (
                    "lesen — сильный глагол: во 2-м и 3-м лице e переходит "
                    "в ie. У du и er форма одна и та же: du liest, er liest."
                ),
            },
        },
        {
            "id": "praesens_4",
            "kind": "gap",
            "prompt": "Бард берёт кувшин: «Du ___ den Krug und trinkst.» (nehmen)",
            "options": ["nimmt", "nimmst", "nehmt", "nehme"],
            "answer": 1,
            "explain": (
                "nehmen меняет e на i: du nimmst, er nimmt. Форма nehmt — "
                "это ihr nehmt, а nehme — только ich."
            ),
            "retry": {
                "prompt": (
                    "Трактирщик убирает со стола: «Er ___ das Brot vom "
                    "Tisch.» (nehmen)"
                ),
                "options": ["nimmst", "nehmt", "nimmt", "nehmen"],
                "answer": 2,
                "explain": (
                    "Основа с i плюс окончание -t: er nimmt. Форма nimmst — "
                    "только для du, nehmen — для wir и sie."
                ),
            },
        },
        {
            "id": "praesens_5",
            "kind": "order",
            "prompt": "Собери предложение: сегодня бард поёт песню.",
            "words": ["Heute", "singt", "der", "Barde", "ein", "Lied"],
            "answer": "Heute singt der Barde ein Lied",
            "explain": (
                "Если предложение начинается с heute, глагол всё равно стоит "
                "на втором месте: Heute singt der Barde ein Lied. "
                "Подлежащее уходит после глагола."
            ),
            "retry": {
                "prompt": "Собери предложение: завтра бард едет в Кёльн.",
                "words": ["Morgen", "fährt", "der", "Barde", "nach", "Köln"],
                "answer": "Morgen fährt der Barde nach Köln",
                "explain": (
                    "Morgen fährt der Barde nach Köln: глагол на втором месте. "
                    "Сильный глагол fahren даёт форму er fährt."
                ),
            },
        },
        {
            "id": "praesens_6",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «Я пою, а ты играешь.»",
            "options": [
                "Ich singe, und du spielt.",
                "Ich singt, und du spielst.",
                "Ich singe, und du spielst.",
                "Ich singen, und du spielst.",
            ],
            "answer": 2,
            "explain": (
                "ich singe (окончание -e), du spielst (окончание -st). "
                "Форма spielt подходит только для er/sie/es или ihr."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «Мы поём, а вы танцуете.»",
                "options": [
                    "Wir singt, und ihr tanzt.",
                    "Wir singen, und ihr tanzt.",
                    "Wir singen, und ihr tanzen.",
                    "Wir singen, und ihr tanzst.",
                ],
                "answer": 1,
                "explain": (
                    "wir singen, ihr tanzt. У основы на -z во 2-м лице тоже "
                    "только -t: du tanzt, ihr tanzt."
                ),
            },
        },
        {
            "id": "praesens_7",
            "kind": "error",
            "prompt": "В песне барда одна ошибка — в окончании глагола. Найди её.",
            "sentence": "Du singen heute sehr laut.",
            "wrong": "singen",
            "fix": {
                "options": ["singt", "singst", "singe", "singen"],
                "answer": 1,
                "explain": (
                    "С du нужно окончание -st: du singst. Форма singen — "
                    "для wir и sie."
                ),
            },
            "explain": (
                "С du глагол получает окончание -st: du singst laut. "
                "Форма singen подходит только для wir и sie."
            ),
            "retry": {
                "prompt": "В песне барда одна ошибка — в форме глагола. Найди её.",
                "sentence": "Der Barde lest ein Buch über Köln.",
                "wrong": "lest",
                "fix": {
                    "options": ["lest", "lese", "liest", "lesen"],
                    "answer": 2,
                    "explain": (
                        "der Barde — это er, и сильный глагол lesen даёт "
                        "форму er liest."
                    ),
                },
                "explain": (
                    "С er глагол lesen даёт форму liest (e → ie). "
                    "Форма lest — это ihr lest."
                ),
            },
        },
        {
            "id": "praesens_8",
            "kind": "mc",
            "prompt": (
                "Бард поёт о девушке из трактира: «___ singt heute mit dem "
                "Wirt.» (das Mädchen)"
            ),
            "options": ["Sie", "Es", "Er", "Ihr"],
            "answer": 1,
            "explain": (
                "das Mädchen — средний род, поэтому местоимение es. По "
                "значению это девушка, но род немецкого слова важнее."
            ),
            "retry": {
                "prompt": (
                    "Бард поёт о трактирщике: «___ spielt auch Laute.» "
                    "(der Wirt)"
                ),
                "options": ["Sie", "Es", "Er", "Ihr"],
                "answer": 2,
                "explain": (
                    "der Wirt — мужской род, поэтому er. Местоимение "
                    "согласуется с родом немецкого слова."
                ),
            },
        },
    ],
}
