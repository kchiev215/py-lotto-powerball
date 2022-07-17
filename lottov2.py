# lotto picker by manny juan  (juanm@wellsfargo.com or manny@bdt.com)

from random import randint


def welcome_message():
    print("Welcome to the Billion dollar Lottery!")
    print("Select five numbers from 1 to 69; "
          "and one POWERBALL number from 1 to 26.")

def user_number_choices():
    user_choices = []
    while True:
        try:
            while True:
                choice_1 = int(input("First number"))
                if 69 > choice_1 > 0:
                    user_choices.append(choice_1)
                    break
                else:
                    print('positive numbers only')
            while True:
                choice_2 = int(input("Second number"))
                if 69 > choice_2 > 0 and choice_2 not in user_choices:
                    user_choices.append(choice_2)
                    break
                elif(choice_2 in user_choices):
                    print("Pick another number")
                else:
                    print("Pick another number")
            while True:
                choice_3 = int(input("Third number"))
                if 69> choice_3 > 0 and choice_3 not in user_choices:
                    user_choices.append(choice_3)
                    break
                elif (choice_3 in user_choices):
                    print("Pick another number")
                else:
                    print("Pick another number")
            while True:
                choice_4 = int(input("Fourth number"))
                if 69> choice_4 > 0 and choice_4 not in user_choices:
                    user_choices.append(choice_4)
                    break
                elif (choice_4 in user_choices):
                    print("Pick another number")
                else:
                    print("Pick another number")
            while True:
                choice_5 = int(input("Fifth number"))
                if 69 > choice_5 > 0 and choice_5 not in user_choices:
                    user_choices.append(choice_5)
                    break
                elif (choice_5 in user_choices):
                    print("Pick another number")
                else:
                    print("Pick another number")
            while True:
                POWERBALL = int(input("POWERBALL number"))
                if 26 > POWERBALL > 0:
                    user_choices.append(POWERBALL)
                    break
                else:
                    print("Pick another number")
            break
        except ValueError:
            print("Only numbers")
    return user_choices


def check_lottery(user_choices, v):
    listing = []
    for i in user_choices:
        for j in v:
            if i == j:
                listing.append(i)
    print(listing)



def pick_lotto():
    maxm = 53
    maxj = 6
    m = maxm
    # create all numbers from 0 to m
    r = list(range(m + 1))
    # start with an empty result
    v = []
    for j in range(maxj):
        # get ith number from r...
        i = randint(1, m)
        n = r[i]
        # remove it from r...
        r[i:i + 1] = []
        m = m - 1
        # and append to the result
        v.append(n)
    return v


def run():
    done = 0
    while not done:
        try:
            x = input('\npress Enter for Lotto picks (Q to quit). ')
        except EOFError:
            x = 'q'
        if x and (x[0] == 'q' or x[0] == 'Q'):
            done = 1
            print('done')
        else:
            print(pick_lotto())

def main():
    welcome_message()
    listing = []
    for i in user_number_choices():
        for j in pick_lotto():
            if i == j:
                listing.append(i)
    print(listing)

# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
    main()
    # run()
# else:
#     print("Module lotto imported.")
#     print("To run, type: lotto.run()")
#     print("To reload after changes to the source, type: reload(lotto)")
# # end of lotto.py
