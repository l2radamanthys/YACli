import re


def getTokens(text, tokens=[]):
    regex = re.compile(r'%\w+%')
    result = regex.search(text)
    if result != None:
        result = result.group()
        text = text.replace(result, '')
        result = result.replace('%', '')
        tokens.append(result)
        return getTokens(text, tokens)
    else:
        return tokens


# Testing
# test = 'hola %titulo% como %sdev% estas, que dia %34% es hoy'
# print(getToken(test))