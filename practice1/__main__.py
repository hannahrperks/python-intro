# def is called a function
def print_hello_world():
    print("Hello")
    print("World")


def print_multiples_of_six():
    a = 6
    print("6 x 1 =", a * 1)
    print("6 x 2 =", a * 2)
    print("6 x 3 =", a * 3)
    print("6 x 4 =", a * 4)
    print("6 x 5 =", a * 5)
    print("6 x 6 =", a * 6)
    print("6 x 7 =", a * 7)
    print("6 x 8 =", a * 8)
    print("6 x 9 =", a * 9)
    print("6 x 10 =", a * 10)


def print_halt():
    print("Halt!")
    user_input = input("Who goes there? ")
    print("You may pass,", user_input)


def print_assignment_practice():
    a = 1
    print(a)
    a = a + 1
    print(a)
    a = a * 2
    print(a)


def print_assignment_practice_two():
    number = float(input("Type in a number: "))
    integer = int(input("Type in an integer: "))
    text = input("Type in a string: ")
    print("number =", number)
    print("number is a", type(number))
    print("number x 2 =", number * 2)
    print("integer =", integer)
    print("integer x 2 =", integer * 2)
    print("text =", text)
    print("text is a", type(text))
    print("text x 2 =", text * 2)

def print_olly_oy():
    print("If I say olly, you say oy!")
    user_input = input("Olly! ")
    user_input = input("Olly! ")
    user_input = input("Olly, Olly, Olly! ")

# This function calculates times from given distances and rates.
def print_rates_times():
    print("Input a rate and a distance to calculate time.")
    rate = float(input("Rate: "))
    distance = float(input("Distance: "))
    time = (distance / rate)
    print("Time: ", time)

def print_count_to_ten():
    a = 0
    while a < 10:
        a = a + 1
        print(a)

def print_calculate_sum():
    a = 1
    s = 0
    print("Enter numbers to add to the sum.")
    print("Enter 0 to quit.")
    while a != 0:
        print("Current sum: ", s)
        a = float(input("Number: "))
        s = s + a
    print("Total Sum =", s)

def print_infinite_loop():
    while 1 == 1:
        print("Help! I'm stuck in a loop.")

def print_fibonacci_sequence():
    a = 0
    b = 1
    count = 0
    max_count = 15
    while count < max_count:
        count = count + 1
        print(a, b, end=" ") # =" " keeps all on one line.
        a = a + b
        b = a + b
    print()


def print_password():
    password = str()
    while password != "let me in":
        password = input("Password: ")
    print("Welcome in.")

def print_username_and_password():
    print("Please enter your username and password.")
    username = input("Username: ")
    password = input("Password: ")
    print("To logout type 'lock'.")
    command = None
    input1 = None
    input2 = None
    while command != "lock":
        command = input("What is your command? ")
    while input1 != username:
        input1 = input("What is your username? ")
    while input2 != password:
        input2 = input("What is your password? ")
    print("Welcome in.")


def print_if_loop_warmup():
    n = int(input("Number? "))
    if n < 0:
        print("The absolute value of", n, "is", -n)
    else:
        print("The absolute value of", n, "is", n)


def print_elif_practice():
    a = 0
    while a < 9:
        a = a + 1
        if a > 6:
            print(a, ">", 6)
        elif a <= 3:
            print(a, "<=", 3)
        else:
            print("Neither tests are true.")


def print_higher_or_lower():
    number = 24
    guess = 1
    print("Guess what number I'm thinking of.")
    while guess != number:
        guess = int(input("Is it... "))
        if guess == number:
            print("Woo, you got it!")
        elif guess < number:
            print("A bit higher.")
        elif guess > number:
            print("Too high!")


def print_practice_git():
    print("Testing testing 123")


def print_whats_your_name():
    name = input('Your name: ')
    if name == 'Hannah':
        print("That is a nice name!")
    elif name == 'James':
        print("Sounds like a weirdo to me...")
    else:
        print("You have a nice name.")


def print_sum_of_two():
    input1 = float(input('Pick a number: '))
    input2 = float(input('Pick another: '))
    sum = input1 + input2
    print(sum)
    if sum > 100:
        print("That is a big number.")


def hello():
    print('Hello!')

def print_welcome(name):
    print('Welcome,', name)

def area_square(side_length):
    return(side_length**2)

def area_rectangle(width, height):
    return width * height

def area_circle(radius):
    return(3.14 * radius**2)

def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Must be a positive number.')
        number = float(input(prompt))
        return number

def print_area_of_shape():
    name = input("What's your name? ")
    hello()
    print_welcome(name)
    shape = input("Would you like to find the area of a square, a rectangle or a circle? ")
    if shape == 'square':
        l = float(input('Side Length: '))
        print('Side Length =', l, 'so area of the square =', area_square(l))
    elif shape == 'rectangle':
        w = float(input('Width: '))
        h = float(input('Height: '))
        print('Width =', w, 'and height =', h, 'so area of the rectangle =', area_rectangle(w, h))
    elif shape == 'circle':
        r = float(input('Radius: '))
        print('Radius =', r, 'so area of the circle =', area_circle(r))
    else:
        print('Shape not recognised.')


if __name__ == '__main__':

   print_area_of_shape()




