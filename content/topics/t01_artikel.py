"""Тема 1. Bestimmter und unbestimmter Artikel."""

TOPIC = {
    "id": "artikel",
    "nr": 1,
    "title": "Артикли: der/die/das, ein/eine",
    "short": "Артикли",
    "title_de": "Bestimmter und unbestimmter Artikel",
    "location": "Любек, рыночная площадь",
    "location_de": "Lübeck, Marktplatz",
    "intro": (
        "Бард-новичок входит в Любек через Гольстенские ворота. Утро пахнет "
        "хлебом и солью: торговцы раскладывают товар и называют его по имени. "
        "Бард достаёт перо, чтобы записать первую строчку. Но спеть о вещах "
        "нельзя, пока не научишься их называть — вместе с артиклем."
    ),
    "listen": (
        "Бард прикладывает ладонь к стене склада и слушает рынок: торговка "
        "пересчитывает яблоки — «ein Apfel, noch ein Apfel», мальчишка гонит "
        "кота — «die Katze!». Три ключа к любому существительному: der, die, das."
    ),
    "theory": [
        {
            "title": "Три рода — три артикля",
            "body": (
                "У каждого немецкого существительного есть род, и артикль его "
                "показывает: der (мужской), die (женский), das (средний). Род "
                "часто не совпадает с русским, поэтому слово учат сразу с артиклем.\n\n"
                "der Barde — бард, der Apfel — яблоко, der Markt — рынок\n"
                "die Laute — лютня, die Stadt — город, die Nacht — ночь\n"
                "das Lied — песня, das Brot — хлеб, das Wasser — вода"
            ),
        },
        {
            "title": "Неопределённый артикль: говорю впервые",
            "body": (
                "Если предмет упоминается впервые и мы не знаем, какой именно, "
                "ставим ein (для der и das) или eine (для die).\n\n"
                "Ein Barde kommt in die Stadt. Das ist ein Apfel. Auf dem Markt "
                "singt eine Verkäuferin.\n\n"
                "Множественное число артикля не имеет: Bäcker, Lieder, Städte."
            ),
        },
        {
            "title": "Определённый артикль и Akkusativ",
            "body": (
                "der/die/das ставим, когда предмет уже назван или единственный "
                "в своём роде: Der Barde ist müde. Die Sonne scheint.\n\n"
                "В винительном падеже (Akkusativ) меняется только мужской род: "
                "der → den, ein → einen. Женский и средний не меняются.\n\n"
                "Ich sehe den Barden. Ich stimme die Laute. Ich singe ein Lied."
            ),
        },
    ],
    "song_line": (
        "Am Markt von Lübeck, im Morgenlicht,\n"
        "kauf ich ein Brot und ein Lied — mehr braucht ein Barde nicht."
    ),
    "exercises": [
        {
            "id": "artikel_1",
            "kind": "gap",
            "prompt": "Ich sehe ___ Hund auf dem Markt. (der Hund)",
            "options": ["den", "dem", "der", "die"],
            "answer": 0,
            "explain": (
                "Hund — мужской род, здесь Akkusativ (вижу кого? den Hund). "
                "В Akkusativ мужской род меняется: der → den, ein → einen."
            ),
            "retry": {
                "prompt": "Der Barde grüßt ___ Wirt am Stand. (der Wirt)",
                "options": ["den", "dem", "der", "das"],
                "answer": 0,
                "explain": (
                    "grüßen требует Akkusativ: кого? — den Wirt. Мужской род "
                    "в Akkusativ получает форму den."
                ),
            },
        },
        {
            "id": "artikel_2",
            "kind": "gap",
            "prompt": "___ Katze sitzt auf dem Fass. (Katze)",
            "options": ["Die", "Der", "Das", "Den"],
            "answer": 0,
            "explain": (
                "die Katze — женский род, в Nominativ (кто? что?) остаётся die. "
                "Определённый артикль здесь потому, что кот во дворе один, "
                "о нём уже говорили."
            ),
            "retry": {
                "prompt": "___ Brot liegt auf dem Tisch. (Brot)",
                "options": ["Das", "Der", "Die", "Den"],
                "answer": 0,
                "explain": "das Brot — средний род, в Nominativ форма das.",
            },
        },
        {
            "id": "artikel_3",
            "kind": "mc",
            "prompt": (
                "Бард показывает торговке вещь, о которой речь впервые: "
                "«Das ist ___ Apfel!»"
            ),
            "options": ["ein", "eine", "einen", "der"],
            "answer": 0,
            "explain": (
                "Apfel — мужской род, предмет упоминается впервые, значит "
                "неопределённый артикль: ein Apfel. Форма einen — это Akkusativ "
                "(ich kaufe einen Apfel)."
            ),
            "retry": {
                "prompt": (
                    "Торговка впервые называет свою соседку: "
                    "«Auf dem Markt steht ___ Verkäuferin.» (Verkäuferin)"
                ),
                "options": ["eine", "ein", "einen", "das"],
                "answer": 0,
                "explain": (
                    "die Verkäuferin — женский род, первое упоминание: eine "
                    "Verkäuferin."
                ),
            },
        },
        {
            "id": "artikel_4",
            "kind": "gap",
            "prompt": "Der Barde kauft Brot. ___ Brot ist noch warm. (Brot)",
            "options": ["Das", "Der", "Die", "Ein"],
            "answer": 0,
            "explain": (
                "О хлебе уже сказали в первом предложении, поэтому ставим "
                "определённый артикль: das Brot (средний род)."
            ),
            "retry": {
                "prompt": "Eine Frau singt am Brunnen. ___ Frau hat eine Laute. (Frau)",
                "options": ["Die", "Der", "Das", "Ein"],
                "answer": 0,
                "explain": (
                    "Повторное упоминание → определённый артикль: die Frau."
                ),
            },
        },
        {
            "id": "artikel_5",
            "kind": "order",
            "prompt": "Собери предложение: бард видит птицу.",
            "words": ["Der", "Barde", "sieht", "einen", "Vogel"],
            "answer": "Der Barde sieht einen Vogel",
            "explain": (
                "Vogel — мужской род, в Akkusativ: einen Vogel. Порядок слов "
                "в простом предложении: сначала подлежащее, потом сказуемое "
                "и дополнение."
            ),
            "retry": {
                "prompt": "Собери предложение: кот видит пса.",
                "words": ["Die", "Katze", "sieht", "einen", "Hund"],
                "answer": "Die Katze sieht einen Hund",
                "explain": (
                    "Die Katze — подлежащее (женский род в Nominativ), einen "
                    "Hund — дополнение в Akkusativ."
                ),
            },
        },
        {
            "id": "artikel_6",
            "kind": "error",
            "prompt": "В предложении барда одна ошибка — в артикле. Найди её.",
            "sentence": "Das Barde spielt eine Laute.",
            "wrong": "Das",
            "fix": {
                "options": ["Der", "Die", "Den", "Dem"],
                "answer": 0,
                "explain": (
                    "der Barde — мужской род, Nominativ: Der Barde spielt eine "
                    "Laute. Средний артикль das здесь невозможен."
                ),
            },
            "explain": (
                "der Barde — мужской род (подлежащее в Nominativ), поэтому "
                "нужен Der, а не Das. Ошибка в роде существительного."
            ),
            "retry": {
                "prompt": "В предложении барда одна ошибка — в артикле. Найди её.",
                "sentence": "Der Stadt ist alt und laut.",
                "wrong": "Der",
                "fix": {
                    "options": ["Die", "Das", "Den", "Dem"],
                    "answer": 0,
                    "explain": "die Stadt — женский род: Die Stadt ist alt und laut.",
                },
                "explain": "die Stadt — женский род, значит Die, а не Der.",
            },
        },
        {
            "id": "artikel_7",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «Я покупаю яблоко и хлеб.»",
            "options": [
                "Ich kaufe einen Apfel und ein Brot.",
                "Ich kaufe ein Apfel und einen Brot.",
                "Ich kaufe eine Apfel und einen Brot.",
                "Ich kauft einen Apfel und ein Brot.",
            ],
            "answer": 0,
            "explain": (
                "Apfel — мужской род, Akkusativ: einen Apfel. Brot — средний род, "
                "в Akkusativ остаётся ein Brot. Глагол с ich: kaufe."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «Он поёт песню.»",
                "options": [
                    "Er singt ein Lied.",
                    "Er singt einen Lied.",
                    "Er singt eine Lied.",
                    "Er singt ein Lieder.",
                ],
                "answer": 0,
                "explain": (
                    "das Lied — средний род, Akkusativ совпадает с Nominativ: "
                    "ein Lied. Формы einen/eine здесь невозможны."
                ),
            },
        },
        {
            "id": "artikel_8",
            "kind": "transform",
            "prompt": (
                "Бард поёт о девушке: «Eine Frau geht zum Markt.» Скажи то же "
                "о знакомой девушке (она уже упоминалась) — замени артикль."
            ),
            "options": [
                "Die Frau geht zum Markt.",
                "Der Frau geht zum Markt.",
                "Eine Frau geht zum Markt.",
                "Das Frau geht zum Markt.",
            ],
            "answer": 0,
            "explain": (
                "Вместо неопределённого артикля при повторном упоминании ставим "
                "определённый: eine Frau → die Frau."
            ),
            "retry": {
                "prompt": (
                    "В трактире впервые говорят о барде: «Ein Barde singt laut.» "
                    "Скажи то же о том барде, о котором уже шла речь."
                ),
                "options": [
                    "Der Barde singt laut.",
                    "Die Barde singt laut.",
                    "Das Barde singt laut.",
                    "Den Barde singt laut.",
                ],
                "answer": 0,
                "explain": "ein Barde → der Barde (мужской род, Nominativ).",
            },
        },
    ],
}
