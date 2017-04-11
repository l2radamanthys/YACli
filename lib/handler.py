from . import angular
from . import typescript


def call_handler(argv):
    element = argv[0]
    if element == 'angular-component' or element == 'ng-c':
        angular.angular2_component(argv[1])

    elif element == 'angular-service' or element == 'ng-s':
        angular.angular2_service(argv[1])

    elif element == 'typescript-class' or element == 'ts-c':
        typescript.typescript_class(argv[1])

    elif element == 'angular-class':
        angular.angular2_class(argv[1])


    else:
        print('Comando no valido:', element)
        print(
            'use:',
            'angular-component',
            'angular-service',
            'typescript-class',
            'angular-class',
            sep = '\n -> ')