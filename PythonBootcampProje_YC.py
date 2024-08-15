import random

def tas_kagit_makas_Yagmur_Celik():
    # Introduction of the game
    print("\n***Welcome to the Rock-Paper-Scissors game! 🎉***")
    print("In this game, two players will choose rock, paper, or scissors and face off against each other!")
    print("• Rock crushes scissors, scissors cut paper, and paper covers rock.")
    print("• In each round, the choices for both players will be made randomly.")
    print("• The first player to win 2 rounds will be the champion.")
    print()
    print("Let's get started and may the best player win!")

    # Defining the game options
    options = ["Rock", "Paper", "Scissors"]

    while True:
        # Initialize scores and round counter
        player_score = 0
        computer_score = 0
        round = 1

        # Ask the player if they are ready to play
        ready = input("Are you ready to play? (yes/no): ").lower()
        if ready == "no":
            print("Oh, come on! Let's not miss out on the fun. I'm ready when you are! Let's play and see who wins! 😄")
            continue

        # Loop until either the player or the computer wins 2 rounds
        while player_score < 2 and computer_score < 2:
            print(f"Round {round}")

            # Ask the player for their choice and validate it
            player = input("Choose Rock, Paper, or Scissors: ")

            while player not in options:
                player = input("Invalid choice! Please choose Rock, Paper, or Scissors: ").capitalize()

            # Randomly select the computer's choice
            computer = random.choice(options)

            # Display the choices
            print(f"Player : {player}")
            print(f"Computer : {computer}")

            # Determine the outcome of the round
            if computer == player:
                print("It's tie!")
                print(f"Score: {player_score} - {computer_score}")

            elif (player == "Rock" and computer == "Scissors") or \
                    (player == "Paper" and computer == "Rock") or \
                    (player == "Scissors" and computer == "Paper"):
                # Player wins the round
                print("You win round!")
                player_score += 1
                print(f"Score: {player_score} - {computer_score}")
                round += 1

            else:
                # Computer wins the round
                print("You lost this round :(")
                computer_score += 1
                print(f"Score: {player_score} - {computer_score}")
                round += 1

        # Check if the player or the computer won the game
        if player_score == 2:
            print("\nCongratulations! You won the game.")
        else:
            print("\nYou lost the game :(")

        # Ask the player if they want to play another game
        player_continue = input("Do you want to play another game? (yes/no): ").lower()
        # Randomly decide if the computer wants to continue
        computer_continue = random.choice(["yes", "no"])
        print(f"Computer's decision to continue: {computer_continue}")

        # End the game if either the player or the computer decides not to continue
        if player_continue == "no" or computer_continue == "no":
            print("Game over. Thanks for playing!")
            break


tas_kagit_makas_Yagmur_Celik()
