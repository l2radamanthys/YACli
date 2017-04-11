import re
from .settings import PATH


pattP = re.compile(r'(.)([A-Z][a-z]+)')
pattF = re.compile('([a-z0-9])([A-Z])')


def get_tokens(text):
    """
        Obtener tokens de un string
    """
    regex = re.compile(r'%\w+%')
    result = regex.findall(text)
    if len(result) > 0:
        result = list(set(result))
        tokens = [w.replace('%', '') for w in result]
        return tokens
    else:
        return []


def to_pascal(text):
    """
        comvierte camel case en notacion pascal
    """
    return pattF.sub(r'\1-\2', pattP.sub(r'\1-\2', text)).lower()


class View:
    """
        View parse class
    """
    def __init__(self, template_name):
        self.template_name = template_name
        self.template = open(PATH + template_name, 'r').readlines()


    def build(self, data):
        result = []
        for line in self.template:
            tokens = get_tokens(line);
            if len(tokens) > 0:
                for token in tokens:
                    value = data.get(token, None)
                    if value != None:
                        token = '%' + token + '%'
                    line = line.replace(token, value)
            result.append(line)
        return result


    def build_and_save(self, data, output_name):
        result = self.build(data)
        output = open(output_name, 'w')
        for line in result:
            output.write(line)
        output.close()



if __name__ == '__main__':
    # Testing
    test = 'hola %titulo% como %sdev% estas, que dia %34% es hoy'
    print(to_pascal("HolaComoEstasFEOs"))
    print(get_tokens(test))
