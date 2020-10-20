import sys

menu = {}

def main_menu():
    menu[1]="Multiplication" 
    menu[2]="Division"
    menu[3]="Exit"
    print("\n| Tip, '|' = context, '>' = choice, '=' = input-field\n")
    print(60 * '-')
    print(f"|\t   12 x and 12 ÷ Tables Generator. \n|\n|\t\t 1. {menu[1]} \n|\t\t 2. {menu[2]} \n|\t\t 3. {menu[3]}")
    print(60 * '=')
    user_choice = int(input(">\t   Choose a selection from 1-3: \n= "))
    return user_choice

#def option_one(user_choice):

#def option_two(user_choice):

def option_three(user_choice):
    print("You have excited the program.")
    raise SystemExit

def main():
    main_menu()
    if option_three(user_choice) == 3:
        


main()
