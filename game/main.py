import random

def choose_options():
    options = ("piedra", "papel", "tijera")
    user_option = input("Piedra, papel o tijera =>")
    user_option = user_option.lower()

    if not user_option in options:
        print("Esa opcion no es valida")
        #continue    #continue provoca saltar todo el codigo que sigue y vuelve a validar opcion
        return None,None

    computer_option = random.choice(options)

    print("User option =>", user_option)
    print("Computer option =>", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana a tijera")
            print("User gano")
            user_wins += 1
        else:
            print("Papel gana a piedra")
            print("computer gano!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana a piedra")
            print("User gano")
            user_wins += 1
        else: 
            print("Tijera gana a papel")
            print("Computer gano")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel")
            print("User gana")
            user_wins += 1
        else:
            print("Piedra gana a tijera")
            print("Computer gano")
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1
    while True:

        print("*" * 10)
        print("ROUND ", rounds)
        print("*" * 10)

        print("Computer wins", computer_wins)
        print("User wins", user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
        if computer_wins == 2:
            print("El ganador es la computadora")
            break
        if user_wins == 2:
            print("El ganador es el usuario")
            break

run_game()