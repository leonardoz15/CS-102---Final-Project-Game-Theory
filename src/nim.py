# Work by Chris Cook, Andrew C. Everitt, Simon Burrows, & Zach Leonardo
# Team Nondiscrete Chaos
# Computer Science 102: Discrete Structures


def nim_sum(pile_list):  # Function to find nim sum
    # Function to find and return the Nim sum
    nim_sum = pile_list[0]
    for i in range(len(pile_list) - 1):
        nim_sum = nim_sum ^ pile_list[i + 1]  # XOR
    return nim_sum
    # End of nim_sum()


def prediction(nim_sum):
    # Function to determine the winner based on the nim sum
    if int(nim_sum) != 0:
        print("The user should win given best play")
    else:
        print("The computer should win given best play")


def isFinished(pile_list):
    # Function to check if the game is done
    fin = False
    fin = all(i == 0 for i in pile_list)
    return fin


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
                  index + 1, ". It is the computer's turn.")
    return pile_list


def computer(sum, pile_list):
    # Function to calculate and display computer's move
    temp_list = pile_list[:]
    if sum == 0:
        # computer makes "random" move because it thinks it will lose
        # takes one from first non-empty pile
        i = 0
        while i < len(temp_list):
            if temp_list[i] != 0:  # Checks for piles of 0
                index = i
                temp_list[i] = temp_list[i] - 1
                print(temp_list[i])
                break
            else:
                i += 1
        print("The computer removed 1 from pile number ",
              index + 1, " it is now your turn.")
        pile_list = temp_list[:]
        return pile_list
    else:  # computer makes "calculated" move to reduce nim_sum to zero
        test = nim_sum(temp_list)
        y = 1
        while test != 0:
            i = 0
            c = 0
            for i in range(len(temp_list)):
                if temp_list[i] == 0:
                    c += 1
                    temp_list = pile_list[:]
                else:
                    temp_list[i] -= y
                    test = nim_sum(temp_list)
                    if test != 0:
                        c += 1
                        temp_list = pile_list[:]
                    else:
                        break
                if c == len(pile_list):
                    y += 1
        for i in temp_list:
            if i not in pile_list:
                value = i
                print(i)
                index = temp_list.index(value)
                diff = pile_list[index] - value
                print("The computer removed ", diff, " from pile number ",
                      index + 1, " it is now your turn.")
    pile_list = temp_list[:]
    return pile_list


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
    index = int(
        input("Human will go first. Start the game by selecting a pile to pick from: "))
    over_bool = False
    while over_bool is False:
        pile_list = play(index, n_piles, pile_list)
        over_bool = isFinished(pile_list)
        if over_bool is True:
            print("Congrats you won!")
            break
        sum = nim_sum(pile_list)
        pile_list = computer(sum, pile_list)
        over_bool = isFinished(pile_list)
        if over_bool is True:
            print("You lost :(")
            break
        print("The piles now look like this: ")
        i = 0
        for i in range(len(pile_list)):
            print("Pile number ", i + 1, " contains ", pile_list[i])
        index = int(input("What pile do you want to remove from: "))
        over_bool = isFinished(pile_list)
    print("Thanks for playing Nim!")
    exit()


main()
