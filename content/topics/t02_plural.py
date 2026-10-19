"""Тема 2. Plural der Substantive."""

TOPIC = {
    "id": "plural",
    "nr": 2,
    "title": "Множественное число существительных",
    "short": "Множественное число",
    "title_de": "Plural der Substantive",
    "location": "Гамбург, порт",
    "location_de": "Hamburg, Hafen",
    "intro": (
        "Бард доходит до Гамбурга по берегу и спускается в порт. Ветер несёт "
        "крик чаек, матросы катят бочки, на причале громоздятся тюки и ящики. "
        "Бард хочет воспеть весь этот шум, но одна бочка — das Fass, а их "
        "много... как сказать? Перо замирает над пергаментом."
    ),
    "listen": (
        "Бард садится на перевёрнутый ящик и слушает порт: волны бьют в борта "
        "(das Schiff — die Schiffe), чайки кричат над мачтами (die Möwe — "
        "die Möwen), а старый боцман считает бочки: «ein Fass, zwei Fässer, "
        "drei Fässer»."
    ),
    "theory": [
        {
            "title": "Пять окончаний множественного числа",
            "body": (
                "Во множественном числе существительное получает одно из "
                "окончаний: -e, -en/-n, -er, -s — или не меняется вовсе.\n\n"
                "-e: der Tisch → die Tische, das Schiff → die Schiffe, "
                "das Seil → die Seile\n"
                "-en/-n: die Frau → die Frauen, die Kiste → die Kisten, "
                "der Matrose → die Matrosen\n"
                "-er (часто с умлаутом): das Kind → die Kinder, "
                "das Fass → die Fässer, das Buch → die Bücher\n"
                "-s: das Auto → die Autos, das Foto → die Fotos\n"
                "без окончания: der Anker → die Anker, der Hafen → die Häfen, "
                "das Mädchen → die Mädchen\n\n"
                "Окончание запоминают вместе со словом: der Sack — die Säcke."
            ),
        },
        {
            "title": "Артикль во множественном числе — всегда die",
            "body": (
                "Во множественном числе у всех существительных артикль die, "
                "независимо от рода в единственном числе:\n\n"
                "der Sack → die Säcke, die Kiste → die Kisten, "
                "das Fass → die Fässer.\n\n"
                "Неопределённого артикля во множественном числе нет: "
                "ein Sack → Säcke. После mein, dein, kein артикль тоже "
                "не нужен: meine Säcke, keine Fässer.\n\n"
                "Числительные и слова viele, wenige сами показывают "
                "множественное число: drei Schiffe, viele Matrosen, "
                "zwei Kisten.\n\n"
                "Глагол тоже ставят во множественное число: Das Schiff kommt. "
                "→ Die Schiffe kommen. Der Matrose trägt. → Die Matrosen tragen."
            ),
        },
        {
            "title": "Как выбрать окончание",
            "body": (
                "Женские слова чаще всего берут -(e)n: die Frau → die Frauen, "
                "die Möwe → die Möwen, die Kiste → die Kisten. Слова на -in "
                "удваивают n: die Sängerin → die Sängerinnen.\n\n"
                "Слова на -er, -en, -el часто не меняются: der Anker → "
                "die Anker, der Kuchen → die Kuchen; иногда появляется умлаут: "
                "der Hafen → die Häfen, der Garten → die Gärten.\n\n"
                "Односложные слова часто берут -e или -er: das Boot → "
                "die Boote, der Tag → die Tage, das Netz → die Netze, "
                "der Mann → die Männer, das Fass → die Fässer.\n\n"
                "Заимствованные слова берут -s: das Auto → die Autos, "
                "das Hobby → die Hobbys.\n\n"
                "Сомневаешься — проверь словарь: слово учат сразу с формой "
                "множественного числа."
            ),
        },
    ],
    "song_line": (
        "Am Hamburger Kai, wo die Möwen schrein,\n"
        "zähl ich die Fässer und reim sie mir ein."
    ),
    "exercises": [
        {
            "id": "plural_1",
            "kind": "gap",
            "prompt": (
                "Матрос катит по причалу бочки: «Der Matrose rollt zwei ___ "
                "über den Kai.» (das Fass)"
            ),
            "options": ["Fässern", "Fässer", "Fasser", "Fasses"],
            "answer": 1,
            "explain": (
                "das Fass → die Fässer: односложное среднее слово берёт -er "
                "и умлаут. Fässern — это Dativ, а формы Fasser и Fasses "
                "неверны."
            ),
            "retry": {
                "prompt": (
                    "Матрос несёт мешки на корабль: «Der Matrose trägt zwei "
                    "___ zum Schiff.» (der Sack)"
                ),
                "options": ["Säcken", "Säcke", "Sacks", "Sackes"],
                "answer": 1,
                "explain": (
                    "der Sack → die Säcke: односложное мужское слово берёт -e "
                    "и умлаут. Säcken — Dativ множественного числа, "
                    "Sacks и Sackes — неверные формы."
                ),
            },
        },
        {
            "id": "plural_2",
            "kind": "gap",
            "prompt": (
                "Бард смотрит на рейд: «Im Hafen liegen viele ___.» "
                "(das Schiff)"
            ),
            "options": ["Schiffs", "Schiffe", "Schiffen", "Schiffes"],
            "answer": 1,
            "explain": (
                "das Schiff → die Schiffe: тип -e. После viele артикль "
                "не нужен, а Schiffs и Schiffes — формы единственного числа, "
                "Schiffen — Dativ."
            ),
            "retry": {
                "prompt": (
                    "На причале стоят моряки: «Am Kai stehen drei ___ .» "
                    "(der Matrose)"
                ),
                "options": ["Matrosen", "Matrose", "Matroses"],
                "answer": 0,
                "explain": (
                    "der Matrose → die Matrosen: слова на -e часто берут -n. "
                    "Matrose — единственное число, Matroses — ошибка по "
                    "образцу английского языка."
                ),
            },
        },
        {
            "id": "plural_3",
            "kind": "transform",
            "prompt": (
                "Бард поёт: «Das Schiff kommt in den Hafen.» Спой то же "
                "о нескольких кораблях."
            ),
            "options": [
                "Die Schiffen kommen in den Hafen.",
                "Die Schiffe kommen in den Hafen.",
                "Die Schiffe kommt in den Hafen.",
                "Die Schiffs kommen in den Hafen.",
            ],
            "answer": 1,
            "explain": (
                "die Schiffe — множественное число, значит и глагол во "
                "множественном: kommen. Формы Schiffen, Schiffs и форма "
                "глагола kommt здесь неверны."
            ),
            "retry": {
                "prompt": (
                    "Бард поёт: «Die Möwe fliegt über das Wasser.» Спой "
                    "о стае чаек."
                ),
                "options": [
                    "Die Möwes fliegen über das Wasser.",
                    "Die Möwen fliegt über das Wasser.",
                    "Die Möwen fliegen über das Wasser.",
                    "Die Möwe fliegen über das Wasser.",
                ],
                "answer": 2,
                "explain": (
                    "die Möwe → die Möwen (-n), глагол тоже во множественном "
                    "числе: Die Möwen fliegen. Форма Möwes невозможна, "
                    "а без -n пропадает множественное число."
                ),
            },
        },
        {
            "id": "plural_4",
            "kind": "order",
            "prompt": "Собери предложение: в порту лежат три корабля.",
            "words": ["Im", "Hafen", "liegen", "drei", "Schiffe"],
            "answer": "Im Hafen liegen drei Schiffe",
            "explain": (
                "Сначала обстоятельство, потом глагол: Im Hafen liegen. "
                "После числительного drei артикль не нужен: drei Schiffe."
            ),
            "retry": {
                "prompt": "Собери предложение: на причале стоят многие ящики.",
                "words": ["Auf", "dem", "Kai", "stehen", "viele", "Kisten"],
                "answer": "Auf dem Kai stehen viele Kisten",
                "explain": (
                    "Auf dem Kai stehen viele Kisten. die Kiste → die Kisten: "
                    "женское слово берёт -n."
                ),
            },
        },
        {
            "id": "plural_5",
            "kind": "error",
            "prompt": (
                "В песне барда одна ошибка — в форме множественного числа. "
                "Найди её."
            ),
            "sentence": "Im Hamburger Hafen liegen viele Schiffs.",
            "wrong": "Schiffs",
            "fix": {
                "options": ["Schiffen", "Schiffes", "Schiffe", "Schiffs"],
                "answer": 2,
                "explain": (
                    "das Schiff → die Schiffe: односложное слово берёт -e. "
                    "Schiffs и Schiffes — единственное число, Schiffen — Dativ."
                ),
            },
            "explain": (
                "После viele нужно множественное число: viele Schiffe. "
                "Ошибка в слове Schiffs — так множественное число "
                "не образуется."
            ),
            "retry": {
                "prompt": (
                    "В песне барда одна ошибка — в форме множественного "
                    "числа. Найди её."
                ),
                "sentence": "Am Kai tragen drei Matrose die Kisten.",
                "wrong": "Matrose",
                "fix": {
                    "options": ["Matrosen", "Matrose", "Matroses"],
                    "answer": 0,
                    "explain": (
                        "der Matrose → die Matrosen: слова на -e берут -n. "
                        "Matrose — единственное число."
                    ),
                },
                "explain": (
                    "После drei нужно множественное число: drei Matrosen. "
                    "Форма Matrose — единственное число."
                ),
            },
        },
        {
            "id": "plural_6",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «три корабля и две бочки».",
            "options": [
                "drei Schiffs und zwei Fässer",
                "drei Schiffe und zwei Fässer",
                "drei Schiffe und zwei Fasser",
                "drei Schiffen und zwei Fässer",
            ],
            "answer": 1,
            "explain": (
                "das Schiff → die Schiffe, das Fass → die Fässer. Без умлаута "
                "(Fasser), с -s (Schiffs) и в Dativ (Schiffen) множественное "
                "число неверно."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «много матросов и чаек».",
                "options": [
                    "viel Matrosen und Möwen",
                    "viele Matrose und Möwen",
                    "viele Matrosen und Möwen",
                    "viele Matrosen und Möwes",
                ],
                "answer": 2,
                "explain": (
                    "der Matrose → die Matrosen, die Möwe → die Möwen; после "
                    "viele артикль не нужен. Форма viel стоит перед "
                    "неисчисляемыми словами: viel Wasser."
                ),
            },
        },
        {
            "id": "plural_7",
            "kind": "mc",
            "prompt": (
                "Бард показывает на тюки, о которых уже говорили: "
                "«Das sind ___ Säcke aus Lübeck.»"
            ),
            "options": ["die", "der", "das", "ein"],
            "answer": 0,
            "explain": (
                "Во множественном числе артикль всегда die. Неопределённого "
                "артикля ein во множественном числе не существует."
            ),
            "retry": {
                "prompt": (
                    "Бард говорит о лодках, которые уже упоминал: "
                    "«Das sind ___ Boote aus dem Hafen.»"
                ),
                "options": ["der", "die", "das", "ein"],
                "answer": 1,
                "explain": (
                    "die Boote: во множественном числе только die, независимо "
                    "от рода в единственном числе."
                ),
            },
        },
        {
            "id": "plural_8",
            "kind": "gap",
            "prompt": (
                "Бард поёт о семье: «Meine zwei ___ arbeiten im Hafen.» "
                "(der Bruder)"
            ),
            "options": ["Bruders", "Bruder", "Brüder", "Brüdern"],
            "answer": 2,
            "explain": (
                "der Bruder → die Brüder: окончание не добавляется, "
                "но появляется умлаут. Bruders — родительный падеж, "
                "Brüdern — Dativ множественного числа."
            ),
            "retry": {
                "prompt": (
                    "Бард смотрит на рыбаков: «Die Fischer tragen zwei ___ "
                    "mit Fisch.» (der Korb)"
                ),
                "options": ["Korbs", "Körbe", "Korbe", "Körben"],
                "answer": 1,
                "explain": (
                    "der Korb → die Körbe: -e и умлаут. Форма Korbe без "
                    "умлаута неверна, Korbs — ошибка, Körben — Dativ."
                ),
            },
        },
    ],
}
