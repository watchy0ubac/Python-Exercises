def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    fin_phrase = ''
    for ltr in phrase:
        if ltr == to_swap.upper() or ltr == to_swap.lower():
            if ltr.isupper() == True:
                ltr = ltr.lower()
                fin_phrase += ltr
            elif ltr.islower() == True:
                ltr = ltr.upper()
                fin_phrase += ltr
        else:
            fin_phrase += ltr
    return fin_phrase
