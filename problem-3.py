def long_substr(text):

    l = 0

    for i in range(len(text)):

        c = ""

        for e in range(i, len(text)):

            if text[e] in c:
                break

            c = c + text[e]

            if len(c) > l:
                l = len(c)

    return l
  
