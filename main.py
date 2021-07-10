import interface as i
import calculate as cal

def calculator():
    print("Witaj w kalkulatorze")
    user_choice = i.display_menu()
    arguments = i.get_arguments()
    calc_func = cal.symbol_to_func[user_choice]
    print(calc_func(*arguments))


if __name__ == '__main__':
    calculator()

cal.factorial(3)