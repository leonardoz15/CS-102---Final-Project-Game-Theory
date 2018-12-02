# Work by Chris Cook, Andrew C. Everitt, Simon Burrows, & Zach Leonardo
# Team Nondiscrete Chaos
# Computer Science 102: Discrete Structures
from random import randint


def nim_sum(pile_list):  # Function to find nim sum
    # Function to find and return the Nim sum
    # pile_binary = []
    # for pile in pile_list:
    #     pile = bin(pile)[2:]
    #     pile_binary.append(pile)  # list of piles in binary
    # length = [len(pile) for pile in pile_binary]
    # max_len = max(length)
    # pile_binary = ["0" * (max_len - len(pile))
    #                + pile for pile in pile_binary]  # fill out with 0s
    # nim_sum = ""
    # for i in range(max_len):
    #     mom = 0
    #     for pile in pile_binary:
    #         mom = int(pile[i])
    #         mom %= 2
    #     nim_sum += str(mom)
    # print(nim_sum)
    nim_sum = pile_list[0]
    for i in range(len(pile_list)-1):
        nim_sum = nim_sum ^ pile_list[i+1] #XOR
    return nim_sum
    # End of nim_sum()


def prediction(nim_sum):
    # Function to determine the winner based on the nim sum
    if int(nim_sum) == 0:
        print("The user should win given best play")
    else:
        print("The computer should win given best play")


def isFinished(index, pile_list):
    # Function to check if the game is done
    i = 0
    fin = False
    while i < index:
        if (pile_list[i] != 0):
            return fin
        else:
            fin = True
            return fin


def declareWinner(index, pile_list, fin):
    # Function to see who wins
    if (fin is True):
        res = 0
        for i in range(index):
            res ^= pile_list[index]  # XOR
            if (res == 0 or index % 2 == 0):
                print("Human wins!")
            else:
                print("Computer wins!")


def play(index, n_piles, pile_list):
    # Function for when human is playing
    if index > n_piles:  # Checks if pile exists
        index = int(input("Please enter a lower pile number: "))
        play(index, n_piles, pile_list)
    else:
        # i = 0
        # Prompts user to make move
        index -= 1  # changes to index of pile
        removed = int(input("How many do you want to remove? \n"))
        if removed > pile_list[index]:  # Checks if there are enough
            print("Please enter a lower number to remove")
        else:
            pile_list[index] = pile_list[index] - removed
            print("You removed ", removed, " from pile number ",
                  index, ". It is the computer's turn.")


def computer(nim_sum, pile_list):
    # Function to calculate and display computer's move
    if nim_sum == 0:
        # computer makes "random" move because it thinks it will lose
        # takes one from first non-empty pile
        i = 0
        while i < len(pile_list):
            if pile_list[i] == 0:
                i += 1
            else:
                value = 1
                choice = i + 1
                pile_list[i] = pile_list[i] - 1
    else:  # computer makes "calculated" move to reduce nim_sum to zero
        temp_list = pile_list
        i = 0
        test = nim_sum(temp_list)
        print(test)
        while test != 0:
            # while i < len(pile_list):
            #     if pile_list[i] == 0:
            #         i += 1
            #else:
            #temp_list[i] -= randint(0, 2)
            temp_list[1] = 4
            test = nim_sum(temp_list)
        print(test)
        li_dif = [i for i in pile_list
                  + temp_list if i not in pile_list or i not in temp_list]
        #print(li_dif[0])
        #print("The computer has removed ", value, " from pile number ",
          #choice, ". The piles now look like this: ")


def main():
    # Main Function
    # Lets user determine number of piles
    n_piles = int(input("How many piles do you want? "))
    i = 0
    pile_list = []
    while i < n_piles:  # Asks user for pile size
        # Adds to a list (each index is its own pile)
        pile_size = int(input("What size should this pile be? "))
        pile_list.append(pile_size)
        i += 1  # Moves to next pile
    x = nim_sum(pile_list)
    prediction(x)
    index = int(input("Human will go first. Start the game by selecting a pile to pick from: "))
    over_bool = False
    while over_bool is False:
        play(index, n_piles, pile_list)
        computer(nim_sum, pile_list)
        print("The piles now look like this: ")
        if i < len(pile_list):
            print("Pile number ", i + 1, " contains ", pile_list[i])
        index = int(input("What pile do you want to remove from: "))
        over_bool = isFinished(index, pile_list)
    isFinished(index, pile_list)


main()
