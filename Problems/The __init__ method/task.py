def check_word(word):
    if not '0' in word:
        return word
    else:
        raise NotWordError(word)

def error_handling(word):
    try:
        print(check_word(word))
    except NotWordError as err:
        print(err)
