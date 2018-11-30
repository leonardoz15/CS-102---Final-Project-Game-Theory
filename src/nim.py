# Work by Chris Cook, Andrew C. Everitt, Simon Burrows, & Zach Leonardo (Team Nondiscrete Chaos)
# Computer Science 102: Discrete Structures


class Nim:
    def nim_sum(pile_list):  # Function to find nim sum of starting move
    """Function to find and return the Nim-sum"""
    pile_binary[]
    for pile in pile_list:
        pile_binary.append(bin(pile)[2:])
    length = [len(pile) for pile in pile_binary]
    max_len = max(length)
    pile_binary = ["0" * (max_len - len(pile)) + pile for pile in pile_binary] #fill out with 0s
    nim_sum = ""
    for i in range(max_len):
        bin = 0
        for pile in pile_binary:
            bin = int(pile_binary[i])
            bin %= 2
        nim_sum += str(bin)
    return nim_sum
    #End of nim_sum()

    def prediction(nim_sum):
    """Function to determine the winner based on the nim sum"""
    if int(nim_sum) = 0:
        print("The user should win given best play")
    else:
        print("The computer should win given best play")


    def isFinished():
    """Function to check if the game is done"""
      int i = 0
      bool fin = False
      for i < n:
        if (piles[i] != 0):
            return fin
      return fin = True

    def declareWinner(n, pile_list, fin):
    """Function to see who wins"""
    if fin = True
      res = 0
       for i in range(n):
            res ^= pile_list[n]
        if (res == 0 or n % 2 == 0):
            print("Human wins!")
        else:
            print("Computer wins!")

    def play(index):
    """Function for when human is playing"""
       if index > len(n_piles):  # Checks if pile exists
            index = int(input("Please enter a lower pile number"))
            return index
            play()
        else:
            # Prompts user to make move
            removed = int(input("How many do you want to remove?"))
            if removed > pile_list[index]:  # Checks if there are enough
                print("Please enter a lower number to remove")
            else:
                pile_list[index] = pile_list[index] - removed
                print("You removed ", removed, " from pile number ",
                      index, ". It is the computer's turn.")
                computer()

    def computer(nim_sum):
        """Function to calculate and display computer's move"""
        if num_sum = "0":
            # computer makes "random" move because it thinks it will lose
            for i < len(pile_list):
                if pile_list[i] = 0:
                    i += 1
                else:
                    value = 1
                    choice = i+1
                    pile_list[i] = pile_list[i]-1
        else:
            # computer makes "calculated" move to reduce nim_sum to zero


        print("The computer has removed ", value, " from pile number ",
              choice, ". The piles now look like this: ")
        for i < len(pile_list):
            print("Pile number ", i + 1, " contains " pile_list[i])
        index = int(input("What pile do you want to remove from: "))-1
        return index
        play()

# End of Nim class


def main():
    # Main Function
    # Lets user determine number of piles
    n_piles = int(input("How many piles do you want? "))
    for i < len(n_piles):  # Asks user for pile size
        # Adds to a list (each index is its own pile)
        pile_list[i] = int(input("What size should this pile be? "))
        i += 1  # Moves to next pile
    prediction()
    index = int(input("Start the game by selecting a pile to pick from: ")) -1  # Subtracts one to find index of pile
    return index
    n = len(index)
    play()
