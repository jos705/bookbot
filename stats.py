def count_words(string):
    num_words = len(string.split())
    return num_words

def count_characters(string):
    counted_characters = {}
    for c in string.lower():
        if c not in counted_characters:
            counted_characters[c] = 1
        elif c in counted_characters:
            counted_characters[c] += 1
    return counted_characters

def sort_on(dict):
    return dict["num"]

def sort_output(dict_in):
    output = []
    for i in dict_in:
        if i.isalpha():
            x = {}
            x["char"] = i
            x["num"] = dict_in[i]
            output.append(x)
    output.sort(reverse=True, key=sort_on)
    return output



