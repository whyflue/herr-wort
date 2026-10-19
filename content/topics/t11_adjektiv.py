"""Тема 11. Adjektivdeklination: schwach, stark, gemischt."""

TOPIC = {
    "id": "adjektiv",
    "nr": 11,
    "title": "Склонение прилагательных",
    "short": "Склонение прилагательных",
    "title_de": "Adjektivdeklination (schwach, stark, gemischt)",
    "location": "Страсбург, площадь у собора",
    "location_de": "Straßburg, Platz am Münster",
    "intro": (
        "Бард приходит в Страсбург и останавливается на площади у собора, где "
        "шумит большая ярмарка. На прилавках лежат вещи, и у каждой свой "
        "характер: пёстрое полотно, старое серебро, маленькая лютня. Бард "
        "выбирает то, о чём хочется спеть, и понимает: мало сказать «schön» — "
        "слово должно встать рядом с вещью правильно. Весь вечер он приделывает "
        "к прилагательным верные окончания."
    ),
    "listen": (
        "Бард слушает ярмарку: торговка расхваливает «ein schönes Tuch», старик "
        "вертит в руках «das alte Buch», а про зиму здесь говорят «kalte "
        "Nächte». В каждом слове звенит последний слог — в нём спрятаны род и "
        "падеж. Бард ловит эти слоги на слух, как ноты."
    ),
    "theory": [
        {
            "title": "Три типа склонения — всё решает артикль",
            "body": (
                "Прилагательное перед существительным всегда стоит с окончанием, "
                "и это окончание показывает род и падеж: das alte Buch, die alte "
                "Laute, der alte Meister.\n\n"
                "Тип склонения выбирает слово перед прилагательным:\n"
                "— слабое: после der/die/das, dieser — das alte Buch;\n"
                "— смешанное: после ein/eine/kein/mein — ein altes Buch;\n"
                "— сильное: артикля нет вообще — altes Brot, kalte Nächte.\n\n"
                "Правило простое: если артикль уже показал род и падеж (das, die, "
                "der), прилагательному достаточно слабого окончания -e или -en. "
                "Если артикля нет, прилагательное берёт окончание артикля: -er, "
                "-es, -e."
            ),
        },
        {
            "title": "Слабое склонение: только -e и -en",
            "body": (
                "После определённого артикля у прилагательного всего два "
                "окончания: -e и -en.\n\n"
                "Nominativ: der alte Meister, die alte Laute, das alte Buch, die "
                "alten Bücher\n"
                "Akkusativ: den alten Meister, die alte Laute, das alte Buch, die "
                "alten Bücher\n"
                "Dativ: dem alten Meister, der alten Laute, dem alten Buch, den "
                "alten Büchern\n\n"
                "Запомни: -e стоит только в Nominativ единственного числа (все три "
                "рода) и там, где Akkusativ совпадает с Nominativ (женский и "
                "средний род). Во всех остальных формах, включая всё "
                "множественное число, — -en: mit dem jungen Meister, mit der "
                "alten Laute."
            ),
        },
        {
            "title": "Смешанное и сильное склонение",
            "body": (
                "Смешанное склонение (ein, eine, kein, mein). Артикль показывает "
                "род не всегда, поэтому прилагательное берёт сильное окончание "
                "там, где у ein окончание «пустое».\n\n"
                "ein alter Meister (Nominativ, -er), einen alten Meister "
                "(Akkusativ, -en), eine alte Laute, ein altes Buch; в Dativ всегда "
                "-en: einem alten Meister, mit einer alten Laute.\n\n"
                "Сильное склонение (без артикля): прилагательное работает как "
                "артикль.\n"
                "Nominativ: alter Wein, alte Laute, altes Brot, kalte Nächte\n"
                "Akkusativ: alten Wein, alte Laute, altes Brot, kalte Nächte\n"
                "Dativ: altem Wein, alter Laute, altem Brot, kalten Nächten\n\n"
                "Во множественном числе без артикля окончание -e (kalte Nächte), "
                "а в Dativ — -en (mit kalten Nächten)."
            ),
        },
    ],
    "song_line": (
        "Das alte Buch, das schöne Lied im Wind,\n"
        "die kalte Nacht — sie alle sing ich, wie sie sind."
    ),
    "exercises": [
        {
            "id": "adjektiv_1",
            "kind": "gap",
            "prompt": "Das ___ Buch auf dem Tisch ist sehr alt. (alt)",
            "options": ["alte", "alten", "altes", "alter"],
            "answer": 0,
            "explain": (
                "После определённого артикля склонение слабое. В Nominativ "
                "единственного числа прилагательное получает только -e: das alte "
                "Buch. Артикль das уже показал средний род, прилагательному "
                "больше не нужно."
            ),
            "retry": {
                "prompt": "Die ___ Laute hängt an der Wand. (alt)",
                "options": ["alte", "alten", "altes", "alter"],
                "answer": 0,
                "explain": (
                    "die Laute — женский род, Nominativ. Слабое склонение после "
                    "определённого артикля: die alte Laute."
                ),
            },
        },
        {
            "id": "adjektiv_2",
            "kind": "gap",
            "prompt": "Im Korb liegt ___ Brot vom Markt. (alt)",
            "options": ["altes", "alte", "alten", "alter"],
            "answer": 0,
            "explain": (
                "Артикля нет, значит склонение сильное: прилагательное само "
                "показывает род и берёт окончание артикля. Brot — средний род, "
                "поэтому altes Brot (так же, как altes Buch)."
            ),
            "retry": {
                "prompt": "Der Wirt schenkt ___ Wein ein. (rot)",
                "options": ["roten", "roter", "rote", "rotes"],
                "answer": 0,
                "explain": (
                    "Без артикля прилагательное берёт сильное окончание: здесь "
                    "Akkusativ мужского рода, поэтому roten Wein (der Wein → den "
                    "Wein → roten Wein)."
                ),
            },
        },
        {
            "id": "adjektiv_3",
            "kind": "gap",
            "prompt": "Der Barde kauft ein ___ Buch für den Meister. (alt)",
            "options": ["alte", "altes", "alten", "alter"],
            "answer": 1,
            "explain": (
                "После ein склонение смешанное. У ein в среднем роде нет "
                "окончания, поэтому прилагательное берёт сильное -es: ein altes "
                "Buch."
            ),
            "retry": {
                "prompt": "Auf dem Markt singt eine ___ Frau. (jung)",
                "options": ["junge", "junges", "jungen", "junger"],
                "answer": 0,
                "explain": (
                    "eine Frau — женский род, Nominativ. Женский артикль eine уже "
                    "показывает род, прилагательное получает -e: eine junge Frau."
                ),
            },
        },
        {
            "id": "adjektiv_4",
            "kind": "mc",
            "prompt": (
                "Бард идёт к собору с молодым мастером: «Der Barde geht mit ___ "
                "Meister zum Münster.»"
            ),
            "options": ["dem jungen", "dem junge", "der jungen", "den jungen"],
            "answer": 0,
            "explain": (
                "Предлог mit всегда требует Dativ, а после определённого артикля "
                "в Dativ прилагательное получает -en: mit dem jungen Meister. "
                "Форма den jungen — это Akkusativ, она стояла бы без предлога."
            ),
            "retry": {
                "prompt": "Бард поёт о старой песне: «Der Barde singt von einem ___ "
                          "Lied.» (alt)",
                "options": ["alten", "altem", "alte", "altes"],
                "answer": 0,
                "explain": (
                    "von требует Dativ. После einem прилагательное всегда получает "
                    "-en: von einem alten Lied. Сильное -em здесь невозможно, "
                    "артикль уже занял это место."
                ),
            },
        },
        {
            "id": "adjektiv_5",
            "kind": "error",
            "prompt": (
                "В предложении барда одна ошибка — в окончании прилагательного. "
                "Найди её."
            ),
            "sentence": "Der Barde singt ein schöner Lied.",
            "wrong": "schöner",
            "fix": {
                "options": ["schönes", "schöne", "schönen", "schönem"],
                "answer": 0,
                "explain": (
                    "das Lied — средний род. После ein в Nominativ и Akkusativ "
                    "прилагательное получает -es: ein schönes Lied. Окончание -er "
                    "стоит только в мужском роде."
                ),
            },
            "explain": (
                "ein schöner Lied — неверно: Lied среднего рода, значит ein "
                "schönes Lied (смешанное склонение, окончание -es)."
            ),
            "retry": {
                "prompt": (
                    "В предложении барда одна ошибка — в окончании "
                    "прилагательного. Найди её."
                ),
                "sentence": "Der Barde grüßt eine alter Frau.",
                "wrong": "alter",
                "fix": {
                    "options": ["alte", "alten", "altes", "altem"],
                    "answer": 0,
                    "explain": (
                        "eine Frau — женский род, Akkusativ совпадает с Nominativ, "
                        "поэтому прилагательное получает -e: eine alte Frau."
                    ),
                },
                "explain": (
                    "eine alter Frau — неверно: в женском роде после eine стоит "
                    "окончание -e, значит eine alte Frau."
                ),
            },
        },
        {
            "id": "adjektiv_6",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «Старая книга лежит на столе.»",
            "options": [
                "Das alte Buch liegt auf dem Tisch.",
                "Das alten Buch liegt auf dem Tisch.",
                "Das altes Buch liegt auf dem Tisch.",
                "Der alte Buch liegt auf dem Tisch.",
            ],
            "answer": 0,
            "explain": (
                "Buch — средний род, поэтому das alte Buch: в слабом склонении "
                "после das стоит только -e. Формы alten и altes здесь неверны, и "
                "артикль der тоже: он для мужского рода."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «Прекрасная песня звучит громко.»",
                "options": [
                    "Das schöne Lied klingt laut.",
                    "Das schöner Lied klingt laut.",
                    "Das schönes Lied klingt laut.",
                    "Das schönen Lied klingt laut.",
                ],
                "answer": 0,
                "explain": (
                    "das Lied — средний род, Nominativ. Слабое склонение: после "
                    "das прилагательное получает -e, значит das schöne Lied."
                ),
            },
        },
        {
            "id": "adjektiv_7",
            "kind": "order",
            "prompt": "Собери предложение: холодные ночи здесь очень долгие.",
            "words": ["Kalte", "Nächte", "sind", "hier", "sehr", "lang"],
            "answer": "Kalte Nächte sind hier sehr lang",
            "explain": (
                "Во множественном числе без артикля прилагательное получает -e: "
                "kalte Nächte (сильное склонение). Глагол sein согласуется с "
                "подлежащим: Nächte — множественное число, поэтому sind."
            ),
            "retry": {
                "prompt": "Собери предложение: старые стены стоят у собора.",
                "words": ["Alte", "Mauern", "stehen", "am", "Münster"],
                "answer": "Alte Mauern stehen am Münster",
                "explain": (
                    "Alte Mauern — множественное число без артикля, окончание -e. "
                    "Сказуемое stehen тоже во множественном числе; am Münster = an "
                    "dem Münster (Dativ)."
                ),
            },
        },
        {
            "id": "adjektiv_8",
            "kind": "transform",
            "prompt": (
                "Бард убирает артикль: «Der alte Wein ist teuer.» Скажи то же без "
                "артикля."
            ),
            "options": [
                "Alter Wein ist teuer.",
                "Alte Wein ist teuer.",
                "Altes Wein ist teuer.",
                "Alten Wein ist teuer.",
            ],
            "answer": 0,
            "explain": (
                "Без артикля работает сильное склонение: прилагательное берёт "
                "окончание артикля. der alte Wein → alter Wein (мужской род, "
                "Nominativ, окончание -er)."
            ),
            "retry": {
                "prompt": (
                    "Бард убирает артикль: «Die alten Glocken klingen schön.» "
                    "Скажи то же без артикля."
                ),
                "options": [
                    "Alte Glocken klingen schön.",
                    "Alter Glocken klingen schön.",
                    "Altes Glocken klingen schön.",
                    "Alten Glocken klingen schön.",
                ],
                "answer": 0,
                "explain": (
                    "Множественное число без артикля — окончание -e: alte Glocken "
                    "(Nominativ). Форма alten стояла бы только в Dativ, например "
                    "mit alten Glocken."
                ),
            },
        },
    ],
}
