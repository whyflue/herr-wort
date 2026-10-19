"""Тема 3: Personalpronomen und Verben im Präsens."""

TOPIC = {'id': 'praesens',
 'nr': 3,
 'title': 'Личные местоимения и глагол в Präsens',
 'short': 'Глаголы в Präsens',
 'title_de': 'Personalpronomen und Verben im Präsens',
 'location': 'Бремен, трактир у ратуши',
 'location_de': 'Bremen, Wirtshaus am Rathaus',
 'intro': 'В Бремене бард сворачивает к ратуше и заходит в трактир. Здесь тепло и шумно: служанка '
          'разносит блюда, хозяин расспрашивает гостей, а за столом кто-то хвастается дальней '
          'дорогой. Бард понимает: чтобы рассказать о себе, нужно менять глагол под каждое '
          'местоимение — ich singe, du singst, er singt. Он берёт лютню и пробует спеть о себе.',
 'listen': 'Бард слушает трактир: хозяин спрашивает «Was trinkst du?», служанка напевает «Ich '
           'bringe Brot und Bier», а сосед за столом хвастается: «Ich fahre morgen nach Köln». '
           'Каждое лицо — своё окончание.',
 'theory': [{'title': 'Личные местоимения',
             'body': 'ich — я, du — ты, er — он, sie — она, es — оно, wir — мы, ihr — вы (друзья, '
                     'не вежливая форма), sie — они, Sie — Вы (вежливо, всегда с большой буквы).\n'
                     '\n'
                     'er/sie/es выбираем по роду немецкого слова: der Wirt → er, die Laute → sie, '
                     'das Lied → es.\n'
                     '\n'
                     'Важно: das Mädchen — средний род, поэтому es, хотя речь идёт о девушке.\n'
                     '\n'
                     'sie значит и «она», и «они»; форма глагола подскажет: sie singt — она поёт, '
                     'sie singen — они поют.\n'
                     '\n'
                     'Вежливое Sie подходит и одному человеку, и нескольким: Wie heißen Sie?'},
            {'title': 'Окончания в Präsens',
             'body': 'Слабые глаголы меняются по образцу machen:\n'
                     '\n'
                     'ich mache\n'
                     'du machst\n'
                     'er/sie/es macht\n'
                     'wir machen\n'
                     'ihr macht\n'
                     'sie/Sie machen\n'
                     '\n'
                     'Окончания: -e, -st, -t, -en, -t, -en.\n'
                     '\n'
                     'Основа на -t или -d добавляет e: du arbeitest, er arbeitet.\n'
                     'Основа на -s, -ß, -z во 2-м лице берёт только -t: du tanzt, du heißt, du '
                     'sitzt.\n'
                     '\n'
                     'Глагол стоит в предложении на втором месте: Der Barde singt ein Lied. Heute '
                     'singt der Barde ein Lied.'},
            {'title': 'Сильные глаголы меняют гласную',
             'body': 'Во 2-м и 3-м лице единственного числа у многих сильных глаголов меняется '
                     'гласная в корне:\n'
                     '\n'
                     'fahren: du fährst, er fährt (a → ä)\n'
                     'lesen: du liest, er liest (e → ie)\n'
                     'nehmen: du nimmst, er nimmt (e → i)\n'
                     'sehen: du siehst, er sieht\n'
                     'essen: du isst, er isst\n'
                     '\n'
                     'В формах wir и ihr изменений нет: wir fahren, ihr fahrt, wir lesen, ihr '
                     'lest.\n'
                     '\n'
                     'У du и er формы часто различаются только окончанием -st/-t: du nimmst, er '
                     'nimmt.'}],
 'song_line': 'In Bremen sing ich, wer ich bin,\nund du, mein Wirt, hörst freundlich hin.',
 'exercises': [{'id': 'praesens_1',
                'kind': 'mc',
                'prompt': 'Meine Schwester ___ in Leipzig.',
                'options': ['wohne', 'wohnt', 'wohnen'],
                'answer': 1,
                'explain': '«sie» (3-е лицо Singular) → окончание -t.',
                'explain_de': '„sie“ (3. Person Singular) → Endung -t.'},
               {'id': 'praesens_2',
                'kind': 'gap',
                'prompt': 'Der Barde ___ ein neues Lied. (schreiben)',
                'answer': 'schreibt',
                'explain': '«er» → окончание -t; «schreiben» без чередования.',
                'explain_de': '„er“ → Endung -t; „schreiben“ ohne Vokalwechsel.'},
               {'id': 'praesens_3',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Wir', 'lernen', 'heute', 'Deutsch'],
                'answer': 'Wir lernen heute Deutsch',
                'explain': '«wir» → окончание -en; глагол на 2-м месте.',
                'explain_de': '„wir“ → Endung -en; das Verb steht an zweiter Stelle.'},
               {'id': 'praesens_4',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Der König sprechen mit dem Ritter.',
                'wrong': 'sprechen',
                'solution': 'Der König spricht mit dem Ritter',
                'explain': '«sprechen» — e → i в 3-м лице Singular → spricht.',
                'explain_de': '„sprechen“ — e → i in der 3. Person Singular → spricht.'},
               {'id': 'praesens_5',
                'kind': 'input',
                'prompt': 'Ersetze „ich“ durch „du“: Ich spiele Gitarre.',
                'answers': ['Du spielst Gitarre'],
                'explain': 'окончание -st для «du».',
                'explain_de': 'Endung -st für „du“.'},
               {'id': 'praesens_6',
                'kind': 'mc',
                'prompt': 'Du ___ gut Laute.',
                'options': ['spielst', 'spielt', 'spielen'],
                'answer': 0,
                'explain': '«du» → окончание -st.',
                'explain_de': '„du“ → Endung -st.'},
               {'id': 'praesens_7',
                'kind': 'gap',
                'prompt': 'Ich ___ jeden Morgen Kaffee. (trinken)',
                'answer': 'trinke',
                'explain': '«ich» → окончание -e.',
                'explain_de': '„ich“ → Endung -e.'},
               {'id': 'praesens_8',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Der', 'Ritter', 'reitet', 'durch', 'den', 'Wald'],
                'answer': 'Der Ritter reitet durch den Wald',
                'explain': '«er» → -et (основа на -t); «durch» + Akkusativ → den Wald.',
                'explain_de': '„er“ → -et (Stamm auf -t); „durch“ + Akkusativ → den Wald.'},
               {'id': 'praesens_9',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Er fahrt zu schnell.',
                'wrong': 'fahrt',
                'solution': 'Er fährt zu schnell',
                'explain': '«fahren» — a → ä в 3-м лице Singular → fährt.',
                'explain_de': '„fahren“ — a → ä in der 3. Person Singular → fährt.'},
               {'id': 'praesens_10',
                'kind': 'input',
                'prompt': 'Ersetze „er“ durch „ihr“: Er singt ein Lied.',
                'answers': ['Ihr singt ein Lied'],
                'explain': '«ihr» → окончание -t (основа без чередования).',
                'explain_de': '„ihr“ → Endung -t (Stamm ohne Vokalwechsel).'},
               {'id': 'praesens_11',
                'kind': 'mc',
                'prompt': '___ arbeitest heute lange?',
                'options': ['Du', 'Er', 'Ihr'],
                'answer': 0,
                'explain': 'окончание -est указывает на «du» (глагол на -t).',
                'explain_de': 'Die Endung -est weist auf „du“ hin (Verb auf -t).'},
               {'id': 'praesens_12',
                'kind': 'gap',
                'prompt': 'Der Barde ___ lange. (schlafen)',
                'answer': 'schläft',
                'explain': '«schlafen» — a → ä в 3-м лице Singular → schläft.',
                'explain_de': '„schlafen“ — a → ä in der 3. Person Singular → schläft.'},
               {'id': 'praesens_13',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Ihr', 'kommt', 'aus', 'Deutschland'],
                'answer': 'Ihr kommt aus Deutschland',
                'explain': '«ihr» → окончание -t.',
                'explain_de': '„ihr“ → Endung -t.'},
               {'id': 'praesens_14',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Die Ritter reitet in die Stadt.',
                'wrong': 'reitet',
                'solution': 'Die Ritter reiten in die Stadt',
                'explain': 'подлежащее во Plural → окончание -en.',
                'explain_de': 'Subjekt im Plural → Endung -en.'},
               {'id': 'praesens_15',
                'kind': 'input',
                'prompt': 'Setze ins Präsens: Ich (lesen) ein Buch.',
                'answers': ['Ich lese ein Buch'],
                'explain': '«ich» → lese (без чередования в 1-м лице).',
                'explain_de': '„ich“ → lese (kein Vokalwechsel in der 1. Person).'},
               {'id': 'praesens_16',
                'kind': 'mc',
                'prompt': 'Der König ___ einen Brief.',
                'options': ['schreibt', 'schreibe', 'schreiben'],
                'answer': 0,
                'explain': '«er» → окончание -t.',
                'explain_de': '„er“ → Endung -t.'},
               {'id': 'praesens_17',
                'kind': 'gap',
                'prompt': 'Wann ___ du nach Hause? (gehen)',
                'answer': 'gehst',
                'explain': '«du» → окончание -st.',
                'explain_de': '„du“ → Endung -st.'},
               {'id': 'praesens_18',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Sprichst', 'du', 'mit', 'dem', 'Barden'],
                'answer': 'Sprichst du mit dem Barden?',
                'explain': 'Ja/Nein-Frage: глагол на 1-м месте; «sprechen» — e → i → sprichst; '
                           '«mit» + Dativ → dem Barden.',
                'explain_de': 'Ja/Nein-Frage: Verb an erster Stelle; „sprechen“ — e → i → '
                              'sprichst; „mit“ + Dativ → dem Barden.'},
               {'id': 'praesens_19',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Wir lernt Deutsch.',
                'wrong': 'lernt',
                'solution': 'Wir lernen Deutsch',
                'explain': '«wir» → окончание -en.',
                'explain_de': '„wir“ → Endung -en.'},
               {'id': 'praesens_20',
                'kind': 'input',
                'prompt': 'Ersetze „ich“ durch „er“: Ich laufe schnell.',
                'answers': ['Er läuft schnell'],
                'explain': '«laufen» — au → äu в 3-м лице Singular → läuft.',
                'explain_de': '„laufen“ — au → äu in der 3. Person Singular → läuft.'},
               {'id': 'praesens_21',
                'kind': 'mc',
                'prompt': 'Ihr ___ heute zu spät.',
                'options': ['kommt', 'komme', 'kommen'],
                'answer': 0,
                'explain': '«ihr» → окончание -t.',
                'explain_de': '„ihr“ → Endung -t.'},
               {'id': 'praesens_22',
                'kind': 'gap',
                'prompt': 'Ich ___ auf einer Laute. (spielen)',
                'answer': 'spiele',
                'explain': '«ich» → окончание -e.',
                'explain_de': '„ich“ → Endung -e.'},
               {'id': 'praesens_23',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Er', 'nimmt', 'den', 'Bus'],
                'answer': 'Er nimmt den Bus',
                'explain': '«nehmen» — e → i → nimmt; «Bus» — мужской род, Akkusativ → den.',
                'explain_de': '„nehmen“ — e → i → nimmt; „Bus“ ist maskulin, Akkusativ → den.'},
               {'id': 'praesens_24',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Der König gibt den Ritter das Schwert.',
                'wrong': 'den',
                'solution': 'Der König gibt dem Ritter das Schwert',
                'explain': '«geben» + Dativ; «Ritter» → dem (Dativ мужского рода).',
                'explain_de': '„geben“ + Dativ; „Ritter“ → dem (Dativ maskulin).'},
               {'id': 'praesens_25',
                'kind': 'input',
                'prompt': 'Bilde eine Ja/Nein-Frage: Du gehst heute ins Kino.',
                'answers': ['Gehst du heute ins Kino?'],
                'explain': 'в вопросе без вопросительного слова глагол на 1-м месте, окончание -st '
                           'сохраняется.',
                'explain_de': 'In der Frage ohne Fragewort steht das Verb an erster Stelle, die '
                              'Endung -st bleibt.'}]}
