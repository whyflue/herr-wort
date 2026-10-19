"""Тема 1: Bestimmter und unbestimmter Artikel."""

TOPIC = {'id': 'artikel',
 'nr': 1,
 'title': 'Артикли: der/die/das, ein/eine',
 'short': 'Артикли',
 'short_de': 'Artikel',
 'title_de': 'Bestimmter und unbestimmter Artikel',
 'location': 'Любек, рыночная площадь',
 'location_de': 'Lübeck, Marktplatz',
 'intro': 'Бард-новичок входит в Любек через Гольстенские ворота. Утро пахнет хлебом и солью: '
          'торговцы раскладывают товар и называют его по имени. Бард достаёт перо, чтобы записать '
          'первую строчку. Но спеть о вещах нельзя, пока не научишься их называть — вместе с '
          'артиклем.',
 'listen': 'Бард прикладывает ладонь к стене склада и слушает рынок: торговка пересчитывает яблоки '
           '— «ein Apfel, noch ein Apfel», мальчишка гонит кота — «die Katze!». Три ключа к любому '
           'существительному: der, die, das.',
 'theory': [{'title': 'Три рода — три артикля',
             'body': 'У каждого немецкого существительного есть род, и артикль его показывает: der '
                     '(мужской), die (женский), das (средний). Род часто не совпадает с русским, '
                     'поэтому слово учат сразу с артиклем.\n'
                     '\n'
                     'der Barde — бард, der Apfel — яблоко, der Markt — рынок\n'
                     'die Laute — лютня, die Stadt — город, die Nacht — ночь\n'
                     'das Lied — песня, das Brot — хлеб, das Wasser — вода',
             'body_de': 'Jedes deutsche Substantiv hat ein Genus, und der Artikel zeigt es: der '
                        '(maskulin), die (feminin), das (neutrum). Das Genus stimmt oft nicht mit '
                        'dem russischen überein, deshalb lernt man ein Wort immer zusammen mit dem '
                        'Artikel.\n'
                        '\n'
                        'der Barde, der Apfel, der Markt\n'
                        'die Laute, die Stadt, die Nacht\n'
                        'das Lied, das Brot, das Wasser'},
            {'title': 'Неопределённый артикль: говорю впервые',
             'body': 'Если предмет упоминается впервые и мы не знаем, какой именно, ставим ein '
                     '(для der и das) или eine (для die).\n'
                     '\n'
                     'Ein Barde kommt in die Stadt. Das ist ein Apfel. Auf dem Markt singt eine '
                     'Verkäuferin.\n'
                     '\n'
                     'Множественное число артикля не имеет: Bäcker, Lieder, Städte.',
             'body_de': 'Wenn ein Gegenstand zum ersten Mal genannt wird und wir nicht wissen, '
                        'welcher genau gemeint ist, steht ein (bei der und das) oder eine (bei '
                        'die).\n'
                        '\n'
                        'Ein Barde kommt in die Stadt. Das ist ein Apfel. Auf dem Markt singt eine '
                        'Verkäuferin.\n'
                        '\n'
                        'Im Plural gibt es keinen unbestimmten Artikel: Bäcker, Lieder, Städte.'},
            {'title': 'Определённый артикль и Akkusativ',
             'body': 'der/die/das ставим, когда предмет уже назван или единственный в своём роде: '
                     'Der Barde ist müde. Die Sonne scheint.\n'
                     '\n'
                     'В винительном падеже (Akkusativ) меняется только мужской род: der → den, ein '
                     '→ einen. Женский и средний не меняются.\n'
                     '\n'
                     'Ich sehe den Barden. Ich stimme die Laute. Ich singe ein Lied.',
             'body_de': 'der/die/das steht, wenn der Gegenstand schon genannt oder der einzige '
                        'seiner Art ist: Der Barde ist müde. Die Sonne scheint.\n'
                        '\n'
                        'Im Akkusativ ändert sich nur das Maskulinum: der → den, ein → einen. '
                        'Femininum und Neutrum bleiben gleich.\n'
                        '\n'
                        'Ich sehe den Barden. Ich stimme die Laute. Ich singe ein Lied.'}],
 'song_line': 'Am Markt von Lübeck, im Morgenlicht,\n'
              'kauf ich ein Brot und ein Lied — mehr braucht ein Barde nicht.',
 'exercises': [{'id': 'artikel_1',
                'kind': 'mc',
                'prompt': '___ Lehrer kommt heute später.',
                'options': ['Der', 'Die', 'Das'],
                'answer': 0,
                'explain': '«Lehrer» — мужской род, Nominativ Singular → der.',
                'explain_de': '„Lehrer“ ist maskulin, Nominativ Singular → der.'},
               {'id': 'artikel_2',
                'kind': 'gap',
                'prompt': 'In der Burg wohnt ___ König. (ein)',
                'answer': 'ein',
                'explain': '«König» — мужской род, Nominativ Singular, неопределённый артикль → '
                           'ein.',
                'explain_de': '„König“ ist maskulin, Nominativ Singular, unbestimmter Artikel → '
                              'ein.'},
               {'id': 'artikel_3',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Eine', 'Studentin', 'liest', 'das', 'Buch'],
                'answer': 'Eine Studentin liest das Buch',
                'explain': 'В повествовательном предложении глагол на 2-м месте; подлежащее с '
                           'неопределённым артиклем стоит в начале.',
                'explain_de': 'Im Aussagesatz steht das finite Verb an zweiter Stelle; das Subjekt '
                              'mit unbestimmtem Artikel steht am Anfang.'},
               {'id': 'artikel_4',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Die Ritter trägt einen Helm.',
                'wrong': 'Die',
                'solution': 'Der Ritter trägt einen Helm',
                'explain': '«Ritter» здесь Singular мужского рода → der; глагол «trägt» тоже '
                           'указывает на Singular.',
                'explain_de': '„Ritter“ ist hier Singular maskulin → der; das Verb „trägt“ zeigt '
                              'ebenfalls Singular.'},
               {'id': 'artikel_5',
                'kind': 'input',
                'prompt': 'Ersetze den bestimmten Artikel durch den unbestimmten: Das Kind spielt.',
                'answers': ['Ein Kind spielt'],
                'explain': '«Kind» — средний род, Nominativ → ein.',
                'explain_de': '„Kind“ ist neutrum, Nominativ → ein.'},
               {'id': 'artikel_6',
                'kind': 'mc',
                'prompt': 'Der Barde singt ___ Lied.',
                'options': ['ein', 'eine', 'einen'],
                'answer': 0,
                'explain': '«Lied» — средний род, Akkusativ → ein (совпадает с Nominativ).',
                'explain_de': '„Lied“ ist neutrum, Akkusativ → ein (gleich wie Nominativ).'},
               {'id': 'artikel_7',
                'kind': 'gap',
                'prompt': 'Ich brauche ___ Lampe. (ein)',
                'answer': 'eine',
                'explain': '«Lampe» — женский род, Akkusativ → eine.',
                'explain_de': '„Lampe“ ist feminin, Akkusativ → eine.'},
               {'id': 'artikel_8',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Der', 'König', 'trägt', 'eine', 'Krone'],
                'answer': 'Der König trägt eine Krone',
                'explain': '«Krone» — женский род, Akkusativ → eine; глагол на 2-м месте.',
                'explain_de': '„Krone“ ist feminin, Akkusativ → eine; das Verb steht an zweiter '
                              'Stelle.'},
               {'id': 'artikel_9',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Ich sehe das Lehrer.',
                'wrong': 'das',
                'solution': 'Ich sehe den Lehrer',
                'explain': '«Lehrer» — мужской род; «sehen» требует Akkusativ → den.',
                'explain_de': '„Lehrer“ ist maskulin; „sehen“ verlangt den Akkusativ → den.'},
               {'id': 'artikel_10',
                'kind': 'input',
                'prompt': 'Ersetze den unbestimmten Artikel durch den bestimmten: Ein Ritter '
                          'kämpft.',
                'answers': ['Der Ritter kämpft'],
                'explain': '«Ritter» — мужской род, Nominativ → der.',
                'explain_de': '„Ritter“ ist maskulin, Nominativ → der.'},
               {'id': 'artikel_11',
                'kind': 'mc',
                'prompt': 'Wir wohnen in ___ kleinen Wohnung.',
                'options': ['ein', 'eine', 'einer'],
                'answer': 2,
                'explain': '«Wohnung» — женский род, Dativ после «in» (место) → einer.',
                'explain_de': '„Wohnung“ ist feminin, Dativ nach „in“ (Ort) → einer.'},
               {'id': 'artikel_12',
                'kind': 'gap',
                'prompt': 'Der Barde spielt auf ___ Laute. (ein)',
                'answer': 'einer',
                'explain': '«Laute» — женский род, Dativ (место, auf + Dativ) → einer.',
                'explain_de': '„Laute“ ist feminin, Dativ (Ort, auf + Dativ) → einer.'},
               {'id': 'artikel_13',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Das', 'Mädchen', 'kauft', 'ein', 'Brot'],
                'answer': 'Das Mädchen kauft ein Brot',
                'explain': '«Mädchen» — средний род (суффикс -chen), Nominativ → das; «Brot» — '
                           'средний род, Akkusativ → ein.',
                'explain_de': '„Mädchen“ ist neutrum (Suffix -chen), Nominativ → das; „Brot“ ist '
                              'neutrum, Akkusativ → ein.'},
               {'id': 'artikel_14',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Der König gibt die Ritter ein Schwert.',
                'wrong': 'die',
                'solution': 'Der König gibt dem Ritter ein Schwert',
                'explain': '«geben» требует Dativ для адресата; «Ritter» — мужской род, Dativ '
                           'Singular → dem.',
                'explain_de': '„geben“ verlangt Dativ für den Adressaten; „Ritter“ ist maskulin, '
                              'Dativ Singular → dem.'},
               {'id': 'artikel_15',
                'kind': 'input',
                'prompt': 'Ersetze den bestimmten Artikel durch den unbestimmten im Akkusativ: Ich '
                          'lese die Zeitung.',
                'answers': ['Ich lese eine Zeitung'],
                'explain': '«Zeitung» — женский род, Akkusativ → eine.',
                'explain_de': '„Zeitung“ ist feminin, Akkusativ → eine.'},
               {'id': 'artikel_16',
                'kind': 'mc',
                'prompt': '___ Barden singen auf dem Markt.',
                'options': ['Der', 'Die', 'Das'],
                'answer': 1,
                'explain': 'Plural → определённый артикль всегда die.',
                'explain_de': 'Plural → der bestimmte Artikel ist immer die.'},
               {'id': 'artikel_17',
                'kind': 'gap',
                'prompt': 'Hast du ___ Kugelschreiber für mich? (ein)',
                'answer': 'einen',
                'explain': '«Kugelschreiber» — мужской род, Akkusativ → einen.',
                'explain_de': '„Kugelschreiber“ ist maskulin, Akkusativ → einen.'},
               {'id': 'artikel_18',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Ein', 'Barde', 'schreibt', 'ein', 'Lied'],
                'answer': 'Ein Barde schreibt ein Lied',
                'explain': 'Оба существительных — мужской/средний род в Nominativ/Akkusativ → ein; '
                           'глагол на 2-м месте.',
                'explain_de': 'Beide Nomen sind maskulin/neutrum im Nominativ/Akkusativ → ein; das '
                              'Verb steht an zweiter Stelle.'},
               {'id': 'artikel_19',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Das Auto von mein Bruder ist neu.',
                'wrong': 'mein',
                'solution': 'Das Auto von meinem Bruder ist neu',
                'explain': '«von» требует Dativ; «Bruder» — мужской род, Dativ → meinem.',
                'explain_de': '„von“ verlangt Dativ; „Bruder“ ist maskulin, Dativ → meinem.'},
               {'id': 'artikel_20',
                'kind': 'input',
                'prompt': 'Setze den Artikel im Dativ ein: Der Ritter dankt ___ König (der).',
                'answers': ['dem König', 'Der Ritter dankt dem König.', 'dem'],
                'explain': '«danken» + Dativ; «König» — мужской род → dem.',
                'explain_de': '„danken“ + Dativ; „König“ ist maskulin → dem.'},
               {'id': 'artikel_21',
                'kind': 'mc',
                'prompt': 'Ich fahre mit ___ Fahrrad zur Arbeit.',
                'options': ['das', 'dem', 'den'],
                'answer': 1,
                'explain': '«mit» всегда + Dativ; «Fahrrad» — средний род, Dativ → dem.',
                'explain_de': '„mit“ immer + Dativ; „Fahrrad“ ist neutrum, Dativ → dem.'},
               {'id': 'artikel_22',
                'kind': 'gap',
                'prompt': 'Die Ritter reiten durch ___ Wald. (der)',
                'answer': 'den',
                'explain': '«durch» + Akkusativ; «Wald» — мужской род, Akkusativ → den.',
                'explain_de': '„durch“ + Akkusativ; „Wald“ ist maskulin, Akkusativ → den.'},
               {'id': 'artikel_23',
                'kind': 'order',
                'prompt': 'Собери предложение из слов.',
                'words': ['Wir', 'brauchen', 'einen', 'Tisch', 'und', 'einen', 'Stuhl'],
                'answer': 'Wir brauchen einen Tisch und einen Stuhl',
                'explain': '«Tisch» и «Stuhl» — мужской род, Akkusativ → einen.',
                'explain_de': '„Tisch“ und „Stuhl“ sind maskulin, Akkusativ → einen.'},
               {'id': 'artikel_24',
                'kind': 'error',
                'prompt': 'В предложении есть ошибка — найди слово, в котором она.',
                'sentence': 'Die Burg hat ein großes Tor und ein kleine Mauer.',
                'wrong': 'ein',
                'solution': 'Die Burg hat ein großes Tor und eine kleine Mauer',
                'explain': '«Mauer» — женский род, Akkusativ → eine.',
                'explain_de': '„Mauer“ ist feminin, Akkusativ → eine.'},
               {'id': 'artikel_25',
                'kind': 'input',
                'prompt': 'Ergänze den Artikel im Genitiv: Das ist das Haus ___ Nachbarn (der).',
                'answers': ['des Nachbarn', 'Das ist das Haus des Nachbarn.', 'des'],
                'explain': 'Genitiv мужского рода → des; «Nachbar» относится к n-Deklination (des '
                           'Nachbarn).',
                'explain_de': 'Genitiv maskulin → des; „Nachbar“ gehört zur n-Deklination (des '
                              'Nachbarn).'}]}
