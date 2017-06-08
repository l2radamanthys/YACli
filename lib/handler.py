from . import angular
from . import typescript


def call_handler(argv):
    element = argv[0]
    if element == 'angular-component' or element == 'ng-c':
        angular.angular2_component(argv[1])

    elif element == 'angular-service' or element == 'ng-s':
        angular.angular2_service(argv[1])

    elif element == 'angular-module' or element == 'ng-m':
        angular.angular2_module(argv[1])

    elif element == 'angular-pipe' or element == 'ng-p':
        angular.angular2_pipe(argv[1])

    elif element == 'angular-class':
        angular.angular2_class(argv[1])

    elif element == 'typescript-class' or element == 'ts-c':
        typescript.typescript_class(argv[1])


    else:
        print('Comando no valido:', element)
        print(
            'use:',
            'angular-component | ng-c',
            'angular-service | ng-s',
            'typescript-class | ng-m',
            'angular-pipe | ng-p',
            'angular-module | ng-p'
            'angular-class',
            'typescript-class | ts-c',
            sep = '\n -> ')