# ------------------------------------------------------
#        Name: tfernsler
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
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
        if "food" in user_str:
            print("You used the secret word!")
            break
        elif "dog"in user_str or "Dog" in user_str:
            print('you used the word "dog" or the word "Dog"!\n')
            break
        else:
            print("Try again")



# Task 2
def check_greater():
    """ Add your docstring """
    pass



# Task 3
def get_special_numbers():
    """ Add your docstring """
    pass


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

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
