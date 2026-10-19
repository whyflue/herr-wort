"""Тема 9. Präteritum von sein, haben und Modalverben."""

TOPIC = {
    "id": "praeteritum",
    "nr": 9,
    "title": "Претеритум: sein, haben, модальные глаголы",
    "short": "Präteritum: sein/haben",
    "title_de": "Präteritum von sein, haben, Modalverben",
    "location": "Вартбург, замок легенд",
    "location_de": "Wartburg, Schloss der Legenden",
    "intro": (
        "Дорога ведёт барда в Вартбург — замок, где стены помнят легенды. В зале "
        "у очага старики рассказывают о королях и певцах: кто здесь жил, чего "
        "хотел и что мог. Бард слушает и пересказывает истории дальше, а для "
        "рассказа о прошлом нужны самые частые формы: war, hatte, konnte, "
        "musste, wollte."
    ),
    "listen": (
        "Бард слушает, как гудят своды Вартбурга. У очага старик ведёт рассказ: "
        "«Es war einmal ein König. Er hatte eine Tochter. Sie wollte singen, aber "
        "sie konnte nicht.» Каждое слово о прошлом — это war, hatte, wollte, "
        "konnte; их форма зависит от того, кто действует."
    ),
    "theory": [
        {
            "title": "Präteritum: sein и haben",
            "body": (
                "В рассказе о прошлом важнее всего две таблицы.\n\n"
                "sein: ich war, du warst, er/sie/es war, wir waren, ihr wart, "
                "sie/Sie waren.\n\n"
                "haben: ich hatte, du hattest, er/sie/es hatte, wir hatten, "
                "ihr hattet, sie/Sie hatten.\n\n"
                "Es war einmal ein König. Er hatte eine schöne Tochter. Wir waren "
                "müde.\n\n"
                "Формы ich и er совпадают: ich war, er war; ich hatte, er hatte. "
                "Отличается только du: du warst, du hattest."
            ),
        },
        {
            "title": "Модальные глаголы в Präteritum",
            "body": (
                "Модальные глаголы теряют умляут и получают окончания как у sein "
                "и haben:\n\n"
                "können → konnte, müssen → musste, wollen → wollte, dürfen → "
                "durfte, sollen → sollte, mögen → mochte.\n\n"
                "Ich konnte nicht singen. Der König musste bleiben. Die Sänger "
                "wollten spielen.\n\n"
                "У ich и er окончания нет: ich musste, er musste. У du — -st: "
                "du musstest. У wir, sie — -en: wir mussten."
            ),
        },
        {
            "title": "Präteritum в рассказе",
            "body": (
                "Präteritum — время рассказчика: так звучат легенды, сказки и "
                "старые истории. В разговоре чаще говорят в Perfekt.\n\n"
                "Es war einmal ein Barde. Er hatte eine Laute und wollte singen. "
                "Aber er konnte die Worte nicht finden.\n\n"
                "Сначала назови, когда это было и что было (war, hatte), потом "
                "скажи, что герой мог, должен был или хотел (konnte, musste, "
                "wollte). После модального глагола стоит инфинитив: er wollte "
                "singen."
            ),
        },
    ],
    "song_line": (
        "Ich saß auf der Wartburg im Kerzenschein,\n"
        "die alten Sagen waren mein."
    ),
    "exercises": [
        {
            "id": "praeteritum_1",
            "kind": "gap",
            "prompt": "Ich ___ gestern auf der Wartburg. (sein)",
            "options": ["war", "hatte", "konnte", "wollte"],
            "answer": 0,
            "explain": (
                "От sein форма для ich — war. Форма hatte — от haben, а konnte и "
                "wollte требуют после себя инфинитив."
            ),
            "retry": {
                "prompt": "Ich ___ früher eine alte Laute. (haben)",
                "options": ["hatte", "war", "konnte", "wollte"],
                "answer": 0,
                "explain": (
                    "От haben форма для ich — hatte: ich hatte eine Laute. "
                    "Модальные глаголы здесь невозможны без инфинитива."
                ),
            },
        },
        {
            "id": "praeteritum_2",
            "kind": "gap",
            "prompt": "___ du früher auf der Wartburg? (sein)",
            "options": ["Warst", "Wart", "Bist", "Hattest"],
            "answer": 0,
            "explain": (
                "У du форма warst. Wart — это форма для ihr, bist — Präsens, "
                "а hattest — от другого глагола."
            ),
            "retry": {
                "prompt": "Du ___ damals eine schöne Laute. (haben)",
                "options": ["hattest", "hatte", "hattet", "hat"],
                "answer": 0,
                "explain": (
                    "У du форма hattest. Hattet — для ihr, hatte — для ich и er, "
                    "hat — Präsens."
                ),
            },
        },
        {
            "id": "praeteritum_3",
            "kind": "gap",
            "prompt": "Es war einmal ein König. Er ___ sehr alt. (sein)",
            "options": ["war", "warst", "wart", "gewesen"],
            "answer": 0,
            "explain": (
                "У er форма war, она совпадает с формой для ich: ich war, er war. "
                "Gewesen — это Partizip II, а не Präteritum."
            ),
            "retry": {
                "prompt": "Es war einmal ein König. Er ___ eine schöne Tochter. (haben)",
                "options": ["hatte", "hattest", "hattet", "gehabt"],
                "answer": 0,
                "explain": (
                    "У er форма hatte (как у ich). Hattest — для du, hattet — "
                    "для ihr, gehabt — Partizip II."
                ),
            },
        },
        {
            "id": "praeteritum_4",
            "kind": "gap",
            "prompt": (
                "Der Barde kannte die Wörter nicht, deshalb ___ er nicht singen. "
                "(können)"
            ),
            "options": ["konnte", "konntest", "konntet", "gekonnt"],
            "answer": 0,
            "explain": (
                "У er/sie/es в Präteritum нет окончания: er konnte. Konntest — "
                "для du, konntet — для ihr, gekonnt — Partizip II."
            ),
            "retry": {
                "prompt": (
                    "Der König sagte: «Bleib!», deshalb ___ der Barde auf der Burg "
                    "bleiben. (müssen)"
                ),
                "options": ["musste", "musstest", "musstet", "gemusst"],
                "answer": 0,
                "explain": (
                    "У er форма musste: er musste bleiben. Musstest — для du, "
                    "musstet — для ihr."
                ),
            },
        },
        {
            "id": "praeteritum_5",
            "kind": "transform",
            "prompt": (
                "Бард говорит о настоящем: «Der Barde ist müde.» Расскажи то же "
                "о прошлом — поставь sein в Präteritum."
            ),
            "options": [
                "Der Barde war müde.",
                "Der Barde hatte müde.",
                "Der Barde ist müde.",
                "Der Barde wart müde.",
            ],
            "answer": 0,
            "explain": (
                "sein в Präteritum для er — war: Der Barde war müde. Форма hatte "
                "идёт от haben, а wart — это форма для ihr."
            ),
            "retry": {
                "prompt": (
                    "Бард говорит о настоящем: «Ich will ein Lied singen.» "
                    "Расскажи то же о прошлом."
                ),
                "options": [
                    "Ich wollte ein Lied singen.",
                    "Ich willte ein Lied singen.",
                    "Ich wollte ein Lied gesungen.",
                    "Ich will ein Lied singen.",
                ],
                "answer": 0,
                "explain": (
                    "wollen в Präteritum: ich wollte (без умляута и без -t "
                    "в конце). После модального глагола стоит инфинитив: singen."
                ),
            },
        },
        {
            "id": "praeteritum_6",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «Вчера я был на Вартбурге.»",
            "options": [
                "Gestern war ich auf der Wartburg.",
                "Gestern ich war auf der Wartburg.",
                "Gestern hatte ich auf der Wartburg.",
                "Gestern bin ich auf der Wartburg.",
            ],
            "answer": 0,
            "explain": (
                "Сказуемое стоит на втором месте: Gestern war ich ... Форма war — "
                "это Präteritum от sein."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «Мы должны были долго ждать.»",
                "options": [
                    "Wir mussten lange warten.",
                    "Wir mussten lange gewartet.",
                    "Wir musste lange warten.",
                    "Wir musst lange warten.",
                ],
                "answer": 0,
                "explain": (
                    "У wir форма mussten. После модального глагола — инфинитив "
                    "warten, а не Partizip II."
                ),
            },
        },
        {
            "id": "praeteritum_7",
            "kind": "error",
            "prompt": (
                "В предложении барда одна ошибка — форма глагола в Präteritum. "
                "Найди её."
            ),
            "sentence": "Gestern warst ich auf der Wartburg.",
            "wrong": "warst",
            "fix": {
                "options": ["war", "waren", "wart", "bin"],
                "answer": 0,
                "explain": (
                    "С ich употребляется форма war: Gestern war ich auf der "
                    "Wartburg. Warst — форма для du."
                ),
            },
            "explain": (
                "У ich в Präteritum форма war (как у er). Warst подходит только "
                "к du, wart — к ihr."
            ),
            "retry": {
                "prompt": (
                    "В предложении барда одна ошибка — форма глагола в Präteritum. "
                    "Найди её."
                ),
                "sentence": "Der König wolltet auf der Burg bleiben.",
                "wrong": "wolltet",
                "fix": {
                    "options": ["wollte", "wollten", "wolltest", "will"],
                    "answer": 0,
                    "explain": (
                        "У er/sie/es форма wollte: Der König wollte auf der Burg "
                        "bleiben. Wolltet — форма для ihr."
                    ),
                },
                "explain": (
                    "У er в Präteritum нет окончания -t: er wollte. Wolltet — "
                    "форма для ihr."
                ),
            },
        },
        {
            "id": "praeteritum_8",
            "kind": "mc",
            "prompt": "Бард начинает легенду о замке. Какой зачин верен?",
            "options": [
                "Es war einmal ein König.",
                "Es hatte einmal ein König.",
                "Es war einmal einen König.",
                "Es waren einmal ein König.",
            ],
            "answer": 0,
            "explain": (
                "Зачин легенд и сказок: Es war einmal ... Подлежащее стоит "
                "в Nominativ: ein König. Форма waren подходит только ко "
                "множественному числу."
            ),
            "retry": {
                "prompt": "Бард рассказывает о прошлом. Какой вариант верен?",
                "options": [
                    "Er hatte eine Laute.",
                    "Er hatten eine Laute.",
                    "Er hattest eine Laute.",
                    "Er hat eine Laute.",
                ],
                "answer": 0,
                "explain": (
                    "У er форма hatte (как у ich). Hatten — для wir/sie, hattest — "
                    "для du, hat — Präsens."
                ),
            },
        },
    ],
}
