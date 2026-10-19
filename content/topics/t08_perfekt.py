"""Тема 8: Perfekt mit haben/sein."""

TOPIC = {'id': 'perfekt',
 'nr': 8,
 'title': 'Perfekt с haben и sein',
 'short': 'Perfekt: haben/sein',
 'title_de': 'Perfekt mit haben/sein',
 'location': 'Ротенбург-на-Таубере, городская стена',
 'location_de': 'Rothenburg ob der Tauber, Stadtmauer',
 'intro': 'Дорога приводит барда в Ротенбург, и он поднимается на городскую стену. Отсюда видно '
          'всю долину, а вечером здесь собираются путники: каждый рассказывает, где он был и что '
          'успел сделать. Бард тоже хочет рассказать о своей дороге, но для прошедшего времени '
          'одного глагола мало.',
 'listen': 'Бард прижимается ухом к тёплым камням стены. Внизу скрипят телеги и звучат чужие '
           'рассказы: «Ich bin heute früh gekommen», «Er hat die ganze Nacht gesungen», «Wir sind '
           'bis zum Tor gegangen». В каждом — два глагола: haben или sein на втором месте и '
           'Partizip II в самом конце.',
 'theory': [{'title': 'Рамка Perfekt: два глагола',
             'body': 'Perfekt — прошедшее время для разговора и рассказа. Сказуемое состоит из '
                     'двух частей, они образуют рамку:\n'
                     '\n'
                     'haben или sein — на втором месте;\n'
                     'Partizip II — в самом конце.\n'
                     '\n'
                     'Ich habe ein Lied gesungen. Der Barde ist zur Mauer gegangen.\n'
                     '\n'
                     'Вспомогательный глагол спрягается: ich habe/bin, du hast/bist, er hat/ist, '
                     'wir haben/sind.\n'
                     '\n'
                     'Все остальные слова стоят между ними: Ich habe gestern auf der Mauer '
                     'gesungen.'},
            {'title': 'haben или sein?',
             'body': 'С sein идут глаголы движения и смены состояния: gehen, fahren, kommen, '
                     'laufen, aufstehen, einschlafen.\n'
                     '\n'
                     'Der Barde ist nach Rothenburg gefahren. Ich bin früh aufgestanden. Die Stadt '
                     'ist schön geworden.\n'
                     '\n'
                     'Остальные глаголы — с haben: machen, singen, kaufen, sehen, finden, helfen, '
                     'lesen.\n'
                     '\n'
                     'Ich habe die Stadt gesehen. Er hat mir geholfen. Wir haben Brot gekauft.\n'
                     '\n'
                     'Подсказка: движение «куда-то» и смена состояния — sein, обычное действие — '
                     'haben.'},
            {'title': 'Partizip II: как построить',
             'body': 'Слабые глаголы: ge- + основа + -t: machen → gemacht, kaufen → gekauft, sagen '
                     '→ gesagt.\n'
                     '\n'
                     'Сильные глаголы меняют гласную и кончаются на -en: singen → gesungen, sehen '
                     '→ gesehen, kommen → gekommen, gehen → gegangen, finden → gefunden.\n'
                     '\n'
                     'Без ge-: глаголы с неотделяемыми приставками be-, ver-, er- и глаголы на '
                     '-ieren: besuchen → besucht, verlieren → verloren, studieren → studiert.\n'
                     '\n'
                     'Partizip II всегда стоит в конце: Wir haben lange gesungen.'}],
 'song_line': 'Ich bin durch Täler und Städte gegangen,\n'
              'habe am Rothenburger Tor ein Lied angefangen.',
 'exercises': [{'id': 'perfekt_1',
                'kind': 'mc',
                'prompt': 'Der König ___ einen Brief geschrieben.',
                'options': ['ist', 'hat', 'haben'],
                'answer': 1,
                'explain': '«schreiben» — переходный глагол → Perfekt с haben.',
                'explain_de': '„schreiben“ ist transitiv → Perfekt mit haben.'},
               {'id': 'perfekt_2',
                'kind': 'gap',
                'prompt': 'Meine Freundin ___ nach Hause gegangen. (sein)',
                'answer': 'ist',
                'explain': '«gehen» — движение → Perfekt с sein.',
                'explain_de': '„gehen“ — Bewegung → Perfekt mit sein.'},
               {'id': 'perfekt_3',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Der', 'Barde', 'hat', 'ein', 'Lied', 'gesungen'],
                'answer': 'Der Barde hat ein Lied gesungen',
                'explain': 'Partizip II в конце.',
                'explain_de': 'Das Partizip II steht am Ende.'},
               {'id': 'perfekt_4',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Ich bin einen Film gesehen.',
                'wrong': 'bin',
                'solution': 'Ich habe einen Film gesehen',
                'explain': '«sehen» — переходный → Perfekt с haben.',
                'explain_de': '„sehen“ ist transitiv → Perfekt mit haben.'},
               {'id': 'perfekt_5',
                'kind': 'input',
                'prompt': 'Setze ins Perfekt: Der Ritter kauft Brot.',
                'answers': ['Der Ritter hat Brot gekauft'],
                'explain': '«kaufen» → Perfekt с haben; Partizip II gekauft.',
                'explain_de': '„kaufen“ → Perfekt mit haben; Partizip II gekauft.'},
               {'id': 'perfekt_6',
                'kind': 'mc',
                'prompt': 'Wir ___ gestern ins Kino gegangen.',
                'options': ['haben', 'sind', 'seid'],
                'answer': 1,
                'explain': '«gehen» — движение → sein; «wir» → sind.',
                'explain_de': '„gehen“ — Bewegung → sein; „wir“ → sind.'},
               {'id': 'perfekt_7',
                'kind': 'gap',
                'prompt': 'Der Barde ___ auf der Laute gespielt. (haben)',
                'answer': 'hat',
                'explain': '«spielen» — действие → haben.',
                'explain_de': '„spielen“ — Handlung → haben.'},
               {'id': 'perfekt_8',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Ich', 'habe', 'das', 'Buch', 'gelesen'],
                'answer': 'Ich habe das Buch gelesen',
                'explain': '«lesen» → Perfekt с haben; Partizip II gelesen.',
                'explain_de': '„lesen“ → Perfekt mit haben; Partizip II gelesen.'},
               {'id': 'perfekt_9',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Die Ritter haben in die Burg geritten.',
                'wrong': 'haben',
                'solution': 'Die Ritter sind in die Burg geritten',
                'explain': '«reiten» — движение → sein; Partizip II geritten.',
                'explain_de': '„reiten“ — Bewegung → sein; Partizip II geritten.'},
               {'id': 'perfekt_10',
                'kind': 'input',
                'prompt': 'Setze ins Perfekt: Ich trinke Kaffee.',
                'answers': ['Ich habe Kaffee getrunken'],
                'explain': '«trinken» → haben; Partizip II getrunken.',
                'explain_de': '„trinken“ → haben; Partizip II getrunken.'},
               {'id': 'perfekt_11',
                'kind': 'mc',
                'prompt': 'Der König ___ gestern früh aufgestanden.',
                'options': ['hat', 'ist', 'hat ... ge'],
                'answer': 1,
                'explain': '«aufstehen» — изменение состояния → sein; Partizip II aufgestanden.',
                'explain_de': '„aufstehen“ — Zustandsveränderung → sein; Partizip II '
                              'aufgestanden.'},
               {'id': 'perfekt_12',
                'kind': 'gap',
                'prompt': 'Wir ___ die Hausaufgaben gemacht. (haben)',
                'answer': 'haben',
                'explain': '«machen» → haben.',
                'explain_de': '„machen“ → haben.'},
               {'id': 'perfekt_13',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Der', 'König', 'ist', 'in', 'die', 'Burg', 'gegangen'],
                'answer': 'Der König ist in die Burg gegangen',
                'explain': '«gehen» → sein; Partizip II gegangen; «in» + Akkusativ (направление).',
                'explain_de': '„gehen“ → sein; Partizip II gegangen; „in“ + Akkusativ (Richtung).'},
               {'id': 'perfekt_14',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Ich habe nach Berlin gefahren.',
                'wrong': 'habe',
                'solution': 'Ich bin nach Berlin gefahren',
                'explain': '«fahren» — движение → sein; Partizip II gefahren.',
                'explain_de': '„fahren“ — Bewegung → sein; Partizip II gefahren.'},
               {'id': 'perfekt_15',
                'kind': 'input',
                'prompt': 'Setze ins Perfekt: Die Ritter kämpfen.',
                'answers': ['Die Ritter haben gekämpft'],
                'explain': '«kämpfen» → haben; Partizip II gekämpft.',
                'explain_de': '„kämpfen“ → haben; Partizip II gekämpft.'},
               {'id': 'perfekt_16',
                'kind': 'mc',
                'prompt': '___ du schon in Deutschland gewesen?',
                'options': ['Hast', 'Bist', 'Haben'],
                'answer': 1,
                'explain': '«sein» → Perfekt с sein; «du» → bist.',
                'explain_de': '„sein“ → Perfekt mit sein; „du“ → bist.'},
               {'id': 'perfekt_17',
                'kind': 'gap',
                'prompt': 'Der Barde ___ ein Lied geschrieben. (haben)',
                'answer': 'hat',
                'explain': '«schreiben» → haben.',
                'explain_de': '„schreiben“ → haben.'},
               {'id': 'perfekt_18',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Wir', 'sind', 'nach', 'Hause', 'gefahren'],
                'answer': 'Wir sind nach Hause gefahren',
                'explain': '«fahren» → sein.',
                'explain_de': '„fahren“ → sein.'},
               {'id': 'perfekt_19',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Der König hat in der Burg geblieben.',
                'wrong': 'hat',
                'solution': 'Der König ist in der Burg geblieben',
                'explain': '«bleiben» → Perfekt с sein; Partizip II geblieben.',
                'explain_de': '„bleiben“ → Perfekt mit sein; Partizip II geblieben.'},
               {'id': 'perfekt_20',
                'kind': 'input',
                'prompt': 'Setze ins Perfekt: Er studiert Germanistik.',
                'answers': ['Er hat Germanistik studiert'],
                'explain': 'глаголы на -ieren → без ge-; Perfekt с haben.',
                'explain_de': 'Verben auf -ieren → ohne ge-; Perfekt mit haben.'},
               {'id': 'perfekt_21',
                'kind': 'mc',
                'prompt': 'Die Barden ___ auf dem Markt gesungen.',
                'options': ['haben', 'sind', 'haben ... ge'],
                'answer': 0,
                'explain': '«singen» → haben; Partizip II gesungen.',
                'explain_de': '„singen“ → haben; Partizip II gesungen.'},
               {'id': 'perfekt_22',
                'kind': 'gap',
                'prompt': 'Ich ___ gestern früh eingeschlafen. (sein)',
                'answer': 'bin',
                'explain': '«einschlafen» — изменение состояния → sein.',
                'explain_de': '„einschlafen“ — Zustandsveränderung → sein.'},
               {'id': 'perfekt_23',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Der', 'Ritter', 'hat', 'das', 'Schwert', 'verloren'],
                'answer': 'Der Ritter hat das Schwert verloren',
                'explain': '«verlieren» → haben; неотделяемая приставка → без ge-; Partizip II '
                           'verloren.',
                'explain_de': '„verlieren“ → haben; untrennbares Präfix → ohne ge-; Partizip II '
                              'verloren.'},
               {'id': 'perfekt_24',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Sie sind die Prüfung bestanden.',
                'wrong': 'sind',
                'solution': 'Sie haben die Prüfung bestanden',
                'explain': '«bestehen» — переходный → haben; Partizip II bestanden (без ge-).',
                'explain_de': '„bestehen“ ist transitiv → haben; Partizip II bestanden (ohne '
                              'ge-).'},
               {'id': 'perfekt_25',
                'kind': 'input',
                'prompt': 'Setze ins Perfekt: Der Barde nimmt die Laute.',
                'answers': ['Der Barde hat die Laute genommen'],
                'explain': '«nehmen» → haben; Partizip II genommen.',
                'explain_de': '„nehmen“ → haben; Partizip II genommen.'}]}
