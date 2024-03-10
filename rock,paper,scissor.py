import random
def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It is tie"
    elif (user_choice=='rock' and computer_choice=='scissors') or\
         (user_choice=='scissors' and computer_choice=='paper') or\
         (user_choice=='paper' and computer_choice=='rock') :
        return "you win!"
    else:
        return "Computer wins!"

def play_game():
    user_score=0
    computer_score=0
    while True:
        user_choice=input("Choose rock,paper, or scissors:").lower()
        computer_choice=random.choice(['rock','paper','scissors'])
        print(f"you choose:{user_choice}")
        print(f"Computer choose:{computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if 'win' in result:
            user_score += 1
        elif 'tie' not in result:
            computer_score += 1
        
        print(f"Your score: {user_score}, Computer's score: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

print("Welcome to Rock, Paper, Scissors game!")
play_game()

        
        
                                  
    

    
