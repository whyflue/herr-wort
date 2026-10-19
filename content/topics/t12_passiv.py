"""Тема 12. Passiv im Präsens und Präteritum (финальная локация)."""

TOPIC = {
    "id": "passiv",
    "nr": 12,
    "title": "Пассив (Präsens, Präteritum)",
    "short": "Passiv: Präsens/Präteritum",
    "title_de": "Passiv (Präsens, Präteritum)",
    "location": "Аахен, собор Карла Великого",
    "location_de": "Aachen, Dom Karls des Großen",
    "intro": (
        "Аахен — последняя остановка баллады. Бард входит под своды собора "
        "Карла Великого, где камни помнят мастеров: собор строили веками, его "
        "освящали, в нём короновали королей. Здесь о великом говорят не «кто это "
        "сделал», а «что было сделано». Бард записывает последнюю строчку: "
        "теперь и его песня «wird gebaut»."
    ),
    "listen": (
        "Бард прислоняется к холодной колонне и слушает собор. Внизу кто-то "
        "говорит: «der Stein wird gelegt», на башне — «die Glocken werden "
        "geläutet», а под сводами звучит старое торжественное «der Dom wurde "
        "gebaut». Ни одного имени мастера — только само дело."
    ),
    "theory": [
        {
            "title": "Что такое пассив и как он устроен",
            "body": (
                "Passiv отвечает на вопрос «что происходит с предметом?», а не "
                "«кто это делает?».\n\n"
                "Формула: werden + Partizip II.\n"
                "Präsens: Der Dom wird gebaut. Die Glocken werden geläutet.\n"
                "Präteritum: Der Dom wurde gebaut. Die Glocken wurden geläutet.\n\n"
                "В пассиве на первом плане действие, а исполнитель часто вообще "
                "не назван: Der Stein wird gelegt. — Камень кладут.\n\n"
                "werden спрягается по лицу и числу: ich werde, du wirst, er/sie/es "
                "wird, wir werden, ihr werdet, sie werden. В Präteritum: ich wurde, "
                "er wurde; wir wurden, sie wurden. Partizip II при этом не "
                "меняется."
            ),
        },
        {
            "title": "Порядок слов, время и исполнитель",
            "body": (
                "В простом предложении werden (wurde) стоит на втором месте, "
                "Partizip II — в самом конце: Der Dom wird von den Meistern gebaut.\n\n"
                "Если предложение начинается не с подлежащего, werden всё равно "
                "на втором месте, а подлежащее уходит за него:\n"
                "Im Jahr 800 wurde der Dom gebaut. Jeden Tag werden die Glocken "
                "geläutet.\n\n"
                "Исполнителя вводим через von + Dativ (von dem → vom): Der Dom "
                "wurde von Karl dem Großen gebaut. Die Glocken wurden von den "
                "Meistern geläutet. Во множественном числе Dativ: von den Meistern "
                "(артикль den, у существительного -n).\n\n"
                "Aktiv → Passiv: Der Baumeister baut den Dom. → Der Dom wird "
                "gebaut. Дополнение в Akkusativ становится подлежащим."
            ),
        },
        {
            "title": "Präsens или Präteritum: выбирает werden",
            "body": (
                "Время в пассиве показывает вспомогательный глагол — форма "
                "Partizip II не меняется.\n\n"
                "Präsens (wird / werden): действие сейчас, регулярно или как "
                "правило.\n"
                "Der Dom wird restauriert. Die Glocken werden am Morgen geläutet.\n\n"
                "Präteritum (wurde / wurden): рассказ о прошлом.\n"
                "Der Dom wurde gebaut. Die Glocken wurden geläutet.\n\n"
                "Согласование с подлежащим: der Dom wird/wurde — единственное "
                "число; die Glocken werden/wurden — множественное. Не путай wurde "
                "(ед. ч.) и wurden (мн. ч.).\n\n"
                "Частая ошибка: вместо Partizip II поставить инфинитив. «Der Dom "
                "wird bauen» — неверно, нужно Der Dom wird gebaut."
            ),
        },
    ],
    "song_line": (
        "Nun wird das Lied gebaut aus Stein und Zeit,\n"
        "der Dom steht fest — der Barde ist bereit."
    ),
    "exercises": [
        {
            "id": "passiv_1",
            "kind": "transform",
            "prompt": "Преобразуй в пассив (Präsens): «Der Baumeister baut den Dom.»",
            "options": [
                "Der Dom wird gebaut.",
                "Der Dom wird bauen.",
                "Der Dom baut den Meister.",
                "Der Dom wurde gebaut.",
            ],
            "answer": 0,
            "explain": (
                "Формула пассива: werden + Partizip II. Дополнение den Dom "
                "становится подлежащим: der Dom. Der Baumeister baut den Dom → Der "
                "Dom wird gebaut."
            ),
            "retry": {
                "prompt": "Преобразуй в пассив (Präsens): «Die Meister bauen die Kirche.»",
                "options": [
                    "Die Kirche wird gebaut.",
                    "Die Kirche wird bauen.",
                    "Die Kirche werden gebaut.",
                    "Die Kirche wurde gebaut.",
                ],
                "answer": 0,
                "explain": (
                    "Подлежащее die Kirche — единственное число, поэтому wird "
                    "gebaut. Форму werden мы поставили бы при подлежащем во "
                    "множественном числе, а wurde gebaut — это Präteritum."
                ),
            },
        },
        {
            "id": "passiv_2",
            "kind": "transform",
            "prompt": "Преобразуй в пассив (Präteritum): «Der Meister baute den Turm.»",
            "options": [
                "Der Turm wurde gebaut.",
                "Der Turm wird gebaut.",
                "Der Turm wurde bauen.",
                "Der Turm wurden gebaut.",
            ],
            "answer": 0,
            "explain": (
                "Пассив в Präteritum: wurde/wurden + Partizip II. Der Meister baute "
                "den Turm → Der Turm wurde gebaut. Подлежащее der Turm стоит в "
                "единственном числе, поэтому wurde."
            ),
            "retry": {
                "prompt": "Преобразуй в пассив (Präteritum): «Die Arbeiter trugen die Steine.»",
                "options": [
                    "Die Steine wurden getragen.",
                    "Die Steine wurde getragen.",
                    "Die Steine werden getragen.",
                    "Die Steine wurden tragen.",
                ],
                "answer": 0,
                "explain": (
                    "tragen → Partizip II getragen. Подлежащее die Steine — "
                    "множественное число, Präteritum, значит wurden getragen."
                ),
            },
        },
        {
            "id": "passiv_3",
            "kind": "gap",
            "prompt": "Jeden Tag ___ der Dom von vielen Gästen besucht. (Präsens)",
            "options": ["wird", "werden", "wurde", "wurden"],
            "answer": 0,
            "explain": (
                "Подлежащее der Dom — единственное число, время Präsens, поэтому "
                "wird. Форма werden — для множественного числа (die Gäste "
                "werden), wurde и wurden — Präteritum."
            ),
            "retry": {
                "prompt": "Im alten Aachen ___ die Glocken am Morgen geläutet. (Präteritum)",
                "options": ["wurden", "wurde", "werden", "wird"],
                "answer": 0,
                "explain": (
                    "Подлежащее die Glocken — множественное число, Präteritum: "
                    "wurden geläutet. Форма wurde стояла бы при подлежащем в "
                    "единственном числе."
                ),
            },
        },
        {
            "id": "passiv_4",
            "kind": "gap",
            "prompt": "Der Dom wurde von Karl dem Großen ___. (bauen)",
            "options": ["gebaut", "bauen", "baute", "baut"],
            "answer": 0,
            "explain": (
                "В пассиве в конце предложения стоит Partizip II: bauen → gebaut. "
                "Инфинитив bauen и личные формы baute/baut после wurde невозможны."
            ),
            "retry": {
                "prompt": "Die Glocken werden am Abend ___. (läuten)",
                "options": ["geläutet", "läuten", "läutete", "läutet"],
                "answer": 0,
                "explain": (
                    "läuten → Partizip II geläutet. После werden в пассиве стоит "
                    "только Partizip II: Die Glocken werden am Abend geläutet."
                ),
            },
        },
        {
            "id": "passiv_5",
            "kind": "mc",
            "prompt": (
                "Бард говорит, что собор строят и сейчас. Какое предложение верно?"
            ),
            "options": [
                "Der Dom wird gebaut.",
                "Der Dom wird bauen.",
                "Der Dom werden gebaut.",
                "Der Dom wurde gebaut.",
            ],
            "answer": 0,
            "explain": (
                "Пассив Präsens: werden + Partizip II. Подлежащее der Dom — "
                "единственное число, значит wird gebaut. Инфинитив bauen неверен, "
                "werden — форма множественного числа, а wurde gebaut — это "
                "Präteritum."
            ),
            "retry": {
                "prompt": (
                    "Бард говорит о колоколах, которые звонят по утрам. Какое "
                    "предложение верно?"
                ),
                "options": [
                    "Die Glocken werden geläutet.",
                    "Die Glocken wird geläutet.",
                    "Die Glocken werden läuten.",
                    "Die Glocken wurde geläutet.",
                ],
                "answer": 0,
                "explain": (
                    "Подлежащее die Glocken — множественное число: werden geläutet. "
                    "wird и wurde стоят при единственном числе, а läuten — "
                    "инфинитив."
                ),
            },
        },
        {
            "id": "passiv_6",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «Собор был построен мастерами.»",
            "options": [
                "Der Dom wurde von den Meistern gebaut.",
                "Der Dom wurde von die Meistern gebaut.",
                "Der Dom wurde von den Meister gebaut.",
                "Der Dom wurde von dem Meistern gebaut.",
            ],
            "answer": 0,
            "explain": (
                "Passiv Präteritum: wurde gebaut. Исполнитель вводится через von + "
                "Dativ, во множественном числе артикль den, а существительное "
                "получает -n: von den Meistern."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «Колокола были отлиты раньше.»",
                "options": [
                    "Die Glocken wurden früher gegossen.",
                    "Die Glocken wurde früher gegossen.",
                    "Die Glocken wurden früher gießen.",
                    "Die Glocken werden früher gegossen.",
                ],
                "answer": 0,
                "explain": (
                    "gießen → Partizip II gegossen. Подлежащее die Glocken — "
                    "множественное число, время Präteritum, значит wurden "
                    "gegossen."
                ),
            },
        },
        {
            "id": "passiv_7",
            "kind": "order",
            "prompt": "Собери предложение: собор каждый день посещают гости.",
            "words": [
                "Der", "Dom", "wird", "jeden", "Tag", "von", "Gästen", "besucht",
            ],
            "answer": "Der Dom wird jeden Tag von Gästen besucht",
            "explain": (
                "В пассиве werden стоит на втором месте, а Partizip II — в конце: "
                "Der Dom wird ... besucht. Исполнитель идёт после von + Dativ: von "
                "Gästen."
            ),
            "retry": {
                "prompt": "Собери предложение: камни были привезены из гор.",
                "words": [
                    "Die", "Steine", "wurden", "aus", "den", "Bergen", "gebracht",
                ],
                "answer": "Die Steine wurden aus den Bergen gebracht",
                "explain": (
                    "Präteritum пассива: wurden + gebracht (Partizip II в конце). "
                    "Подлежащее во множественном числе — Die Steine wurden."
                ),
            },
        },
        {
            "id": "passiv_8",
            "kind": "error",
            "prompt": (
                "В предложении барда одна ошибка — в форме глагола werden. Найди её."
            ),
            "sentence": "Das Münster wurden von Karl dem Großen gebaut.",
            "wrong": "wurden",
            "fix": {
                "options": ["wurde", "werden", "wird", "geworden"],
                "answer": 0,
                "explain": (
                    "Подлежащее das Münster — единственное число, время Präteritum: "
                    "wurde gebaut. Форма wurden нужна только при подлежащем во "
                    "множественном числе."
                ),
            },
            "explain": (
                "das Münster — единственное число, значит Das Münster wurde von "
                "Karl dem Großen gebaut. wurden здесь — ошибка согласования."
            ),
            "retry": {
                "prompt": (
                    "В предложении барда одна ошибка — в форме после werden. Найди её."
                ),
                "sentence": "Der Dom wird von den Meistern bauen.",
                "wrong": "bauen",
                "fix": {
                    "options": ["gebaut", "bauen", "baute", "gebauten"],
                    "answer": 0,
                    "explain": (
                        "После werden в пассиве стоит Partizip II: gebaut. "
                        "Инфинитив bauen — типичная ошибка, личная форма baute тоже "
                        "не подходит."
                    ),
                },
                "explain": (
                    "Der Dom wird von den Meistern bauen — неверно: нужен Partizip "
                    "II, Der Dom wird von den Meistern gebaut."
                ),
            },
        },
    ],
}
