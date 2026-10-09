text = input()
i = 0
while(i < len(text)):
    if text[i] == '.':
        text = text[:i:] + ',' + text[i + 1::]
    elif text[i] == ',':
        text = text[:i:] + '.' + text[i + 1::]
    if text[i] == ' ':
        text = text[:i:] + text[i+1::]
        if text[i].isupper():
            text = text[:i+1:] + text[i+1].upper() + text[i+2::]
        else:
            text = text[:i:] + text[i].upper() + text[i+1::]
    i += 1
print(text)

