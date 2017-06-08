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
    parser.blank_file(foldername + '/' + filename + '.html')
    parser.blank_file(foldername + '/' + foldername + '.scss')
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


def angular2_pipe(name):
    print('Creando Angular2 Pipe ->', name)
    data = {
        'classname': name + 'Pipe',
        'selector': parser.to_pascal(name)
    }
    output = parser.to_pascal(name) + '.pipe.ts'
    parser_ = parser.View('angular2-pipe.tpl')
    parser_.build_and_save(data, output)


def angular2_module(name):
    print('Creando Angular2 Module ->', name)
    foldername = parser.to_pascal(name)
    data = {
        'classname': name + 'Module',
        'component': name + 'Component',
        'componentfile': parser.to_pascal(name) + '.component',
    }
    output = parser.to_pascal(name) + '.module.ts'
    parser_ = parser.View('angular2-module.tpl')
    os.system('mkdir ' + foldername)
    parser_.build_and_save(data, foldername + '/' + output)
    angular2_component(name)
