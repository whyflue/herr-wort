"""Тема 7. Akkusativ und Dativ."""

TOPIC = {
    "id": "kasus",
    "nr": 7,
    "title": "Аккузатив и датив",
    "short": "Akkusativ и Dativ",
    "title_de": "Akkusativ und Dativ",
    "location": "Вена, императорский двор",
    "location_de": "Wien, Kaiserhof",
    "intro": (
        "Дорога из Веймара приводит барда в Вену, ко двору императора. Здесь "
        "всё чинно: стража, музыканты, дамы в тяжёлых платьях. Барда просят "
        "спеть перед императором, и он понимает, что одного именительного "
        "падежа мало: по-немецки нужно различать, кого он видит (Akkusativ) и "
        "кому поёт (Dativ)."
    ),
    "listen": (
        "Бард слышит, как переговаривается двор: «Ich sehe den Kaiser», «Der "
        "Barde singt dem Kaiser ein Lied», «Ich helfe dem Sänger». Одни и те же "
        "слова меняют форму: вижу кого-то — den Kaiser, помогаю кому-то — dem "
        "Sänger."
    ),
    "theory": [
        {
            "title": "Akkusativ: кого? что?",
            "body": (
                "Винительный падеж отвечает на вопросы «кого? что?». Его требуют "
                "многие глаголы: sehen, kaufen, haben, singen, suchen, finden, "
                "essen, trinken.\n\n"
                "Меняется только мужской род:\n"
                "der → den, ein → einen.\n\n"
                "Остальные формы такие же, как в Nominativ: die, das, die "
                "(множественное число), eine, ein, eine.\n\n"
                "Ich sehe den Kaiser. Der Barde kauft einen Wein. Die Frau hat "
                "eine Laute.\n\n"
                "Личные местоимения: mich, dich, ihn, sie, es, uns, euch, sie.\n\n"
                "Ich sehe ihn. Kennst du mich?"
            ),
        },
        {
            "title": "Dativ: кому?",
            "body": (
                "Дательный падеж отвечает на вопрос «кому?». С ним идут глаголы "
                "helfen, danken, geben, schenken, gefallen, gehören, antworten.\n\n"
                "Формы артиклей:\n"
                "der → dem, die → der, das → dem, die (множественное) → den "
                "(и существительное получает -n: den Kindern).\n\n"
                "Ich helfe dem Sänger. Der Barde dankt der Kaiserin. Er gibt den "
                "Kindern Brot.\n\n"
                "Личные местоимения: mir, dir, ihm, ihr, ihm, uns, euch, ihnen.\n\n"
                "Helft ihr mir? Ich danke dir."
            ),
        },
        {
            "title": "Два дополнения в предложении",
            "body": (
                "Если при глаголе стоят оба дополнения, сначала идёт Dativ "
                "(кому), потом Akkusativ (что):\n\n"
                "Der Barde schenkt dem Kaiser ein Lied. Ich gebe dem Wirt das "
                "Brot.\n\n"
                "Сначала человек, потом вещь — это главный порядок в немецком "
                "предложении.\n\n"
                "Если Akkusativ выражен местоимением, оно идёт первым: Der Barde "
                "schenkt es dem Kaiser.\n\n"
                "Запомни пару: den Kaiser — вижу, dem Kaiser — пою и дарю. "
                "Одна буква меняет роль слова в предложении."
            ),
        },
    ],
    "song_line": (
        "Der Kaiser in Wien trinkt den Wein,\n"
        "dem Sänger am Hof schenk ich den Reim."
    ),
    "exercises": [
        {
            "id": "kasus_1",
            "kind": "gap",
            "prompt": "Бард видит императора: «Ich sehe ___ Kaiser.» (der Kaiser)",
            "options": ["dem", "den", "der", "das"],
            "answer": 1,
            "explain": (
                "sehen требует Akkusativ, а мужской род в Akkusativ — den: Ich "
                "sehe den Kaiser. Форма dem была бы Dativ."
            ),
            "retry": {
                "prompt": "Бард покупает лютню: «Der Barde kauft ___ Laute.» (die Laute)",
                "options": ["der", "den", "die", "das"],
                "answer": 2,
                "explain": (
                    "Женский род в Akkusativ не меняется: die Laute. Форма der "
                    "подошла бы для Dativ, den — только для мужского рода."
                ),
            },
        },
        {
            "id": "kasus_2",
            "kind": "gap",
            "prompt": "Бард помогает певцу: «Ich helfe ___ Sänger.» (der Sänger)",
            "options": ["den", "der", "dem", "das"],
            "answer": 2,
            "explain": (
                "helfen — глагол с Dativ: ich helfe dem Sänger. Форма den стояла "
                "бы в Akkusativ, например ich sehe den Sänger."
            ),
            "retry": {
                "prompt": "Бард благодарит императрицу: «Der Barde dankt ___ Kaiserin.» (die Kaiserin)",
                "options": ["die", "den", "der", "dem"],
                "answer": 2,
                "explain": (
                    "danken требует Dativ, а женский род в Dativ — der: Der Barde "
                    "dankt der Kaiserin."
                ),
            },
        },
        {
            "id": "kasus_3",
            "kind": "gap",
            "prompt": (
                "Бард дарит мастеру песню: «Der Barde schenkt ___ Meister ein "
                "Lied.» (der Meister)"
            ),
            "options": ["den", "der", "dem", "das"],
            "answer": 2,
            "explain": (
                "schenken требует Dativ для того, кому дарят: schenkt dem Meister "
                "ein Lied. Сначала идёт Dativ, потом Akkusativ."
            ),
            "retry": {
                "prompt": (
                    "Императрица даёт барду книгу: «Die Kaiserin gibt ___ Barden "
                    "ein Buch.» (der Barde)"
                ),
                "options": ["den", "dem", "der", "das"],
                "answer": 1,
                "explain": (
                    "geben требует Dativ: gibt dem Barden ein Buch. Существительное "
                    "мужского рода в Dativ получает -n: dem Barden."
                ),
            },
        },
        {
            "id": "kasus_4",
            "kind": "error",
            "prompt": (
                "В песне барда одна ошибка — в падеже. Найди её."
            ),
            "sentence": "Ich helfe den Sänger.",
            "wrong": "den",
            "fix": {
                "options": ["der", "dem", "die", "das"],
                "answer": 1,
                "explain": (
                    "helfen требует Dativ: ich helfe dem Sänger. Форма den — "
                    "Akkusativ, она стояла бы при глаголе sehen."
                ),
            },
            "explain": (
                "После helfen нужен Dativ: Ich helfe dem Sänger."
            ),
            "retry": {
                "prompt": (
                    "В песне барда одна ошибка — в падеже. Найди её."
                ),
                "sentence": "Der Barde sieht dem Kaiser.",
                "wrong": "dem",
                "fix": {
                    "options": ["der", "den", "die", "das"],
                    "answer": 1,
                    "explain": (
                        "sehen требует Akkusativ: sieht den Kaiser. Форма dem — "
                        "Dativ, она стояла бы при глаголе helfen."
                    ),
                },
                "explain": (
                    "После sehen нужен Akkusativ: Der Barde sieht den Kaiser."
                ),
            },
        },
        {
            "id": "kasus_5",
            "kind": "order",
            "prompt": "Собери предложение: бард дарит императору песню.",
            "words": ["Der", "Barde", "schenkt", "dem", "Kaiser", "ein", "Lied"],
            "answer": "Der Barde schenkt dem Kaiser ein Lied",
            "explain": (
                "Сначала Dativ — кому (dem Kaiser), потом Akkusativ — что (ein "
                "Lied): Der Barde schenkt dem Kaiser ein Lied."
            ),
            "retry": {
                "prompt": "Собери предложение: императрица помогает певцу.",
                "words": ["Die", "Kaiserin", "hilft", "dem", "Sänger"],
                "answer": "Die Kaiserin hilft dem Sänger",
                "explain": (
                    "helfen требует Dativ: Die Kaiserin hilft dem Sänger."
                ),
            },
        },
        {
            "id": "kasus_6",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «Я вижу императора и пою.»",
            "options": [
                "Ich sehe dem Kaiser und singe.",
                "Ich sehe den Kaiser und singt.",
                "Ich sehe den Kaiser und singe.",
                "Ich sehe der Kaiser und singe.",
            ],
            "answer": 2,
            "explain": (
                "sehen требует Akkusativ: sehe den Kaiser. Глаголы с ich стоят "
                "в форме singe, а не singt."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «Я помогаю певцу и благодарю его.»",
                "options": [
                    "Ich helfe den Sänger und danke ihm.",
                    "Ich helfe dem Sänger und danke ihm.",
                    "Ich helfe dem Sänger und danke ihn.",
                    "Ich helfe der Sänger und danke ihm.",
                ],
                "answer": 1,
                "explain": (
                    "helfen и danken требуют Dativ: helfe dem Sänger и danke ihm. "
                    "Местоимение ihn — это Akkusativ."
                ),
            },
        },
        {
            "id": "kasus_7",
            "kind": "join",
            "prompt": (
                "Скажи одной фразой: «Ich sehe den Kaiser. Ich sehe den Wirt.»"
            ),
            "options": [
                "Ich sehe dem Kaiser und dem Wirt.",
                "Ich sehe den Kaiser und den Wirt.",
                "Ich sehe den Kaiser und dem Wirt.",
                "Ich sehe der Kaiser und der Wirt.",
            ],
            "answer": 1,
            "explain": (
                "Оба слова — в Akkusativ, потому что оба являются дополнением "
                "при sehen: den Kaiser und den Wirt."
            ),
            "retry": {
                "prompt": (
                    "Скажи одной фразой: «Ich danke dem Wirt. Ich danke der "
                    "Kaiserin.»"
                ),
                "options": [
                    "Ich danke den Wirt und die Kaiserin.",
                    "Ich danke dem Wirt und die Kaiserin.",
                    "Ich danke dem Wirt und der Kaiserin.",
                    "Ich danke der Wirt und der Kaiserin.",
                ],
                "answer": 2,
                "explain": (
                    "danken требует Dativ: dem Wirt и der Kaiserin. Форма den "
                    "была бы Akkusativ, а die — именительным падежом."
                ),
            },
        },
        {
            "id": "kasus_8",
            "kind": "mc",
            "prompt": (
                "Бард поёт перед императором. Какое предложение верно?"
            ),
            "options": [
                "Der Barde singt den Kaiser ein Lied.",
                "Der Barde singt dem Kaiser ein Lied.",
                "Der Barde singt der Kaiser ein Lied.",
                "Der Barde singt ein Kaiser ein Lied.",
            ],
            "answer": 1,
            "explain": (
                "Петь кому-то — Dativ: singt dem Kaiser ein Lied. Сначала Dativ, "
                "потом Akkusativ."
            ),
            "retry": {
                "prompt": "Бард дарит певице книгу. Какое предложение верно?",
                "options": [
                    "Der Barde schenkt die Sängerin ein Buch.",
                    "Der Barde schenkt der Sängerin ein Buch.",
                    "Der Barde schenkt dem Sängerin ein Buch.",
                    "Der Barde schenkt den Sängerin ein Buch.",
                ],
                "answer": 1,
                "explain": (
                    "schenken требует Dativ, а die Sängerin — женский род: "
                    "schenkt der Sängerin ein Buch."
                ),
            },
        },
    ],
}
