## Work by Chris Cook, Andrew C. Everitt, Simon Burrows, & Zach Leonardo (Team Nondiscrete Chaos)
## Computer Science 102: Discrete Structures


class Nim:
    def nim_sum(pile_list): #Function to find XOR of starting move
    """Function to find Nim-sum (XOR) of starting move"""
    pile_binary[]
    for pile in pile_list:
        pile_binary.append(bin(pile)[2:])
    length = [len(pile) for pile in pile_binary]
    max_len = max(length)
    pile_binary = ["0"*(max_len - len(pile))+pile for pile in pile_binary]
    nim_sum = ""
    for i in range(max_len):
        for pile in pile_binary:

            pile = int(pile_binary[i])
            pile %= 2


    def isFinished():
    """Function to check if the game is done"""
        int i = 0
        for i<n:
            if (piles[i]!=0):
                return (False)

        return (True)


    def declareWinner(n, pile_list):
    """Function to see who wins"""
    if
        res = 0
        for i in range(n):
            res ^= pile_list[n]
        if (res == 0 or n % 2 == 0):
            print("Human wins!")
        else:
            print ("Computer wins!")


    def play(index):
    """Function for when human is playing"""
        if index > len(n_piles): #Checks if pile exists
            index = int(input("Please enter a lower pile number"))
            return index
            play()
        else:
            removed = int(input("How many do you want to remove?")) #Prompts user to make move
            if removed > pile_list[index]: #Checks if there are enough
                print("Please enter a lower number to remove")
            else:
                pile_list[index] = pile_list[index]-removed
                print("You removed ", removed, " from pile number ", index, ". It is the computer's turn.")
                computer()


    def computer():
        """Function to calculate and display computer's move"""
        print("The computer has removed ", value, " from pile number ", choice, ". The piles now look like this: ")
        for i < len(pile_list):
            print("Pile number ", pile_list)
        index = int(input("What pile do you want to remove from: "))
        return index
        play()

#End of Nim class


def main():
 #"Main Function"
    n_piles = int(input("How many piles do you want? ")) #Lets user determine number of piles
    for i < len(n_piles): #Asks user for pile size
        pile_list[i] = int(input("What size should this pile be? ")) #Adds to a list (each index is its own pile)
        i += 1 #Moves to next pile
    index = int(input("Start the game by selecting a pile to pick from: "))-1 #Subtracts one to find index of pile
    return index
    n = len(index)
    play()
