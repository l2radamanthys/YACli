import os
from . import parser
from . import typescript
from .settings import PATH 


def angular2_component(name):
    print('Creando Angular2 Component ->', name)
    filename = parser.to_pascal(name) + '.component'
    foldername = parser.to_pascal(name)
    data = {
        'selector': parser.to_pascal(name),
        'templatename': filename + '.html',
        'classname': name + 'Component',
    }
    os.system('mkdir ' + foldername)
    os.system('touch ' + foldername + '/' + filename + '.html')
    os.system('touch ' + foldername + '/' + filename + '.css')
    output = foldername + '/' + filename + '.ts'
    parser_ = parser.View('angular2-component.tpl')
    parser_.build_and_save(data, output)


def angular2_service(name):
    print('Creando Angular2 Service ->', name)
    data = {
        'classname': name + 'Service',
    }
    output = parser.to_pascal(name) + '.service.ts'
    parser_ = parser.View('angular2-service.tpl')
    parser_.build_and_save(data, output)

def angular2_class(name):
    """
        decorator
    """
    typescript.typescript_class(name)
