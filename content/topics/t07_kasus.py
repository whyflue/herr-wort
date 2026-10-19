"""Тема 7: Akkusativ und Dativ."""

TOPIC = {'id': 'kasus',
 'nr': 7,
 'title': 'Аккузатив и датив',
 'short': 'Akkusativ и Dativ',
 'title_de': 'Akkusativ und Dativ',
 'location': 'Вена, императорский двор',
 'location_de': 'Wien, Kaiserhof',
 'intro': 'Дорога из Веймара приводит барда в Вену, ко двору императора. Здесь всё чинно: стража, '
          'музыканты, дамы в тяжёлых платьях. Барда просят спеть перед императором, и он понимает, '
          'что одного именительного падежа мало: по-немецки нужно различать, кого он видит '
          '(Akkusativ) и кому поёт (Dativ).',
 'listen': 'Бард слышит, как переговаривается двор: «Ich sehe den Kaiser», «Der Barde singt dem '
           'Kaiser ein Lied», «Ich helfe dem Sänger». Одни и те же слова меняют форму: вижу '
           'кого-то — den Kaiser, помогаю кому-то — dem Sänger.',
 'theory': [{'title': 'Akkusativ: кого? что?',
             'body': 'Винительный падеж отвечает на вопросы «кого? что?». Его требуют многие '
                     'глаголы: sehen, kaufen, haben, singen, suchen, finden, essen, trinken.\n'
                     '\n'
                     'Меняется только мужской род:\n'
                     'der → den, ein → einen.\n'
                     '\n'
                     'Остальные формы такие же, как в Nominativ: die, das, die (множественное '
                     'число), eine, ein, eine.\n'
                     '\n'
                     'Ich sehe den Kaiser. Der Barde kauft einen Wein. Die Frau hat eine Laute.\n'
                     '\n'
                     'Личные местоимения: mich, dich, ihn, sie, es, uns, euch, sie.\n'
                     '\n'
                     'Ich sehe ihn. Kennst du mich?'},
            {'title': 'Dativ: кому?',
             'body': 'Дательный падеж отвечает на вопрос «кому?». С ним идут глаголы helfen, '
                     'danken, geben, schenken, gefallen, gehören, antworten.\n'
                     '\n'
                     'Формы артиклей:\n'
                     'der → dem, die → der, das → dem, die (множественное) → den (и '
                     'существительное получает -n: den Kindern).\n'
                     '\n'
                     'Ich helfe dem Sänger. Der Barde dankt der Kaiserin. Er gibt den Kindern '
                     'Brot.\n'
                     '\n'
                     'Личные местоимения: mir, dir, ihm, ihr, ihm, uns, euch, ihnen.\n'
                     '\n'
                     'Helft ihr mir? Ich danke dir.'},
            {'title': 'Два дополнения в предложении',
             'body': 'Если при глаголе стоят оба дополнения, сначала идёт Dativ (кому), потом '
                     'Akkusativ (что):\n'
                     '\n'
                     'Der Barde schenkt dem Kaiser ein Lied. Ich gebe dem Wirt das Brot.\n'
                     '\n'
                     'Сначала человек, потом вещь — это главный порядок в немецком предложении.\n'
                     '\n'
                     'Если Akkusativ выражен местоимением, оно идёт первым: Der Barde schenkt es '
                     'dem Kaiser.\n'
                     '\n'
                     'Запомни пару: den Kaiser — вижу, dem Kaiser — пою и дарю. Одна буква меняет '
                     'роль слова в предложении.'}],
 'song_line': 'Der Kaiser in Wien trinkt den Wein,\ndem Sänger am Hof schenk ich den Reim.',
 'exercises': [{'id': 'kasus_1',
                'kind': 'mc',
                'prompt': 'Ich sehe ___ Mann.',
                'options': ['der', 'den', 'dem'],
                'answer': 1,
                'explain': '«sehen» + Akkusativ; мужской род → den.',
                'explain_de': '„sehen“ + Akkusativ; maskulin → den.'},
               {'id': 'kasus_2',
                'kind': 'gap',
                'prompt': 'Der König hilft ___ Ritter. (der)',
                'answer': 'dem',
                'explain': '«helfen» + Dativ; мужской род → dem.',
                'explain_de': '„helfen“ + Dativ; maskulin → dem.'},
               {'id': 'kasus_3',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Ich', 'gebe', 'meiner', 'Freundin', 'ein', 'Buch'],
                'answer': 'Ich gebe meiner Freundin ein Buch',
                'explain': 'адресат в Dativ (meiner Freundin), предмет в Akkusativ (ein Buch).',
                'explain_de': 'Der Adressat steht im Dativ (meiner Freundin), die Sache im '
                              'Akkusativ (ein Buch).'},
               {'id': 'kasus_4',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Der Barde dankt den König.',
                'wrong': 'den',
                'solution': 'Der Barde dankt dem König',
                'explain': '«danken» + Dativ → dem König.',
                'explain_de': '„danken“ + Dativ → dem König.'},
               {'id': 'kasus_5',
                'kind': 'input',
                'prompt': 'Ersetze „der Lehrer“ durch ein Pronomen: Ich helfe dem Lehrer.',
                'answers': ['Ich helfe ihm'],
                'explain': 'Dativ мужского рода Singular → ihm.',
                'explain_de': 'Dativ maskulin Singular → ihm.'},
               {'id': 'kasus_6',
                'kind': 'mc',
                'prompt': 'Die Ritter geben ___ König ein Schwert.',
                'options': ['der', 'den', 'dem'],
                'answer': 2,
                'explain': '«geben» + Dativ для адресата; «König» — мужской род → dem.',
                'explain_de': '„geben“ + Dativ für den Adressaten; „König“ ist maskulin → dem.'},
               {'id': 'kasus_7',
                'kind': 'gap',
                'prompt': 'Ich kaufe ___ Buch. (ein)',
                'answer': 'ein',
                'explain': '«Buch» — средний род, Akkusativ → ein.',
                'explain_de': '„Buch“ ist neutrum, Akkusativ → ein.'},
               {'id': 'kasus_8',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Der', 'Barde', 'schenkt', 'dem', 'König', 'ein', 'Lied'],
                'answer': 'Der Barde schenkt dem König ein Lied',
                'explain': 'Dativ (dem König) перед Akkusativ (ein Lied).',
                'explain_de': 'Dativ (dem König) vor Akkusativ (ein Lied).'},
               {'id': 'kasus_9',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Ich danke dich für die Hilfe.',
                'wrong': 'dich',
                'solution': 'Ich danke dir für die Hilfe',
                'explain': '«danken» + Dativ; «du» в Dativ → dir.',
                'explain_de': '„danken“ + Dativ; „du“ im Dativ → dir.'},
               {'id': 'kasus_10',
                'kind': 'input',
                'prompt': 'Ersetze „das Schwert“ durch ein Pronomen: Der Ritter hat das Schwert.',
                'answers': ['Der Ritter hat es'],
                'explain': 'Akkusativ среднего рода Singular → es.',
                'explain_de': 'Akkusativ neutrum Singular → es.'},
               {'id': 'kasus_11',
                'kind': 'mc',
                'prompt': 'Das Buch gehört ___.',
                'options': ['mir', 'mich', 'ich'],
                'answer': 0,
                'explain': '«gehören» + Dativ → mir.',
                'explain_de': '„gehören“ + Dativ → mir.'},
               {'id': 'kasus_12',
                'kind': 'gap',
                'prompt': 'Der König gibt ___ Barden einen Auftrag. (die Barden — Plural)',
                'answer': 'den',
                'explain': 'Dativ Plural → den Barden.',
                'explain_de': 'Dativ Plural → den Barden.'},
               {'id': 'kasus_13',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Wir', 'zeigen', 'dem', 'Gast', 'die', 'Stadt'],
                'answer': 'Wir zeigen dem Gast die Stadt',
                'explain': 'Dativ (dem Gast) перед Akkusativ (die Stadt).',
                'explain_de': 'Dativ (dem Gast) vor Akkusativ (die Stadt).'},
               {'id': 'kasus_14',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Die Ritter helfen den König.',
                'wrong': 'den',
                'solution': 'Die Ritter helfen dem König',
                'explain': '«helfen» + Dativ → dem König.',
                'explain_de': '„helfen“ + Dativ → dem König.'},
               {'id': 'kasus_15',
                'kind': 'input',
                'prompt': 'Ersetze „die Blumen“ durch ein Pronomen: Ich schenke meiner Mutter die '
                          'Blumen.',
                'answers': ['Ich schenke sie meiner Mutter'],
                'explain': 'оба дополнения — существительное и местоимение; Akkusativ-местоимение '
                           'стоит перед Dativ.',
                'explain_de': 'Beide Ergänzungen — Substantiv und Pronomen; das Akkusativpronomen '
                              'steht vor dem Dativ.'},
               {'id': 'kasus_16',
                'kind': 'mc',
                'prompt': 'Der Barde singt ___ König ein Lied.',
                'options': ['der', 'den', 'dem'],
                'answer': 2,
                'explain': 'адресат в Dativ → dem König.',
                'explain_de': 'Der Adressat steht im Dativ → dem König.'},
               {'id': 'kasus_17',
                'kind': 'gap',
                'prompt': 'Ich brauche ___ Stuhl. (ein)',
                'answer': 'einen',
                'explain': '«Stuhl» — мужской род, Akkusativ → einen.',
                'explain_de': '„Stuhl“ ist maskulin, Akkusativ → einen.'},
               {'id': 'kasus_18',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Die', 'Ritter', 'danken', 'dem', 'König'],
                'answer': 'Die Ritter danken dem König',
                'explain': '«danken» + Dativ → dem König.',
                'explain_de': '„danken“ + Dativ → dem König.'},
               {'id': 'kasus_19',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Ich sehe dem Auto.',
                'wrong': 'dem',
                'solution': 'Ich sehe das Auto',
                'explain': '«sehen» + Akkusativ; «Auto» — средний род → das.',
                'explain_de': '„sehen“ + Akkusativ; „Auto“ ist neutrum → das.'},
               {'id': 'kasus_20',
                'kind': 'input',
                'prompt': 'Ersetze „der Barde“ durch ein Pronomen: Der König dankt dem Barden.',
                'answers': ['Der König dankt ihm'],
                'explain': 'Dativ мужского рода Singular → ihm.',
                'explain_de': 'Dativ maskulin Singular → ihm.'},
               {'id': 'kasus_21',
                'kind': 'mc',
                'prompt': 'Ich schreibe ___ Freund einen Brief.',
                'options': ['mein', 'meinen', 'meinem'],
                'answer': 2,
                'explain': '«schreiben» + Dativ для адресата; мужской род → meinem.',
                'explain_de': '„schreiben“ + Dativ für den Adressaten; maskulin → meinem.'},
               {'id': 'kasus_22',
                'kind': 'gap',
                'prompt': 'Der König zeigt ___ Ritter die Burg. (die Ritter — Plural)',
                'answer': 'den',
                'explain': 'Dativ Plural → den Rittern (с -n).',
                'explain_de': 'Dativ Plural → den Rittern (mit -n).'},
               {'id': 'kasus_23',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Er', 'erklärt', 'den', 'Studenten', 'die', 'Regel'],
                'answer': 'Er erklärt den Studenten die Regel',
                'explain': 'Dativ (den Studenten) перед Akkusativ (die Regel).',
                'explain_de': 'Dativ (den Studenten) vor Akkusativ (die Regel).'},
               {'id': 'kasus_24',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Der Barde antwortet den König.',
                'wrong': 'den',
                'solution': 'Der Barde antwortet dem König',
                'explain': '«antworten» + Dativ → dem König.',
                'explain_de': '„antworten“ + Dativ → dem König.'},
               {'id': 'kasus_25',
                'kind': 'input',
                'prompt': 'Ersetze „dem Kind“ und „das Buch“ durch Pronomen: Ich gebe dem Kind das '
                          'Buch.',
                'answers': ['Ich gebe es ihm'],
                'explain': 'оба местоимения: Akkusativ (es) перед Dativ (ihm).',
                'explain_de': 'Beide Ergänzungen sind Pronomen: Akkusativ (es) vor Dativ (ihm).'}]}
