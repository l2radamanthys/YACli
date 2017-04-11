import lib.angular


def call_handler(argv):
    element = argv[0]
    if element == 'angular-component':
        lib.angular.angular2_component(argv[1])

    elif element == 'angular-service':
        lib.angular.angular2_service(argv[1])

    else:
        print('Comando no valido')