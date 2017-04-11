import os

import lib.parser

PATH = 'D:\\Workspace\\Python\\YACli\\templates\\'

def angular2_component(name):
    print('Creando Angular2 Component ->', name)
    filename = name.lower() + '.component'
    foldername = name.lower()
    data = {
        'selector': name.lower(),
        'templatename': filename + '.html',
        'classname': name + 'Component',
    }
    os.system('mkdir ' + foldername)
    os.system('touch ' + foldername + '/' + filename + '.html')
    # Todo falta implementar el resto
    # path = os.getcwd()
    template = open(PATH + 'angular2-component.tpl', 'r').readlines()
    output = open(foldername + '/' + filename + '.ts', 'w')

    for line in template:
        tokens = lib.parser.get_tokens(line)
        if (len(tokens) > 0):
            for token in tokens:
                value = data.get(token, None)
                if value != None:
                    token = '%' + token + '%'
                    line = line.replace(token, value)
        output.write(line)
    output.close()


def angular2_service(name):
    print('Creando Angular2 Service ->', name)
    pass