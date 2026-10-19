"""Тема 10. Nebensätze: weil, dass, wenn."""

TOPIC = {
    "id": "nebensaetze",
    "nr": 10,
    "title": "Придаточные с weil, dass, wenn",
    "short": "Nebensätze: weil, dass",
    "title_de": "Nebensätze: weil, dass, wenn",
    "location": "Гейдельберг, библиотека",
    "location_de": "Heidelberg, Bibliothek",
    "intro": (
        "Из Вартбурга дорога ведёт барда в Гейдельберг, к старой библиотеке. "
        "Здесь тихо, пахнет пылью и воском, а в книгах предложения длинные: одно "
        "объясняет другое. Барду тоже пора объяснять — почему он поёт и что он "
        "знает, — а для этого нужны придаточные с weil, dass и wenn."
    ),
    "listen": (
        "Бард слушает библиотеку: скрипят переплёты, шелестят страницы. Рядом "
        "бормочет студент: «Ich lese, weil ich eine Prüfung habe ... ich weiß, "
        "dass das schwer ist ... wenn ich Zeit habe, komme ich wieder.» Три союза "
        "— weil, dass, wenn, — а глагол в придаточном всегда уходит в конец."
    ),
    "theory": [
        {
            "title": "Три союза: weil, dass, wenn",
            "body": (
                "Придаточное предложение (Nebensatz) начинается с союза и отвечает "
                "на вопрос:\n\n"
                "weil — почему? причина: Ich lese, weil ich Zeit habe.\n"
                "dass — что? факт: Ich weiß, dass das Buch alt ist.\n"
                "wenn — когда? если? условие: Wenn es regnet, lese ich zu Hause.\n\n"
                "Союз всегда стоит на первом месте в придаточном и не считается "
                "членом предложения: подлежащее идёт сразу после него."
            ),
        },
        {
            "title": "Глагол уходит в конец",
            "body": (
                "Главное правило придаточного: спрягаемый глагол стоит в самом "
                "конце.\n\n"
                "Ich lese, weil das Buch alt ist.\n"
                "Ich weiß, dass der Barde gut singen kann.\n"
                "Wenn es regnet, bleiben wir hier.\n\n"
                "Сравни порядок слов:\n"
                "Der Tag war lang (главное предложение) — ..., weil der Tag lang "
                "war (придаточное).\n\n"
                "Союз denn не меняет порядок слов — это тоже частая ошибка: "
                "..., weil der Tag lang war, но ..., denn der Tag war lang."
            ),
        },
        {
            "title": "Придаточное в начале предложения",
            "body": (
                "Если придаточное стоит первым, то в главном предложении глагол "
                "идёт сразу после запятой, а потом подлежащее:\n\n"
                "Wenn es regnet, bleiben wir im Haus.\n"
                "Weil ich müde bin, lese ich ruhig.\n\n"
                "Схема: союз … , глагол (главного) + подлежащее …\n\n"
                "Типичная ошибка: «Ich lese, weil das Buch ist gut.» — глагол ist "
                "должен стоять в конце: ..., weil das Buch gut ist."
            ),
        },
    ],
    "song_line": (
        "Ich lese die Bücher, weil ich verstehen will,\n"
        "und wenn ich es weiß, dann werde ich still."
    ),
    "exercises": [
        {
            "id": "nebensaetze_1",
            "kind": "join",
            "prompt": (
                "Бард объясняет, почему он читает: «Ich lese. Das Buch ist alt.» "
                "Соедини предложения союзом weil."
            ),
            "options": [
                "Ich lese, weil das Buch alt ist.",
                "Ich lese, weil das Buch ist alt.",
                "Ich lese, weil ist das Buch alt.",
                "Ich lese, denn das Buch alt ist.",
            ],
            "answer": 0,
            "explain": (
                "В придаточном с weil спрягаемый глагол уходит в конец: ..., weil "
                "das Buch alt ist. Союз denn порядок слов не меняет, с ним глагол "
                "стоял бы на втором месте."
            ),
            "retry": {
                "prompt": (
                    "Бард объясняет, почему он устал: «Ich bin müde. Der Tag war "
                    "lang.» Соедини предложения союзом weil."
                ),
                "options": [
                    "Ich bin müde, weil der Tag lang war.",
                    "Ich bin müde, weil der Tag war lang.",
                    "Ich bin müde, weil war der Tag lang.",
                    "Ich bin müde, denn der Tag lang war.",
                ],
                "answer": 0,
                "explain": (
                    "Глагол придаточного — в конце: ..., weil der Tag lang war. "
                    "Форма war остаётся в конце, подлежащее der Tag идёт сразу "
                    "после союза."
                ),
            },
        },
        {
            "id": "nebensaetze_2",
            "kind": "join",
            "prompt": (
                "Бард говорит, что он знает: «Ich weiß. Die Bibliothek ist alt.» "
                "Соедини предложения союзом dass."
            ),
            "options": [
                "Ich weiß, dass die Bibliothek alt ist.",
                "Ich weiß, dass die Bibliothek ist alt.",
                "Ich weiß, dass ist die Bibliothek alt.",
                "Ich weiß, dass die Bibliothek alt.",
            ],
            "answer": 0,
            "explain": (
                "После dass глагол тоже уходит в конец: ..., dass die Bibliothek "
                "alt ist. Подлежащее die Bibliothek стоит сразу после союза."
            ),
            "retry": {
                "prompt": (
                    "Бард говорит, что он думает о песне: «Ich glaube. Das Lied "
                    "ist alt.» Соедини предложения союзом dass."
                ),
                "options": [
                    "Ich glaube, dass das Lied alt ist.",
                    "Ich glaube, dass das Lied ist alt.",
                    "Ich glaube, dass ist das Lied alt.",
                    "Ich glaube, dass das Lied alt.",
                ],
                "answer": 0,
                "explain": (
                    "В придаточном с dass глагол ist стоит в конце: ..., dass das "
                    "Lied alt ist."
                ),
            },
        },
        {
            "id": "nebensaetze_3",
            "kind": "join",
            "prompt": (
                "Бард мечтает о тихом вечере: «Ich habe Zeit. Ich lese ein Buch.» "
                "Соедини предложения союзом wenn."
            ),
            "options": [
                "Wenn ich Zeit habe, lese ich ein Buch.",
                "Wenn ich Zeit habe, ich lese ein Buch.",
                "Wenn ich habe Zeit, lese ich ein Buch.",
                "Dass ich Zeit habe, lese ich ein Buch.",
            ],
            "answer": 0,
            "explain": (
                "В придаточном с wenn глагол стоит в конце: wenn ich Zeit habe. "
                "В главном предложении после запятой глагол идёт сразу: lese ich "
                "ein Buch."
            ),
            "retry": {
                "prompt": (
                    "Бард говорит о дожде: «Es regnet. Wir lesen zu Hause.» "
                    "Соедини предложения союзом wenn."
                ),
                "options": [
                    "Wenn es regnet, lesen wir zu Hause.",
                    "Wenn es regnet, wir lesen zu Hause.",
                    "Wenn regnet es, lesen wir zu Hause.",
                    "Wenn es regnet, zu Hause lesen wir.",
                ],
                "answer": 0,
                "explain": (
                    "В придаточном глагол в конце (wenn es regnet), а в главном "
                    "после придаточного он стоит сразу после запятой: ..., lesen "
                    "wir zu Hause."
                ),
            },
        },
        {
            "id": "nebensaetze_4",
            "kind": "order",
            "prompt": "Собери предложение: бард читает, потому что он любит книги.",
            "words": ["Der", "Barde", "liest,", "weil", "er", "Bücher", "liebt"],
            "answer": "Der Barde liest, weil er Bücher liebt",
            "explain": (
                "Сначала главное предложение: Der Barde liest. Потом союз weil, "
                "подлежащее er, а глагол liebt — в самом конце придаточного."
            ),
            "retry": {
                "prompt": "Собери предложение: я остаюсь здесь, потому что идёт дождь.",
                "words": ["Ich", "bleibe", "hier,", "weil", "es", "regnet"],
                "answer": "Ich bleibe hier, weil es regnet",
                "explain": (
                    "В придаточном с weil глагол regnet стоит на последнем месте, "
                    "а подлежащее es — сразу после союза."
                ),
            },
        },
        {
            "id": "nebensaetze_5",
            "kind": "gap",
            "prompt": "Бард объясняет причину: «Ich bleibe hier, ___ es stark regnet.»",
            "options": ["weil", "dass", "wenn", "denn"],
            "answer": 0,
            "explain": (
                "Причина — это weil: ..., weil es stark regnet. После denn глагол "
                "стоял бы на втором месте (... denn es regnet stark), а dass "
                "вводит факт, wenn — условие."
            ),
            "retry": {
                "prompt": "Бард говорит о том, что он знает: «Ich weiß, ___ das Buch alt ist.»",
                "options": ["dass", "weil", "wenn", "denn"],
                "answer": 0,
                "explain": (
                    "После глаголов знания (wissen, glauben, sagen) ставим dass: "
                    "«Ich weiß, dass das Buch alt ist.»"
                ),
            },
        },
        {
            "id": "nebensaetze_6",
            "kind": "gap",
            "prompt": "Ich lese, weil das Buch spannend ___.",
            "options": ["ist", "sind", "bist", "seid"],
            "answer": 0,
            "explain": (
                "Подлежащее das Buch → форма ist. Глагол стоит в конце "
                "придаточного, поэтому ist идёт после spannend."
            ),
            "retry": {
                "prompt": "Der Barde singt, weil er die alten Lieder ___.",
                "options": ["liebt", "liebe", "liebst", "lieben"],
                "answer": 0,
                "explain": (
                    "Подлежащее придаточного er → форма liebt. Она стоит на "
                    "последнем месте: ..., weil er die alten Lieder liebt."
                ),
            },
        },
        {
            "id": "nebensaetze_7",
            "kind": "error",
            "prompt": (
                "В предложении барда одна ошибка — порядок слов в придаточном. "
                "Найди её."
            ),
            "sentence": "Der Barde liest, weil das Buch ist spannend.",
            "wrong": "ist",
            "fix": {
                "options": ["spannend ist", "ist spannend", "spannend sind", "spannend sein"],
                "answer": 0,
                "explain": (
                    "В придаточном с weil глагол уходит в самый конец: ..., weil "
                    "das Buch spannend ist."
                ),
            },
            "explain": (
                "Глагол ist стоит в середине придаточного — это ошибка. Правильно: "
                "..., weil das Buch spannend ist."
            ),
            "retry": {
                "prompt": (
                    "В предложении барда одна ошибка — порядок слов в придаточном. "
                    "Найди её."
                ),
                "sentence": "Ich weiß, dass der Barde kann gut singen.",
                "wrong": "kann",
                "fix": {
                    "options": [
                        "gut singen kann",
                        "kann gut singen",
                        "gut singt kann",
                        "gut singen können",
                    ],
                    "answer": 0,
                    "explain": (
                        "Модальный глагол ставится в конец придаточного: ..., dass "
                        "der Barde gut singen kann."
                    ),
                },
                "explain": (
                    "После dass глагол kann должен стоять в конце: ..., dass der "
                    "Barde gut singen kann."
                ),
            },
        },
        {
            "id": "nebensaetze_8",
            "kind": "mc",
            "prompt": "Бард объясняет, почему он поёт вечером. Выбери верное предложение.",
            "options": [
                "Abends singe ich, weil ich Zeit habe.",
                "Abends singe ich, weil ich habe Zeit.",
                "Abends singe ich, weil ich Zeit.",
                "Abends singe ich, weil habe ich Zeit.",
            ],
            "answer": 0,
            "explain": (
                "В придаточном с weil глагол habe стоит в конце: ..., weil ich "
                "Zeit habe. В главном предложении после Abends глагол singe идёт "
                "вторым, поэтому подлежащее ich после него."
            ),
            "retry": {
                "prompt": "Бард говорит, что он думает о песне. Выбери верное предложение.",
                "options": [
                    "Ich finde, dass das Lied schön ist.",
                    "Ich finde, dass das Lied ist schön.",
                    "Ich finde, dass ist das Lied schön.",
                    "Ich finde, dass das Lied schön.",
                ],
                "answer": 0,
                "explain": (
                    "После dass глагол ist стоит в конце придаточного: ..., dass "
                    "das Lied schön ist."
                ),
            },
        },
    ],
}
