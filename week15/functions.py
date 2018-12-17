# what's function?
#
import random


def display(message):
    print(message)


# Global variable
# def display_value():
#     print(value)


def give_me_random():
    return random.randint(0, 100)


def answer_question(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

# default parameter value
# def answer_question2(question='Please enter y or n'):


if __name__ == "__main__":
    display("Here is a message")

    number = give_me_random()
    display(number)

    answer = answer_question("enter y or n ")
    print(answer)

    # Global variable
    # value = 10
    # display_value()
