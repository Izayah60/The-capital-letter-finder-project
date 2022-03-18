def capit_letter(word):
    result = []
    for item in word:
        if item.isupper() is True:
            result.append(item)
            continue

    return result


capit_letter("WiRdEsFC")
