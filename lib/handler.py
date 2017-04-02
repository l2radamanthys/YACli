import lib.angular


def call_handler(argv):
    element = argv[0]
    if element == 'angular-component':
        lib.angular.angular2_component(argv[1])

    if element == 'angular-service':
        lib.angular.angular2_service(argv[1])
