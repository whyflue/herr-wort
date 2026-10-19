"""Тема 12: Passiv (Präsens, Präteritum)."""

TOPIC = {'id': 'passiv',
 'nr': 12,
 'title': 'Пассив (Präsens, Präteritum)',
 'short': 'Passiv: Präsens/Präteritum',
 'title_de': 'Passiv (Präsens, Präteritum)',
 'location': 'Аахен, собор Карла Великого',
 'location_de': 'Aachen, Dom Karls des Großen',
 'intro': 'Аахен — последняя остановка баллады. Бард входит под своды собора Карла Великого, где '
          'камни помнят мастеров: собор строили веками, его освящали, в нём короновали королей. '
          'Здесь о великом говорят не «кто это сделал», а «что было сделано». Бард записывает '
          'последнюю строчку: теперь и его песня «wird gebaut».',
 'listen': 'Бард прислоняется к холодной колонне и слушает собор. Внизу кто-то говорит: «der Stein '
           'wird gelegt», на башне — «die Glocken werden geläutet», а под сводами звучит старое '
           'торжественное «der Dom wurde gebaut». Ни одного имени мастера — только само дело.',
 'theory': [{'title': 'Что такое пассив и как он устроен',
             'body': 'Passiv отвечает на вопрос «что происходит с предметом?», а не «кто это '
                     'делает?».\n'
                     '\n'
                     'Формула: werden + Partizip II.\n'
                     'Präsens: Der Dom wird gebaut. Die Glocken werden geläutet.\n'
                     'Präteritum: Der Dom wurde gebaut. Die Glocken wurden geläutet.\n'
                     '\n'
                     'В пассиве на первом плане действие, а исполнитель часто вообще не назван: '
                     'Der Stein wird gelegt. — Камень кладут.\n'
                     '\n'
                     'werden спрягается по лицу и числу: ich werde, du wirst, er/sie/es wird, wir '
                     'werden, ihr werdet, sie werden. В Präteritum: ich wurde, er wurde; wir '
                     'wurden, sie wurden. Partizip II при этом не меняется.'},
            {'title': 'Порядок слов, время и исполнитель',
             'body': 'В простом предложении werden (wurde) стоит на втором месте, Partizip II — в '
                     'самом конце: Der Dom wird von den Meistern gebaut.\n'
                     '\n'
                     'Если предложение начинается не с подлежащего, werden всё равно на втором '
                     'месте, а подлежащее уходит за него:\n'
                     'Im Jahr 800 wurde der Dom gebaut. Jeden Tag werden die Glocken geläutet.\n'
                     '\n'
                     'Исполнителя вводим через von + Dativ (von dem → vom): Der Dom wurde von Karl '
                     'dem Großen gebaut. Die Glocken wurden von den Meistern geläutet. Во '
                     'множественном числе Dativ: von den Meistern (артикль den, у существительного '
                     '-n).\n'
                     '\n'
                     'Aktiv → Passiv: Der Baumeister baut den Dom. → Der Dom wird gebaut. '
                     'Дополнение в Akkusativ становится подлежащим.'},
            {'title': 'Präsens или Präteritum: выбирает werden',
             'body': 'Время в пассиве показывает вспомогательный глагол — форма Partizip II не '
                     'меняется.\n'
                     '\n'
                     'Präsens (wird / werden): действие сейчас, регулярно или как правило.\n'
                     'Der Dom wird restauriert. Die Glocken werden am Morgen geläutet.\n'
                     '\n'
                     'Präteritum (wurde / wurden): рассказ о прошлом.\n'
                     'Der Dom wurde gebaut. Die Glocken wurden geläutet.\n'
                     '\n'
                     'Согласование с подлежащим: der Dom wird/wurde — единственное число; die '
                     'Glocken werden/wurden — множественное. Не путай wurde (ед. ч.) и wurden (мн. '
                     'ч.).\n'
                     '\n'
                     'Частая ошибка: вместо Partizip II поставить инфинитив. «Der Dom wird bauen» '
                     '— неверно, нужно Der Dom wird gebaut.'}],
 'song_line': 'Nun wird das Lied gebaut aus Stein und Zeit,\n'
              'der Dom steht fest — der Barde ist bereit.',
 'exercises': [{'id': 'passiv_1',
                'kind': 'mc',
                'prompt': 'Das Burgtor ___ jeden Abend geschlossen.',
                'options': ['ist', 'wird', 'hat'],
                'answer': 1,
                'explain': 'Vorgangspassiv Präsens: «wird» + Partizip II.',
                'explain_de': 'Vorgangspassiv Präsens: „wird“ + Partizip II.'},
               {'id': 'passiv_2',
                'kind': 'gap',
                'prompt': 'Das Haus ___ im letzten Jahr gebaut. (werden, Präteritum)',
                'answer': 'wurde',
                'explain': 'Passiv Präteritum Singular: «wurde» + Partizip II.',
                'explain_de': 'Passiv Präteritum Singular: „wurde“ + Partizip II.'},
               {'id': 'passiv_3',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Die', 'Schwerter', 'werden', 'heute', 'gereinigt'],
                'answer': 'Die Schwerter werden heute gereinigt',
                'explain': 'Passiv Präsens Plural: «werden» + Partizip II.',
                'explain_de': 'Passiv Präsens Plural: „werden“ + Partizip II.'},
               {'id': 'passiv_4',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Die Briefe wird heute geschrieben.',
                'wrong': 'wird',
                'solution': 'Die Briefe werden heute geschrieben',
                'explain': '«Briefe» — Plural; поэтому «werden».',
                'explain_de': '„Briefe“ ist Plural; daher „werden“.'},
               {'id': 'passiv_5',
                'kind': 'input',
                'prompt': 'Bilde das Passiv im Präsens: Der Schmied repariert das Schwert.',
                'answers': ['Das Schwert wird vom Schmied repariert'],
                'explain': 'Akkusativ-объект становится подлежащим; «wird» + Partizip II.',
                'explain_de': 'Das Akkusativobjekt wird Subjekt; „wird“ + Partizip II.'},
               {'id': 'passiv_6',
                'kind': 'mc',
                'prompt': 'Die Rechnung ___ gestern bezahlt.',
                'options': ['wird', 'wurde', 'werden'],
                'answer': 1,
                'explain': 'Präteritum Passiv Singular → wurde.',
                'explain_de': 'Präteritum Passiv Singular → wurde.'},
               {'id': 'passiv_7',
                'kind': 'gap',
                'prompt': 'Die Burg ___ im 12. Jahrhundert gebaut. (werden, Präteritum)',
                'answer': 'wurde',
                'explain': 'Passiv Präteritum Singular → wurde.',
                'explain_de': 'Passiv Präteritum Singular → wurde.'},
               {'id': 'passiv_8',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Das', 'Dokument', 'wird', 'morgen', 'kopiert'],
                'answer': 'Das Dokument wird morgen kopiert',
                'explain': 'Passiv Präsens Singular: «wird» + Partizip II.',
                'explain_de': 'Passiv Präsens Singular: „wird“ + Partizip II.'},
               {'id': 'passiv_9',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Die Ritter wird von dem König eingeladen.',
                'wrong': 'wird',
                'solution': 'Die Ritter werden von dem König eingeladen',
                'explain': 'подлежащее во Plural → «werden».',
                'explain_de': 'Subjekt im Plural → „werden“.'},
               {'id': 'passiv_10',
                'kind': 'input',
                'prompt': 'Bilde das Passiv im Präteritum: Der Arzt untersuchte den Patienten.',
                'answers': ['Der Patient wurde vom Arzt untersucht'],
                'explain': 'Akkusativ-объект становится подлежащим; «wurde» + Partizip II.',
                'explain_de': 'Akkusativobjekt wird Subjekt; „wurde“ + Partizip II.'},
               {'id': 'passiv_11',
                'kind': 'mc',
                'prompt': 'Das Lied ___ vom Barden gesungen.',
                'options': ['wird', 'werden', 'wurde'],
                'answer': 0,
                'explain': 'Präsens Passiv Singular → wird (das Lied).',
                'explain_de': 'Präsens Passiv Singular → wird (das Lied).'},
               {'id': 'passiv_12',
                'kind': 'gap',
                'prompt': 'Die Tickets ___ am Bahnhof verkauft. (werden, Präsens)',
                'answer': 'werden',
                'explain': 'Passiv Präsens Plural → werden.',
                'explain_de': 'Passiv Präsens Plural → werden.'},
               {'id': 'passiv_13',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Der', 'König', 'wird', 'von', 'dem', 'Barden', 'gelobt'],
                'answer': 'Der König wird von dem Barden gelobt',
                'explain': 'Passiv Präsens: «wird» + Partizip II; действующее лицо с «von» + '
                           'Dativ.',
                'explain_de': 'Passiv Präsens: „wird“ + Partizip II; der Handelnde mit „von“ + '
                              'Dativ.'},
               {'id': 'passiv_14',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Das Fenster wurde gestern reparieren.',
                'wrong': 'reparieren',
                'solution': 'Das Fenster wurde gestern repariert',
                'explain': 'в пассиве стоит Partizip II, а не инфинитив.',
                'explain_de': 'Im Passiv steht das Partizip II, nicht der Infinitiv.'},
               {'id': 'passiv_15',
                'kind': 'input',
                'prompt': 'Bilde das Passiv im Präsens: Die Ritter schützen die Burg.',
                'answers': ['Die Burg wird von den Rittern geschützt'],
                'explain': 'Akkusativ-объект становится подлежащим; «wird» + Partizip II.',
                'explain_de': 'Akkusativobjekt wird Subjekt; „wird“ + Partizip II.'},
               {'id': 'passiv_16',
                'kind': 'mc',
                'prompt': 'Die Straße ___ letzte Woche renoviert.',
                'options': ['wird', 'wurde', 'werden'],
                'answer': 1,
                'explain': 'Präteritum Passiv Singular → wurde.',
                'explain_de': 'Präteritum Passiv Singular → wurde.'},
               {'id': 'passiv_17',
                'kind': 'gap',
                'prompt': 'Das Fest ___ jedes Jahr gefeiert. (werden, Präsens)',
                'answer': 'wird',
                'explain': 'Passiv Präsens Singular → wird.',
                'explain_de': 'Passiv Präsens Singular → wird.'},
               {'id': 'passiv_18',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Die', 'Briefe', 'wurden', 'gestern', 'geschickt'],
                'answer': 'Die Briefe wurden gestern geschickt',
                'explain': 'Passiv Präteritum Plural → wurden + Partizip II.',
                'explain_de': 'Passiv Präteritum Plural → wurden + Partizip II.'},
               {'id': 'passiv_19',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Die Burg wird von den Rittern schützen.',
                'wrong': 'schützen',
                'solution': 'Die Burg wird von den Rittern geschützt',
                'explain': 'в пассиве стоит Partizip II.',
                'explain_de': 'Im Passiv steht das Partizip II.'},
               {'id': 'passiv_20',
                'kind': 'input',
                'prompt': 'Bilde das Passiv im Präteritum: Die Firma stellte neue Mitarbeiter ein.',
                'answers': ['Neue Mitarbeiter wurden von der Firma eingestellt'],
                'explain': 'Akkusativ-объект становится подлежащим; «wurden» + Partizip II; '
                           'отделяемый глагол → eingestellt.',
                'explain_de': 'Akkusativobjekt wird Subjekt; „wurden“ + Partizip II; trennbares '
                              'Verb → eingestellt.'},
               {'id': 'passiv_21',
                'kind': 'mc',
                'prompt': 'Die Lieder ___ vom Barden geschrieben.',
                'options': ['werden', 'wird', 'wurde'],
                'answer': 0,
                'explain': 'Präsens Passiv Plural → werden.',
                'explain_de': 'Präsens Passiv Plural → werden.'},
               {'id': 'passiv_22',
                'kind': 'gap',
                'prompt': 'Das Auto ___ in der Werkstatt repariert. (werden, Präteritum)',
                'answer': 'wurde',
                'explain': 'Präteritum Passiv Singular → wurde.',
                'explain_de': 'Präteritum Passiv Singular → wurde.'},
               {'id': 'passiv_23',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Das', 'Schwert', 'wurde', 'von', 'dem', 'Schmied', 'geschmiedet'],
                'answer': 'Das Schwert wurde von dem Schmied geschmiedet',
                'explain': 'Passiv Präteritum: «wurde» + Partizip II; действующее лицо с «von» + '
                           'Dativ.',
                'explain_de': 'Passiv Präteritum: „wurde“ + Partizip II; der Handelnde mit „von“ + '
                              'Dativ.'},
               {'id': 'passiv_24',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Die Kinder werden von den Eltern abholen.',
                'wrong': 'abholen',
                'solution': 'Die Kinder werden von den Eltern abgeholt',
                'explain': 'в пассиве стоит Partizip II.',
                'explain_de': 'Im Passiv steht das Partizip II.'},
               {'id': 'passiv_25',
                'kind': 'input',
                'prompt': 'Bilde das Passiv im Präsens: Der König ruft den Barden.',
                'answers': ['Der Barde wird vom König gerufen'],
                'explain': 'Akkusativ-объект становится подлежащим; «wird» + Partizip II.',
                'explain_de': 'Akkusativobjekt wird Subjekt; „wird“ + Partizip II.'}]}
