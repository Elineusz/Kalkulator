import interface as interface
import calculate as calc

def calculator():
    print("Witaj w kalkulatorze")
    user_choice = interface.display_menu()
    arguments = interface.get_arguments(user_choice)
    calc_func = calc.symbol_to_func[user_choice]

    print(interface.print_results(user_choice, arguments, calc_func(arguments[0],arguments[1])))

if __name__ == '__main__':
    calculator()

