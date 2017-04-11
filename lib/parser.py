import re


def get_tokens(text, tokens=[]):
    regex = re.compile(r'%\w+%')
    result = regex.search(text)
    if result != None:
        result = result.group()
        text = text.replace(result, '')
        result = result.replace('%', '')
        tokens.append(result)
        return get_tokens(text, tokens)
    else:
        return tokens



class View:
    def __init__():
        data = {}


    def build():
        pass


    def save():
        pass


def view_build(template_name='', data={}):
    pass


# Testing
# test = 'hola %titulo% como %sdev% estas, que dia %34% es hoy'
# print(getToken(test))