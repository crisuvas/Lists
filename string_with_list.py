n = ["Michael", "Lieberman"]


def join_strings(words):
    result = ""
    for w in range(len(words)):
        result += words[w]
        result += " "
    return result


print(join_strings(n))
