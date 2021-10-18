# Write your code here
import random

player_decision = "continue"
while player_decision == "continue":
    print(""" 
Welcome to the Domino Game! Let's see who is the better player, YOU OR COMPUTER ;) 
The following are the instructions of the game!
    1) There are 28 domino pieces in the game. Each player will be entitled to 7 pieces, and the rest will be known as the stock pieces, 
    where you will draw from if you are unable to make a move.
    
    2) The player who possesses the higher double domino piece will start the game first. The system will be checking both players 
    hand to ensure that the higher double domino piece will be placed on the board first.
    * Double domino piece means pieces like [2, 2] and [5, 5] and in this case, [5, 5] is the higher double domino piece.
    
    3) To place a domino piece on the right side of the domino chain, you just need to input the number beside your piece. 
    However, if you want to place it on the left side, you will need to add a '-' sign before you input the number.
    
    4) Do not worry about the flipping of domino piece as the system will do it automatically for you.
    
    5) The game will end when either side run out of domino piece (player who run out of domino piece wins) or when an identical number
     appear in the domino snake for 8 times (both side tie). """)

    full_set = []
    for x in range(7):
        for y in range(7):
            if y >= x:
                full_set.append([x, y])

    status = "no double pieces"

    while status == "no double pieces":
        stock_pieces = random.sample(full_set, 14)
        partial_set = [x for x in full_set if x not in stock_pieces]
        computer_pieces = random.sample(partial_set, 7)
        player_pieces = [x for x in partial_set if x not in computer_pieces]
        # To find the sum of the individual double domino pieces in the player and computer pieces to decide who start the game first
        double_computer = [ele[0]*2 for ele in computer_pieces if ele[0] == ele[1]]
        double_player = [ele[0]*2 for ele in player_pieces if ele[0] == ele[1]]

        if max(double_computer, default=0) > max(double_player, default=0):
            status = "player"
            domino_snake = [[int(max(double_computer) / 2), int(max(double_computer) / 2)]]
            computer_pieces.remove(domino_snake[0])
        elif max(double_player, default=0) > max(double_computer, default=0):
            status = "computer"
            max_sum = max(double_player)
            domino_snake = [[int(max(double_player) / 2), int(max(double_player) / 2)]]
            player_pieces.remove(domino_snake[0])
        else:
            status = "no double pieces"  # To restart the loop and redistribute the domino pieces if there are no double domino pieces with the computer and player

    freq_num_snake = {}
    for i in domino_snake[0]:
        freq_num_snake[i] = freq_num_snake.get(i, 0) + 1  # To create a frequency table to ensure that the game will end if identical number appear in the domino snake for 8 times

    while (freq_num_snake[domino_snake[0][0]] != 8 or (domino_snake[0][0] != domino_snake[-1][-1])) and len(player_pieces) >= 0 and len(computer_pieces) >= 0:
        print('=' * 70)
        print(f"Stock size: {len(stock_pieces)}")
        print(f"Computer pieces: {len(computer_pieces)}")
        print("\n")
        if len(domino_snake) > 6:
            domino_snake1 = []  # A new list for printing when length of domino_snake > 6
            for ele in domino_snake[:3]:
                domino_snake1.append(ele)
            domino_snake1.append("...")
            for ele in domino_snake[-3:]:
                domino_snake1.append(ele)
            for ele in domino_snake1:
                print(ele, end="")
        else:
            for ele in domino_snake:
                print(ele, end="")
        print("\n")
        print("Your pieces:")
        for count, pieces in enumerate(player_pieces, 1):
            print(f"{count}:{pieces}")
        print("\n")

        if len(player_pieces) == 0:
            print("Status: The game is over. You won!")
            break
        elif len(computer_pieces) == 0:
            print("Status: The game is over. The computer won!")
            break
        elif freq_num_snake[domino_snake[0][0]] == 8 and domino_snake[0][0] == domino_snake[-1][-1]:
            print("Status: The game is over. It's a draw.")
            break
        else:
            if status == 'player':
                print("Status: It's your turn to make a move. Enter your command.")
                player_input = "undefined"
                while player_input == "undefined":
                    try:
                        player_input = int(input())
                    except Exception:
                        print("Invalid input. Please try again.")
                        player_input = "undefined"
                        continue
                    else:
                        if player_input > 0 and player_input <= len(player_pieces):
                            index = player_input - 1
                            right_end_num = domino_snake[-1][-1]
                            trial_piece = player_pieces[index]
                            if right_end_num in trial_piece:
                                if right_end_num == trial_piece[0]:
                                    verified_piece = player_pieces.pop(index)
                                    domino_snake.append(verified_piece)
                                else:
                                    verified_piece = [trial_piece[1], trial_piece[0]]  # To swap the numbers from left to right
                                    del player_pieces[index]
                                    domino_snake.append(verified_piece)
                            else:
                                print("Illegal move. Please try again.")
                                player_input = "undefined"  # To restart the while loop to prompt player to make a legal move
                                continue

                            for i in verified_piece:
                                freq_num_snake[i] = freq_num_snake.get(i, 0) + 1
                            status = "computer"  # Change status to computer so that the next while loop will be for computer to make a move
                            break

                        elif player_input == 0:
                            if len(stock_pieces) != 0:
                                extra_piece = stock_pieces.pop()
                                player_pieces.append(extra_piece)
                                status = "computer"
                            else:
                                status = "computer"
                            break
                        elif player_input < 0 and abs(player_input) <= len(player_pieces):
                            index = abs(player_input) - 1
                            left_end_num = domino_snake[0][0]
                            trial_piece = player_pieces[index]
                            if left_end_num in trial_piece:
                                if left_end_num == trial_piece[1]:
                                    verified_piece = player_pieces.pop(index)
                                    domino_snake.insert(0, verified_piece)
                                else:
                                    verified_piece = [trial_piece[1], trial_piece[0]]  # To swap the numbers from left to right
                                    del player_pieces[index]
                                    domino_snake.insert(0, verified_piece)
                            else:
                                print("Illegal move. Please try again.")
                                player_input = "undefined"  # To restart the while loop to prompt player to make a legal move
                                continue
                            for i in verified_piece:
                                freq_num_snake[i] = freq_num_snake.get(i, 0) + 1
                            status = "computer"
                            break
                        else:
                            print("Invalid input. Please try again.")
                            player_input = "undefined"
                            continue
            else:
                computer_input = input("Status: Computer is about to make a move. Press Enter to continue...\n")

                # To compute scores of the individual domino in computer pieces. The higher the score of the individual domino, it means that the numbers on the domino piece has appeared
                # numerous times in the domino_snake and on your hand, hence the less valuable it is to be kept on hand and thus it will be prioritise first.

                comp_list = [num for domino in computer_pieces for num in domino]  # To flatten out the list i.e. combine list of lists to a single list
                snake_list = [num for domino in domino_snake for num in domino]
                keys = [0, 1, 2, 3, 4, 5, 6]
                count_dict = dict.fromkeys(keys, 0)  # To initialise a dict with number 0-7 as keys and the same value of 0
                for key in count_dict:
                    count_dict[key] = comp_list.count(key) + snake_list.count(key)
                list_score = []
                for domino in computer_pieces:
                    indiv_score = count_dict[domino[0]] + count_dict[domino[1]]
                    list_score.append(indiv_score)
                sorted_list = sorted(list_score, reverse=True)

                # To try and see whether each of the domino can be fitted to left or right of snake, starting with the domino with the highest score
                counter = 0
                while counter < len(list_score):
                    index = list_score.index(sorted_list[counter])  # To find the index of the domino who has the highest score
                    trial_piece = computer_pieces[index]
                    left_end_num = domino_snake[0][0]
                    right_end_num = domino_snake[-1][-1]
                    if left_end_num in trial_piece:  # Check left side of snake
                        if left_end_num == trial_piece[1]:
                            verified_piece = computer_pieces.pop(index)
                            domino_snake.insert(0, verified_piece)
                        else:
                            verified_piece = [trial_piece[1], trial_piece[0]]  # To swap the numbers from left to right
                            del computer_pieces[index]
                            domino_snake.insert(0, verified_piece)
                        for i in verified_piece:
                            freq_num_snake[i] = freq_num_snake.get(i, 0) + 1
                        status = "player"
                        break
                    elif right_end_num in trial_piece:  # Check right side of snake
                        if right_end_num == trial_piece[0]:
                            verified_piece = computer_pieces.pop(index)
                            domino_snake.append(verified_piece)
                        else:
                            verified_piece = [trial_piece[1], trial_piece[0]]
                            del computer_pieces[index]
                            domino_snake.append(verified_piece)
                        for i in verified_piece:
                            freq_num_snake[i] = freq_num_snake.get(i, 0) + 1
                        status = "player"
                        break
                    else:
                        counter += 1
                        continue
                else:  # When the while loop fails after trying all the dominoes in computer_pieces, code underneath will run
                    if len(stock_pieces) != 0:
                        extra_piece = stock_pieces.pop()
                        computer_pieces.append(extra_piece)
                        status = "player"
                    else:
                        status = "player"

    player_decision = input("If you want to play again, type 'continue'! If you want to quit the game, type 'quit'! Thanks for playing :)\n")

