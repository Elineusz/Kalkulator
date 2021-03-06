def get_operation():
    pass


def get_from_user(msg, validation_func, no_of_tries=3):



    numberOfWrongAttempts = 0
    while numberOfWrongAttempts < no_of_tries:
        answer = input(msg)
        answer = validation_func(answer)
        if not answer:
            numberOfWrongAttempts += 1
        else:
            return answer
    raise RuntimeError('przekroczono ilość prób')

def display_menu():
    msg = ('''Wybierz rodzaj działania:
                + : dodawanie
                - : odejmowanie
                * : mnożenie
                / : dzielenie
               ** : potęga
                ! : silnia : 
                
                Twój wybór: ''')
    def validation_func(answer):
        if answer not in ['+','-','*','/','**','!']:
            print("Niepoprawny kod działania")
            return None
        return answer
    return get_from_user(msg, validation_func)

def get_arguments(calculus):
    msg = '''
    Podaj argumenty oddzielone przecinkami
    Na przykład 3, 4 lub jedną liczbę dla silni
    '''
    def validation_func(answer):
        arguments = answer.split(',')
        try:
            arguments = [int(arg) for arg in arguments]
        except ValueError as error_1:
            print('Nie podano liczb, tylko inne znaki np litery. ')
            return None
        if calculus == '!':
            if len(arguments) != 1:
                raise TypeError('Podaj tylko jedną liczbę')
                return None
        else:
            if len(arguments) != 2:
                raise TypeError('Podaj dwie liczby')
                return None
        return arguments
    return get_from_user(msg, validation_func)

def print_results(calculus, numbers, result):
    if result == None:
        return None
    napis = ''

    for i, number in enumerate(numbers):
        napis = napis + str(number)  + ' '
        if i < len(numbers) - 1 :
            napis = napis + calculus + ' '
    napis = napis + "= " + str(result)
    return napis