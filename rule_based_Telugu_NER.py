import nltk


def extracting_nouns():
    sentence = u" `06`1`00`1 `0.`0$`0? `02`0`1`07`1`0.`0? `09`1`0&`1`00`0>`0,`0>`0&`1`02`1 `0`1`0$`0(`1`0/ `08`1`0`1`02`1`02`1 `00`1`0`0!`1 `08`0`05`0$`1`08`00`0>`02`1 `0`0 `00`1`0*`0>`0/`0? `0`1`0!`0> `0`00`1`0`1`0*`1`0`02`1"
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    print(tagged)

    verbs = [token for token, pos in tagged if pos.startswith('V')]
    print(verbs)

    location_noun = list()
    organisation_name = list()
    person_name = list()
    time_ner = list()
    currency_ner = list()

    for i in range(len(tokens) - 1):
        word = tokens[i]
        next_word = tokens[i + 1]
        prev_word = tokens[i - 1]
        if word.endswith('`0(`0`00`0'):                              # Extracting Location Nouns
            location_noun.append(word)
        elif word.endswith('`0*`1`00`0'):
            location_noun.append(word)
        elif word.endswith('`0`0?`02`1`02`0>'):
            location_noun.append(word)
        elif word.endswith('`0,`0>`0&`1'):
            location_noun.append(word)
        elif word.endswith('`0*`1`0'):
            location_noun.append(word)
        elif word.endswith('`0*`0>`02`1`0'):
            location_noun.append(word)
        if word.endswith('`0(`0`00`0`0`0?'):
            location_noun.append(word)
        elif word.endswith('`0*`1`00`0`0`0?'):
            location_noun.append(word)
        elif word.endswith('`0`0?`02`1`02`0>`0`0?'):
            location_noun.append(word)
        elif word.endswith('`0,`0>`0&`1`0`0?'):
            location_noun.append(word)
        elif word.endswith('`0*`1`0`0`0?'):
            location_noun.append(word)
        elif word.endswith('`0*`0>`02`1`0`0`0?'):
            location_noun.append(word)
        elif word.endswith('`0`1`0!`0>`0`0?'):
            location_noun.append(word)
        elif word.endswith('`0(`0`00`0`02`1'):
            location_noun.append(word)
        elif word.endswith('`0*`1`00`0`02`1'):
            location_noun.append(word)
        elif word.endswith('`0`0?`02`1`02`0>`02`1'):
            location_noun.append(word)
        elif word.endswith('`0,`0>`0&`1`02`1'):
            location_noun.append(word)
        elif word.endswith('`0*`1`0`02`1'):
            location_noun.append(word)
        elif word.endswith('`0*`0>`02`1`0`02`1'):
            location_noun.append(word)
        elif word.endswith('`0`1`0!`0>`02`1'):
            location_noun.append(word)
        if word == '`06`1`00`1 ':
            person_name.append(word)                                 # Extracting Person Names
            person_name.append(next_word)
        elif word == '`06`1`00`1 `0.`0$`0?':
            person_name.append(word)
            person_name.append(next_word)
        elif word == '`0`1`0.`0>`00`0?':
            person_name.append(word)
            person_name.append(next_word)
        elif word == '`0!`0>.':
            person_name.append(word)
            person_name.append(next_word)
        elif word == '`0.`1`0`1`0/`0.`0`0$`1`00`0?':
            person_name.append(word)
            person_name.append(next_word)
        elif word == '`0*`1`00`0'`0>`0(`0.`0`0$`1`00`0?':
            person_name.append(word)
            person_name.append(next_word)
        elif word == '`00`0>`07`1`0`1`00`0*`0$`0?':
            person_name.append(word)
            person_name.append(next_word)
        elif word == '`0*`1`00`1 ':
            person_name.append(word)
            person_name.append(next_word)
        if word.endswith('`08`0`08`1`0%'):
            organisation_name.append(prev_word)                 # Extracting Organisation names
            organisation_name.append(word)
        elif word.endswith('`08`1`0`1`02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0`03`0>`06`0>`02'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0`0>`02`1`0`1 '):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`05`0?`0&`1`0/`0>`02`0/`0'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0/`1`0(`0?`05`00`1`08`0?`0`1 '):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0`0`0*`1`0(`1 '):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0/`1`0(`0?`0/`0(`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0,`1`0/`0>`0`0`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`09`1`0`02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        if word.endswith('`08`0`08`1`0%`0`0?'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`08`1`0`1`02`1`0`0?'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0`03`0>`06`0>`02`0`0?'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0`0>`02`1`0`1 `0`0?'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`05`0?`0&`1`0/`0>`02`0/`0`0`0?'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0/`1`0(`0?`05`00`1`08`0?`0`1 `0`0?'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0`0`0*`1`0(`1 `0`0?'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0/`1`0(`0?`0/`0(`1`0`0?'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0,`1`0/`0>`0`0`1`0`0?'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`09`1`0`02`1`0`0?'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        if word.endswith('`08`0`08`1`0%`02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`08`1`0`1`02`1`02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0`03`0>`06`0>`02`02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0`0>`02`1`0`1 `02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`05`0?`0&`1`0/`0>`02`0/`0`02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0/`1`0(`0?`05`00`1`08`0?`0`1 `02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0`0`0*`1`0(`1 `02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0/`1`0(`0?`0/`0(`1`02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`0,`1`0/`0>`0`0`1`02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
        elif word.endswith('`09`1`0`02`1`02`1'):
            organisation_name.append(prev_word)
            organisation_name.append(word)
            
        if word.isdigit():                                  # Extracting Time and Currency
            if next_word == '`00`1`0*`0>`0/`0?':
                currency_ner.append(word)
                currency_ner.append(next_word)
            elif next_word == '`0`0`0`02`1' or next_word == '`0(`0?`0.`1`07`0>`02`1' or next_word == '`08`0`05`0$`1`08`00`0' or next_word == '`0(`1`02':
                time_ner.append(word)
                time_ner.append(next_word)
        elif word == '`0`0' or word == '`00`1`0`0!`1' or word == '`0.`1`0!`1' or word == '`0(`0>`02`1`0`1' or word == '`0`0&`1' or word == '`0`00`1' or word == '`0`0!`1' or word == '`0`0(`0?`0.`0?`0&`0?' or word == '`0$`1
`0.`1`0.`0?`0&`0?' or word == '`0*`0&`0?':
            if next_word == '`0(`0?`0.`0?`07`0' or next_word == '`0`0`0' or next_word == '`08`0`05`0$`1`08`00`0' or next_word == '`0(`1`02' or next_word == '`0(`0?`0.`1`07`0>`02`1' or next_word == '`0`0`0`02`1' or next_word == '`08`0`05`0$`1`08`00`0>`02`1' or next_word == '`0(`1`02`02`1':
                time_ner.append(word)
                time_ner.append(next_word)
            elif next_word == '`00`1`0*`0>`0/`0?' or '`00`1`0*`0>`0/`0?`02`1':
                currency_ner.append(word)
                currency_ner.append(next_word)
        elif word.startswith('`0*`0&'):
            if next_word == '`0(`0?`0.`1`07`0>`02`1' or next_word == '`0`0`0`02`1' or next_word == '`08`0`05`0$`1`08`00`0>`02`1' or next_word == '`0(`1`02`02`1':
                time_ner.append(word)
                time_ner.append(next_word)
            elif next_word == '`00`1`0*`0>`0/`0?`02`1':
                currency_ner.append(word)
                currency_ner.append(next_word)
        elif word.startswith('`0`00'):
            if next_word == '`0(`0?`0.`1`07`0>`02`1' or next_word == '`0`0`0`02`1' or next_word == '`08`0`05`0$`1`08`00`0>`02`1' or next_word == '`0(`1`02`02`1':
                time_ner.append(word)
                time_ner.append(next_word)
            elif next_word == '`00`1`0*`0>`0/`0?`02`1':
                currency_ner.append(word)
                currency_ner.append(next_word)

        else:
            if word.endswith('`0`0?'):                             # Extracting with the help of sub-categories
                for p in verbs:
                    if p.startswith('`05'):
                        location_noun.append(word)
                        organisation_name.append(prev_word)
                        organisation_name.append(word)
            elif word.endswith('`02`1'):
                for p in verbs:
                    if p.startswith('`0	`0(`1`0('):
                        location_noun.append(word)
                        organisation_name.append(prev_word)
                        organisation_name.append(word)
            elif 'w\s?`0(`1`0`0`0?':
                for p in verbs:
                    if p.startswith('`05`1'):
                        location_noun.append(word)
                        organisation_name.append(prev_word)
                        organisation_name.append(word)
            elif word.endswith('`0*`0`1`0.?'):
                for p in verbs:
                    if p.startswith('`05`1'):
                        organisation_name.append(prev_word)
                    elif p.startswith('`0	`0(`1`0('):
                        organisation_name.append(prev_word)
                        organisation_name.append(word)
            elif 'w\s?`0.`1 `0&.?':
                for p in verbs:
                    if p.startswith('`0	`0(`1`0('):
                        organisation_name.append(prev_word)
                        organisation_name.append(word)
            for p in verbs:
                if p.endswith('`0`0&`0?'):
                    person_name.append(word)
                elif p.endswith('`00`1'):
                    person_name.append(word)
                elif p.endswith('`0!`1'):
                    person_name.append(word)

    print("The location Nouns in the sentence are:", location_noun)
    print("The organization names in the sentence are:", organisation_name)
    print("The person names in the sentence are:", person_name)
    print("The time NERs are:", time_ner)
    print("The currency NERs are:", currency_ner)


nouns_in_sentence = extracting_nouns()



