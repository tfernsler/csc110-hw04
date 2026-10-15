# ------------------------------------------------------
#        Name: tfernsler
#       Peers: (add any collaborators)
#  References: pythontutor, austinhenley.com/blog/vowels.html
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ This function checks if the user has used the secret word, and outputs
    "You used the secret word!" is they do, it also outputs 'you used the word
    "dog" or the word "Dog"!' if they use those words """
        
    while True:
        user_str = input("give me a sentence: ")
        if secret_word in user_str:
            print("You used the secret word!")
            break
        elif "dog" in user_str or "Dog" in user_str:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        else:
            print("Try again")



# Task 2
def check_greater():
    """ this function gets two integers from the user and checks which is greater """
        
    while True:
        fir = input("give me an int: ")
        seco = input("give me another int: ")
        if fir > seco:
            print("First is Greater")
            break
        elif seco > fir:
            print("Second is Greater")
            break
        else:
            print("Try again")


# Task 3
def get_special_numbers():
    """ this function examines numbers over a range and only prints them if they
        meet the conditions: odd, multiple of 3, and not a multiple of 5 """
    for i in range(1, 40):
        if (i % 2 == 1) and (i % 3 == 0) and (i % 5 != 0):
            print(i)
        else:
            pass


# Task 4.a
def my_for_loop():
    """ this function determines if each character in user input is a vowel or consonant """
    usr_str = input("give me a word between 2 and 5 chrs: ")
    if len(usr_str) >= 5 or len(usr_str) <= 2:
        print("bad word")
        return
    vowels = ['a', 'e', 'i', 'o', 'u']
    for chr in usr_str:
        if chr in vowels:
            print(f"{chr} is a vowel")
        else:
            print(f"{chr} is a consonant")
    

# Task 4.b
def my_while_loop():
    """ this loop offers the user a short menu, if they choose 'a' then the menu repeats,
        'b' it prints 'Goodby' and returns, and 'c' the program exits, anything else and
        it prints 'try again' and repeats """
    while True:
        chce = input("pick a, b, or c: ")
        if chce == 'a':
            continue
        elif chce == 'b':
            print("Goodbye")
            return
        elif chce == 'c':
            sys.exit()
        else:
            print("try again")
    

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
