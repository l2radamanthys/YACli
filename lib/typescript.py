import os
from . import parser
from .settings import PATH 


def typescript_class(name):
    print('Creando TypeScript Class ->', name)
    data = {
        'classname': name,
    }
    output = parser.to_pascal(name) + '.ts'
    parser_ = parser.View('typescript-class.tpl')
    parser_.build_and_save(data, output)