import random

def display(message):
    print(message)

def give_random_number():
    value = random.randint(0, 100)
    return value

def answer_question(question):
    response = None
    while response != 'y' and response != 'n':
        response = input(question).lower()
    return response


def answer_question2(question='please type y or n'):
    response = None
    while response != 'y' and response != 'n':
        response = input(question).lower()
    return response

def give_random_number2(low=0, high=100, message="here is the number"):
    value = random.randint(low, high)
    print(message + " " + str(value))
    return value

# display("print something")
# value = give_random_number
#
# print(value())

# print(answer_question('you like python? '))
#print(display("message"))


if __name__ == '__main__':
    give_random_number2(high=1000, message="here: ")