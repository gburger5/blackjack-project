
from p1_random import P1Random


rng = P1Random() #outside of the loop


# print(rng.next_int(13) + 1)

game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
ties = 0
games_played = 0


#Control # of games the player will play
while game_continue: # game #1, #2, #3
    # 1. print game_num message
    game_num += 1
    print(f"START GAME #{game_num}")
    # 2. Deal Card
    hand = 0
    #deal a card
    card = (rng.next_int(13) + 1)
    if card == 1:
        print("Your card is a ACE!")
        card = 1
    elif 2<= card <= 10:
        # print out card value
        print(f"Your card is a {card}!")
        card = card
    elif card == 11:
        print("Your card is a JACK!")
        card = 10
    elif card == 12:
        print("Your card is a QUEEN!")
        card = 10
    elif card == 13:
        print("Your card is a KING!")
        card = 10
    hand += card
    #3 Add to player hand
    print(f"Your hand is: {hand}")
    if hand == 21:
        print("BLACKJACK! You win!")
        games_played += 1
    if hand > 21:
        print("You exceeded 21! You lose.")
        games_played += 1
    #4 print hand value
    #5. Keep playing the current game by prompting the player to choose a menu option
    no_winner = True
    while no_winner:
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit \n")
        choice = int(input("Choose an option: "))
        if choice == 1:
            # deal another card to the player
            # calculate the player's hand value
            card = (rng.next_int(13) + 1)
            if card == 1:
                print("Your card is a ACE!")
                card = 1
            elif 2 <= card <= 10:
                # print out card value
                print(f"Your card is a {card}!")
                card = card
            elif card == 11:
                print("Your card is a JACK!")
                card = 10
            elif card == 12:
                print("Your card is a QUEEN!")
                card = 10
            elif card == 13:
                print("Your card is a KING!")
                card = 10
            hand += card
            print(f"Your hand is: {hand}")
            if hand == 21:
                print("BLACKJACK! You win!")
                no_winner = False
                player_wins += 1
                games_played += 1
            elif hand > 21:
                print("You exceeded 21! You lose.")
                no_winner = False
                dealer_wins += 1
                games_played += 1

            # set no_winner = false
            # if player hand = 21 print winning message
            # update the number of games player/dealer win
        elif choice == 2:
            no_winner = False
            dealer_hand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {hand}")
            # compare player hand w dealer hand
            if dealer_hand > 21:
                print("\nYou win!")
                player_wins += 1
            elif dealer_hand > hand: # dealer wins
                print("\nDealer wins!")
                dealer_wins += 1
            elif hand > dealer_hand:
                print("\nYou win!")
                player_wins += 1
            elif hand == dealer_hand:
                print("It's a tie! No one wins!")
                ties += 1
            games_played += 1
            # deal a card to the dealer
            # no_winner False
        elif choice == 3:
            # print statistics
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {ties}")
            print(f"Total # of games played is: {games_played}")
            win_percentage = (player_wins/games_played) * 100
            print(f"Percentage of Player wins: {win_percentage:.1f}%")
        elif choice == 4:
            no_winner = False # get outside of inner while loop
            game_continue = False # get outside of outer while loop
        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")# print invalid message

