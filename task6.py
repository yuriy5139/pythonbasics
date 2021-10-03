def firstcap(line):
    return line.capitalize()

def textcap(text):
    return ' '.join(list(map(lambda item: firstcap(item), text.split())))

print(textcap("blabla blablb blabla blabla"))